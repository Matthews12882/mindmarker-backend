#!/usr/bin/env python3
"""
generate_quizzes.py — turn corpus articles into 3 machine-readable quizzes each.

WHY THIS EXISTS
    The reading-quiz app serves pre-generated quizzes (cheap and fast at request
    time). This is the batch job that builds them: for every article it writes an
    easy, a medium and a hard quiz, each with 10 questions, as JSON the API can
    load directly.

    The format is documented in quizzes/README.md and the prompt lives in
    quizzes/quiz_prompt.md. Read the README before changing anything here.

WHAT IT DOES
    1. Reads articles/index.json and works out what still needs generating.
    2. For each article + difficulty, sends the article text and the prompt to
       an LLM (OpenRouter by default) and asks for one JSON quiz.
    3. Validates the reply against the quiz invariants, normalises it to the
       exact schema, and writes quizzes/<id>_<slug>_<difficulty>.json.
    4. Retries bad replies and skips work whose file already exists, so the job
       is resumable and can be run in chunks.

USAGE
    export OPENROUTER_API_KEY=sk-or-...        # or put it in .env
    ./venv/bin/python generate_quizzes.py --ids 0001        # one article
    ./venv/bin/python generate_quizzes.py --limit 5         # first 5 pending
    ./venv/bin/python generate_quizzes.py                   # everything pending

    On a terminal it asks which model to use (primary + fallbacks) each run.
    Skip the picker with --primary / --fallback-models, or --no-prompt to use
    the defaults. See the choices with --list-models, e.g.

    ./venv/bin/python generate_quizzes.py --limit 20 --primary poolside/laguna-s-2.1:free

    Free OpenRouter models allow 20 requests/min and (with >=$10 credits) 1000
    requests/day. 300 articles x 3 quizzes = 900 requests, so chunk the work and
    keep the default --delay.

REQUIRES
    requests (already in ./venv). A free OpenRouter API key.
    Quality is "usable, not perfect" on purpose — this is a hobby app.
"""

from __future__ import annotations

import argparse
import json
import os
import random
import re
import sys
import time
from pathlib import Path

import requests

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

OPENROUTER_CHAT_URL = "https://openrouter.ai/api/v1/chat/completions"
OPENROUTER_KEY_URL = "https://openrouter.ai/api/v1/key"
OPENROUTER_MODELS_URL = "https://openrouter.ai/api/v1/models"

# Free model by default, so a full run costs nothing. Swap with --model.
DEFAULT_MODEL = "nvidia/nemotron-3.5-super-vl:free"

DIFFICULTIES = ("easy", "medium", "hard")
REQUIRED_QUESTIONS = 10
OPTIONS_PER_QUESTION = 4

# Difficulty definitions, appended to the user prompt per quiz so the model is
# told exactly what each level means (the prompt file's summary is the fallback).
#   easy   — only the article's intro (lead section before the first heading).
#   medium — the whole article, but kept simple and plainly worded.
#   hard   — no recall; the reader must interpret the facts.
DIFFICULTY_GUIDANCE = {
    "easy": (
        "Difficulty: EASY. Base every question only on the article's "
        "introduction — the lead section before the first heading. Ask for "
        "literal recall of facts stated there (who, what, where, how many), in "
        "simple, direct language. Do not use material from the later sections."
    ),
    "medium": (
        "Difficulty: MEDIUM. Draw questions from the whole article, including "
        "its later sections, but keep them simple: cover the main ideas and "
        "clearly stated facts in plain, everyday language. Do not set puzzles, "
        "scenarios, or questions that require interpreting or applying ideas."
    ),
    "hard": (
        "Difficulty: HARD. Do not ask for facts to be recalled. Ask the reader "
        "to interpret facts drawn from the whole article: what they mean, why "
        "they matter, what they imply, how ideas relate, compare or conflict, "
        "and what conclusions follow. Every question must still be answerable "
        "from the article text."
    ),
}

DEFAULT_ARTICLES = "articles"
DEFAULT_QUIZZES = "quizzes"
DEFAULT_PROMPT = "quizzes/quiz_prompt.md"

# Keep the prompt (and cost) bounded for very long articles.
DEFAULT_MAX_ARTICLE_CHARS = 20000
# Cap on generated tokens per quiz: 10 questions with four explanations each can
# run long; too low a cap truncates the JSON mid-string.
MAX_OUTPUT_TOKENS = 4500
# Total wall-clock seconds allowed for one model response (a stalled/streaming
# model is abandoned after this and, if it's the primary, dropped from the chain).
DEFAULT_REQUEST_TIMEOUT = 180.0
# If no stream data arrives for this long, treat the model as stalled and rotate.
DEFAULT_STALL_TIMEOUT = 45.0
CONNECT_TIMEOUT = 10.0
# Free tier is 20 req/min => one request every 3s keeps us under the limit.
DEFAULT_DELAY = 3.0
# Transport failures retried inside the HTTP call; this is content retries.
DEFAULT_RETRIES = 2

# Some free models spend most of max_tokens on hidden "reasoning" and truncate
# the JSON before finishing. Turning reasoning off fixed that (and cut a quiz
# from ~28s to ~13s). Override with --reasoning.
DEFAULT_REASONING = "off"
REASONING_PARAMS: dict[str, dict | None] = {
    "off": {"enabled": False},
    "auto": None,
    "low": {"effort": "low"},
    "medium": {"effort": "medium"},
    "high": {"effort": "high"},
}

APP_TITLE = "reading-quiz-app"

# Upstream hiccups worth retrying (429 = rate limit, 5xx = provider trouble).
RETRYABLE_STATUS = {408, 409, 429, 500, 502, 503, 504, 520, 522, 524, 529}

# Free models to fail over to when the primary is down/overloaded. All are
# ":free", so a fallback never spends credits. Override or clear with
# --fallback-models (pass "" to disable failover).
DEFAULT_FALLBACK_MODELS = (
    "cohere/north-mini-code:free",
    "liquid/lfm-2.5-2.6b:free",
)

# OpenRouter rejects a 'models' array longer than this ("must have 3 items or
# fewer"), so the whole chain (primary + fallbacks) is capped at 3.
MAX_CHAIN = 3

# Used for the interactive picker when the live model list can't be fetched.
MODEL_LIST_FALLBACK = (
    "nvidia/nemotron-3-ultra-550b-a55b:free",
    "poolside/laguna-s-2.1:free",
    "xingchen-agi/xing4.0-29b-a4b:free",
    "nvidia/nemotron-3.5-super-vl:free",
    "dots-studio/dots-3-note-preview:free",
    "poolside/laguna-xs-2.1:free",
    "cohere/north-mini-code:free",
)


# ---------------------------------------------------------------------------
# Small helpers
# ---------------------------------------------------------------------------

def log(msg: str) -> None:
    print(msg, flush=True)


def load_dotenv(path: Path) -> None:
    """Minimal .env loader: KEY=VALUE lines, existing env wins."""
    if not path.exists():
        return
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        key, value = key.strip(), value.strip().strip('"').strip("'")
        if key and key not in os.environ:
            os.environ[key] = value


def strip_front_matter(text: str) -> str:
    """Drop the leading YAML front matter so the model sees prose, not metadata."""
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            return text[end + 4:].lstrip("\n")
    return text


def intro_from_body(body: str) -> str:
    """Return the lead section: everything before the first '##' heading.

    Used for easy quizzes so they only draw on the article's introduction.
    """
    lines = body.splitlines()
    for index, line in enumerate(lines):
        if line.startswith("## "):
            return "\n".join(lines[:index]).strip()
    return body.strip()


def slug_from_file(filename: str) -> str:
    """'0001_the_arts.md' -> 'the_arts' (keeps quiz names in step with articles)."""
    stem = Path(filename).stem
    return stem.split("_", 1)[1] if "_" in stem else stem


def quiz_filename(article_id: str, slug: str, difficulty: str) -> str:
    return f"{article_id}_{slug}_{difficulty}.json"


def sleep_for(seconds: float) -> None:
    if seconds > 0:
        time.sleep(seconds)


def _make_ticker(interval: float = 4.0):
    """Return a callback that prints a '.' at most every `interval` seconds.

    Used as streaming progress feedback so a long generation never looks hung.
    """
    state = {"last": time.monotonic()}

    def tick() -> None:
        now = time.monotonic()
        if now - state["last"] >= interval:
            print(".", end="", flush=True)
            state["last"] = now

    return tick


# ---------------------------------------------------------------------------
# Prompt
# ---------------------------------------------------------------------------

def load_prompt(path: Path) -> tuple[str, str]:
    """Split quizzes/quiz_prompt.md into (system, user_template)."""
    text = path.read_text(encoding="utf-8")
    match = re.search(r"^##\s+System\s*$(.*?)^##\s+User\s*$(.*)\Z",
                      text, re.S | re.M)
    if not match:
        raise RuntimeError(f"could not find '## System' / '## User' in {path}")
    return match.group(1).strip(), match.group(2).strip()


def body_for_difficulty(body: str, difficulty: str) -> str:
    """Restrict the article text to what a difficulty is allowed to draw on.

    easy quizzes see only the intro; medium and hard see the whole article.
    """
    if difficulty == "easy":
        return intro_from_body(body)
    return body


def render_user(template: str, article: dict, difficulty: str,
                body: str) -> str:
    text = (template
            .replace("{{ARTICLE_ID}}", article["id"])
            .replace("{{ARTICLE_TITLE}}", article["title"])
            .replace("{{DIFFICULTY}}", difficulty)
            .replace("{{ARTICLE_TEXT}}", body))
    guidance = DIFFICULTY_GUIDANCE.get(difficulty)
    if guidance:
        text += "\n\n" + guidance
    return text


# ---------------------------------------------------------------------------
# Model call
# ---------------------------------------------------------------------------

class ModelError(RuntimeError):
    pass


def call_model(session: requests.Session, api_key: str, model: str,
               system: str, user: str, attempts: int = 5,
               fallback_models: list[str] | None = None,
               request_timeout: float = DEFAULT_REQUEST_TIMEOUT,
               stall_timeout: float = DEFAULT_STALL_TIMEOUT,
               reasoning: dict | None = None,
               on_progress=None) -> str:
    """Stream one chat completion, retrying rate-limit/provider failures.

    Replies are read as a Server-Sent-Events stream so we can report progress
    and detect a stalled model instead of blocking silently. When
    `fallback_models` is given, OpenRouter is asked to fail over to those models
    automatically if the primary is down, overloaded or rate-limited; if the
    whole chain keeps failing, the front model is dropped so the next attempt
    starts from a different one (no long silent sleeps).

    `request_timeout` is the total wall-clock cap for one attempt and
    `stall_timeout` the longest gap allowed between streamed chunks.
    """
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "X-Title": APP_TITLE,
    }
    base_chain = [model, *(fallback_models or [])][:MAX_CHAIN]
    chain = list(base_chain)
    last_error: Exception | None = None
    attempt = 0

    while attempt < attempts:
        attempt += 1
        if not chain:                                   # every model rotated out
            chain = list(base_chain)                    # cycle back around

        payload = {
            "messages": [
                {"role": "system", "content": system},
                {"role": "user", "content": user},
            ],
            "temperature": 0.5,
            "max_tokens": MAX_OUTPUT_TOKENS,
            "stream": True,
        }
        if len(chain) > 1:
            payload["models"] = list(chain)             # OpenRouter tries these in order
        else:
            payload["model"] = chain[0]
        if reasoning is not None:
            payload["reasoning"] = reasoning

        try:
            with session.post(OPENROUTER_CHAT_URL, headers=headers, json=payload,
                              timeout=(CONNECT_TIMEOUT, stall_timeout), stream=True) as resp:
                if resp.status_code in RETRYABLE_STATUS:
                    last_error = ModelError(f"HTTP {resp.status_code}: {_error_message(resp)}")
                    sleep_for(min(_retry_after(resp) or 1.0, 5.0))
                elif resp.status_code >= 400:           # 401/402/403/404: don't retry
                    raise ModelError(f"HTTP {resp.status_code}: {_error_message(resp)}")
                else:
                    try:
                        return _read_stream(resp, time.monotonic() + request_timeout,
                                            stall_timeout, on_progress)
                    except TimeoutError as exc:
                        last_error = ModelError(
                            f"no content from {chain[0]} ({exc or 'stalled'})")
        except requests.exceptions.ReadTimeout as exc:
            last_error = exc
        except requests.RequestException as exc:
            last_error = exc
            sleep_for(_backoff(attempt))
            continue

        # Rotate the front model so the next attempt uses a different provider
        # rather than re-hammering a rate-limited or slow one.
        chain = chain[1:]

    raise ModelError(f"model call failed after {attempts} tries: {last_error}")


def _read_stream(resp: requests.Response, deadline: float, stall_timeout: float,
                 on_progress) -> str:
    """Accumulate an SSE chat stream into the assistant's reply text.

    OpenRouter sends *comment* keepalives (": OPENROUTER PROCESSING") while a
    model is queued; those reset the socket read timeout, so we enforce both a
    total `deadline` and a `stall_timeout` (max gap between real data events)
    ourselves on every line.
    """
    parts: list[str] = []
    last_event = time.monotonic()
    finish_reason = None
    saw_done = False
    for line in resp.iter_lines(decode_unicode=True):
        now = time.monotonic()
        if now > deadline:
            raise TimeoutError("exceeded the response time cap")
        if now - last_event > stall_timeout:
            raise TimeoutError(f"no data for {stall_timeout:.0f}s")
        if not line:
            continue
        if not line.startswith("data:"):
            continue                    # ": keepalive" comments and blank separators
        data = line[5:].strip()
        if data == "[DONE]":
            saw_done = True
            break
        last_event = now                # a real event arrived
        if on_progress is not None:
            on_progress()
        try:
            obj = json.loads(data)
        except ValueError:
            continue
        if "error" in obj:
            raise ModelError(str(obj["error"])[:300])
        try:
            choice = obj["choices"][0]
        except (KeyError, IndexError, TypeError):
            continue
        if choice.get("finish_reason"):
            finish_reason = choice["finish_reason"]
        delta = choice.get("delta") or {}
        piece = delta.get("content")
        if piece:
            parts.append(piece)
    if finish_reason == "length":
        raise TimeoutError("response hit max_tokens before completing")
    if not saw_done and finish_reason is None:
        raise TimeoutError("stream ended early")
    if not parts:
        raise TimeoutError("stream ended without any content")
    return "".join(parts)


def _backoff(attempt: int, base: float = 2.0, cap: float = 30.0) -> float:
    """Exponential backoff with jitter: ~2s, 4s, 8s, 16s, 30s..."""
    return min(cap, base * (2 ** (attempt - 1))) + random.uniform(0.0, 1.0)


def _error_message(resp: requests.Response) -> str:
    try:
        return json.dumps(resp.json().get("error", resp.text))[:300]
    except ValueError:
        return (resp.text or "")[:300]


def _retry_after(resp: requests.Response) -> float | None:
    value = resp.headers.get("Retry-After")
    if not value:
        return None
    try:
        return float(value)
    except ValueError:
        return None


def free_requests_remaining(session: requests.Session, api_key: str) -> str:
    """Best-effort daily free-request budget readout (never fatal)."""
    try:
        resp = session.get(OPENROUTER_KEY_URL,
                           headers={"Authorization": f"Bearer {api_key}"},
                           timeout=30)
        resp.raise_for_status()
        free = resp.json().get("data", {}).get("free_model_daily_requests", {})
        return f"{free.get('remaining', '?')}/{free.get('limit', '?')} free requests left today"
    except Exception:
        return "daily free-request budget unknown"


# ---------------------------------------------------------------------------
# Model selection
# ---------------------------------------------------------------------------

def split_list(value: str | None) -> list[str] | None:
    if value is None:
        return None
    return [item.strip() for item in value.split(",") if item.strip()]


def fetch_free_models(session: requests.Session) -> list[str]:
    """Live list of free, text-output model ids from OpenRouter (best effort)."""
    try:
        resp = session.get(OPENROUTER_MODELS_URL, timeout=30)
        resp.raise_for_status()
        entries = resp.json().get("data", [])
    except Exception:
        return []

    ids: list[str] = []
    for entry in entries:
        model_id = entry.get("id", "")
        if not model_id.endswith(":free"):
            continue
        outputs = (entry.get("architecture") or {}).get("output_modalities") or []
        if outputs and "text" not in outputs:
            continue
        ids.append(model_id)
    return sorted(set(ids))


def parse_selection(raw: str, choices: list[str]) -> list[str]:
    """Turn '2,3' or a raw model id list into model ids."""
    picked: list[str] = []
    for token in raw.split(","):
        token = token.strip()
        if not token:
            continue
        if token.isdigit() and 1 <= int(token) <= len(choices):
            picked.append(choices[int(token) - 1])
        else:
            picked.append(token)          # assume a raw model id
    return picked


def prompt_for_models(choices: list[str], primary: str | None,
                      fallbacks: list[str] | None) -> tuple[str, list[str]]:
    """Ask the user to pick a primary model and its fallbacks."""
    log("Free models available:")
    for index, model_id in enumerate(choices, 1):
        log(f"  [{index:>2}] {model_id}")

    if primary is None:
        while True:
            raw = input("Primary model [1] (number or id): ").strip()
            if not raw:
                primary = choices[0]
                break
            picked = parse_selection(raw, choices)
            if len(picked) == 1:
                primary = picked[0]
                break
            log("  pick exactly one primary model.")

    if fallbacks is None:
        default_fb = [m for m in choices if m != primary][:MAX_CHAIN - 1]
        shown = ", ".join(default_fb) if default_fb else "none"
        raw = input(f"Fallback models (numbers/ids, comma-separated) [{shown}]: ").strip()
        if raw == "":
            fallbacks = default_fb
        elif raw.lower() in {"none", "-"}:
            fallbacks = []
        else:
            fallbacks = parse_selection(raw, choices)

    return primary, fallbacks[:MAX_CHAIN - 1]


def resolve_models(args: argparse.Namespace,
                   session: requests.Session) -> tuple[str, list[str]]:
    """Return (primary, fallbacks); prompt interactively unless flags cover it.

    The picker only appears when neither --primary nor --fallback-models was
    given, so naming either one skips it (as does --no-prompt or a non-terminal).
    """
    primary = args.model
    fallbacks = split_list(args.fallback_models)
    resolved_primary = primary or DEFAULT_MODEL
    if fallbacks is None:
        fallbacks = [m for m in DEFAULT_FALLBACK_MODELS if m != resolved_primary]
    if len(fallbacks) > MAX_CHAIN - 1:
        log(f"  (capping to {MAX_CHAIN - 1} fallback(s): OpenRouter allows {MAX_CHAIN} models in total)")
        fallbacks = fallbacks[:MAX_CHAIN - 1]
    defaults = (resolved_primary, fallbacks)

    provided = primary is not None or args.fallback_models is not None
    interactive = sys.stdin.isatty() and not args.no_prompt and not args.dry_run
    if provided or not interactive:
        return defaults

    choices = fetch_free_models(session) or list(MODEL_LIST_FALLBACK)
    log("")
    try:
        return prompt_for_models(choices, None, None)
    except (EOFError, KeyboardInterrupt):
        log("")
        return defaults


# ---------------------------------------------------------------------------
# Parse + validate
# ---------------------------------------------------------------------------

def extract_json(text: str) -> object:
    """Pull a JSON object out of a model reply that may wrap it in prose/fences."""
    text = text.strip()
    text = re.sub(r"^```[a-zA-Z]*\s*", "", text)
    text = re.sub(r"\s*```$", "", text).strip()
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        start, end = text.find("{"), text.rfind("}")
        if start != -1 and end > start:
            return json.loads(text[start:end + 1])
        raise


def normalize_quiz(raw: object, article_id: str, difficulty: str):
    """Coerce a model reply into the exact quiz schema. Returns (quiz, problems).

    `quiz` is None when the reply is unusable. `problems` lists what was wrong
    (used both for logging and to nudge the model on a retry).
    """
    problems: list[str] = []
    if not isinstance(raw, dict):
        return None, ["reply was not a JSON object"]

    questions = raw.get("questions")
    if not isinstance(questions, list) or not questions:
        return None, ["reply had no 'questions' list"]

    clean: list[dict] = []
    for index, item in enumerate(questions, start=1):
        if not isinstance(item, dict):
            problems.append(f"q{index} was not an object")
            continue
        question = str(item.get("question", "")).strip()
        options = item.get("options")
        explanations = item.get("answer_explanations")

        if not question:
            problems.append(f"q{index} had no question text")
            continue
        if not isinstance(options, list) or len(options) != OPTIONS_PER_QUESTION:
            problems.append(f"q{index} did not have {OPTIONS_PER_QUESTION} options")
            continue
        options = [str(opt).strip() for opt in options]
        if any(not opt for opt in options):
            problems.append(f"q{index} had an empty option")
            continue
        if not isinstance(explanations, list) or len(explanations) != len(options):
            problems.append(f"q{index} needed one explanation per option")
            continue

        clean.append({
            "id": len(clean) + 1,
            "question": question,
            "options": options,
            "answer_explanations": [str(e).strip() for e in explanations],
        })

    if len(clean) > REQUIRED_QUESTIONS:
        clean = clean[:REQUIRED_QUESTIONS]
    if len(clean) != REQUIRED_QUESTIONS:
        problems.append(f"got {len(clean)} usable questions, need {REQUIRED_QUESTIONS}")
        return None, problems

    quiz = {
        "article_id": article_id,
        "difficulty": difficulty,
        "question_count": len(clean),
        "questions": clean,
    }
    return quiz, problems


# ---------------------------------------------------------------------------
# Work planning
# ---------------------------------------------------------------------------

def load_articles(articles_dir: Path) -> list[dict]:
    manifest = json.loads((articles_dir / "index.json").read_text(encoding="utf-8"))
    return manifest["articles"]


def plan_work(articles: list[dict], quizzes_dir: Path, difficulties,
              ids: set[str] | None, force: bool) -> list[tuple[dict, list[str]]]:
    todo: list[tuple[dict, list[str]]] = []
    for article in articles:
        if ids and article["id"] not in ids:
            continue
        slug = slug_from_file(article["file"])
        missing = [
            difficulty for difficulty in difficulties
            if force or not (quizzes_dir / quiz_filename(article["id"], slug, difficulty)).exists()
        ]
        if missing:
            todo.append((article, missing))
    return todo


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--articles", default=DEFAULT_ARTICLES,
                        help=f"article corpus folder (default {DEFAULT_ARTICLES}/)")
    parser.add_argument("--quizzes", default=DEFAULT_QUIZZES,
                        help=f"output folder (default {DEFAULT_QUIZZES}/)")
    parser.add_argument("--prompt", default=DEFAULT_PROMPT,
                        help=f"prompt file (default {DEFAULT_PROMPT})")
    parser.add_argument("--model", "--primary", dest="model", default=None,
                        help="OpenRouter primary model id (skips the interactive "
                             f"picker; default when non-interactive: {DEFAULT_MODEL})")
    parser.add_argument("--fallback-models", default=None,
                        help="comma-separated fallback models, tried in order when "
                             "the primary is down (pass \"\" to disable failover). "
                             f"Up to {MAX_CHAIN - 1} are used — OpenRouter allows "
                             f"{MAX_CHAIN} models per request. Naming any model flag "
                             "skips the interactive picker.")
    parser.add_argument("--no-prompt", action="store_true",
                        help="never prompt for models; use the defaults")
    parser.add_argument("--list-models", action="store_true",
                        help="print the available free models and exit")
    parser.add_argument("--ids", default="",
                        help="comma-separated article ids to (re)generate, e.g. 0001,0002")
    parser.add_argument("--limit", type=int, default=0,
                        help="only process the first N pending articles (chunking)")
    parser.add_argument("--difficulties", default="easy,medium,hard",
                        help="which quizzes to generate (default all three)")
    parser.add_argument("--force", action="store_true",
                        help="regenerate even if the quiz file already exists")
    parser.add_argument("--dry-run", action="store_true",
                        help="show what would be generated without calling the model")
    parser.add_argument("--delay", type=float, default=DEFAULT_DELAY,
                        help=f"seconds between model requests (default {DEFAULT_DELAY})")
    parser.add_argument("--retries", type=int, default=DEFAULT_RETRIES,
                        help=f"content retries per quiz (default {DEFAULT_RETRIES})")
    parser.add_argument("--transport-retries", type=int, default=5,
                        help="HTTP retries per request on 429/5xx (default 5)")
    parser.add_argument("--request-timeout", type=float, default=DEFAULT_REQUEST_TIMEOUT,
                        help="seconds to wait for one model response before "
                             f"abandoning it (default {DEFAULT_REQUEST_TIMEOUT:.0f})")
    parser.add_argument("--reasoning", choices=sorted(REASONING_PARAMS), default=DEFAULT_REASONING,
                        help="model reasoning budget; 'off' avoids free models burning "
                             f"max_tokens on hidden thinking (default {DEFAULT_REASONING})")
    parser.add_argument("--max-article-chars", type=int, default=DEFAULT_MAX_ARTICLE_CHARS,
                        help=f"truncate long articles (default {DEFAULT_MAX_ARTICLE_CHARS})")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    load_dotenv(Path(".env"))

    session = requests.Session()

    if args.list_models:
        for model_id in fetch_free_models(session) or list(MODEL_LIST_FALLBACK):
            log(model_id)
        return 0

    articles_dir = Path(args.articles)
    quizzes_dir = Path(args.quizzes)
    try:
        system, user_template = load_prompt(Path(args.prompt))
        articles = load_articles(articles_dir)
    except Exception as exc:
        log(f"ERROR: {exc}")
        return 1

    difficulties = tuple(d.strip() for d in args.difficulties.split(",") if d.strip())
    ids = {i.strip() for i in args.ids.split(",") if i.strip()} or None

    quizzes_dir.mkdir(parents=True, exist_ok=True)
    all_todo = plan_work(articles, quizzes_dir, difficulties, ids, args.force)

    if not all_todo:
        log("All requested quizzes already exist — nothing to do. (Use --force to regenerate.)")
        return 0

    todo = all_todo[:args.limit] if args.limit else all_todo

    pending_quizzes = sum(len(missing) for _, missing in all_todo)
    planned = sum(len(missing) for _, missing in todo)
    log(f"{pending_quizzes} quiz(zes) pending across {len(all_todo)} article(s).")
    if len(todo) < len(all_todo):
        log(f"This run handles the first {len(todo)} article(s) (~{planned} quiz(zes)); "
            f"{len(all_todo) - len(todo)} article(s) left for later runs.")
    primary, fallback_models = resolve_models(args, session)
    log(f"Using model '{primary}'.")
    if fallback_models:
        log(f"  failover chain: {' -> '.join(fallback_models)}")
    if ":free" not in primary:
        log("  NOTE: primary model is not a ':free' variant — this spends credits.")

    if args.dry_run:
        for article, missing in todo:
            for difficulty in missing:
                filename = quiz_filename(article["id"], slug_from_file(article["file"]), difficulty)
                log(f"  would write {quizzes_dir / filename} ({difficulty})")
        log("Dry run — no API calls made.")
        return 0

    api_key = os.environ.get("OPENROUTER_API_KEY", "").strip()
    if not api_key:
        log("ERROR: set OPENROUTER_API_KEY (env var or a .env file).")
        return 1

    log(f"  {free_requests_remaining(session, api_key)}.")

    reasoning_params = REASONING_PARAMS[args.reasoning]
    log(f"  reasoning: {args.reasoning}")

    written = skipped = 0
    failures: list[str] = []
    last_request = 0.0

    for article, missing in todo:
        slug = slug_from_file(article["file"])
        path = articles_dir / article["file"]
        try:
            body = strip_front_matter(path.read_text(encoding="utf-8"))
        except Exception as exc:
            failures.append(f"{article['id']} ({article['title']}): cannot read article: {exc}")
            continue
        if len(body) > args.max_article_chars:
            body = body[:args.max_article_chars].rstrip() + "\n\n...[article truncated]"

        for difficulty in missing:
            out_path = quizzes_dir / quiz_filename(article["id"], slug, difficulty)
            user = render_user(user_template, article, difficulty,
                               body_for_difficulty(body, difficulty))
            quiz = None
            note = ""
            reason = ""
            print(f"  [{article['id']}] {difficulty}: ", end="", flush=True)
            ticker = _make_ticker()

            for attempt in range(1, args.retries + 2):
                sleep_for(max(0.0, args.delay - (time.monotonic() - last_request)))
                last_request = time.monotonic()
                try:
                    reply = call_model(session, api_key, primary, system,
                                       user + note,
                                       attempts=args.transport_retries,
                                       fallback_models=fallback_models,
                                       request_timeout=args.request_timeout,
                                       reasoning=reasoning_params,
                                       on_progress=ticker)
                except ModelError as exc:
                    reason = str(exc)
                    note = ""
                    continue

                try:
                    raw = extract_json(reply)
                except (ValueError, json.JSONDecodeError) as exc:
                    reason = f"invalid JSON: {exc}"
                    note = ("\n\nYour previous reply was not valid JSON "
                            f"({exc}). Reply with only the JSON object.")
                    continue

                quiz, problems = normalize_quiz(raw, article["id"], difficulty)
                if quiz:
                    break
                reason = "; ".join(problems[:5])
                note = ("\n\nYour previous reply was rejected: "
                        + "; ".join(problems[:5])
                        + ". Reply again with only the corrected JSON object.")

            if not quiz:
                failures.append(f"{article['id']}/{difficulty}: {reason or 'no valid quiz'}")
                log(f"FAILED ({reason})")
                skipped += 1
                continue

            out_path.write_text(
                json.dumps(quiz, indent=2, ensure_ascii=False) + "\n",
                encoding="utf-8")
            written += 1
            log(f"wrote {out_path.name}")

    log("")
    log(f"Done. {written} quiz(zes) written, {skipped} failed this run.")

    remaining = plan_work(articles, quizzes_dir, difficulties, ids, False)
    remaining_quizzes = sum(len(missing) for _, missing in remaining)
    if not remaining:
        log("All requested quizzes are now generated — you're done.")
    else:
        log(f"{remaining_quizzes} quiz(zes) still pending across {len(remaining)} article(s) "
            "— re-run the same command to continue.")

    if failures:
        log(f"{len(failures)} problem(s) this run; those quizzes stayed pending, "
            "so a re-run retries them:")
        for problem in failures:
            log(f"  - {problem}")
        return 1
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except KeyboardInterrupt:
        log("")
        log("Interrupted — quizzes already written are saved; re-run to continue where you left off.")
        raise SystemExit(130)
