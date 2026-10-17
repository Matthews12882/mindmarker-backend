#!/usr/bin/env python3
"""
get_articles.py — build a local corpus of the most *vital* Wikipedia articles.

WHY THIS EXISTS
    The reading-quiz app takes real articles and turns them into AI-generated
    reading-comprehension quizzes. This script builds the raw material: clean,
    self-contained Markdown files for Wikipedia's most important general-knowledge
    articles, plus a manifest the backend can load.

    (An earlier version ranked articles by pageviews. Pageviews surface whatever
    is trending — current events, entertainment, true crime — which is poor
    material for a study app. This version uses Wikipedia's "Vital articles"
    lists instead: a curated ranking of the topics that matter most.)

WHAT IT DOES
    1. Reads the Wikipedia "Vital articles" lists (Levels 1-3), which rank the
       most important topics, and walks them in importance order.
    2. Downloads each article through the free MediaWiki Action API and converts
       the HTML to clean Markdown (markdownify).
    3. Writes one .md file per article, an index.json manifest, and a README.md
       explaining how to use the corpus.

USAGE
    ./venv/bin/python get_articles.py                 # top 300, levels 1-3
    ./venv/bin/python get_articles.py --limit 20      # small sample
    ./venv/bin/python get_articles.py --levels 1,2    # only the most vital
    ./venv/bin/python get_articles.py --out articles

REQUIRES
    requests, beautifulsoup4, markdownify   (already installed in ./venv)
No API key is needed: every endpoint used here is free and public.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import sys
import time
from pathlib import Path
from string import Template
from urllib.parse import quote

import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as html_to_md

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

# Wikipedia asks every automated client to identify itself. Keep a real contact
# here so the request is polite: https://meta.wikimedia.org/wiki/User-Agent_policy
USER_AGENT = "reading-quiz-app/0.1 (educational Congressional App Challenge project)"
HEADERS = {"User-Agent": USER_AGENT, "Api-User-Agent": USER_AGENT}

ACTION_API = "https://en.wikipedia.org/w/api.php"

# Each "Wikipedia:Vital articles/Level N" page holds the most vital articles,
# in importance order: Level 1 = top 10, Level 2 = top 100, Level 3 = top 1000.
# (The pages are cumulative, so we walk 1 -> 2 -> 3 and de-duplicate.)
VITAL_PAGE = "Wikipedia:Vital articles/Level {level}"
DEFAULT_LEVELS = (1, 2, 3)
VITAL_SOURCE_LIST = "Wikipedia:Vital articles"

DEFAULT_LIMIT = 300  # how many articles to keep ("the top N")
DEFAULT_OUT = "articles"
DEFAULT_TOPIC = "Core topics"  # fallback subject when a list has no section heading

# HTML we throw away before converting to Markdown. These are chrome, not prose.
DROP_SELECTORS = [
    "style", "script", "sup.reference", "span.mw-editsection",
    "table.infobox", "div.infobox", "table.sidebar", "div.sidebar",
    "div.navbox", "table.navbox", "div.metadata", "table.metadata",
    "div.ambox", "div.hatnote", "div.sistersitebox", "div.mw-references-wrap",
    "ol.references", "div.reflist", "div.thumb", "figure", "img",
    "div.navigation-not-searchable", "div.printfooter", "span.mw-cite-backlink",
    "div.toc", "div.mw-empty-elt", "div.shortdescription",
]

# Appendix headings. Everything from the first one onwards is dropped, because
# references / see-also / external links are noise for a reading quiz.
STOP_HEADINGS = {
    "references", "see also", "external links", "notes", "further reading",
    "bibliography", "citations", "sources", "footnotes", "general sources",
    "works cited", "explanatory notes",
}

MAX_SUMMARY_CHARS = 600  # cap the intro blurb stored in front matter


# ---------------------------------------------------------------------------
# Small helpers
# ---------------------------------------------------------------------------

def log(msg: str) -> None:
    print(msg, flush=True)


def yaml_quote(value: object) -> str:
    """Render a scalar as a safe double-quoted YAML/JSON-ish string."""
    text = re.sub(r"\s+", " ", str(value)).strip()
    text = text.replace("\\", "\\\\").replace('"', '\\"')
    return f'"{text}"'


def slugify(title: str, max_len: int = 60) -> str:
    """'Atmosphere of Earth' -> 'atmosphere_of_earth'."""
    slug = title.lower().replace("&", " and ")
    slug = re.sub(r"[^a-z0-9]+", "_", slug).strip("_")
    return slug[:max_len].strip("_") or "article"


def chunked(items: list, size: int):
    for i in range(0, len(items), size):
        yield items[i:i + size]


def api_get(session: requests.Session, params: dict, retries: int = 3) -> dict:
    """GET the MediaWiki Action API as JSON, with simple backoff retries."""
    params = {**params, "format": "json", "formatversion": 2}
    last_error = None
    for attempt in range(retries):
        try:
            resp = session.get(ACTION_API, params=params, timeout=45)
            resp.raise_for_status()
            data = resp.json()
            if "error" in data:
                raise RuntimeError(data["error"].get("info", "unknown API error"))
            return data
        except (requests.RequestException, RuntimeError, ValueError) as exc:
            last_error = exc
            time.sleep(1.5 * (attempt + 1))
    raise RuntimeError(f"API request failed: {last_error}")


# ---------------------------------------------------------------------------
# Step 1 — harvest the Vital articles lists, in importance order
# ---------------------------------------------------------------------------

def strip_wiki_markup(text: str) -> str:
    """Turn a wikitext heading such as 'Science and [[medicine]]' into plain text."""
    text = re.sub(r"\[\[[^\]|]*\|([^\]]*)\]\]", r"\1", text)  # [[target|label]]
    text = re.sub(r"\[\[([^\]]*)\]\]", r"\1", text)           # [[target]]
    return re.sub(r"[\[\]{}]", "", text).strip()


def vital_entries(wikitext: str):
    """Yield (article_title, topic) for each bulleted link, in page order.

    Entries look like `* {{Icon|FA}} [[Article]]` and are grouped under
    `== Topic ==` headings (e.g. History, Geography, People, ...).
    """
    topic = ""
    for line in wikitext.split("\n"):
        stripped = line.strip()
        heading = re.match(r"^==([^=].*?)==\s*$", stripped)  # == Topic == but not === Sub ===
        if heading:
            topic = strip_wiki_markup(heading.group(1))
            continue
        if stripped.startswith("*"):
            for link in re.findall(r"\[\[([^\[\]]+?)\]\]", stripped):
                target = link.split("|")[0].split("#")[0].strip()
                if target and not target.startswith(":"):
                    yield target, topic


def resolve_articles(session, entries, seen: set) -> list[dict]:
    """Keep only existing main-space articles, de-duplicated against `seen`.

    `entries` is an ordered list of (title, topic). Returns an ordered list of
    {"title", "topic"} dicts (using the canonical page title).
    """
    kept: list[dict] = []
    for batch in chunked(entries, 50):
        titles = [title for title, _ in batch]
        data = api_get(session, {"action": "query", "prop": "info",
                                 "redirects": 1, "titles": "|".join(titles)})
        query = data.get("query", {})

        # The API may rename our input (underscores -> spaces) and follow
        # redirects; one alias map lets us look results back up.
        alias = {}
        for entry in query.get("normalized", []) + query.get("redirects", []):
            alias[entry["from"]] = entry["to"]
        pages = {p["title"]: p for p in query.get("pages", [])}

        for title, topic in batch:
            key, hops = title, set()
            while key in alias and key not in hops:
                hops.add(key)
                key = alias[key]
            page = pages.get(key)
            if page and page.get("ns") == 0 and "missing" not in page \
                    and page["title"] not in seen:
                seen.add(page["title"])
                kept.append({"title": page["title"], "topic": topic})
    return kept


def fetch_vital_articles(session, levels, limit: int) -> list[dict]:
    """Return the top `limit` vital articles, most vital first.

    Each item is {"title", "topic", "level"} plus a 1-based "rank".
    """
    seen: set[str] = set()
    articles: list[dict] = []
    for level in levels:
        data = api_get(session, {"action": "parse", "prop": "wikitext",
                                 "redirects": 1,
                                 "page": VITAL_PAGE.format(level=level)})
        entries = list(vital_entries(data["parse"]["wikitext"]))
        resolved = resolve_articles(session, entries, seen)
        for item in resolved:
            item["level"] = level
        articles.extend(resolved)
        log(f"  Level {level}: +{len(resolved)} articles")

    # Some articles (e.g. the Level 1 ones) have no section heading on the page
    # we first met them; borrow a topic from a later listing when possible.
    topic_by_title: dict[str, str] = {}
    for item in articles:
        if item["topic"]:
            topic_by_title.setdefault(item["title"], item["topic"])
    for item in articles:
        if not item["topic"]:
            item["topic"] = topic_by_title.get(item["title"], DEFAULT_TOPIC)

    articles = articles[:limit]
    for rank, item in enumerate(articles, start=1):
        item["rank"] = rank
    return articles


# ---------------------------------------------------------------------------
# Step 2 — metadata (short description + intro summary) in batches of 50
# ---------------------------------------------------------------------------

def fetch_metadata(session: requests.Session, titles: list[str]) -> dict:
    """Map {title: {description, summary, pageid, url}}.

    Uses action=query with prop=description|extracts so 50 titles cost one
    request instead of 50.
    """
    meta: dict[str, dict] = {}
    for batch in chunked(titles, 50):
        data = api_get(session, {
            "action": "query", "prop": "description|extracts|info",
            "exintro": 1, "explaintext": 1, "redirects": 1, "inprop": "url",
            "titles": "|".join(batch),
        })
        query = data.get("query", {})

        alias = {}
        for entry in query.get("normalized", []) + query.get("redirects", []):
            alias[entry["from"]] = entry["to"]
        pages = {p["title"]: p for p in query.get("pages", []) if "missing" not in p}

        for title in batch:
            key, hops = title, set()
            while key in alias and key not in hops:
                hops.add(key)
                key = alias[key]
            page = pages.get(key)
            if not page:
                continue
            meta[title] = {
                "description": page.get("description") or "",
                "summary": (page.get("extract") or "").strip(),
                "pageid": page.get("pageid"),
                "url": page.get("fullurl")
                or f"https://en.wikipedia.org/wiki/{quote(title.replace(' ', '_'))}",
            }
    return meta


# ---------------------------------------------------------------------------
# Step 3 — article HTML -> clean Markdown
# ---------------------------------------------------------------------------

def fetch_html(session: requests.Session, title: str, retries: int = 3):
    """Fetch a page's rendered HTML (and its pageid) via action=parse."""
    params = {
        "action": "parse", "page": title, "prop": "text",
        "redirects": 1, "disableeditsection": 1,
    }
    last_error = None
    for attempt in range(retries):
        try:
            data = api_get(session, params)
            return data["parse"]["text"], data["parse"].get("pageid")
        except (RuntimeError, KeyError) as exc:
            last_error = exc
            time.sleep(1.5 * (attempt + 1))
    raise RuntimeError(f"failed to fetch {title!r}: {last_error}")


def html_to_markdown(html: str) -> str:
    """Turn Wikipedia HTML into tidy Markdown."""
    soup = BeautifulSoup(html, "html.parser")
    for selector in DROP_SELECTORS:
        for element in soup.select(selector):
            element.decompose()

    text = html_to_md(str(soup), heading_style="ATX")

    text = text.replace("[edit]", "")
    text = text.replace("[](#", "")  # leftover empty anchors
    # Rewrite relative links so they still work when the file is opened offline.
    text = text.replace("](//", "](https://")
    text = re.sub(r"\]\(/", "](https://en.wikipedia.org/", text)
    # Whitespace clean-up.
    text = re.sub(r"[ \t]+\n", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def trim_appendix(markdown: str) -> str:
    """Drop everything from the first appendix heading (References, ...)."""
    lines = markdown.split("\n")
    for i, line in enumerate(lines):
        if line.startswith("## "):
            heading = line[3:].strip().lower().rstrip(".")
            if heading in STOP_HEADINGS:
                return "\n".join(lines[:i]).rstrip()
    return markdown


# ---------------------------------------------------------------------------
# Step 4 — write the files
# ---------------------------------------------------------------------------

def build_article_file(record: dict) -> str:
    """Assemble the final Markdown document for one article."""
    front_matter = "\n".join([
        "---",
        f"id: {record['id']}",
        f"title: {yaml_quote(record['title'])}",
        f"rank: {record['rank']}",
        f"level: {record['level']}",
        f"topic: {yaml_quote(record['topic'])}",
        f"url: {yaml_quote(record['url'])}",
        f"pageid: {record['pageid']}",
        f"description: {yaml_quote(record['description'])}",
        f"summary: {yaml_quote(record['summary'])}",
        "source: Wikipedia",
        f"source_list: {yaml_quote(VITAL_SOURCE_LIST)}",
        'license: "CC BY-SA 4.0"',
        f"retrieved: {record['retrieved']}",
        "---",
    ])

    attribution = (
        f"*Source: [Wikipedia — {record['title']}]({record['url']}). "
        "Text licensed under "
        "[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).*"
    )

    return (
        f"{front_matter}\n\n"
        f"# {record['title']}\n\n"
        f"{record['body']}\n\n"
        f"---\n\n{attribution}\n"
    )


def write_index(out_dir: Path, records: list[dict], levels) -> None:
    index = {
        "generated": dt.datetime.now().isoformat(timespec="seconds"),
        "source": "Wikipedia:Vital articles (via the MediaWiki Action API)",
        "levels": list(levels),
        "count": len(records),
        "license": "CC BY-SA 4.0",
        "articles": [
            {
                "id": r["id"],
                "title": r["title"],
                "file": r["file"],
                "rank": r["rank"],
                "level": r["level"],
                "topic": r["topic"],
                "pageid": r["pageid"],
                "description": r["description"],
                "url": r["url"],
            }
            for r in records
        ],
    }
    (out_dir / "index.json").write_text(
        json.dumps(index, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )


README_TEMPLATE = Template("""\
# Reading-Quiz Article Corpus

> Auto-generated by [`../get_articles.py`](../get_articles.py) on $generated.
> Do not hand-edit these files — re-run the script instead.

This folder holds **$count Wikipedia articles** as clean Markdown, ready to be
turned into AI-generated reading-comprehension quizzes. They come from
Wikipedia's **Vital articles** lists — a curated ranking of the most important
general-knowledge topics — rather than from what happens to be trending.

## What's here

| File | Purpose |
|------|---------|
| `README.md` | This note. |
| `index.json` | Machine-readable manifest of every article. The backend loads this. |
| `NNNN_<slug>.md` | One Markdown file per article. |

## Where the data comes from

No API key is required — all endpoints are free and public.

* **Which articles:** Wikipedia's [Vital articles](https://en.wikipedia.org/wiki/Wikipedia:Vital_articles)
  lists, Levels $levels. Each level page ranks its topics by importance
  (Level 1 = the ~10 most vital, Level 2 = the ~100 most vital, Level 3 = the
  ~1,000 most vital). Articles are taken in importance order:
  Level 1, then Level 2, then Level 3.
* **Article text:** the MediaWiki [Action API](https://www.mediawiki.org/wiki/API:Main_page)
  (`action=parse`), converted from HTML to Markdown with `markdownify`.
* **Descriptions + intro summaries:** `action=query&prop=description|extracts`.

## Article file format

Every `NNNN_<slug>.md` file starts with YAML front matter:

```yaml
---
id: $ex_id
title: $ex_title
rank: $ex_rank
level: $ex_level
topic: $ex_topic
url: $ex_url
pageid: $ex_pageid
description: $ex_description
summary: $ex_summary
source: Wikipedia
source_list: "Wikipedia:Vital articles"
license: "CC BY-SA 4.0"
retrieved: $ex_retrieved
---
```

Field notes:

* `id` — stable id used by the app and its quiz JSON (`study_0001`, ...).
* `rank` — position in the importance-ordered list (1 = most vital).
* `level` — Vital articles level the topic belongs to (1, 2 or 3).
* `topic` — subject area, e.g. `History`, `Geography`, `People`. Group the
  library by this to build "browse by subject" screens.
* `pageid` — permanent MediaWiki page id; a durable key if the ranking changes.

...followed by the article body:

```markdown
# <Title>

<lead section, headings, paragraphs, lists, tables>
```

### Cleaning applied

* Infoboxes, navigation boxes, edit links, footnotes and reference lists removed.
* Appendix sections (`References`, `See also`, `External links`, ...) trimmed off.
* Relative wiki links rewritten to absolute `https://en.wikipedia.org/...` URLs.
* Images removed, so the corpus is pure text.

## How to use this corpus

**1. Load the list of articles (backend)**

```python
import json, pathlib

manifest = json.loads(pathlib.Path("articles/index.json").read_text())
for article in manifest["articles"]:
    print(article["id"], article["title"], "-", article["topic"])
```

**2. Read one article and (later) generate its quiz**

```python
article = next(a for a in manifest["articles"] if a["id"] == "study_0001")
text = pathlib.Path("articles", article["file"]).read_text()
# Send `text` to your LLM with the quiz prompt, then store the quiz JSON
# under the same `article["id"]`.
```

**3. Keep ids consistent**

Set the quiz's `Article-ID` equal to the article `id` so quizzes, progress and
points all join on one key:

```json
{ "Article-ID": "study_0001", "questions": [ ] }
```

## Regenerating / customising

```bash
./venv/bin/python get_articles.py                 # top 300 vital articles (levels 1-3)
./venv/bin/python get_articles.py --limit 50      # fewer articles
./venv/bin/python get_articles.py --levels 1,2    # only the most vital
./venv/bin/python get_articles.py --out other_dir
```

The vital-articles ranking changes slowly, so `id` / `rank` are fairly stable
between runs. If you need a key that never changes, use `pageid`.

## Licensing

Wikipedia text is licensed under
[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). Each file links
back to its source article for attribution. Keep that source link (and this
notice) visible in the app, for example on the article page, to stay compliant.
""")


def short(text: str, limit: int = 90) -> str:
    text = re.sub(r"\s+", " ", text).strip()
    return text if len(text) <= limit else text[:limit].rstrip() + "..."


def write_readme(out_dir: Path, records: list[dict], levels, generated: str) -> None:
    example = records[0]
    readme = README_TEMPLATE.substitute(
        generated=generated,
        count=len(records),
        levels=", ".join(str(l) for l in levels),
        ex_id=example["id"],
        ex_title=yaml_quote(example["title"]),
        ex_rank=example["rank"],
        ex_level=example["level"],
        ex_topic=yaml_quote(example["topic"]),
        ex_url=yaml_quote(example["url"]),
        ex_pageid=example["pageid"],
        ex_description=yaml_quote(short(example["description"])),
        ex_summary=yaml_quote(short(example["summary"])),
        ex_retrieved=example["retrieved"],
    )
    (out_dir / "README.md").write_text(readme, encoding="utf-8")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--limit", type=int, default=DEFAULT_LIMIT,
                        help=f"how many articles to keep (default {DEFAULT_LIMIT})")
    parser.add_argument("--levels", default="1,2,3",
                        help="vital-articles levels to include, in importance "
                             "order (default 1,2,3)")
    parser.add_argument("--out", default=DEFAULT_OUT,
                        help=f"output folder (default {DEFAULT_OUT}/)")
    parser.add_argument("--delay", type=float, default=0.1,
                        help="seconds to wait between article downloads")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    levels = tuple(int(x) for x in str(args.levels).replace(" ", "").split(",") if x)

    session = requests.Session()
    session.headers.update(HEADERS)

    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)

    log("Reading the Wikipedia vital-articles lists ...")
    try:
        articles = fetch_vital_articles(session, levels, args.limit)
    except Exception as exc:
        log(f"  ERROR: {exc}")
        return 1
    log(f"  Selected the top {len(articles)} vital articles.")
    if not articles:
        log("  No articles found — aborting.")
        return 1

    log("Fetching descriptions and summaries ...")
    meta = fetch_metadata(session, [a["title"] for a in articles])
    log(f"  Got metadata for {len(meta)}/{len(articles)} articles.")

    retrieved = dt.date.today().isoformat()
    records: list[dict] = []
    failures: list[tuple[str, str]] = []

    log(f"Downloading and converting articles into {out_dir}/ ...")
    for item in articles:
        title = item["title"]
        article_id = f"study_{item['rank']:04d}"
        filename = f"{item['rank']:04d}_{slugify(title)}.md"
        info = meta.get(title, {})
        try:
            html, pageid = fetch_html(session, title)
            body = trim_appendix(html_to_markdown(html))
            if not body:
                raise RuntimeError("empty article body")

            summary = info.get("summary", "")
            if len(summary) > MAX_SUMMARY_CHARS:
                summary = summary[:MAX_SUMMARY_CHARS].rstrip() + "..."

            record = {
                "id": article_id,
                "title": title,
                "rank": item["rank"],
                "level": item["level"],
                "topic": item["topic"],
                "url": info.get("url")
                or f"https://en.wikipedia.org/wiki/{quote(title.replace(' ', '_'))}",
                "pageid": info.get("pageid") or pageid or "",
                "description": info.get("description", ""),
                "summary": summary,
                "retrieved": retrieved,
                "file": filename,
                "body": body,
            }
            (out_dir / filename).write_text(build_article_file(record),
                                            encoding="utf-8")
            records.append(record)
            size_kb = len(record["body"]) / 1024
            log(f"  [{item['rank']:>3}/{len(articles)}] {title} ({size_kb:.0f} KB)")
        except Exception as exc:  # keep going; report at the end
            failures.append((title, str(exc)))
            log(f"  [{item['rank']:>3}/{len(articles)}] SKIP {title}: {exc}")

        time.sleep(args.delay)

    if not records:
        log("Nothing downloaded — aborting before writing an empty corpus.")
        return 1

    generated = dt.datetime.now().isoformat(timespec="seconds")
    write_index(out_dir, records, levels)
    write_readme(out_dir, records, levels, generated)

    log("")
    log(f"Done. {len(records)} articles + index.json + README.md written to {out_dir}/")
    if failures:
        log(f"{len(failures)} article(s) failed:")
        for title, error in failures:
            log(f"  - {title}: {error}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
