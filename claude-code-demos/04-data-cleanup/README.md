# Demo 04 — Data Cleanup (no coding background needed)

**Goal:** experience why non-programmers use Claude Code: it can write and run little
programs *for you* to process data, while you just describe what you want.

`club-signups.csv` is a deliberately messy spreadsheet export — 40 rows of fictional
sign-ups for a (made-up) university hiking club, with classic real-world problems
hiding in it.

## Steps

1. `cd` into this folder and run `claude`.
2. **Audit first:** *"Read club-signups.csv and list every data-quality problem you
   find. Don't fix anything yet — just report, with examples."*
   It should find most of: inconsistent date formats, duplicate people, mixed-case and
   misspelled membership tiers, blank emails, a phone number in the email column,
   inconsistent name capitalization — and two rows where an unquoted comma inside the
   date ("Jan 27, 2026") breaks the column alignment entirely.
3. **Decide the rules.** You're the boss: tell it how to standardize (e.g., dates as
   YYYY-MM-DD, tiers as Basic/Plus, drop exact duplicates but flag near-duplicates for
   review instead of deleting them).
4. **Clean:** *"Apply those rules. Write the result to club-signups-clean.csv and a
   report of every change to cleanup-report.md. Never edit the original file."*
5. **Analyze:** *"From the clean file: how many members per tier, sign-ups per month,
   and what percentage of rows had at least one problem?"*
6. **Verify one thing yourself.** Open both CSVs and spot-check 3 rows. Trust, but
   verify — that habit is the real lesson (guide, Module 09).

## Done when

You have a clean CSV, a change report, three answered questions about the data — and
the original file untouched.
