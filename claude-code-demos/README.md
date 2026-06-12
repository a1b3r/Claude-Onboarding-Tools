# Claude Code Demos

> 📖 Pairs with [Module 06 (Claude Code & CLAUDE.md)](../guide/index.html#m6).

Four hands-on exercises, easiest first. None require prior coding experience — demo 01
and 04 are specifically designed for non-CS majors.

## Setup (once)

1. Install Node.js if you don't have it: https://nodejs.org (LTS version).
2. Install Claude Code: `npm install -g @anthropic-ai/claude-code`
   (current install options: https://docs.claude.com/en/docs/claude-code/overview)
3. Open a terminal, `cd` into a demo folder, and run `claude`.

> **What's a terminal?** The text-based command window on your computer. macOS: open
> the "Terminal" app. Windows: open "PowerShell." `cd foldername` moves into a folder;
> `ls` (macOS) / `dir` (Windows) lists what's there.

## The demos

| # | Demo | You'll practice | Time |
|---|---|---|---|
| 01 | [First session](01-first-session/) | Exploring, asking, making a small change, reviewing a diff | 20 min |
| 02 | [CLAUDE.md workshop](02-claude-md-workshop/) | Diagnosing a bad CLAUDE.md and fixing it | 25 min |
| 03 | [Portfolio site](03-build-a-portfolio-site/) | Plan mode, iterating on a real multi-file project | 60–90 min |
| 04 | [Data cleanup](04-data-cleanup/) | Using Claude Code for non-coding work (messy CSV → clean analysis) | 30 min |

## Safety habits (apply to every demo)

- Work inside the demo folder, not your real projects, until you're comfortable.
- Read what Claude proposes before approving — especially anything that deletes or
  runs commands.
- A **diff** is the before/after view of a change. Reading diffs is the core skill;
  approving without reading is how surprises happen.
- `/clear` resets the conversation context between unrelated tasks.
