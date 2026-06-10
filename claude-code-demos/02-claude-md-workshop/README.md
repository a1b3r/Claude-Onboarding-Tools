# Demo 02 — The CLAUDE.md Workshop

**Goal:** learn what makes a CLAUDE.md good by fixing a bad one.

The `recipe-box/` folder is a small project for storing recipes. It ships with
`CLAUDE.bad.md` — a real-world-style mess: bloated, vague, contradictory, and missing
the things Claude actually needs. Your job is to turn it into something useful, then
compare against `CLAUDE.good.md`.

## Steps

1. Read `CLAUDE.bad.md` yourself first. Note everything that strikes you as useless,
   vague, or contradictory (there are at least six planted problems).
2. `cd recipe-box`, rename the bad file into place: `cp ../CLAUDE.bad.md CLAUDE.md`,
   and start `claude`.
3. Ask: *"Read CLAUDE.md and this project. Which instructions in CLAUDE.md are vague,
   contradictory, impossible to follow, or missing? What important context about this
   project is absent?"*
4. Ask Claude to rewrite it following best practices: short, specific commands, code
   style, workflow rules, gotchas.
5. Compare your result with `../CLAUDE.good.md`. Yours doesn't need to match — it
   needs to be *checkable*: could every line be objectively followed or not?

## The planted problems (don't peek until step 5)

<details>
<summary>Reveal</summary>

1. **Vague virtues** ("write good code", "be careful") — uncheckable, so useless.
2. **Contradiction** — says "always add comments to every line" AND "keep code
   comment-free."
3. **Missing commands** — never says how to run or test the project.
4. **Stale info** — references a `database/` folder that doesn't exist.
5. **Novel-length irrelevance** — three paragraphs about the company's founding story.
6. **Dangerous default** — "feel free to delete files that look unused."
</details>

## Done when

Your CLAUDE.md fits on one screen, every rule is checkable, and it includes: run/test
commands, style rules, workflow rules, and at least one project-specific gotcha.
