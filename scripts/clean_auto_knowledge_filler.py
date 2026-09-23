#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Remove auto-generated 知识延伸 blocks and 延伸 § padding from zh lessons."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs" / "season-01"

FILLER_LINE = re.compile(
    r"^\*\*(手算抽查|可视化纪律|跨语言|ensemble 与 ablation)（延伸 §\d+）\*\*.*$",
    re.M,
)


def clean_md(text: str) -> str:
    # Drop entire auto ### 知识延伸 section (through --- or 实战总结).
    text = re.sub(
        r"\n### 知识延伸[\s\S]*?(?=\n---\n\n## 实战总结\n|\n## 实战总结\n)",
        "\n",
        text,
    )
    # Any paragraph containing auto-padding marker.
    parts = re.split(r"\n\n+", text)
    kept = [
        p
        for p in parts
        if "延伸 §" not in p
        and "本课 stdout 锚点：" not in p
        and p.strip() != "---"
    ]
    text = "\n\n".join(kept)
    text = FILLER_LINE.sub("", text)
    text = re.sub(r"\n{4,}", "\n\n\n", text)
    # Stray --- immediately before 实战总结 with nothing between.
    text = re.sub(r"\n---\n\n(?=## 实战总结\n)", "\n\n", text)
    return text


def main() -> None:
    for path in sorted(DOC.glob("day-*.md")):
        if path.name.endswith(".en.md"):
            continue
        raw = path.read_text(encoding="utf-8")
        new = clean_md(raw)
        if new != raw:
            path.write_text(new, encoding="utf-8")
            print(f"cleaned {path.name}")


if __name__ == "__main__":
    main()
