#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Rebuild day-03..20 zh: four sections, no template filler outside 拓展."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs" / "season-01"

sys_path = ROOT / "scripts"
import sys

sys.path.insert(0, str(sys_path))
from _patch_season01_d03_20_depth import EXPAND, cjk_count  # noqa: E402
from _zh_knowledge_extension import pad_lesson_to_cjk  # noqa: E402

def extract_prefix(text: str) -> str:
    m = re.search(r"([\s\S]*?)\n---\n\n## 拓展领域\n", text)
    if not m:
        raise ValueError("missing 拓展领域")
    return m.group(1).strip()


def extract_short_expand(text: str) -> str:
    m = re.search(
        r"## 拓展领域\n\n([\s\S]*?\*\*Closing\*\*[^\n]*)",
        text,
    )
    return m.group(1).strip() if m else ""


def extract_lab(text: str) -> str:
    m = re.search(r"(## 实战总结[\s\S]*)", text)
    if not m:
        raise ValueError("missing 实战总结")
    return m.group(1).strip()


def rebuild_day(day: int) -> str:
    path = DOC / f"day-{day:02d}.md"
    text = path.read_text(encoding="utf-8")
    prefix = extract_prefix(text)
    short = extract_short_expand(text)
    lab = extract_lab(text)
    extra = EXPAND.get(day, "").strip()
    expand_block = short + "\n\n" + extra
    body = prefix + "\n\n---\n\n## 拓展领域\n\n" + expand_block
    body += "\n\n---\n\n" + lab
    body = pad_lesson_to_cjk(body, day)
    return body


def main() -> None:
    for day in range(3, 21):
        md = rebuild_day(day)
        n = cjk_count(md)
        (DOC / f"day-{day:02d}.md").write_text(md, encoding="utf-8")
        print(f"day-{day:02d}: CJK {n}")
    print("clean rebuild done")


if __name__ == "__main__":
    main()
