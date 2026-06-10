# Demo 03 — Build Your Portfolio Site

**Goal:** ship a real, personal artifact — a portfolio/personal site — while practicing
the workflow that matters on bigger projects: **plan first, build in steps, review
diffs, course-correct early.**

This demo is prompts-only: you start from an empty folder, because that's how real
projects start. Budget 60–90 minutes.

## Optional warm-up: design first

If you have access to Claude Design (guide, Module 07), prototype the look there first
and export/screenshot it. Showing Claude Code a picture of the target beats describing
it in words.

## The checkpoints

**1. Brief and plan (don't skip this).** Create an empty folder, start `claude`, and:

```text
I want to build a single-page personal portfolio site: plain HTML, CSS, and a
little JavaScript — no frameworks, no build step, so I can host it free on
GitHub Pages. Sections: intro, about, 2–3 projects, contact links.
Before writing any code, ask me what you need to know about my content and
style preferences, then propose a plan with the files you'll create.
```

Answer its questions. Approve the plan only when it matches what you want.
(Tip: Claude Code has a plan mode — check `/help` — that keeps it from editing files
while you're still deciding.)

**2. Skeleton.** Have it build structure and placeholder content only. Open
`index.html` in your browser. This is your first checkpoint: layout right, content fake.

**3. Real content.** Give it your actual bio and project descriptions (or point it at
your resume). One section per request — small steps make diffs reviewable.

**4. Polish pass.**

```text
Review the site like a picky design friend: spacing, font sizes, mobile view,
contrast. List the top 5 improvements, let me choose which to apply.
```

**5. Ship it (optional).** Ask Claude to walk you through publishing on GitHub Pages,
step by step, explaining each git command as it goes.

## Done when

The site opens in your browser, contains your real content, looks acceptable on a
phone-width window — and you can name one moment where you course-corrected Claude
instead of accepting its first idea.
