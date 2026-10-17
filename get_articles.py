#!/usr/bin/env python3
"""
get_articles.py — build a local corpus of the most-read Wikipedia articles.

WHY THIS EXISTS
    The reading-quiz app takes real articles and turns them into AI-generated
    reading-comprehension quizzes. This script builds the raw material: clean,
    self-contained Markdown files for the most-viewed English Wikipedia
    articles, plus a manifest the backend can load.

WHAT IT DOES
    1. Asks the free Wikimedia Pageviews API which articles were viewed most
       in a given month.
    2. Filters out non-article pages (Main_Page, Special:*, Wikipedia:*, ...).
    3. Downloads each article through the free MediaWiki Action API and
       converts the HTML to clean Markdown (markdownify).
    4. Writes one .md file per article, an index.json manifest, and a README.md
       explaining how to use the corpus.

USAGE
    ./venv/bin/python get_articles.py                 # top 300, latest full month
    ./venv/bin/python get_articles.py --limit 20      # small sample
    ./venv/bin/python get_articles.py --year 2026 --month 9
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
PAGEVIEWS_API = (
    "https://wikimedia.org/api/rest_v1/metrics/pageviews/top/"
    "en.wikipedia/all-access/{year}/{month:02d}/all-days"
)

DEFAULT_LIMIT = 300  # how many articles to keep ("the top N")
DEFAULT_OUT = "articles"

# Pages that live in a MediaWiki namespace are not articles. Anything with one
# of these prefixes is skipped.
NON_ARTICLE_PREFIXES = (
    "Special:", "Wikipedia:", "File:", "Template:", "Category:", "Portal:",
    "Help:", "Talk:", "User:", "User_talk:", "Draft:", "Module:", "MediaWiki:",
    "Book:", "TimedText:", "Media:", "Template_talk:", "Category_talk:",
)

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
    """'Neatsville,_Kentucky' -> 'neatsville_kentucky'."""
    slug = title.lower().replace("&", " and ")
    slug = re.sub(r"[^a-z0-9]+", "_", slug).strip("_")
    return slug[:max_len].strip("_") or "article"


def chunked(items: list, size: int):
    for i in range(0, len(items), size):
        yield items[i:i + size]


def is_article(title: str) -> bool:
    """True when a pageview entry looks like a real, readable article."""
    if title == "Main_Page":
        return False
    if title.startswith(NON_ARTICLE_PREFIXES):
        return False
    if title.endswith("(disambiguation)"):
        return False
    return True


# ---------------------------------------------------------------------------
# Step 1 — which articles were most viewed?
# ---------------------------------------------------------------------------

def fetch_top_pageviews(session: requests.Session, year: int, month: int):
    """Return the ranked pageview list for a month, or None if unavailable."""
    url = PAGEVIEWS_API.format(year=year, month=month)
    resp = session.get(url, timeout=30)
    if resp.status_code == 404:  # month not published yet
        return None
    resp.raise_for_status()
    return resp.json()["items"][0]["articles"]


def resolve_month(session, year=None, month=None):
    """Work out which month to use and return (year, month, ranked_articles).

    Pageview data lags behind the calendar, so when no month is given we walk
    backwards from last month until we find published data.
    """
    if year and month:
        items = fetch_top_pageviews(session, year, month)
        if items is None:
            sys.exit(f"No pageview data published for {year}-{month:02d}.")
        return year, month, items

    today = dt.date.today()
    y, m = today.year, today.month
    for _ in range(6):
        m -= 1
        if m == 0:
            m, y = 12, y - 1
        items = fetch_top_pageviews(session, y, m)
        if items:
            return y, m, items
    sys.exit("Could not find any recent pageview data.")


# ---------------------------------------------------------------------------
# Step 2 — metadata (short description + intro summary) in batches of 50
# ---------------------------------------------------------------------------

def fetch_metadata(session: requests.Session, titles: list[str]) -> dict:
    """Map {underscore_title: {description, summary, pageid, url}}.

    Uses action=query with prop=description|extracts so 50 titles cost one
    request instead of 50.
    """
    meta: dict[str, dict] = {}
    for batch in chunked(titles, 50):
        params = {
            "action": "query",
            "format": "json",
            "formatversion": 2,
            "prop": "description|extracts|info",
            "exintro": 1,
            "explaintext": 1,
            "redirects": 1,
            "inprop": "url",
            "titles": "|".join(batch),
        }
        resp = session.get(ACTION_API, params=params, timeout=30)
        resp.raise_for_status()
        query = resp.json().get("query", {})

        # The API may rename our input (underscores -> spaces) and follow
        # redirects. Build one alias map so we can look results back up by the
        # title we originally asked for.
        alias = {}
        for entry in query.get("normalized", []) + query.get("redirects", []):
            alias[entry["from"]] = entry["to"]

        pages = {p["title"]: p for p in query.get("pages", []) if "missing" not in p}

        for title in batch:
            key, seen = title, set()
            while key in alias and key not in seen:
                seen.add(key)
                key = alias[key]
            page = pages.get(key)
            if not page:
                continue  # redirect to a missing page, etc.
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
        "action": "parse",
        "page": title,
        "prop": "text",
        "format": "json",
        "formatversion": 2,
        "redirects": 1,
        "disableeditsection": 1,
    }
    last_error = None
    for attempt in range(retries):
        try:
            resp = session.get(ACTION_API, params=params, timeout=45)
            resp.raise_for_status()
            data = resp.json()
            if "error" in data:
                raise RuntimeError(data["error"].get("info", "unknown API error"))
            return data["parse"]["text"], data["parse"].get("pageid")
        except (requests.RequestException, RuntimeError, KeyError) as exc:
            last_error = exc
            time.sleep(1.5 * (attempt + 1))  # simple backoff
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
        f"views: {record['views']}",
        f"url: {yaml_quote(record['url'])}",
        f"pageid: {record['pageid']}",
        f"description: {yaml_quote(record['description'])}",
        f"summary: {yaml_quote(record['summary'])}",
        "source: Wikipedia",
        'license: "CC BY-SA 4.0"',
        f"month: \"{record['month']}\"",
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


def write_index(out_dir: Path, records: list[dict], month: str) -> None:
    index = {
        "generated": dt.datetime.now().isoformat(timespec="seconds"),
        "source": "Wikimedia Pageviews API + MediaWiki Action API (en.wikipedia.org)",
        "month": month,
        "count": len(records),
        "license": "CC BY-SA 4.0",
        "articles": [
            {
                "id": r["id"],
                "title": r["title"],
                "file": r["file"],
                "rank": r["rank"],
                "views": r["views"],
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
turned into AI-generated reading-comprehension quizzes.

## What's here

| File | Purpose |
|------|---------|
| `README.md` | This note. |
| `index.json` | Machine-readable manifest of every article. The backend loads this. |
| `study_XXXX_<slug>.md` | One Markdown file per article. |

## Where the data comes from

No API key is required — all endpoints are free and public.

* **Which articles:** the most-viewed English Wikipedia pages for
  **$month**, from the Wikimedia [Pageviews API](https://wikimedia.org/api/rest_v1/)
  (`/metrics/pageviews/top/en.wikipedia/all-access/$month_path/all-days`).
* **Article text:** the MediaWiki [Action API](https://www.mediawiki.org/wiki/API:Main_page)
  (`action=parse`), converted from HTML to Markdown with `markdownify`.
* **Descriptions + intro summaries:** `action=query&prop=description|extracts`.

## Article file format

Every `study_XXXX_<slug>.md` file starts with YAML front matter:

```yaml
---
id: study_0001                # stable id shared by the app and its quiz JSON
title: "Lizzie Borden"
rank: 4                       # position in the monthly pageview ranking
views: 8522591                # pageviews during $month
url: "https://en.wikipedia.org/wiki/Lizzie_Borden"
pageid: 214796                # permanent MediaWiki page id
description: "American woman acquitted of murder (1860–1927)"
summary: "Lizzie Andrew Borden (July 19, 1860 – June 1, 1927) was ..."
source: Wikipedia
license: "CC BY-SA 4.0"
month: "$month"
retrieved: $date
---
```

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
    print(article["id"], article["title"], article["description"])
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
./venv/bin/python get_articles.py                 # top 300, latest full month
./venv/bin/python get_articles.py --limit 20      # small sample
./venv/bin/python get_articles.py --year 2026 --month 9
./venv/bin/python get_articles.py --out other_dir
```

Note: `id` and file names are based on the ranking *for that month*, so they
change if you regenerate with a different month. The `pageid` field is stable
across runs — use it if you need a permanent key.

## Licensing

Wikipedia text is licensed under
[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). Each file links
back to its source article for attribution. Keep that source link (and this
notice) visible in the app, for example on the article page, to stay compliant.
""")


def write_readme(out_dir: Path, count: int, month: str, generated: str) -> None:
    readme = README_TEMPLATE.substitute(
        count=count,
        month=month,
        month_path=month.replace("-", "/"),
        date=dt.date.today().isoformat(),
        generated=generated,
    )
    (out_dir / "README.md").write_text(readme, encoding="utf-8")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--limit", type=int, default=DEFAULT_LIMIT,
                        help=f"how many articles to keep (default {DEFAULT_LIMIT})")
    parser.add_argument("--year", type=int, default=None,
                        help="pageview year (default: latest published month)")
    parser.add_argument("--month", type=int, default=None,
                        help="pageview month 1-12 (default: latest published month)")
    parser.add_argument("--out", default=DEFAULT_OUT,
                        help=f"output folder (default {DEFAULT_OUT}/)")
    parser.add_argument("--delay", type=float, default=0.1,
                        help="seconds to wait between article downloads")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    session = requests.Session()
    session.headers.update(HEADERS)

    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)

    log("Finding the most-viewed articles ...")
    year, month, ranked = resolve_month(session, args.year, args.month)
    month_str = f"{year}-{month:02d}"
    log(f"  Using pageview data for {month_str} ({len(ranked)} entries).")

    candidates = [a for a in ranked if is_article(a["article"])][: args.limit]
    log(f"  Kept the top {len(candidates)} real articles (after filtering namespaces).")

    log("Fetching descriptions and summaries ...")
    meta = fetch_metadata(session, [a["article"] for a in candidates])
    log(f"  Got metadata for {len(meta)}/{len(candidates)} articles.")

    retrieved = dt.date.today().isoformat()
    records: list[dict] = []
    failures: list[tuple[str, str]] = []

    log(f"Downloading and converting articles into {out_dir}/ ...")
    for position, entry in enumerate(candidates, start=1):
        title = entry["article"]
        article_id = f"study_{position:04d}"
        filename = f"{article_id}_{slugify(title)}.md"
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
                "title": title.replace("_", " "),
                "rank": entry["rank"],
                "views": entry["views"],
                "url": info.get("url")
                or f"https://en.wikipedia.org/wiki/{quote(title)}",
                "pageid": info.get("pageid") or pageid or "",
                "description": info.get("description", ""),
                "summary": summary,
                "month": month_str,
                "retrieved": retrieved,
                "file": filename,
                "body": body,
            }
            (out_dir / filename).write_text(build_article_file(record),
                                            encoding="utf-8")
            records.append(record)
            size_kb = len(record["body"]) / 1024
            log(f"  [{position:>3}/{len(candidates)}] {record['title']} ({size_kb:.0f} KB)")
        except Exception as exc:  # keep going; report at the end
            failures.append((title, str(exc)))
            log(f"  [{position:>3}/{len(candidates)}] SKIP {title}: {exc}")

        time.sleep(args.delay)

    if not records:
        log("Nothing downloaded — aborting before writing an empty corpus.")
        return 1

    generated = dt.datetime.now().isoformat(timespec="seconds")
    write_index(out_dir, records, month_str)
    write_readme(out_dir, len(records), month_str, generated)

    log("")
    log(f"Done. {len(records)} articles + index.json + README.md written to {out_dir}/")
    if failures:
        log(f"{len(failures)} article(s) failed:")
        for title, error in failures:
            log(f"  - {title}: {error}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
