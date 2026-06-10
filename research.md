# The Interactive Guide

> 📖 This is the hub. Every other folder in the repo is the lab for one of its modules.

`index.html` is a single, self-contained file — open it in any browser, no install or
internet connection required (fonts load from Google Fonts when online; the guide still
works offline with fallback fonts).

## Viewing it

- **Locally:** double-click `index.html`, or from a terminal: `open guide/index.html`
  (macOS) / `start guide\index.html` (Windows).
- **Hosted:** if this repo has GitHub Pages enabled (Settings → Pages → deploy from
  branch), the guide is served live. Point Pages at the repo root or `/guide`.

## The 9 modules

| # | Module | Lab folder |
|---|---|---|
| 01 | The ecosystem map | — |
| 02 | Claude Chat | [`prompts/`](../prompts/) |
| 03 | Prompting that works | [`prompts/`](../prompts/) |
| 04 | Claude Cowork | [`cowork-workflows/`](../cowork-workflows/) |
| 05 | Claude Code & CLAUDE.md | [`claude-code-demos/`](../claude-code-demos/) |
| 06 | Connectors & MCP | [`troubleshooting/connectors-faq.md`](../troubleshooting/connectors-faq.md) |
| 07 | Claude Design | — |
| 08 | Student starter pack | [`prompts/`](../prompts/) + demos |
| 09 | Ethics & responsible use | [`workshop/exercises/04-ethics-scenarios.md`](../workshop/exercises/04-ethics-scenarios.md) |

## Editing notes

The quizzes are plain HTML with a small script: each question is a `.q` block whose
`data-answer` attribute is the index (0-based) of the correct option, with feedback text
in `data-good`/`data-bad`. Totals (progress bar, scores) are computed automatically from
the DOM — but the *static* text in the hero tags and rail checklist must be updated by
hand if modules are added. See the root `CLAUDE.md` for full conventions.
