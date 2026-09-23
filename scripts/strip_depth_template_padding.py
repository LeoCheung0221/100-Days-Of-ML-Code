#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Remove DEPTH_TEMPLATES filler paragraphs from season-01 zh lessons."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs" / "season-01"
sys.path.insert(0, str(ROOT / "scripts"))
from _zh_depth_templates import DEPTH_TEMPLATES  # noqa: E402


def template_regexes() -> list[re.Pattern[str]]:
    out: list[re.Pattern[str]] = []
    for tpl in DEPTH_TEMPLATES:
        esc = re.escape(tpl)
        esc = esc.replace(re.escape("{day}"), r"\d+")
        out.append(re.compile(r"^" + esc + r"$"))
    # Also match "第N课" / "第N天" variants embedded in same sentences
    return out


PATTERNS = template_regexes()

MARKERS = (
    "回测代码审查时，第",
    "混池实验（如第37课）",
    "第1课写 commit message 时建议带 verify",
    "第1课扩展阅读：Lopez de Prado",
    "第1课 narrative 收束",
)


def is_template_paragraph(para: str) -> bool:
    p = para.strip()
    if not p:
        return False
    for pat in PATTERNS:
        if pat.match(p):
            return True
    for day in range(1, 101):
        for tpl in DEPTH_TEMPLATES:
            if p == tpl.format(day=day):
                return True
    # Loose: single-line checklist referencing "第N课" at start without ** bold headers
    if any(p.startswith(m.replace("第1", f"第{d}")) for d in range(1, 101) for m in MARKERS if "第1" in m):
        return True
    if p.startswith("回测代码审查时，第") and "课要求先打开终端" in p:
        return True
    if "课扩展阅读：" in p and p.startswith("第") and "课" in p[:8]:
        return True
    if re.match(r"^第\d+课与第\d+天", p):
        return True
    if re.match(r"^第\d+课写 commit message", p):
        return True
    if re.match(r"^第\d+课 narrative 收束", p):
        return True
    if re.match(r"^第\d+课读者若是", p):
        return True
    if re.match(r"^第\d+课若在 (notebook|Docker)", p):
        return True
    if re.match(r"^第\d+课 (unit test|code review|teaching assistant|若翻译|交叉引用|避免写|若提到|图表若用|完成后)", p):
        return True
    if re.match(r"^第\d+课若接入实时", p):
        return True
    checklist = (
        "混池实验",
        "FORBIDDEN 特征课",
        "缺失填充课",
        "标准化泄漏",
        "时间切分课",
        "随机切分对照",
        "事件规则课",
        "双分数课",
        "成本门（如第39课）",
        "泄漏清单（第40课）",
        "停牌间隔（如第35课）",
        "复权口径（如第36课）",
        "窗口均值（如第30",
        "市场同期信号（如第38课）",
        "固定 panel（第21课）",
        "lag-1 方向（第22课）",
        "三连规则（第23课）",
        "early 非 score（第24课）",
        "open scale 泄漏（第29课）",
        "high FORBIDDEN（第28课）",
        "因子入库前，应用与第",
    )
    for prefix in checklist:
        if p.startswith(prefix) and "第" in p and "课" in p:
            return True
    return False


def strip_md(text: str) -> tuple[str, int]:
    parts = re.split(r"\n\n+", text)
    kept: list[str] = []
    removed = 0
    for para in parts:
        if is_template_paragraph(para):
            removed += 1
            continue
        kept.append(para)
    return "\n\n".join(kept), removed


def cjk_count(text: str) -> int:
    return sum(1 for c in text if "\u4e00" <= c <= "\u9fff")


def main() -> int:
    total_removed = 0
    for path in sorted(DOC.glob("day-*.md")):
        if path.name.endswith(".en.md"):
            continue
        raw = path.read_text(encoding="utf-8")
        new, n = strip_md(raw)
        if n:
            path.write_text(new, encoding="utf-8")
            total_removed += n
            print(f"{path.name}: removed {n} template paragraphs, CJK {cjk_count(raw)} -> {cjk_count(new)}")
    print(f"Done. Total paragraphs removed: {total_removed}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
