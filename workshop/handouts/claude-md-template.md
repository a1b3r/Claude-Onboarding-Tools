# CLAUDE.md template (annotated)

Copy the skeleton below into a file named `CLAUDE.md` at your project's root —
Claude Code reads it automatically at the start of every session. Or run `/init`
and let Claude draft one from your actual project, then shape it with this as the
target. Delete the *(annotations in italics)*.

---

```markdown
# CLAUDE.md — <project name>

<One sentence: what this project is.>

## Commands
- Run: <command>
- Test: <command — and when to run it, e.g., "before every commit">
- <Any other daily-use command>

## Code style
- <Concrete, checkable rules only: "use ES modules, not CommonJS">
- <Naming/structure conventions a newcomer wouldn't guess>

## Workflow
- <Branch/commit etiquette: "always branch; never commit to main">
- <Review rules: "show and explain diffs before applying">
- Never commit secrets or .env files.

## Gotchas
- <The surprising things: "the /legacy folder is deprecated — don't touch">
- <Anything that broke before and must not break again>
```

---

**The four rules of a good CLAUDE.md:**

1. **Short.** One screen. If a human teammate wouldn't read it, it won't work.
2. **Checkable.** Every line can objectively be followed or not. ("Be careful" — no.
   "Never edit recipes.json directly" — yes.)
3. **Things code can't say.** Commands, conventions, history, warnings — not
   restatements of what's visible in the files.
4. **Alive.** Same mistake twice → new rule. (Typing `#` in a session adds one on
   the spot.)
