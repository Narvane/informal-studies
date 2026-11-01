#!/usr/bin/env python3
"""Regenerate the study progress section in the repository README."""

from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
STUDIES = ROOT / "studies"
START = "<!-- STUDY_PROGRESS:START -->"
END = "<!-- STUDY_PROGRESS:END -->"
TOPIC_RE = re.compile(
    r"^\s*-\s+\[([ xX])\]\s+\[([ xX])\]\s+"
    r"\*\*([A-Za-z0-9][A-Za-z0-9._-]*)\*\*\s+—\s+(.+?)\s*$"
)


def bar(done: int, total: int, width: int = 10) -> str:
    if total == 0:
        return "▱" * width
    filled = round(done / total * width)
    return "▰" * filled + "▱" * (width - filled)


def percent(done: int, total: int) -> int:
    return round(done / total * 100) if total else 0


def study_summary(plan: Path) -> tuple[str, int, int, int]:
    text = plan.read_text(encoding="utf-8")
    title_match = re.search(r"^#\s+(.+?)\s*$", text, re.MULTILINE)
    title = title_match.group(1) if title_match else plan.parent.name.replace("-", " ").title()
    total = studied = evaluated = 0

    for number, line in enumerate(text.splitlines(), start=1):
        if not re.match(r"^\s*-\s+\[[ xX]\]", line):
            continue
        match = TOPIC_RE.match(line)
        if not match:
            raise ValueError(
                f"Invalid topic format in {plan.relative_to(ROOT)}:{number}. "
                "Use: - [ ] [ ] **ID** — title"
            )
        covered, understood = match.group(1).lower() == "x", match.group(2).lower() == "x"
        if understood and not covered:
            raise ValueError(
                f"Topic assessed without being marked as studied in {plan.relative_to(ROOT)}:{number}. "
                "Check the first box before the second."
            )
        total += 1
        studied += int(covered)
        evaluated += int(understood)

    return title, total, studied, evaluated


def render() -> str:
    plans = sorted(STUDIES.glob("*/plan.md"), key=lambda path: path.parent.name.casefold())
    if not plans:
        return "_No studies are registered yet. See `studies/README.md` to add the first one._"

    sections: list[str] = []
    for plan in plans:
        title, total, studied, evaluated = study_summary(plan)
        sections.append(
            "\n".join(
                [
                    f"### [{title}](studies/{plan.parent.name}/plan.md)",
                    f"**{total} proposed topics** · **{studied} studied** · **{evaluated} assessed**",
                    f"Study: `{bar(studied, total)}` {percent(studied, total)}%  ·  "
                    f"Understanding: `{bar(evaluated, total)}` {percent(evaluated, total)}%",
                ]
            )
        )
    return "\n\n".join(sections)


def main() -> None:
    text = README.read_text(encoding="utf-8")
    if START not in text or END not in text:
        raise SystemExit(f"Could not find the dashboard markers in {README.name}.")
    before, remainder = text.split(START, maxsplit=1)
    _, after = remainder.split(END, maxsplit=1)
    updated = f"{before}{START}\n{render()}\n{END}{after}"
    README.write_text(updated, encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
