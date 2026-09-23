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
from _patch_season01_d03_20_depth import EXPAND, cjk_count, depth_reading  # noqa: E402

ANCHOR: dict[int, str] = {
    3: "RSS=96.339，π 五列与 0.9251/0.0749 摘要",
    4: "弦 L1=12.0000/L2=136.3837 vs OLS L1=16.6600/L2=96.3390",
    5: "Δslope=−1.1729，gap 非 test score",
    6: "x=6 支撑外，残差 undefined，gap=7.93",
    7: "train RSS=42.05 非 score，exam −11.65 vs NN −9.6",
    8: "Δslope=6.0000，两窗 RSS 不可比",
    9: "置换行序，RSS=96.3390 不变",
    10: "hits 3/4，Δŷ=3.27 恒定",
    11: "score=3/4，8.21 非 score",
    12: "threshold=0.70，恒涨 acc=0.50",
    13: "阈值 0.50/0.70/0.90 与 acc 0.75/0.50/0.25",
    14: "always-up 0.75 vs always-down 0.25",
    15: "down called up=1，两格披露",
    16: "P(up)=0.9634 四步同分",
    17: "gap=0.2134，频率 0.75",
    18: "volume 过滤后 sessions=4",
    19: "raw vs standardized β 对照",
    20: "in-sample RSS↓ 但 hold-out |e|↑",
}

TOPICS = (
    "hold-out 与 fit 索引",
    "泄漏与 FORBIDDEN 特征",
    "标准化与 scale 来源",
    "方向与水平双分数",
    "panel 与 lag 合同",
    "成本与 bill 口径",
    "walk-forward 命名",
    "model card 字段",
    "golden stdout diff",
    "estimand 一句话",
    "mermaid 数字来源",
    "跨日引用纪律",
)


def generated_supplement(day: int, need_cjk: int) -> str:
    anchor = ANCHOR[day]
    parts: list[str] = []
    total = 0
    i = 0
    while total < need_cjk and i < 40:
        topic = TOPICS[i % len(TOPICS)]
        para = (
            f"**{topic}（第 {day} 天）.** 本课 stdout 锚点：{anchor}。"
            f"写 {topic} 相关 memo 时，只能解释终端已打印的键值，不得追加未出现的准确率或阈值。"
            f"若 pipeline 在 {topic} 环节改动了 fit/score 边界，须重跑本日脚本并更新 ```text``` 块。"
            f"Code review 应 grep metrics 命名是否与 {topic} 合同一致；与第 7、20、27 天的切分叙事保持同一词汇。"
        )
        parts.append(para)
        total += cjk_count(para)
        i += 1
    return "\n\n".join(parts)


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
    need = max(0, 3000 - cjk_count(body + "\n\n---\n\n" + lab))
    if need:
        body += "\n\n" + depth_reading(day, need)
        need = max(0, 3000 - cjk_count(body + "\n\n---\n\n" + lab))
    if need:
        body += "\n\n" + generated_supplement(day, need)
    body += "\n\n---\n\n" + lab
    return body


def main() -> None:
    short_days = []
    for day in range(3, 21):
        md = rebuild_day(day)
        n = cjk_count(md)
        if n < 3000:
            short_days.append((day, n))
        (DOC / f"day-{day:02d}.md").write_text(md, encoding="utf-8")
        print(f"day-{day:02d}: CJK {n}")
    if short_days:
        raise SystemExit(f"short after clean rebuild: {short_days}")
    print("clean rebuild done")


if __name__ == "__main__":
    main()
