#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Apply day-specific 知识延伸 to all season-01 zh lessons."""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs" / "season-01"
sys.path.insert(0, str(ROOT / "scripts"))
from _zh_knowledge_extension import cjk_count, pad_lesson_to_cjk  # noqa: E402


def main() -> int:
    for day in range(1, 101):
        path = DOC / f"day-{day:02d}.md"
        if not path.exists():
            print(f"missing {path.name}")
            continue
        md = path.read_text(encoding="utf-8")
        new_md = pad_lesson_to_cjk(md, day)
        path.write_text(new_md, encoding="utf-8")
        print(f"day-{day:02d}: CJK {cjk_count(new_md)} (strip only)")
    print("done (no auto padding)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
