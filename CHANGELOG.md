# Changelog

All notable changes to this repo. Dates use YYYY-MM-DD.

## 2026-06-12

- New guide module 02, "Picking a model: Haiku, Sonnet, Opus & Fable" — model
  classes, use cases, and the capability/speed/usage trade-off. Former modules
  02–09 renumbered to 03–10 (guide anchors `#m2`–`#m9` shifted to `#m3`–`#m10`);
  all cross-links in the repo updated. The guide is now 10 modules / 30 quiz
  questions (~50 min).
- Guide quiz progress now persists in the browser via `localStorage`, with a
  "Reset progress" button in the checklist rail.
- Added CI (`.github/workflows/checks.yml`): `scripts/check_links.py` verifies
  every relative Markdown link and guide anchor; `scripts/check_guide.py`
  verifies the guide's module/quiz/checklist counts stay in sync.
- Reworded the audience from recent graduates to current undergraduate
  students across the guide and docs.

## 2026-06-10

- Added root `README.md` with repo map and project structure; removed
  `README-snippet.md` (folded into the README).
- Initial release.
- Interactive guide (`guide/index.html`): 9 modules, 27 quiz questions —
  ecosystem map, Claude Chat, prompting, Cowork, Claude Code & CLAUDE.md,
  Connectors & MCP, Claude Design, student starter pack, ethics.
- Prompt library: studying, career, writing, research, everyday.
- Claude Code demos 01–04 with sample projects and data.
- Cowork workflows 01–04 with fake practice files.
- Troubleshooting FAQs (Chat, Claude Code, Cowork, Connectors) + escalation guide.
- Workshop kit: facilitator guide, Markdown slide deck, 4 exercises, 2 handouts.
