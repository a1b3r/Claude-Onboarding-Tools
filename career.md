# Workflow 02 — Receipts → Expense Spreadsheet

**Situation:** a pile of receipts (here: text exports; in real life often screenshots —
the brief works the same) that needs to become one clean expense sheet.
**Practice data:** `sample-files/02-receipts/` (copy it out of the repo first).

## The brief

```text
Read every receipt in this folder and build expenses.xlsx with columns:
date (YYYY-MM-DD), vendor, category, amount, payment method, source file.

Rules:
- Categories: food, transport, supplies, entertainment, other. If unsure,
  use other and flag it.
- If any value is unreadable or missing from a receipt, leave the cell blank
  and list that receipt in a "needs review" section of your summary — never
  guess an amount.
- Add a second sheet: totals by category and by month.
- Don't modify or move the original receipt files.
```

## Expected outcome

One spreadsheet, every row traceable to a source file, ambiguities flagged rather
than guessed.

## Review checklist

- [ ] Row count matches receipt count (minus legitimately flagged ones).
- [ ] **Verify every amount on 3 random rows against the source receipt.** Numbers are
      where errors are costly — this check is non-negotiable for real finances.
- [ ] Totals sheet sums match a quick mental estimate.
- [ ] The planted trap: one receipt in the practice data has a smudged/ambiguous
      total. It should appear in "needs review," not as a confident number.

**The transferable rule:** for anything numeric, "never guess — flag it" goes in the
brief, and human spot-checks go in the review.
