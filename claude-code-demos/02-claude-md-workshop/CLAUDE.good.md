# CLAUDE.md — recipe-box

A small command-line tool for storing and searching recipes in `recipes.json`.

## Commands
- Run: `python recipe_box.py list` / `add` / `search <term>`
- Test quickly: `python recipe_box.py search lemon` (sample data includes a match)

## Code style
- Plain Python, standard library only — no new dependencies.
- Functions stay under ~25 lines; prefer clear names over comments.

## Workflow
- Show and explain diffs before applying changes.
- Never modify `recipes.json` by hand-editing in a change — go through the program's
  add function so the JSON stays valid.
- Never delete files without asking, even if they look unused.

## Gotchas
- `recipes.json` must remain valid JSON or every command breaks; validate after edits.
- There is no database/ folder — storage is the JSON file. (An old doc said otherwise.)
