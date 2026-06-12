#!/usr/bin/env python3
"""Check that every relative link in the repo's Markdown files resolves.

Verifies that:
- relative link targets (files and folders) exist on disk
- anchors pointing into guide/index.html (e.g. ../guide/index.html#m3)
  match a real id="..." in the HTML

External links (http/https/mailto) are not fetched — they're skipped.
Run from the repo root: python scripts/check_links.py
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
SKIP_PREFIXES = ("http://", "https://", "mailto:")


def html_ids(path: Path) -> set:
    return set(re.findall(r'id="([^"]+)"', path.read_text(encoding="utf-8")))


def main() -> int:
    errors = []
    checked = 0

    for md in sorted(ROOT.rglob("*.md")):
        if ".git" in md.parts:
            continue
        text = md.read_text(encoding="utf-8")
        # Links shown inside code spans or fenced code blocks are examples,
        # not navigation — drop them before scanning.
        text = re.sub(r"```.*?```", "", text, flags=re.DOTALL)
        text = re.sub(r"`[^`\n]*`", "", text)
        for match in LINK_RE.finditer(text):
            target = match.group(1)
            if target.startswith(SKIP_PREFIXES) or target.startswith("#"):
                continue
            checked += 1
            path_part, _, anchor = target.partition("#")
            resolved = (md.parent / path_part).resolve()
            rel = md.relative_to(ROOT)
            if not resolved.exists():
                errors.append(f"{rel}: broken link -> {target}")
                continue
            if anchor and resolved.suffix == ".html":
                if anchor not in html_ids(resolved):
                    errors.append(f"{rel}: missing anchor #{anchor} in {path_part}")

    print(f"Checked {checked} relative links.")
    if errors:
        print(f"\n{len(errors)} broken link(s):")
        for err in errors:
            print(f"  - {err}")
        return 1
    print("All links resolve.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
