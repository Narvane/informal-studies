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
                f"Formato de tópico inválido em {plan.relative_to(ROOT)}:{number}. "
                "Use: - [ ] [ ] **ID** — título"
            )
        covered, understood = match.group(1).lower() == "x", match.group(2).lower() == "x"
        if understood and not covered:
            raise ValueError(
                f"Tópico avaliado sem estar estudado em {plan.relative_to(ROOT)}:{number}. "
                "Marque a primeira caixa antes da segunda."
            )
        total += 1
        studied += int(covered)
        evaluated += int(understood)

    return title, total, studied, evaluated


def render() -> str:
    plans = sorted(STUDIES.glob("*/plan.md"), key=lambda path: path.parent.name.casefold())
    if not plans:
        return "_Nenhum estudo cadastrado ainda. Veja `studies/README.md` para adicionar o primeiro._"

    sections: list[str] = []
    for plan in plans:
        title, total, studied, evaluated = study_summary(plan)
        sections.append(
            "\n".join(
                [
                    f"### [{title}](studies/{plan.parent.name}/plan.md)",
                    f"**{total} tópicos propostos** · **{studied} estudados** · **{evaluated} avaliados**",
                    f"Estudo: `{bar(studied, total)}` {percent(studied, total)}%  ·  "
                    f"Compreensão: `{bar(evaluated, total)}` {percent(evaluated, total)}%",
                ]
            )
        )
    return "\n\n".join(sections)


def main() -> None:
    text = README.read_text(encoding="utf-8")
    if START not in text or END not in text:
        raise SystemExit(f"Não encontrei os marcadores do painel em {README.name}.")
    before, remainder = text.split(START, maxsplit=1)
    _, after = remainder.split(END, maxsplit=1)
    updated = f"{before}{START}\n{render()}\n{END}{after}"
    README.write_text(updated, encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()

\n