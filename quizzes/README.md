# Reading-Quiz JSON — Format & Generation Spec

> Machine-readable quiz files generated from the article corpus in `../articles/`.
> This is the source of truth for the quiz format. Keep it updated when the
> schema changes.

## Layout

One JSON file per article **per difficulty**, all flat in this folder (no
subfolders):

```
quizzes/0001_the_arts_easy.json
quizzes/0001_the_arts_medium.json
quizzes/0001_the_arts_hard.json
```

Naming: `<article_id>_<slug>_<difficulty>.json`, where `difficulty` is one of
`easy`, `medium`, `hard`. There are **3 quizzes per article** and **10 questions
per quiz** (300 articles → 900 files, 9000 questions).

## Schema

```jsonc
{
  "article_id": "0001",          // machine key; snake_case everywhere in code
  "difficulty": "easy",          // easy | medium | hard
  "question_count": 10,
  "questions": [
    {
      "id": 1,                                        // 1-based, sequential
      "question": "The arts are also commonly referred to as what?",
      "options": [                                    // ALWAYS exactly 4
        "The creative arts",                          // [0] is ALWAYS the correct answer
        "The natural sciences",
        "The social sciences",
        "The applied sciences"
      ],
      "answer_explanations": [                        // one entry per option, same order
        "Correct. The opening line states: '...'",
        "Incorrect. The natural sciences study the physical world...",
        "Incorrect. The social sciences study human society...",
        "Incorrect. 'Applied sciences' refers to practical applications..."
      ]
    }
  ]
}
```

## Hard rules (invariants)

These never vary between files:

1. **First option is the correct answer.** The client shuffles options for
   display, so the JSON always stores the correct choice at `options[0]`.
2. **No `correct_index` and no `correct_answer`.** Position is the contract;
   extra fields are omitted.
3. **Exactly 4 options** and **exactly 4 `answer_explanations`**, in the same
   order as `options`.
4. **No option letters (A/B/C/D) anywhere in `answer_explanations`.** The client
   shuffles options, which would invalidate letter references — explanations
   refer to the *content* of the choice ("Correct. ...", "Incorrect. ...").
5. **`article_id`** (snake_case) is the join key everywhere in code/machine
   data. (`articles/README.md` is human-facing and may phrase it differently.)
6. **No article metadata in the quiz** — no title, URL, source, license, or
   generated date. That lives on the article. The quiz carries only
   `article_id`, `difficulty`, `question_count`, and `questions`.
7. Output is **strict JSON** (no comments, no markdown fences).
8. Every question must be **answerable from the article text alone**.

## Difficulty definitions

Difficulty is about the *kind of thinking*, not how obscure the fact is.

- **easy** — drawn **only from the article's intro** (the lead section before
  the first heading): literal recall of facts stated there.
- **medium** — drawn from the **whole article**, but kept **simple**: main
  ideas and clearly stated facts in plain language.
- **hard** — **interpretation of facts**: what they mean, why they matter,
  what they imply, and how ideas relate, compare or conflict. Not simple recall.

These are enforced per quiz: `../generate_quizzes.py` clips the article text to
the intro for **easy** and appends the matching requirements to the model's
user message for each level (see `DIFFICULTY_GUIDANCE`).

## Generation

Quizzes are **pre-generated in a batch job** (`../generate_quizzes.py`), not
created at request time. The reusable prompt lives in
[`quiz_prompt.md`](quiz_prompt.md).

Pipeline shape:

1. Read an article (`../articles/<file>`), its `id`, and the manifest metadata.
2. For each difficulty, call the model with the prompt in `quiz_prompt.md`.
3. Parse the JSON and **validate against the invariants above**; regenerate on
   failure (bounded retries).
4. Write `quizzes/<id>_<slug>_<difficulty>.json`.
5. Skip quizzes whose file already exists, so the job is **resumable**.

```bash
export OPENROUTER_API_KEY=sk-or-...                 # or put it in .env
./venv/bin/python generate_quizzes.py --limit 20    # a chunk
./venv/bin/python generate_quizzes.py               # everything still pending
```

Run it in **chunks** (`--limit N` counts articles) to stay within the free
rate limits (OpenRouter: 20 requests/min; 1,000 free requests/day with ≥$10
credits). Re-run the same command to continue where the last run stopped.

### Choosing the model

Run from a terminal, the script **asks which model to use** on each run: it
lists the available free models and lets you pick a **primary** and its
**fallbacks** by number or id. `--list-models` prints the same list and exits.

Skip the picker by naming the models up front (either flag suppresses the
prompt), or use `--no-prompt` to accept the defaults:

```bash
./venv/bin/python generate_quizzes.py --limit 20 --primary nvidia/nemotron-3.5-super-vl:free
./venv/bin/python generate_quizzes.py --limit 20 \
    --primary nvidia/nemotron-3.5-super-vl:free \
    --fallback-models "cohere/north-mini-code:free,liquid/lfm-2.5-2.6b:free"
./venv/bin/python generate_quizzes.py --limit 20 --fallback-models ""   # from the default primary, no fallback
```

When input isn't a terminal (piped/scripted) the defaults are used, so
unattended runs never block.

### Reliability & failover

Requests go to OpenRouter with a **failover chain**: if the primary model is
down, overloaded (HTTP 503), or rate-limited (429), the next model in
`--fallback-models` is tried automatically. OpenRouter allows **at most 3 models
per request**, so the chain is primary + up to **2** fallbacks (extra entries are
dropped with a warning). The default chain is all `:free` variants, so failover
never spends credits. Override it with `--fallback-models "a:free,b:free"`, or
pass `--fallback-models ""` to disable.

Transport failures are retried with exponential backoff and jitter (honouring
`Retry-After`); non-retryable errors (401/402/403/404) fail fast. Replies are
read as a **stream**, so each quiz prints progress dots and a model that stalls
(no data for 45s) or exceeds the **total time cap** (`--request-timeout`, default
180s) is abandoned and **dropped from the chain**, so a faster fallback takes
over. A reply that is cut off (`finish_reason: "length"`) or ends early is
retried rather than accepted. Invalid or incomplete replies are re-prompted a
bounded number of times. A quiz that still fails is **not written**, so it stays
pending and is retried on the next run. `Ctrl+C` stops cleanly — everything
written so far is kept.

Free models often spend most of `max_tokens` on hidden "reasoning" and truncate
the JSON before it is finished. The script therefore sends
`reasoning: {enabled: false}` by default (`--reasoning`, one of
`off|auto|low|medium|high`). With `off`, a quiz takes ~15s instead of ~30s and
completes reliably.

### Validating output

`../validate_quizzes.py` checks every file in `quizzes/` against the invariants
above (10 questions, 4 options, 4 explanations, correct key set) and prints a
summary:

```bash
./venv/bin/python validate_quizzes.py
```

### Knowing when you're done

Each run prints how many quizzes are pending, then finishes with either:

```
All requested quizzes are now generated — you're done.
```

or a line telling you how many are still pending. **Re-run the same command
until you see the "done" line.** Do not pass `--force` between chunk runs, or it
regenerates finished work.

## Licensing

Questions and explanations are derived from Wikipedia text, which is under
**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)**. Keep the
attribution on the article page.
