#!/usr/bin/env node
/**
 * Assembles the static assets that the Worker serves into `public/`.
 *
 *   articles/index.json          -> public/articles/index.json
 *   articles/NNNN_<slug>.md      -> public/articles/<same name>
 *   quizzes/NNNN_<slug>_<diff>.json -> public/quizzes/<same name>
 *   (generated)                  -> public/quizzes/index.json
 *
 * The generated quiz index is what the API uses to list quizzes and to know
 * which difficulties exist for an article, without guessing from filenames.
 *
 * Run `npm run build`. Cloudflare runs it automatically on every push.
 */
import { cp, mkdir, readdir, rm, writeFile } from "node:fs/promises";
import { existsSync } from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const ARTICLES_DIR = path.join(root, "articles");
const QUIZZES_DIR = path.join(root, "quizzes");
const OUT_DIR = path.join(root, "public");

const ARTICLE_RE = /^\d{4}_[a-z0-9_-]+\.md$/i;
const QUIZ_RE = /^(\d{4})_(.+)_(easy|medium|hard)\.json$/i;
const DIFFICULTIES = ["easy", "medium", "hard"];

async function main() {
  if (!existsSync(path.join(ARTICLES_DIR, "index.json"))) {
    throw new Error("articles/index.json is missing — run get_articles.py first.");
  }

  await rm(OUT_DIR, { recursive: true, force: true });
  await mkdir(path.join(OUT_DIR, "articles"), { recursive: true });
  await mkdir(path.join(OUT_DIR, "quizzes"), { recursive: true });

  // --- articles ------------------------------------------------------------
  const articleFiles = (await readdir(ARTICLES_DIR))
    .filter((name) => ARTICLE_RE.test(name))
    .sort();

  if (articleFiles.length === 0) {
    throw new Error("No article files matched NNNN_<slug>.md in articles/.");
  }

  await cp(
    path.join(ARTICLES_DIR, "index.json"),
    path.join(OUT_DIR, "articles", "index.json"),
  );
  for (const name of articleFiles) {
    await cp(path.join(ARTICLES_DIR, name), path.join(OUT_DIR, "articles", name));
  }

  // --- quizzes -------------------------------------------------------------
  const quizFiles = (await readdir(QUIZZES_DIR))
    .filter((name) => QUIZ_RE.test(name))
    .sort();

  const articleBases = new Set(articleFiles.map((name) => name.replace(/\.md$/i, "")));
  const quizzes = [];
  const seen = new Set();
  const missing = [];

  for (const name of quizFiles) {
    const match = QUIZ_RE.exec(name);
    const [, articleId, slug, difficultyRaw] = match;
    const difficulty = difficultyRaw.toLowerCase();
    const base = `${articleId}_${slug}`;

    if (!articleBases.has(base)) {
      throw new Error(
        `quizzes/${name} has no matching article (expected articles/${base}.md).`,
      );
    }

    const key = `${articleId}/${difficulty}`;
    if (seen.has(key)) {
      throw new Error(`Duplicate "${difficulty}" quiz for article ${articleId}.`);
    }
    seen.add(key);

    await cp(path.join(QUIZZES_DIR, name), path.join(OUT_DIR, "quizzes", name));
    quizzes.push({ article_id: articleId, difficulty, file: name, base });
  }

  for (const base of articleBases) {
    const id = base.slice(0, 4);
    for (const difficulty of DIFFICULTIES) {
      if (!seen.has(`${id}/${difficulty}`)) missing.push(`${base}_${difficulty}`);
    }
  }

  // --- generated quiz index ------------------------------------------------
  const index = {
    generated: new Date().toISOString(),
    count: quizzes.length,
    difficulties: DIFFICULTIES,
    quizzes,
  };
  await writeFile(
    path.join(OUT_DIR, "quizzes", "index.json"),
    `${JSON.stringify(index, null, 2)}\n`,
  );

  console.log(
    `public/ ready — ${articleFiles.length} articles, ${quizzes.length} quizzes`,
  );
  if (missing.length > 0) {
    console.warn(
      `warning: ${missing.length} article(s) are missing at least one quiz ` +
        `(e.g. ${missing.slice(0, 5).join(", ")}) — the API will skip those.`,
    );
  }
}

main().catch((error) => {
  console.error(error);
  process.exit(1);
});
