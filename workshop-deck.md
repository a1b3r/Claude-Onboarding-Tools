# FAQ — Claude Code

> 📖 Pairs with [Module 05](../guide/index.html#m5).

## "Install fails / `claude` isn't recognized"
(1) Confirm Node.js is installed: `node --version` — if not, install the LTS from
https://nodejs.org. (2) Permission errors with `npm install -g` usually mean npm's
global folder needs fixing — ask Claude (in Chat!) to walk you through npm global
prefix setup for your OS, or check the install docs:
https://docs.claude.com/en/docs/claude-code/overview. (3) After install, open a *new*
terminal window so your PATH refreshes.

## "It ignored my CLAUDE.md"
Common causes, in order of likelihood: the file isn't in the directory you launched
`claude` from (or a parent); the instruction is buried in a wall of text (CLAUDE.md
is guidance — short and specific gets followed, novels get diluted); the instruction
is vague ("be careful") rather than checkable ("never edit recipes.json directly").
Demo 02 in this repo exists precisely to build this skill.

## "It's asking permission for everything"
That's the safe default. Reduce friction without removing judgment: per-session
"don't ask again" approvals for repetitive safe actions, and check current permission
options with `/permissions` and the docs — there are modes that auto-approve
low-risk actions while still gating risky ones. Don't blanket-approve everything;
reviewing destructive actions is the job.

## "It went off the rails / made changes I didn't want"
Interrupt early — you can stop it mid-task and redirect. If changes landed: this is
why you work in git. `git status` and `git diff` show what changed;
`git checkout -- <file>` discards uncommitted changes to a file. Ask Claude itself to
revert its changes and explain what it did. Prevention: smaller steps, plan mode for
anything non-trivial, read diffs.

## "It seems confused / quality degraded mid-session"
Long sessions accumulate context debt. Use `/clear` between unrelated tasks. For a
big task gone sideways, sometimes the fastest fix is `/clear` + a better-written
brief incorporating what you learned.

## "It can't find files / acts like the project is empty"
You probably launched `claude` from the wrong directory. `pwd` shows where you are;
`cd` into the project root and relaunch.

## Escalate
Docs: https://docs.claude.com/en/docs/claude-code/overview · Report bugs: the `/bug`
command in Claude Code, or the GitHub issues link in the docs.
