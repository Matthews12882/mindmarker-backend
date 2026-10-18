# Deploying the content API to Cloudflare

This repo ships a small [Cloudflare Worker](https://developers.cloudflare.com/workers/)
that serves the article corpus and the quizzes and adds a JSON API on top of
them, so your frontend can call things like:

```
https://apicongressapp2026backend.mydomain.com/api/quizzes/0001/easy
https://apicongressapp2026backend.mydomain.com/api/articles?topic=History
https://apicongressapp2026backend.mydomain.com/api/random?difficulty=medium
```

## How it fits together

```
GitHub repo (articles/ + quizzes/ + src/ + scripts/)
        │  push to main
        ▼
Cloudflare Workers Builds ── npm run build ──▶ public/   (static assets)
        │  npx wrangler deploy
        ▼
Worker: congressional-app-backend-2026
        ├── /api/*              → src/index.js  (the JSON API)
        ├── /articles, /articles/* → src/index.js → static assets
        ├── /quizzes,  /quizzes/*  → src/index.js → static assets
        └── everything else     → static assets
        │
        ▼
https://apicongressapp2026backend.mydomain.com
```

The 300 articles and 900 quizzes are **uploaded as static assets**, not bundled
into the Worker, so they stay fast to serve. The Worker only sits in front of
them to add the API, CORS headers and explicit content types — it never copies
the files.

## What was added

| File | Purpose |
|------|---------|
| `src/index.js` | The Worker: a dependency-free JSON API over the content. |
| `scripts/build-public.mjs` | Copies `articles/` + `quizzes/` into `public/` and generates `public/quizzes/index.json`. Uses only Node built-ins. |
| `tests/api.test.mjs` | End-to-end checks for the API against the real corpus (`npm test`). |
| `wrangler.jsonc` | Worker configuration (entry point, static assets, `ASSETS` binding). |
| `package.json` | `build` / `dev` / `deploy` scripts and the `wrangler` dev dependency. |
| `DEPLOY.md` | This file. |

`public/` is generated and git-ignored — Cloudflare rebuilds it on every push.

## Prerequisites

1. A Cloudflare account.
2. Your domain (e.g. `mydomain.com`) added as an **active zone** in that account
   (nameservers pointed at Cloudflare). Custom domains only work on zones you
   own.
3. This repo pushed to GitHub (it already is).

You do **not** need Node or Wrangler installed locally for Option A.

---

## Option A — Connect the GitHub repo (recommended)

Every push to `main` rebuilds and redeploys automatically.

1. Push these new files first:

   ```bash
   git add package.json wrangler.jsonc src scripts DEPLOY.md .gitignore
   git commit -m "Add Cloudflare Worker content API"
   git push
   ```

2. In the Cloudflare dashboard, open **Workers & Pages**
   ([dash.cloudflare.com](https://dash.cloudflare.com/?to=/:account/workers-and-pages)).
3. Select **Create application** → **Workers** → **Import a repository**
   (GitHub). Authorise the Cloudflare GitHub App and pick
   `Matthews12882/congressional-app-backend-2026`.
4. Configure the build:
   - **Build command:** `npm run build`
   - **Deploy command:** `npx wrangler deploy` (the default)
   - **Root directory:** leave empty
5. **Save and Deploy.**

> The Worker name in the dashboard **must** equal `name` in `wrangler.jsonc`
> (`congressional-app-backend-2026`), otherwise the build fails. If the
> dashboard auto-named it something else, rename it or edit `wrangler.jsonc`.

You now have a public URL like
`https://congressional-app-backend-2026.<your-subdomain>.workers.dev`. Test it:

```bash
curl -s https://congressional-app-backend-2026.<your-subdomain>.workers.dev/api/quizzes/0001/easy | head -c 400
```

---

## Attach your custom domain

You want `apicongressapp2026backend.mydomain.com` (replacing `mydomain.com`).

**In the dashboard:** Worker → **Settings** → **Domains & Routes** → **Add** →
**Custom domain** → enter `apicongressapp2026backend.mydomain.com` → **Add
Custom Domain**. Cloudflare creates the DNS record and the TLS certificate for
you.

**Or declaratively** — in `wrangler.jsonc` uncomment the `routes` block and
commit it:

```jsonc
"routes": [
  { "pattern": "apicongressapp2026backend.mydomain.com", "custom_domain": true }
]
```

Then the next deploy attaches it. (Custom domains do not support wildcards, and
the hostname must not already have a CNAME record.)

---

## Option B — Deploy from your own machine

Useful for iterating locally without pushing.

```bash
# Node.js 20+ is required
npm install
npx wrangler login          # opens a browser to authorise
npm test                    # build + check the API against the real corpus
npm run dev                 # http://localhost:8787 — live-reloads the Worker
npm run deploy              # builds public/ and deploys
```

`npm run dev` also lets you hit the API locally at
`http://localhost:8787/api/...`.

---

## API reference

All responses are JSON with `Access-Control-Allow-Origin: *`, so any frontend
origin can call them. `GET`/`HEAD`/`OPTIONS` only.

| Endpoint | Description |
|----------|-------------|
| `GET /api/health` | Liveness check. |
| `GET /api/topics` | Topics with article counts. |
| `GET /api/articles` | Article list. Query: `topic`, `level` (1–3), `q` (search), `limit` (≤1000, default 100), `offset`, `random=1`. |
| `GET /api/articles/:id` | One article's metadata. Add `?include=content` for the full Markdown body. |
| `GET /api/quizzes` | Quiz list. Query: `article_id`, `difficulty`, `topic`, `limit`, `offset`. |
| `GET /api/quizzes/:articleId` | All three difficulties for an article. |
| `GET /api/quizzes/:articleId/:difficulty` | One quiz. |
| `GET /api/random` | A random article + one random quiz. Query: `difficulty`, `topic`, `level`. |

`:id` accepts `1`, `0001` or `0001_the_arts`. `:difficulty` is `easy`, `medium`
or `hard`.

### Browsing the raw content

The files themselves are also served, so you can open them in a browser or fetch
them directly from the frontend:

| Path | Returns |
|------|---------|
| `GET /articles` | Every article file, with each `file_url` and `api_url`. |
| `GET /articles/<file>.md` | The raw Markdown (front matter + body). |
| `GET /articles/index.json` | The corpus manifest. |
| `GET /quizzes` | Every quiz file, with each `file_url` and `api_url`. |
| `GET /quizzes/<file>.json` | The raw quiz JSON, exactly as stored. |
| `GET /quizzes/index.json` | The quiz manifest. |

```bash
curl https://apicongressapp2026backend.mydomain.com/articles
curl https://apicongressapp2026backend.mydomain.com/articles/0001_the_arts.md
curl https://apicongressapp2026backend.mydomain.com/quizzes/0001_the_arts_easy.json
```

Notes:

- The short filename works too: `/articles/0001.md` and `/quizzes/0001_easy.json`
  resolve to the real file through the indexes.
- `.md` is served as **`text/plain`**, not `text/markdown`, because Firefox and
  Safari *download* `text/markdown` instead of displaying it. With `text/plain`
  every browser shows the article inline.
- Raw files carry the same `Access-Control-Allow-Origin: *` as the API, so a
  frontend on another origin can `fetch()` them.
- `..`-style paths and dotfiles are rejected with a 404.

Raw files keep the stored shape (`options[0]` is the correct answer). Use
`/api/quizzes/...` when you want the shuffled, client-ready version.

### Quiz shape

The stored files always keep the **correct option at `options[0]`**. The API
fixes that for you: by default it **shuffles the options per request** and tells
you where the answer landed, so the client never has to shuffle and the answer
isn't always first.

```jsonc
// GET /api/quizzes/0001/easy
{
  "article_id": "0001",
  "difficulty": "easy",
  "question_count": 10,
  "shuffled": true,
  "questions": [
    {
      "id": 1,
      "question": "What are the three main branches of the arts?",
      "options": ["music, dance, theatre", "visual arts, literature, and performing arts", "..."],
      "answer_index": 1,
      "answer": "visual arts, literature, and performing arts",
      "answer_explanations": ["...", "Correct. ...", "...", "..."]  // aligned with options
    }
  ]
}
```

Useful query flags on the quiz endpoints:

- `?shuffle=0` — keep the stored option order (`answer_index` will be `0`).
- `?raw=1` — return the quiz file exactly as it is on disk.

Article metadata (title, topic, source URL, license) lives on the article
endpoint, not in the quiz — join the two on `article_id`.

### Caching

List and topic responses are cached at the edge for 1 hour; article and quiz
content for 24 hours. Content is immutable per deploy, so this is safe. If you
ever change a file in place without changing its name, purge the cache
(**Caching → Configuration → Purge Everything**) or wait out the TTL.

---

## Calling it from the frontend

```js
const API = "https://apicongressapp2026backend.mydomain.com";

// Browse history articles
const { articles } = await fetch(`${API}/api/articles?topic=History&limit=20`)
  .then((r) => r.json());

// Read one article
const article = await fetch(`${API}/api/articles/0001?include=content`)
  .then((r) => r.json());
console.log(article.title, article.markdown);

// Play a quiz
const quiz = await fetch(`${API}/api/quizzes/0001/easy`).then((r) => r.json());
const q = quiz.questions[0];
const isRight = selectedIndex === q.answer_index;
console.log(q.answer_explanations[selectedIndex]);

// "Surprise me"
const { article: randomArticle, quiz: randomQuiz } =
  await fetch(`${API}/api/random?difficulty=medium`).then((r) => r.json());

// Raw Markdown, if you would rather render it yourself (same CORS, no key)
const markdown = await fetch(`${API}/articles/0001_the_arts.md`).then((r) => r.text());
```

No API key and no CORS setup is needed. If you later restrict the origin
(tighter than `*`), edit `CORS_HEADERS` in `src/index.js`.

---

## Updating the content

The pipeline stays the same — only the deploy changes:

```bash
./venv/bin/python get_articles.py        # refresh articles/
./venv/bin/python generate_quizzes.py    # add/refresh quizzes/
./venv/bin/python validate_quizzes.py    # sanity-check the format
git add articles quizzes && git commit -m "Refresh content" && git push
```

Cloudflare rebuilds and redeploys on push. The build **fails loudly** if a quiz
file has no matching article or if an article is missing quizzes, so a broken
corpus never goes live.

---

## Option C — Cloudflare Pages instead of Workers

Workers with static assets is the current recommendation and is what this repo
is set up for, but Pages works too:

1. **Workers & Pages → Create → Pages → Connect to Git**, pick the repo.
2. **Build command:** `npm run build` · **Build output directory:** `public`
3. Move the API logic from `src/index.js` into a Pages Function at
   `functions/api/[[route]].js` and export `onRequestGet` (Pages Functions use
   the same Workers runtime, so the handler body is unchanged — you'd just
   forward `env.ASSETS` and adapt the request).

Stay with Workers: one config file, the API and the files share a Worker, and
custom domains and Git deploys are the same experience.

---

## Troubleshooting

| Symptom | Fix |
|---------|-----|
| Build fails: *Worker name must match* | The dashboard Worker name must equal `name` in `wrangler.jsonc`. Rename one to match. |
| `assets/... not found` at deploy | The build step didn't run. Set the build command to `npm run build`. |
| `/api/...` returns 404 | Check the path against the table above. `/api/quizzes/0001/easy` — not `/api/quiz/...`. |
| Every route 404s | `public/` was empty. Confirm `npm run build` copies files (it prints the counts). |
| Custom domain rejected | The apex must be an active Cloudflare zone and the hostname must have no existing CNAME. |
| Stale quiz data after an edit | Content is cached for 24 h — purge the cache or rename the file. |
| Build log shows missing quiz warnings | An article has fewer than 3 quizzes; the API skips the missing ones but keeps working. |

## Free tier

Workers Free includes 100,000 requests/day; static asset requests are not
billed as Worker invocations. The corpus is ~1,200 small files (well under the
20,000-file and 25 MiB-per-file limits), so this comfortably fits the free plan.

## Keep the attribution

Article text is Wikipedia content under
[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). Every article
endpoint returns the `url` and the raw file links back to its source, so keep a
visible source link on the article screen.
