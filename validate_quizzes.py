#!/usr/bin/env python3
"""Check every quiz JSON in quizzes/ against the project invariants.

Usage:
    python validate_quizzes.py [quizzes_dir]

Exits non-zero if any file is malformed. Prints one line per problem.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

TOP_KEYS = {"article_id", "difficulty", "question_count", "questions"}
DIFFICULTIES = {"easy", "medium", "hard"}
QUESTIONS_PER_QUIZ = 10
OPTIONS_PER_QUESTION = 4


def check(path: Path) -> list[str]:
    problems: list[str] = []
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        return [f"{path.name}: not valid JSON ({exc})"]

    if set(data) != TOP_KEYS:
        problems.append(f"{path.name}: top-level keys {sorted(data)} != {sorted(TOP_KEYS)}")
    if data.get("difficulty") not in DIFFICULTIES:
        problems.append(f"{path.name}: bad difficulty {data.get('difficulty')!r}")

    questions = data.get("questions")
    if not isinstance(questions, list) or len(questions) != QUESTIONS_PER_QUIZ:
        problems.append(f"{path.name}: expected {QUESTIONS_PER_QUIZ} questions, "
                        f"got {len(questions) if isinstance(questions, list) else '?'}")
        return problems
    if data.get("question_count") != len(questions):
        problems.append(f"{path.name}: question_count {data.get('question_count')} "
                        f"!= {len(questions)}")

    for i, q in enumerate(questions, 1):
        opts = q.get("options")
        if not isinstance(opts, list) or len(opts) != OPTIONS_PER_QUESTION:
            problems.append(f"{path.name}: q{i} has "
                            f"{len(opts) if isinstance(opts, list) else '?'} options")
            continue
        exps = q.get("answer_explanations")
        if not isinstance(exps, list) or len(exps) != len(opts):
            problems.append(f"{path.name}: q{i} explanation count != option count")
        if not all(isinstance(o, str) and o.strip() for o in opts):
            problems.append(f"{path.name}: q{i} has an empty option")
        if not q.get("question"):
            problems.append(f"{path.name}: q{i} missing question text")

    return problems


def main() -> int:
    quizzes_dir = Path(sys.argv[1] if len(sys.argv) > 1 else "quizzes")
    files = sorted(p for p in quizzes_dir.glob("*.json"))
    all_problems: list[str] = []
    for path in files:
        all_problems.extend(check(path))
    for problem in all_problems:
        print(problem)
    print(f"\n{len(files)} quiz file(s) checked, {len(all_problems)} problem(s).")
    return 1 if all_problems else 0


if __name__ == "__main__":
    raise SystemExit(main())
