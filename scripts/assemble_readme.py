#!/usr/bin/env python3
"""Assemble README from prologue + day list. runnable_max: link days 1..N only."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = Path(__file__).resolve().parent


def parse_titles_from_readme(path: Path) -> dict[int, str]:
    titles: dict[int, str] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        m = re.match(
            r"^- \[(?:第\d+天|Day \d+)　(.+)\]\(docs/season-01/day-(\d+)\.(?:en\.)?md\)",
            line,
        )
        if m:
            titles[int(m.group(2))] = m.group(1)
            continue
        m = re.match(r"^- (?:第\d+天|Day \d+)　(.+)$", line)
        if m:
            pass  # filled when scanning in order below
    if len(titles) == 100:
        return titles
    # scan list section in order
    titles = {}
    n = 0
    for line in path.read_text(encoding="utf-8").splitlines():
        m = re.match(
            r"^- \[(?:第(\d+)天|Day (\d+))　(.+)\]\(docs/season-01/day-(\d+)\.(?:en\.)?md\)",
            line,
        )
        if m:
            day = int(m.group(4))
            titles[day] = m.group(3)
            continue
        m = re.match(r"^- (?:第(\d+)天|Day (\d+))　(.+)$", line)
        if m:
            day = int(m.group(1) or m.group(2))
            titles[day] = m.group(3)
    return titles


def build_day_lines(titles: dict[int, str], *, en: bool, runnable_max: int) -> str:
    lines: list[str] = []
    for n in range(1, 101):
        t = titles[n]
        if en:
            label = f"Day {n:02d}"
            href = f"docs/season-01/day-{n:02d}.en.md"
        else:
            label = f"第{n:02d}天"
            href = f"docs/season-01/day-{n:02d}.md"
        if n <= runnable_max:
            lines.append(f"- [{label}　{t}]({href})")
        else:
            lines.append(f"- {label}　{t}")
    return "\n".join(lines)


def assemble(prologue: Path, out: Path, *, en: bool, runnable_max: int) -> None:
    titles = parse_titles_from_readme(out if out.exists() else ROOT / "README.md")
    if len(titles) != 100:
        raise SystemExit(f"expected 100 titles, got {len(titles)}")
    body = prologue.read_text(encoding="utf-8")
    day_block = build_day_lines(titles, en=en, runnable_max=runnable_max)
    if "<!-- DAY_LIST -->" not in body:
        raise SystemExit("DAY_LIST marker missing")
    out.write_text(body.replace("<!-- DAY_LIST -->", day_block), encoding="utf-8")


def main() -> int:
    runnable = int(sys.argv[1]) if len(sys.argv) > 1 else 100
    assemble(SCRIPTS / "readme_prologue_zh.md", ROOT / "README.md", en=False, runnable_max=runnable)
    assemble(SCRIPTS / "readme_prologue_en.md", ROOT / "README.en.md", en=True, runnable_max=runnable)
    print(f"Wrote README(s), runnable_max={runnable}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
