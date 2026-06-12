#!/usr/bin/env python3
"""Validate the internal structure of guide/index.html.

This automates the manual check described in CLAUDE.md: the number of
quiz blocks must match the rail checklist and the hero tag counts, and
every quiz question must be well-formed. Checks that:

- module sections, rail checklist items, and quiz blocks all carry the
  same module ids, in the same order
- TOTAL_MODULES in the script and the static counts in the hero tags,
  progress label, rail score chip, and final score all agree with the DOM
- every question has a valid data-answer index and data-good/data-bad
  feedback text

Run from the repo root: python scripts/check_guide.py
"""

import re
import sys
from pathlib import Path

GUIDE = Path(__file__).resolve().parent.parent / "guide" / "index.html"


def main() -> int:
    html = GUIDE.read_text(encoding="utf-8")
    errors = []

    modules = re.findall(r'<section class="module" id="(m\d+)"', html)
    rail = re.findall(r'data-rail="(m\d+)"', html)
    quizzes = re.findall(r'data-quiz="(m\d+)"', html)

    if modules != rail:
        errors.append(f"module sections {modules} != rail checklist {rail}")
    if modules != quizzes:
        errors.append(f"module sections {modules} != quiz blocks {quizzes}")

    total_modules_js = re.search(r"TOTAL_MODULES\s*=\s*(\d+)", html)
    if not total_modules_js:
        errors.append("TOTAL_MODULES not found in script")
    elif int(total_modules_js.group(1)) != len(modules):
        errors.append(
            f"TOTAL_MODULES is {total_modules_js.group(1)} but there are "
            f"{len(modules)} module sections"
        )

    hero_modules = re.search(r'<span class="tag">(\d+) modules</span>', html)
    if not hero_modules or int(hero_modules.group(1)) != len(modules):
        errors.append(
            f"hero tag says {hero_modules.group(1) if hero_modules else '?'} modules, "
            f"DOM has {len(modules)}"
        )

    progress = re.search(r'id="progressLabel">0 / (\d+) modules<', html)
    if not progress or int(progress.group(1)) != len(modules):
        errors.append(
            f"progress label says {progress.group(1) if progress else '?'} modules, "
            f"DOM has {len(modules)}"
        )

    # Questions: each .q block has one data-answer'd opts div
    questions = re.findall(
        r'<div class="opts" data-answer="(\d+)">(.*?)</div>', html, re.DOTALL
    )
    n_questions = len(questions)

    hero_questions = re.search(r'<span class="tag">(\d+) quiz questions</span>', html)
    if not hero_questions or int(hero_questions.group(1)) != n_questions:
        errors.append(
            f"hero tag says {hero_questions.group(1) if hero_questions else '?'} quiz "
            f"questions, DOM has {n_questions}"
        )

    for static_id in ("railScore", "finalScore"):
        m = re.search(rf'id="{static_id}">0 / (\d+)<', html)
        if not m or int(m.group(1)) != n_questions:
            errors.append(
                f"{static_id} says 0 / {m.group(1) if m else '?'}, "
                f"DOM has {n_questions} questions"
            )

    for i, (answer, opts_html) in enumerate(questions, 1):
        n_opts = opts_html.count('<button class="opt"')
        if not 0 <= int(answer) < n_opts:
            errors.append(f"question {i}: data-answer={answer} out of range (0..{n_opts - 1})")

    n_feedback = len(re.findall(r'class="feedback" data-good="[^"]+" data-bad="[^"]+"', html))
    if n_feedback != n_questions:
        errors.append(
            f"{n_feedback} feedback blocks with data-good/data-bad, but {n_questions} questions"
        )

    print(f"Guide: {len(modules)} modules, {n_questions} questions.")
    if errors:
        print(f"\n{len(errors)} structure problem(s):")
        for err in errors:
            print(f"  - {err}")
        return 1
    print("Guide structure is consistent.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
