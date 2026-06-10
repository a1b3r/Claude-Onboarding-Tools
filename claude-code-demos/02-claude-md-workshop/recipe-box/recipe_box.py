"""Recipe Box — a tiny command-line recipe store backed by recipes.json.

Usage:
  python recipe_box.py list
  python recipe_box.py add
  python recipe_box.py search <term>
"""

import json
import sys
from pathlib import Path

DATA_FILE = Path(__file__).parent / "recipes.json"


def load_recipes():
    if not DATA_FILE.exists():
        return []
    return json.loads(DATA_FILE.read_text())


def save_recipes(recipes):
    DATA_FILE.write_text(json.dumps(recipes, indent=2))


def cmd_list(recipes):
    if not recipes:
        print("No recipes yet. Add one with: python recipe_box.py add")
        return
    for r in recipes:
        print(f"- {r['name']} ({r['minutes']} min) — tags: {', '.join(r['tags'])}")


def cmd_search(recipes, term):
    term = term.lower()
    hits = [r for r in recipes
            if term in r["name"].lower() or any(term in t.lower() for t in r["tags"])]
    if not hits:
        print(f"No recipes matching '{term}'.")
        return
    for r in hits:
        print(f"- {r['name']} ({r['minutes']} min)")


def cmd_add(recipes):
    name = input("Recipe name: ").strip()
    minutes = int(input("Minutes to make: ").strip())
    tags = [t.strip() for t in input("Tags (comma-separated): ").split(",") if t.strip()]
    recipes.append({"name": name, "minutes": minutes, "tags": tags})
    save_recipes(recipes)
    print(f"Saved '{name}'.")


def main():
    recipes = load_recipes()
    args = sys.argv[1:]
    if not args or args[0] == "list":
        cmd_list(recipes)
    elif args[0] == "add":
        cmd_add(recipes)
    elif args[0] == "search" and len(args) > 1:
        cmd_search(recipes, " ".join(args[1:]))
    else:
        print(__doc__)


if __name__ == "__main__":
    main()
