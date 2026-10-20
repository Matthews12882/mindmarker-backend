# Mindmarker — Backend

> Pick a real article, read it, and prove you understood it with an SI-generated
> quiz. Think **Duolingo for reading comprehension** — gamified, competitive, and
> built on real, high-quality sources instead of made-up passages.

*Mindmarker — a Congressional App Challenge 2026 project.*

---

## The idea

Most reading-comprehension tools use short, generic, artificial passages. This
project instead uses **real articles** (starting with Wikipedia's *Vital
articles* — a curated ranking of the most important general-knowledge topics)
and generates **multiple-choice quizzes** for each one with an LLM. Users
read the article, answer the questions, get feedback and explanations, and earn
points that feed streaks, levels and leaderboards.

Design goals:

- **Anyone can use it** — no account required to read and quiz; simple flow.
- **Idea first, polish second** — the concept should be obvious within seconds.
- **Gamified** — points, levels and streaks to make study feel like a game.

## Status

| Area | State |
|------|-------|
| Article corpus (300 vital articles as clean Markdown) | ✅ done |
| `get_articles.py` downloader | ✅ done |
| SI quiz generation (`generate_quizzes.py`) | ✅ done (900 quizzes for 300 articles) |
| Content API (Cloudflare Worker + static assets) | ✅ done — see [`DEPLOY.md`](DEPLOY.md) |
| Database / users / progress | ⏳ planned |
| Frontend / gamification | ⏳ planned |

The backend currently produces a local, self-contained corpus of articles and
pre-generated quizzes that the rest of the app (API, UI) will build on.

## Repo layout

```
mindmarker-backend/
├── get_articles.py       # downloads the top "vital" Wikipedia articles as Markdown
├── articles/             # the generated corpus (300 .md files)
│   ├── README.md         #   how to use the corpus (read this)
│   ├── index.json        #   machine-readable manifest the backend loads
│   └── NNNN_<slug>.md
├── generate_quizzes.py   # batch-generates the quizzes with a free LLM
├── validate_quizzes.py   # checks every quiz against the format invariants
├── quizzes/              # 900 pre-generated quizzes (300 articles x 3 levels)
│   ├── README.md         #   quiz format + generation spec (read this)
│   ├── quiz_prompt.md    #   the reusable generation prompt
│   └── NNNN_<slug>_<difficulty>.json
├── articles.json         # placeholder (reserved)
├── src/index.js          # Cloudflare Worker: the /api/* JSON API
├── scripts/build-public.mjs  # assembles public/ (the deployed static assets)
├── wrangler.jsonc        # Cloudflare Worker configuration
├── package.json          # build / dev / deploy scripts
├── DEPLOY.md             # how to deploy the API on Cloudflare
├── CITATION.cff          # how to cite this repo (incl. SI attribution)
├── tests/api.test.mjs    # API checks against the real corpus (npm test)
├── venv/                 # local virtualenv (not tracked)
└── README.md             # this file
```

## Quick start

```bash
# 1. Create / reuse the virtualenv
python3 -m venv venv
./venv/bin/pip install requests beautifulsoup4 markdownify

# 2. (Re)build the article corpus — ~6 min for the full run
./venv/bin/python get_articles.py              # top 300 vital articles
./venv/bin/python get_articles.py --limit 20   # fast sample

# 3. Sanity-check the result
./venv/bin/python -c "import json;print(json.load(open('articles/index.json'))['count'], 'articles')"

# 4. (Optional) regenerate quizzes — needs OPENROUTER_API_KEY in .env
./venv/bin/python generate_quizzes.py     # resumes pending articles
./venv/bin/python validate_quizzes.py     # checks the JSON invariants
```

Building the corpus needs no API keys — only free, public Wikipedia endpoints
are used. Quiz generation calls OpenRouter and reads `OPENROUTER_API_KEY`
(see `.env.example`).

## The article corpus

`get_articles.py` walks Wikipedia's **[Vital articles](https://en.wikipedia.org/wiki/Wikipedia:Vital_articles)**
lists (Levels 1–3), which rank the most important general-knowledge topics, and
takes them in importance order (Level 1 → 2 → 3). It resolves each entry to a
real article, downloads the HTML through the MediaWiki Action API, and converts
it to clean Markdown with `markdownify`. Each file carries YAML front matter
(id, title, rank, level, topic, url, description, summary, license, …).

See **[`articles/README.md`](articles/README.md)** for the full file format, the
cleaning rules, and copy-paste snippets for loading the corpus.

## Data conventions

One stable id ties an article, its quiz, and a user's progress together:

```jsonc
// article front matter
id: 0001

// quiz JSON
{
  "article_id": "0001",
  "difficulty": "easy",
  "question_count": 10,
  "questions": [ /* ... */ ]
}
```

`articles/index.json` is the source of truth for the list of articles. The
`pageid` field is Wikimedia's permanent page id — use it as a durable key if the
ranking-based `NNNN` ids ever change.

## Public API

The backend is live at **https://api.mindmarker.dev**. It is read-only: `GET`,
`HEAD` and `OPTIONS` are supported, and every response includes
`Access-Control-Allow-Origin: *` so browser clients can call it directly.

### Content files

The raw corpus can be browsed without going through the JSON API:

| Endpoint | Returns |
|----------|---------|
| `GET /articles` | JSON index of all 300 articles, including each article's `file_url` and `api_url` |
| `GET /articles/<id>.md` or `GET /articles/<id>_<slug>.md` | One article as raw Markdown (YAML front matter + body) |
| `GET /quizzes` | JSON index of all 900 quiz files, with `file_url` and `api_url` |
| `GET /quizzes/<id>_<difficulty>.json` or `GET /quizzes/<id>_<slug>_<difficulty>.json` | One quiz as JSON |

Ids are zero-padded automatically, so `1` and `0001` identify the same article.
The slug is optional, and lookups are case-insensitive.

**Articles — all of these return the same Markdown:**

```bash
curl https://api.mindmarker.dev/articles/0001.md
curl https://api.mindmarker.dev/articles/1.md
curl https://api.mindmarker.dev/articles/0001_the_arts.md
```

```markdown
---
id: 0001
title: "The arts"
rank: 1
level: 1
topic: "Core topics"
...
---

# The arts
...
```

**Quizzes — all of these return the same JSON:**

```bash
curl https://api.mindmarker.dev/quizzes/0001_hard.json
curl https://api.mindmarker.dev/quizzes/1_hard.json
curl https://api.mindmarker.dev/quizzes/0001_the_arts_hard.json
```

```json
{
  "article_id": "0001",
  "difficulty": "hard",
  "question_count": 10,
  "questions": [
    {
      "id": 1,
      "question": "An artist presents a work that consists only of a written set of instructions, producing no physical object. Based on the article's description, this work is best understood as an example of which category?",
      "options": ["Conceptual art", "Ceramic art", "Photography", "Applied art"],
      "answer_explanations": [
        "Correct. The article defines conceptual art as art ...",
        "Incorrect. Ceramic art is made from ceramic materials ...",
        "Incorrect. Photography is a visual art ...",
        "Incorrect. Applied art applies design and decoration ..."
      ]
    }
  ]
}
```

Stored quiz files keep the correct option first, with `answer_explanations` in the
same order as `options`. The `/api` quiz endpoints shuffle by default and add
`answer_index` and `answer` (see below).

### JSON API

All JSON endpoints live under `/api`. Lists are paginated with `limit` (default
100, max 1000) and `offset`; filters can be combined with `&`.

| Endpoint | Description |
|----------|-------------|
| `GET /api/health` | Service health check |
| `GET /api/topics` | Topics and article counts |
| `GET /api/articles?topic=&level=&q=&limit=&offset=&random=1` | Search/filter articles; `random=1` returns one instead of a list |
| `GET /api/articles/:id?include=content` | One article; add `include=content` (or `content=1`) to include its Markdown |
| `GET /api/quizzes?article_id=&difficulty=&topic=&limit=&offset=` | Search/filter quizzes |
| `GET /api/quizzes/:articleId` | All available difficulties for one article |
| `GET /api/quizzes/:articleId/:difficulty?shuffle=0&raw=1` | One quiz. Options are shuffled by default; `shuffle=0` keeps stored order, `raw=1` returns the original file |
| `GET /api/random?difficulty=&topic=&level=` | A random article plus a quiz |

### Query examples

#### Articles

```bash
# first page (100 by default)
curl "https://api.mindmarker.dev/api/articles"

# filter by topic and level
curl "https://api.mindmarker.dev/api/articles?topic=History&level=3&limit=5"

# search titles and descriptions
curl "https://api.mindmarker.dev/api/articles?q=roman&limit=5"

# paginate
curl "https://api.mindmarker.dev/api/articles?limit=2&offset=2"

# one random match
curl "https://api.mindmarker.dev/api/articles?topic=History&random=1"
```

`count` is the number of matches after filtering, while `total_articles` is the
size of the whole corpus. For example, `/api/articles?topic=History&limit=1`
returns:

```json
{
  "total_articles": 300,
  "count": 78,
  "limit": 1,
  "offset": 0,
  "articles": [
    {
      "id": "0011",
      "title": "History",
      "rank": 11,
      "level": 2,
      "topic": "History",
      "description": "Study of the past",
      "pageid": 10772350,
      "url": "https://en.wikipedia.org/wiki/History",
      "file": "0011_history.md"
    }
  ]
}
```

A single article accepts the same id forms as the content routes, so
`/api/articles/1`, `/api/articles/0001` and `/api/articles/0001_the_arts` are
equivalent. Add `include=content` (or `content=1`) to include the Markdown:

```bash
curl "https://api.mindmarker.dev/api/articles/0001?include=content"
```

```json
{
  "id": "0001",
  "title": "The arts",
  "...": "...",
  "markdown": "---\nid: 0001\n..."
}
```

#### Quizzes

```bash
# every quiz for one article
curl "https://api.mindmarker.dev/api/quizzes?article_id=0001"

# filter by topic and difficulty
curl "https://api.mindmarker.dev/api/quizzes?topic=History&difficulty=hard&limit=2"

# all three difficulties for one article, or just one
curl "https://api.mindmarker.dev/api/quizzes/0001"
curl "https://api.mindmarker.dev/api/quizzes/0001/hard"

# article ids accept the same short and slug forms
curl "https://api.mindmarker.dev/api/quizzes/1/hard"
curl "https://api.mindmarker.dev/api/quizzes/0001_the_arts/hard"
```

`/api/quizzes?article_id=0001` returns:

```json
{
  "count": 3,
  "limit": 100,
  "offset": 0,
  "quizzes": [
    {
      "article_id": "0001",
      "difficulty": "easy",
      "file": "0001_the_arts_easy.json",
      "base": "0001_the_arts"
    }
  ]
}
```

`/api/quizzes/0001` returns all available difficulties. A single quiz is
returned by `/api/quizzes/<id>/<difficulty>`:

```json
{
  "article_id": "0001",
  "difficulty": "hard",
  "question_count": 10,
  "shuffled": true,
  "questions": [
    {
      "id": 1,
      "question": "...",
      "options": ["...", "...", "...", "..."],
      "answer_index": 0,
      "answer": "...",
      "answer_explanations": ["...", "...", "...", "..."]
    }
  ]
}
```

Options are shuffled by default, so `answer_index` points at the correct option.
Use `shuffle=0` to keep the stored order, or `raw=1` to return the original file
shape without `answer_index`/`answer`.

#### Random article + quiz

```bash
curl "https://api.mindmarker.dev/api/random?difficulty=medium&topic=History"
```

Returns one article and one matching quiz:

```json
{
  "article": {
    "id": "0267",
    "title": "Cold War",
    "topic": "History",
    "...": "..."
  },
  "quiz": {
    "article_id": "0267",
    "difficulty": "medium",
    "question_count": 10,
    "questions": [{"id": 1, "...": "..."}]
  }
}
```

`difficulty`, `topic` and `level` are optional and combine as filters.

#### Topics and health

```bash
curl "https://api.mindmarker.dev/api/topics"
curl "https://api.mindmarker.dev/api/health"
```

`/api/topics` returns topic names and article counts (`People` 97, `History` 78,
`Geography` 42, …). `/api/health` returns the service status and current time.

The service index at `/` (also `/api`) lists the endpoint summary and corpus
counts. Errors are JSON, for example:

```json
{"error":{"status":404,"message":"No article with id \"9999\"."}}
```

## Self-hosting / deployment

The public deployment is a Cloudflare Worker (static assets + the JSON API).
To run or deploy your own copy:

```bash
npm run dev       # local Worker at http://localhost:8787
npm run deploy    # build public/ and deploy
```

Full setup, GitHub auto-deploy, the custom domain and the endpoint reference are
in **[`DEPLOY.md`](DEPLOY.md)**.

## Planned architecture

- **Frontend / UI** — Streamlit (fast prototyping) or HTML; article browse +
  random-article button, reading view, quiz view, gamified progress page.
- **Backend / API** — ✅ Cloudflare Worker serving the corpus and quizzes as
  static assets behind a JSON API (`src/index.js`, see [`DEPLOY.md`](DEPLOY.md)).
- **Database** — PostgreSQL (Supabase-friendly). Simple, id-linked tables:
  `content` (articles/quizzes), `users` (profile, prefs), `progress`
  (completed articles/quizzes), `achievements` (points, level, badges).
- **SI** — quizzes are **pre-generated** in a batch job and stored, not created
  on the fly (faster and far cheaper at request time).

## Tech stack

| Layer | Choice |
|-------|--------|
| Language | Python |
| Article fetching | `requests`, `beautifulsoup4`, `markdownify` |
| Data source | Wikipedia Vital articles + MediaWiki Action API (free) |
| Database | PostgreSQL / Supabase (planned) |
| Packaging | Docker (planned) |

## Roadmap

- [x] Generate + review a batch of quizzes from the corpus (SI pipeline)
- [ ] Define and store the article/quiz schema in PostgreSQL
- [x] Build the API (random article, get article + quiz, submit answers)
- [ ] Gamification: points, levels, streaks, badges
- [ ] Streamlit frontend: browse → read → quiz → results

## Team

| Person | Focus |
|--------|-------|
| Matthew | Backend, API config, data schemas |
| Kyle | Frontend / UI, article & quiz screens |
| Quinn | Gamification and "juice" (points, levels, streaks) |

## Licensing & attribution

Article text is from Wikipedia under
**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)**. Every
corpus file links back to its source article for attribution — keep that source
link (and the license notice) visible in the app, for example on the article
page, to stay compliant.

Articles are grouped by subject in the `topic` field (`History`, `Geography`,
`People`, `Science and medicine`, `Arts`, …) — handy for building "browse by
subject" screens or nudging users toward a topic they haven't tried yet.

## Credits & citation

- **Development assistance:** Google Gemini — code and general repository
  structure.
- **Articles:** sourced from Wikipedia's *Vital articles*
  (CC BY-SA 4.0 — see above).
- **Quizzes:** generated by **Wild DeepSeek** through OpenRouter
  (`generate_quizzes.py`).

To cite this repository, use **[`CITATION.cff`](CITATION.cff)** (GitHub shows a
**Cite this repository** button for it) or the reference below:

```bibtex
@misc{mindmarker-backend,
  title        = {Mindmarker — Backend},
  author       = {Matthew and Kyle and Quinn},
  year         = {2026},
  howpublished = {\url{https://github.com/Matthews12882/mindmarker-backend}},
  note         = {Development assisted by Google Gemini; quizzes generated by Wild DeepSeek.}
}
```
