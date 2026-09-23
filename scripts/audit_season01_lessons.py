#!/usr/bin/env python3
"""Audit season-01 zh lessons: length, mermaid, sections, stdout block."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs" / "season-01"

SECTIONS = ("## 费曼法讲解", "## 核心知识", "## 拓展领域", "## 实战总结")
TARGET_CJK = 0


def cjk_count(text: str) -> int:
    return sum(1 for c in text if "\u4e00" <= c <= "\u9fff")


def audit_day(day: int) -> dict:
    path = DOC / f"day-{day:02d}.md"
    text = path.read_text(encoding="utf-8")
    return {
        "day": day,
        "cjk": cjk_count(text),
        "mermaid": len(re.findall(r"```mermaid", text)),
        "tables": len(re.findall(r"^\|", text, re.M)),
        "blockquote": text.count("\n>"),
        "sections_ok": all(s in text for s in SECTIONS),
        "text_block": bool(re.search(r"```text\n", text)),
    }


def main() -> int:
    start, end = 1, 100
    if len(sys.argv) >= 2:
        start = end = int(sys.argv[1])
    rows = [audit_day(d) for d in range(start, end + 1 if len(sys.argv) < 2 else start + 1)]
    if len(sys.argv) >= 2:
        rows = [audit_day(start)]

    print(f"{'day':>5} {'cjk':>5} {'mmd':>3} {'tbl':>3} {'sec':>3} {'txt':>3}  note")
    for r in rows:
        note = []
        if r["cjk"] < TARGET_CJK:
            note.append(f"<{TARGET_CJK}字")
        if r["mermaid"] < 1:
            note.append("无mermaid")
        if not r["sections_ok"]:
            note.append("缺段")
        if not r["text_block"]:
            note.append("无text块")
        print(
            f"{r['day']:5d} {r['cjk']:5d} {r['mermaid']:3d} {r['tables']:3d} "
            f"{'Y' if r['sections_ok'] else 'N':>3} {'Y' if r['text_block'] else 'N':>3}  "
            + (", ".join(note) or "ok")
        )

    if len(rows) > 1:
        short = sum(1 for r in rows if r["cjk"] < TARGET_CJK)
        nommd = sum(1 for r in rows if r["mermaid"] < 1)
        print(f"\nSummary: {len(rows)} days, {short} under {TARGET_CJK} CJK, {nommd} without mermaid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
