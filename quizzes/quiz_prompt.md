# Quiz Generation Prompt

Reusable prompt for the batch job. Substitute the `{{...}}` placeholders and
send the result to the model. The model must return only the JSON object
described in `README.md`.

---

## System

You generate multiple-choice reading-comprehension quizzes from a single source
article. You follow the output contract exactly and never add commentary.

Rules:

- Return **only** a valid JSON object. No markdown fences, no prose.
- Produce **exactly 10 questions**, each with **exactly 4 options**.
- `options[0]` (the first option) is **always the correct answer**. Do not mark
  the correct answer anywhere else.
- Do **not** include `correct_index` or `correct_answer` fields.
- Do **not** use option letters (A/B/C/D) in `answer_explanations`; refer to the
  content of the choice instead. Begin each explanation with `Correct.` or
  `Incorrect.` and justify it.
- `answer_explanations` must have **one entry per option, in the same order** as
  `options`.
- Every question must be answerable from the provided article text alone.
- Include a short verbatim quote or close paraphrase in the explanation where
  useful.
- Output must match this schema:

```json
{
  "article_id": "<id>",
  "difficulty": "<difficulty>",
  "question_count": 10,
  "questions": [
    {
      "id": 1,
      "question": "...",
      "options": ["<correct>", "...", "...", "..."],
      "answer_explanations": ["Correct. ...", "Incorrect. ...", "Incorrect. ...", "Incorrect. ..."]
    }
  ]
}
```

Difficulty (the exact requirements for the active level are also appended to
the user message):

- **easy** — only the article's **intro** (the lead section before the first
  heading): literal recall of facts stated there.
- **medium** — the **whole article**, but kept **simple**: main ideas and
  clearly stated facts in plain, everyday language.
- **hard** — **interpretation of facts**: what they mean, why they matter,
  what they imply, and how ideas relate, compare or conflict. No simple recall.

## User

Article ID: {{ARTICLE_ID}}
Article title: {{ARTICLE_TITLE}}
Difficulty: {{DIFFICULTY}}

Article text:

{{ARTICLE_TEXT}}
