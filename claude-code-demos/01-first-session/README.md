# Demo 01 — Your First Claude Code Session

**Goal:** get comfortable with the explore → ask → change → review loop on a tiny,
unbreakable project. The `study-timer/` folder contains a small Python program with
a deliberate bug.

## Steps

1. In a terminal: `cd study-timer` then run `claude`.
2. **Explore.** Ask: *"Read this project and explain what it does in plain English."*
3. **Investigate.** Ask: *"Users report the break timer never ends. Find the bug and
   explain it to me before changing anything."*
   (There is one — see if Claude finds the same one you would.)
4. **Change.** Ask Claude to fix it. **Read the diff it shows you** before approving.
5. **Verify.** Ask: *"Run the program with a 0.1-minute session so we can confirm the
   fix quickly."*
6. **Stretch (optional).** Ask Claude to add a feature: a motivational quote from
   `quotes.txt` shown at each break. Watch how it plans before editing.

## What you should notice

- Claude reads files before editing them (and you can require this by asking).
- Every change comes as a reviewable diff — you're the approver, not a spectator.
- Plain-English instructions work. You never typed a line of code.

## Done when

The timer counts down both sessions and breaks correctly, and you read at least one
diff before approving it.

---

<details>
<summary>Facilitator spoiler — the planted bug</summary>

In `countdown()`, the line `if label == "Study": seconds -= 1` means the counter only
decreases during study sessions — so break countdowns loop forever. The fix is to
decrement unconditionally. Don't reveal this to learners; finding it via Claude is the
exercise.
</details>
