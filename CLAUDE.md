# CLAUDE.md — claude-onboarding

This repo is an onboarding curriculum for the Claude ecosystem, aimed at recent
graduates from all majors. The interactive guide is the hub; everything else is
the lab.

## Project structure

- `guide/index.html` — the interactive guide (single self-contained HTML file,
  no build step). Source of truth for module numbering and terminology.
- `prompts/` — copy-paste prompt templates, one file per life area.
- `claude-code-demos/` — runnable exercises, numbered by difficulty. Each demo
  folder has a README with instructions and (where needed) a tiny sample project.
- `cowork-workflows/` — Cowork "recipes" plus `sample-files/` practice data.
- `troubleshooting/` — symptom-based FAQs, one file per product.
- `workshop/` — facilitator guide, Markdown slide deck, exercises, handouts.

## Conventions

- **Audience first.** Write for a smart reader with zero technical background.
  Define every term of art on first use (terminal, diff, repo, etc.).
- **Tone:** warm, direct, practical. No hype. Short sentences over long ones.
- **Prompt templates** always follow the four-part pattern: role, process,
  standard, guardrail. Show templates in fenced code blocks with [placeholders].
- **Module cross-links.** Every doc links back to its guide module at the top,
  e.g. `> 📖 Pairs with [Module 03 of the guide](../guide/index.html#m3)`.
- **Sample data is always fake.** Names, vendors, and figures in
  `sample-files/` and demo data are invented. Never replace them with real data.
- **No volatile facts.** Plan pricing, usage limits, and availability change
  often — link to official docs (support.claude.com, docs.claude.com) instead
  of hardcoding them. If a doc must mention a dated fact, date-stamp it.
- **Numbered folders stay stable.** Don't renumber demos/workflows; append new
  ones at the end.

## Workflow rules

- Update `CHANGELOG.md` with a dated entry for any content change.
- `guide/index.html` is hand-maintained: when editing, keep it a single file
  (inline CSS/JS, no external dependencies beyond Google Fonts), preserve the
  quiz markup pattern (`data-quiz`, `data-answer`, `data-good`/`data-bad`),
  and keep quiz counts in sync with the rail checklist and hero tags.
- Markdown style: ATX headings, one H1 per file, wrap lines at ~100 chars,
  fenced code blocks with language hints where applicable.
- Never commit real personal data, secrets, or `.env` files.

## Commands

- Preview the guide: open `guide/index.html` in a browser (no server needed).
- Validate guide structure after edits: confirm the number of `data-quiz`
  blocks matches the rail checklist items and the hero tag counts.
