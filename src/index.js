/**
 * Reading-Quiz content API — Congressional App Challenge 2026.
 *
 * The article corpus (Markdown) and the pre-generated quizzes (JSON) are
 * deployed as Cloudflare Workers static assets from `public/`. This script adds
 * a small read-only JSON API in front of them under `/api/*`.
 *
 *   GET /api/health
 *   GET /api/topics
 *   GET /api/articles?topic=&level=&q=&limit=&offset=&random=1
 *   GET /api/articles/:id[?include=content]
 *   GET /api/quizzes?article_id=&difficulty=&topic=&limit=&offset=
 *   GET /api/quizzes/:articleId
 *   GET /api/quizzes/:articleId/:difficulty[?shuffle=0&raw=1]
 *   GET /api/random?difficulty=&topic=&level=
 *
 * Anything that is not /api/* is served from the static assets.
 */

const DIFFICULTIES = ["easy", "medium", "hard"];

// Used only to call the ASSETS binding; the hostname is not meaningful.
const ASSETS = "https://assets.local";

const LIST_CACHE_TTL = 60 * 60; // 1 hour  — lists, topics, service index
const CONTENT_CACHE_TTL = 24 * 60 * 60; // 24 hours — articles and quizzes

const CORS_HEADERS = {
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Methods": "GET, HEAD, OPTIONS",
  "Access-Control-Allow-Headers": "Content-Type",
  "Access-Control-Max-Age": "86400",
};

const DEFAULT_LIMIT = 100;
const MAX_LIMIT = 1000;

/** An error that should be turned into a JSON response with `status`. */
class ApiError extends Error {
  constructor(status, message) {
    super(message);
    this.status = status;
  }
}

// Memoised per isolate so we read each manifest at most once per cold start.
let manifestPromise = null;
let quizIndexPromise = null;

export default {
  async fetch(request, env, ctx) {
    if (request.method === "OPTIONS") {
      return new Response(null, { status: 204, headers: CORS_HEADERS });
    }
    if (request.method !== "GET" && request.method !== "HEAD") {
      return problem(405, "Only GET, HEAD and OPTIONS are allowed.");
    }

    const url = new URL(request.url);
    const path = url.pathname.replace(/\/+$/, "") || "/";

    try {
      return await route(request, env, ctx, url, path);
    } catch (error) {
      if (error instanceof ApiError) return problem(error.status, error.message);
      console.error("Unhandled error:", error);
      return problem(500, "Internal error.");
    }
  },
};

// ---------------------------------------------------------------------------
// Routing
// ---------------------------------------------------------------------------

async function route(request, env, ctx, url, path) {
  const query = url.searchParams;

  if (path === "/" || path === "/api" || path === "/api/health") {
    return serviceIndex(request, env, ctx, path);
  }

  if (path === "/api/topics") {
    return listTopics(request, env, ctx);
  }

  if (path === "/api/articles") {
    return listArticles(request, env, ctx, query);
  }

  const articleMatch = /^\/api\/articles\/([^/]+)$/.exec(path);
  if (articleMatch) {
    return getArticle(request, env, ctx, articleMatch[1], query);
  }

  if (path === "/api/quizzes") {
    return listQuizzes(request, env, ctx, query);
  }

  const quizMatch = /^\/api\/quizzes\/([^/]+)(?:\/([^/]+))?$/.exec(path);
  if (quizMatch) {
    return getQuiz(request, env, ctx, quizMatch[1], quizMatch[2], query);
  }

  if (path === "/api/random") {
    return randomArticleQuiz(request, env, query);
  }

  if (path.startsWith("/api/")) {
    throw new ApiError(404, `Unknown endpoint: ${path}`);
  }

  // Non-API paths: serve the raw asset when it exists (for example
  // /articles/0001_the_arts.md or /quizzes/0001_the_arts_easy.json).
  const asset = await env.ASSETS.fetch(request);
  if (asset.status === 404) {
    throw new ApiError(404, `Not found: ${path}`);
  }
  return asset;
}

// ---------------------------------------------------------------------------
// Handlers
// ---------------------------------------------------------------------------

async function serviceIndex(request, env, ctx, path) {
  if (path === "/api/health") {
    return json({
      status: "ok",
      service: "congressional-app-backend-2026",
      time: new Date().toISOString(),
    });
  }

  return cachedJson(request, ctx, LIST_CACHE_TTL, async () => {
    const [manifest, quizIndex] = await Promise.all([
      getManifest(env),
      getQuizIndex(env),
    ]);
    return {
      service: "Reading-Quiz content API",
      license: "Article text from Wikipedia, CC BY-SA 4.0",
      counts: {
        articles: manifest.articles.length,
        quizzes: quizIndex.quizzes.length,
        difficulties: DIFFICULTIES,
      },
      endpoints: [
        "GET /api/health",
        "GET /api/topics",
        "GET /api/articles?topic=&level=&q=&limit=&offset=&random=1",
        "GET /api/articles/:id?include=content",
        "GET /api/quizzes?article_id=&difficulty=&topic=&limit=&offset=",
        "GET /api/quizzes/:articleId",
        "GET /api/quizzes/:articleId/:difficulty?shuffle=0&raw=1",
        "GET /api/random?difficulty=&topic=&level=",
      ],
    };
  });
}

async function listTopics(request, env, ctx) {
  return cachedJson(request, ctx, LIST_CACHE_TTL, async () => {
    const { articles } = await getManifest(env);
    const counts = new Map();
    for (const article of articles) {
      counts.set(article.topic, (counts.get(article.topic) ?? 0) + 1);
    }
    const topics = [...counts]
      .map(([topic, count]) => ({ topic, count }))
      .sort((a, b) => b.count - a.count || a.topic.localeCompare(b.topic));
    return { count: topics.length, topics };
  });
}

async function listArticles(request, env, ctx, query) {
  return cachedJson(request, ctx, LIST_CACHE_TTL, async () => {
    const { count, articles } = await getManifest(env);
    const filtered = filterArticles(articles, query);

    if (isTruthy(query.get("random"))) {
      const pick = filtered[Math.floor(Math.random() * filtered.length)];
      if (!pick) throw new ApiError(404, "No articles match those filters.");
      return { article: publicArticle(pick) };
    }

    const { limit, offset } = paginate(query);
    return {
      total_articles: count,
      count: filtered.length,
      limit,
      offset,
      articles: filtered.slice(offset, offset + limit).map(publicArticle),
    };
  });
}

async function getArticle(request, env, ctx, idRaw, query) {
  const id = normalizeId(idRaw);
  const { byId } = await getManifest(env);
  const article = byId.get(id);
  if (!article) throw new ApiError(404, `No article with id "${idRaw}".`);

  const include = (query.get("include") ?? "")
    .split(",")
    .map((part) => part.trim().toLowerCase());
  const withContent =
    query.get("content") === "1" || include.includes("content") || include.includes("markdown");

  if (!withContent) {
    return json(publicArticle(article), { cache: LIST_CACHE_TTL });
  }

  return cachedJson(request, ctx, CONTENT_CACHE_TTL, async () => {
    const response = await env.ASSETS.fetch(
      new Request(`${ASSETS}/articles/${article.file}`),
    );
    if (!response.ok) {
      throw new ApiError(500, `Article file ${article.file} is missing from the deployment.`);
    }
    return { ...publicArticle(article), markdown: await response.text() };
  });
}

async function listQuizzes(request, env, ctx, query) {
  return cachedJson(request, ctx, LIST_CACHE_TTL, async () => {
    const { quizzes } = await getQuizIndex(env);
    let items = quizzes;

    const articleId = query.get("article_id") ?? query.get("articleId");
    if (articleId) {
      const id = normalizeId(articleId);
      items = items.filter((quiz) => quiz.article_id === id);
    }

    const difficulty = (query.get("difficulty") ?? "").toLowerCase();
    if (difficulty) {
      if (!DIFFICULTIES.includes(difficulty)) {
        throw new ApiError(400, `difficulty must be one of ${DIFFICULTIES.join(", ")}.`);
      }
      items = items.filter((quiz) => quiz.difficulty === difficulty);
    }

    const topic = query.get("topic");
    if (topic) {
      const { articles } = await getManifest(env);
      const ids = new Set(
        articles
          .filter((article) => article.topic.toLowerCase() === topic.toLowerCase())
          .map((article) => article.id),
      );
      items = items.filter((quiz) => ids.has(quiz.article_id));
    }

    const { limit, offset } = paginate(query);
    return {
      count: items.length,
      limit,
      offset,
      quizzes: items.slice(offset, offset + limit),
    };
  });
}

async function getQuiz(request, env, ctx, idRaw, difficultyRaw, query) {
  const id = normalizeId(idRaw);
  const { byId } = await getManifest(env);
  const article = byId.get(id);
  if (!article) throw new ApiError(404, `No article with id "${idRaw}".`);

  const { byArticle } = await getQuizIndex(env);
  const available = difficultiesFor(article, byArticle);
  if (available.length === 0) {
    throw new ApiError(404, `No quizzes have been generated for article ${id}.`);
  }

  const raw = isTruthy(query.get("raw"));
  const shuffle = query.has("shuffle") ? isTruthy(query.get("shuffle")) : true;

  if (difficultyRaw) {
    const difficulty = extractDifficulty(difficultyRaw);
    if (!difficulty) {
      throw new ApiError(400, `difficulty must be one of ${DIFFICULTIES.join(", ")}.`);
    }
    if (!available.includes(difficulty)) {
      throw new ApiError(
        404,
        `No "${difficulty}" quiz for article ${id}. Available: ${available.join(", ")}.`,
      );
    }
    return cachedJson(request, ctx, CONTENT_CACHE_TTL, async () => {
      const data = await loadQuizFile(env, article, difficulty, byArticle);
      return shapeQuiz(data, { shuffle, raw });
    });
  }

  return cachedJson(request, ctx, CONTENT_CACHE_TTL, async () => {
    const quizzes = await Promise.all(
      available.map(async (difficulty) => {
        const data = await loadQuizFile(env, article, difficulty, byArticle);
        return shapeQuiz(data, { shuffle, raw });
      }),
    );
    return { article_id: id, available_difficulties: available, quizzes };
  });
}

async function randomArticleQuiz(request, env, query) {
  const difficulty = extractDifficulty(query.get("difficulty"));
  if (query.get("difficulty") && !difficulty) {
    throw new ApiError(400, `difficulty must be one of ${DIFFICULTIES.join(", ")}.`);
  }

  const { articles } = await getManifest(env);
  const candidates = filterArticles(articles, query);
  if (candidates.length === 0) {
    throw new ApiError(404, "No articles match those filters.");
  }

  const article = candidates[Math.floor(Math.random() * candidates.length)];
  const { byArticle } = await getQuizIndex(env);
  const available = difficultiesFor(article, byArticle);
  if (available.length === 0) {
    throw new ApiError(404, `No quizzes have been generated for article ${article.id}.`);
  }

  const chosen = difficulty && available.includes(difficulty)
    ? difficulty
    : available[Math.floor(Math.random() * available.length)];
  const data = await loadQuizFile(env, article, chosen, byArticle);

  // Randomised, so never cache.
  return json({
    article: publicArticle(article),
    quiz: shapeQuiz(data, { shuffle: true, raw: false }),
  });
}

// ---------------------------------------------------------------------------
// Asset access
// ---------------------------------------------------------------------------

function getManifest(env) {
  if (!manifestPromise) {
    manifestPromise = loadManifest(env).catch((error) => {
      manifestPromise = null; // let the next request retry
      throw error;
    });
  }
  return manifestPromise;
}

async function loadManifest(env) {
  const response = await env.ASSETS.fetch(
    new Request(`${ASSETS}/articles/index.json`),
  );
  if (!response.ok) {
    throw new ApiError(
      500,
      "articles/index.json is missing from this deployment — run `npm run build`.",
    );
  }
  const raw = await response.json();
  const articles = (raw.articles ?? []).map((article) => ({
    ...article,
    id: String(article.id),
    base: String(article.file ?? "").replace(/\.md$/i, ""),
  }));
  return { ...raw, articles, byId: new Map(articles.map((a) => [a.id, a])) };
}

function getQuizIndex(env) {
  if (!quizIndexPromise) {
    quizIndexPromise = loadQuizIndex(env).catch((error) => {
      quizIndexPromise = null;
      throw error;
    });
  }
  return quizIndexPromise;
}

async function loadQuizIndex(env) {
  const response = await env.ASSETS.fetch(new Request(`${ASSETS}/quizzes/index.json`));
  if (!response.ok) {
    throw new ApiError(
      500,
      "quizzes/index.json is missing from this deployment — run `npm run build`.",
    );
  }
  const raw = await response.json();
  const quizzes = (raw.quizzes ?? []).map((quiz) => ({
    ...quiz,
    article_id: String(quiz.article_id),
  }));
  const byArticle = new Map();
  for (const quiz of quizzes) {
    if (!byArticle.has(quiz.article_id)) byArticle.set(quiz.article_id, new Map());
    byArticle.get(quiz.article_id).set(quiz.difficulty, quiz);
  }
  return { ...raw, quizzes, byArticle };
}

async function loadQuizFile(env, article, difficulty, byArticle) {
  const entry = byArticle.get(article.id)?.get(difficulty);
  const file = entry?.file ?? `${article.base}_${difficulty}.json`;
  const response = await env.ASSETS.fetch(new Request(`${ASSETS}/quizzes/${file}`));
  if (!response.ok) {
    throw new ApiError(404, `No "${difficulty}" quiz for article ${article.id}.`);
  }
  return response.json();
}

// ---------------------------------------------------------------------------
// Response helpers
// ---------------------------------------------------------------------------

function json(data, { status = 200, cache = 0 } = {}) {
  const headers = new Headers(CORS_HEADERS);
  headers.set("Content-Type", "application/json; charset=utf-8");
  headers.set("Cache-Control", cache > 0 ? `public, max-age=${cache}` : "no-store");
  return new Response(JSON.stringify(data), { status, headers });
}

function problem(status, message) {
  return json({ error: { status, message } }, { status });
}

/**
 * Serve `produce()` from the Cloudflare edge cache, keyed on the full URL
 * (including the query string), for `seconds`.
 */
async function cachedJson(request, ctx, seconds, produce) {
  const cache = caches.default;
  const key = new Request(request.url, { method: "GET" });

  const hit = await cache.match(key);
  if (hit) return hit;

  const response = json(await produce(), { cache: seconds });
  if (response.status === 200) {
    ctx.waitUntil(cache.put(key, response.clone()));
  }
  return response;
}

// ---------------------------------------------------------------------------
// Data helpers
// ---------------------------------------------------------------------------

function filterArticles(articles, query) {
  let items = articles;

  const topic = query.get("topic");
  if (topic) {
    const needle = topic.toLowerCase();
    items = items.filter((article) => article.topic.toLowerCase() === needle);
  }

  const level = query.get("level");
  if (level) {
    items = items.filter((article) => String(article.level) === String(level));
  }

  const search = query.get("q");
  if (search) {
    const needle = search.toLowerCase();
    items = items.filter(
      (article) =>
        article.title.toLowerCase().includes(needle) ||
        String(article.description ?? "").toLowerCase().includes(needle),
    );
  }

  return items;
}

function publicArticle(article) {
  return {
    id: article.id,
    title: article.title,
    rank: article.rank,
    level: article.level,
    topic: article.topic,
    description: article.description,
    pageid: article.pageid,
    url: article.url,
    file: article.file,
  };
}

function difficultiesFor(article, byArticle) {
  const available = byArticle.get(article.id);
  if (!available || available.size === 0) return [...DIFFICULTIES];
  return DIFFICULTIES.filter((difficulty) => available.has(difficulty));
}

/**
 * Normalise a quiz for clients: by default the options are shuffled so the
 * correct answer is not always first, and `answer_index` points at it. Pass
 * `shuffle=0` to keep the stored order, or `raw=1` to return the file as-is.
 */
function shapeQuiz(data, { shuffle = true, raw = false } = {}) {
  if (raw) return data;

  const questions = (data.questions ?? []).map((question) => {
    const pairs = (question.options ?? []).map((text, index) => ({
      text,
      explanation: question.answer_explanations?.[index] ?? "",
    }));

    // The stored file always keeps the correct option at index 0.
    const order = shuffle ? shuffledOrder(pairs.length) : pairs.map((_, index) => index);
    const options = order.map((index) => pairs[index].text);
    const answerIndex = order.indexOf(0);

    return {
      id: question.id,
      question: question.question,
      options,
      answer_index: answerIndex,
      answer: options[answerIndex],
      answer_explanations: order.map((index) => pairs[index].explanation),
    };
  });

  return {
    article_id: data.article_id,
    difficulty: data.difficulty,
    question_count: data.question_count ?? questions.length,
    shuffled: shuffle,
    questions,
  };
}

function shuffledOrder(length) {
  const order = Array.from({ length }, (_, index) => index);
  for (let i = length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [order[i], order[j]] = [order[j], order[i]];
  }
  return order;
}

/** Accepts "1", "0001" or "0001_the_arts" and returns "0001". */
function normalizeId(value) {
  const raw = String(value ?? "").trim();
  if (/^\d+$/.test(raw)) return raw.padStart(4, "0");
  const match = /^(\d{4})[_-]/.exec(raw);
  if (match) return match[1];
  return raw;
}

/** Accepts "easy", "EASY" or "0001_the_arts_easy" and returns "easy". */
function extractDifficulty(value) {
  if (!value) return null;
  const raw = String(value).trim().toLowerCase();
  if (DIFFICULTIES.includes(raw)) return raw;
  const match = /[_-](easy|medium|hard)$/.exec(raw);
  return match ? match[1] : null;
}

function paginate(query) {
  const limit = clamp(parseInt(query.get("limit") ?? "", 10), 1, MAX_LIMIT, DEFAULT_LIMIT);
  const offset = clamp(parseInt(query.get("offset") ?? "", 10), 0, Number.MAX_SAFE_INTEGER, 0);
  return { limit, offset };
}

function clamp(value, min, max, fallback) {
  if (!Number.isFinite(value)) return fallback;
  return Math.min(Math.max(value, min), max);
}

function isTruthy(value) {
  if (value === null) return false;
  return !["", "0", "false", "no", "off"].includes(String(value).trim().toLowerCase());
}
