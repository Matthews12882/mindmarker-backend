# Reading Quiz — Backend

> Pick a real article, read it, and prove you understood it with an AI-generated
> quiz. Think **Duolingo for reading comprehension** — gamified, competitive, and
> built on real, high-quality sources instead of made-up passages.

*Working title — Congressional App Challenge 2026 project.*

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
| AI quiz generation (`generate_quizzes.py`) | ✅ done (900 quizzes for 300 articles) |
| Content API (Cloudflare Worker + static assets) | ✅ done — see [`DEPLOY.md`](DEPLOY.md) |
| Database / users / progress | ⏳ planned |
| Frontend / gamification | ⏳ planned |

The backend currently produces a local, self-contained corpus of articles and
pre-generated quizzes that the rest of the app (API, UI) will build on.

## Repo layout

```
congressional-app-backend-2026/
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

## Deploying the API

The corpus and quizzes are served by a Cloudflare Worker (static assets + a
small JSON API) so the frontend can read them over HTTP, for example:

```
GET https://apicongressapp2026backend.<domain>/api/articles?topic=History
GET https://apicongressapp2026backend.<domain>/api/quizzes/0001/easy
GET https://apicongressapp2026backend.<domain>/api/random?difficulty=medium
```

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
- **AI** — quizzes are **pre-generated** in a batch job and stored, not created
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

- [x] Generate + review a batch of quizzes from the corpus (AI pipeline)
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
