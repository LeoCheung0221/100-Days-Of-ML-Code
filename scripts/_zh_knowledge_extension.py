#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Legacy hook: auto 知识延伸 padding disabled (no forced CJK)."""
from __future__ import annotations

import re


def cjk_count(text: str) -> int:
    return sum(1 for c in text if "\u4e00" <= c <= "\u9fff")


def pad_lesson_to_cjk(md: str, day: int, min_cjk: int = 0) -> str:
    """No-op: do not inject filler. Strip stray auto sections if present."""
    md = re.sub(r"\n### 知识延伸[\s\S]*?(?=\n## 实战总结\n|\n---\n\n## 实战总结\n)", "\n", md)
    parts = re.split(r"\n\n+", md)
    kept = [p for p in parts if "延伸 §" not in p and p.strip() != "---"]
    return "\n\n".join(kept)
