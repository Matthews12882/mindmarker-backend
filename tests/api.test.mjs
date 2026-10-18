#!/usr/bin/env node
/**
 * End-to-end checks for the content API in src/index.js.
 *
 * Runs the Worker against the real files in `public/` with the Cloudflare-only
 * bits (`caches`, `ctx.waitUntil`, `env.ASSETS`) stubbed, so it needs no
 * network, no account and no wrangler — just Node 20+.
 *
 *   npm test            # builds public/ first, then runs these checks
 *   node tests/api.test.mjs
 */
import { readFile, stat } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const PUBLIC = path.join(ROOT, "public");

// --- minimal Workers runtime stubs -----------------------------------------
globalThis.caches = {
  default: {
    async match() {
      return undefined;
    },
    async put() {},
  },
};

const env = {
  ASSETS: {
    async fetch(request) {
      const url = typeof request === "string" ? new URL(request) : new URL(request.url);
      const file = path.join(PUBLIC, decodeURIComponent(url.pathname));
      try {
        const info = await stat(file);
        if (!info.isFile()) throw new Error("not a file");
        const body = await readFile(file);
        const type = file.endsWith(".json")
          ? "application/json"
          : file.endsWith(".md")
            ? "text/markdown"
            : "application/octet-stream";
        return new Response(body, { status: 200, headers: { "content-type": type } });
      } catch {
        return new Response("not found", { status: 404 });
      }
    },
  },
};
const ctx = { waitUntil() {}, passThroughOnException() {} };

const worker = (await import(pathToFileURL(path.join(ROOT, "src/index.js")).href)).default;

// --- tiny test harness ------------------------------------------------------
let pass = 0;
let fail = 0;

async function check(name, fn) {
  try {
    await fn();
    console.log(`ok   ${name}`);
    pass += 1;
  } catch (error) {
    console.log(`FAIL ${name}\n     ${error.message}`);
    fail += 1;
  }
}

function assert(condition, message) {
  if (!condition) throw new Error(message);
}

const get = (pathname, init) =>
  worker.fetch(new Request(`https://api.example.com${pathname}`, init), env, ctx);

async function json(pathname) {
  const response = await get(pathname);
  assert(response.status === 200, `${pathname} -> HTTP ${response.status}`);
  return response.json();
}

// --- tests ------------------------------------------------------------------
await check("GET /api/health", async () => {
  assert((await json("/api/health")).status === "ok", "status not ok");
});

await check("GET /api reports the corpus size", async () => {
  const body = await json("/api");
  assert(body.counts.articles === 300, `articles=${body.counts.articles}`);
  assert(body.counts.quizzes === 900, `quizzes=${body.counts.quizzes}`);
});

await check("GET /api/topics", async () => {
  const body = await json("/api/topics");
  assert(body.count === 11, `topics=${body.count}`);
});

await check("GET /api/articles lists + paginates", async () => {
  assert((await json("/api/articles?limit=1000")).count === 300, "not 300 articles");
  const page = await json("/api/articles?limit=10&offset=20");
  assert(page.articles.length === 10, `page size=${page.articles.length}`);
  assert(page.articles[0].id === "0021", `first id=${page.articles[0].id}`);
});

await check("GET /api/articles filters by topic / level / q", async () => {
  assert((await json("/api/articles?topic=History&limit=1000")).count === 78, "topic filter");
  assert((await json("/api/articles?level=1&limit=1000")).count === 10, "level filter");
  const search = await json("/api/articles?q=philippines&limit=1000");
  assert(search.articles.some((a) => a.title === "Philippines"), "search filter");
});

await check("GET /api/articles/:id metadata + content", async () => {
  const meta = await json("/api/articles/0001");
  assert(meta.title === "The arts", `title=${meta.title}`);
  assert(meta.markdown === undefined, "metadata should not include markdown");
  const full = await json("/api/articles/0001?include=content");
  assert(full.markdown.startsWith("---"), "front matter missing");
  assert(full.markdown.length > 5000, "markdown body too small");
});

await check("article ids normalise (1 / 0001 / 0001_the_arts)", async () => {
  for (const id of ["1", "0001", "0001_the_arts"]) {
    assert((await json(`/api/articles/${id}`)).id === "0001", `${id} failed`);
  }
});

await check("GET /api/quizzes lists + filters", async () => {
  assert((await json("/api/quizzes?limit=1000")).count === 900, "not 900 quizzes");
  assert((await json("/api/quizzes?difficulty=easy&limit=1000")).count === 300, "difficulty filter");
  assert((await json("/api/quizzes?article_id=0001")).count === 3, "article filter");
});

await check("GET /api/quizzes/:id returns all difficulties", async () => {
  const body = await json("/api/quizzes/0001");
  assert(body.quizzes.length === 3, `quizzes=${body.quizzes.length}`);
  assert(body.available_difficulties.join(",") === "easy,medium,hard", "difficulties");
});

await check("quiz shape is valid and answers line up", async () => {
  const quiz = await json("/api/quizzes/0001/easy");
  assert(quiz.question_count === 10, `question_count=${quiz.question_count}`);
  assert(quiz.shuffled === true, "expected shuffled output");
  for (const q of quiz.questions) {
    assert(q.options.length === 4, `options=${q.options.length}`);
    assert(q.answer_explanations.length === 4, "explanations length");
    assert(q.answer_index >= 0 && q.answer_index < 4, `answer_index=${q.answer_index}`);
    assert(q.answer === q.options[q.answer_index], "answer/answer_index mismatch");
    assert(
      q.answer_explanations[q.answer_index].startsWith("Correct."),
      "explanation at answer_index is not the correct one",
    );
  }
});

await check("shuffling moves the answer without changing it", async () => {
  const raw = JSON.parse(
    await readFile(path.join(PUBLIC, "quizzes", "0001_the_arts_easy.json"), "utf8"),
  );
  const expected = raw.questions[0].options[0];
  const positions = new Set();
  for (let i = 0; i < 200; i += 1) {
    const q = (await json("/api/quizzes/0001/easy")).questions[0];
    assert(q.answer === expected, "shuffled answer changed");
    positions.add(q.answer_index);
  }
  assert(positions.size >= 3, `answer_index only took ${positions.size} values`);
});

await check("?shuffle=0 keeps stored order; ?raw=1 is untouched", async () => {
  const ordered = await json("/api/quizzes/0001/easy?shuffle=0");
  assert(ordered.questions.every((q) => q.answer_index === 0), "not in stored order");
  const raw = await json("/api/quizzes/0001/easy?raw=1");
  assert(raw.questions[0].answer_index === undefined, "raw should not add answer_index");
});

await check("GET /api/random returns an article + quiz", async () => {
  const body = await json("/api/random?difficulty=medium");
  assert(body.article?.id, "no article");
  assert(body.quiz?.difficulty === "medium", "wrong difficulty");
  assert(body.quiz.questions.length === 10, "wrong question count");
  assert((await json("/api/random?topic=Geography")).article.topic === "Geography", "topic filter");
});

await check("errors: 404 and 400 responses", async () => {
  assert((await get("/api/nope")).status === 404, "unknown endpoint");
  assert((await get("/api/articles/9999")).status === 404, "unknown article");
  assert((await get("/api/quizzes/9999")).status === 404, "unknown quiz");
  assert((await get("/api/quizzes/0001/impossible")).status === 400, "invalid difficulty");
});

await check("methods + CORS", async () => {
  const preflight = await get("/api/quizzes/0001/easy", { method: "OPTIONS" });
  assert(preflight.status === 204, `preflight=${preflight.status}`);
  assert(preflight.headers.get("access-control-allow-origin") === "*", "no CORS header");
  assert((await get("/api/quizzes/0001/easy", { method: "POST" })).status === 405, "POST accepted");
  const ok = await get("/api/health");
  assert((ok.headers.get("content-type") || "").includes("application/json"), "content-type");
});

await check("raw static files pass through", async () => {
  const md = await get("/articles/0001_the_arts.md");
  assert(md.status === 200, `md=${md.status}`);
  assert((await md.text()).includes("# The arts"), "markdown content");
  assert((await get("/quizzes/0001_the_arts_easy.json")).status === 200, "quiz file");
  assert((await get("/no/such/file")).status === 404, "unknown static file");
});

console.log(`\n${pass} passed, ${fail} failed`);
process.exit(fail === 0 ? 0 : 1);
