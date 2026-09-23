#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Verify season-01 docs: four sections, no filler, stdout blocks, CJK floor."""
from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs" / "season-01"

MIN_CJK = 2000
DOC_DAYS = range(51, 101)

FORBIDDEN_ZH = (
    "阶段内读法：",
    "给工程师的阅读顺序",
    "核心块逐行读法",
    "下面逐行说明读法纪律",
    "天终端键",
    "硬锚点",
    "**面板与 lag 构造（全季默认）。**",
    "键名、等号两侧空格",
    "本课 stdout 含",
    "第 71–80 天用 quiet/jump/direction 与 bill 重读误差",
    "深度阅读轮次",
    "match the terminal verbatim",
    "Core block, line by line",
    "Engineer reading order:",
    "**全季 lag-5 合同复述",
    "**白盒检查（每课 30 秒）。**",
)

SECTIONS_ZH = ("## 费曼法讲解", "## 核心知识", "## 拓展领域", "## 实战总结")
SECTIONS_EN = ("## Plain-language account", "## Core", "## Further")
SECTIONS_EN_LAB = ("## Lab summary", "## What the run showed")


def cjk_count(text: str) -> int:
    return sum(1 for c in text if "\u4e00" <= c <= "\u9fff")


def extract_text_block(md: str) -> list[str]:
    m = re.search(r"```text\n(.*?)```", md, re.DOTALL)
    if not m:
        return []
    return [ln.rstrip() for ln in m.group(1).strip().splitlines()]


def script_for_day(day: int) -> Path:
    prefix = f"{day}-"
    for d in sorted((ROOT / "days").iterdir()):
        if d.is_dir() and d.name.startswith(prefix):
            scripts = sorted(d.glob("*.py"))
            if scripts:
                return scripts[0]
    raise FileNotFoundError(f"no day script for {day}")


def run_day_stdout(day: int) -> list[str]:
    script = script_for_day(day)
    proc = subprocess.run(
        [sys.executable, str(script)],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    if proc.returncode != 0:
        raise RuntimeError(f"{script.name} (day {day}) failed: {proc.stderr.strip()}")
    return [ln.rstrip() for ln in proc.stdout.strip().splitlines()]


def check_day(day: int, errors: list[str], cjk_report: list[tuple[int, int]]) -> None:
    zh_path = DOC / f"day-{day:02d}.md"
    en_path = DOC / f"day-{day:02d}.en.md"
    if not zh_path.exists():
        errors.append(f"day-{day:02d}.md: missing")
        return
    if not en_path.exists():
        errors.append(f"day-{day:02d}.en.md: missing")
        return

    zh = zh_path.read_text(encoding="utf-8")
    en = en_path.read_text(encoding="utf-8")
    cjk = cjk_count(zh)
    cjk_report.append((day, cjk))
    if cjk < MIN_CJK:
        errors.append(f"day-{day:02d}.md: CJK {cjk} < {MIN_CJK}")

    for bad in FORBIDDEN_ZH:
        if bad in zh or bad in en:
            errors.append(f"day-{day:02d}: forbidden template fragment: {bad!r}")

    for sec in SECTIONS_ZH:
        if sec not in zh:
            errors.append(f"day-{day:02d}.md: missing section {sec}")
    for sec in SECTIONS_EN:
        if sec not in en:
            errors.append(f"day-{day:02d}.en.md: missing section {sec}")
    if not any(sec in en for sec in SECTIONS_EN_LAB):
        errors.append(f"day-{day:02d}.en.md: missing lab section")

    block = extract_text_block(zh)
    if not block:
        errors.append(f"day-{day:02d}.md: no ```text``` core block")
        return
    try:
        stdout = run_day_stdout(day)
    except (FileNotFoundError, RuntimeError) as e:
        errors.append(str(e))
        return
    norm = lambda lines: [re.sub(r"  +", " ", ln) for ln in lines]
    if norm(block) != norm(stdout):
        errors.append(
            f"day-{day:02d}: ```text``` block ({len(block)} lines) != script stdout ({len(stdout)} lines)"
        )


def main() -> int:
    import argparse

    parser = argparse.ArgumentParser(description="Verify season-01 lesson docs.")
    parser.add_argument("--day", type=int, help="check a single day (51–100)")
    args = parser.parse_args()

    if args.day is not None:
        days = [args.day]
    else:
        days = list(DOC_DAYS)

    errors: list[str] = []
    cjk_report: list[tuple[int, int]] = []

    for day in days:
        check_day(day, errors, cjk_report)

    build = ROOT / "scripts" / "build_season01_51_80_docs.py"
    if build.exists():
        errors.append(f"remove generator: {build}")

    if len(days) == 1:
        span = f"day {days[0]}"
    else:
        span = f"days {DOC_DAYS.start}-{DOC_DAYS.stop - 1}"
    print(f"CJK counts (zh, min {MIN_CJK}, {span}):")
    for day, n in cjk_report:
        flag = " OK" if n >= MIN_CJK else " SHORT"
        print(f"  day-{day:02d}: {n}{flag}")

    if errors:
        print(f"\nFAILURES ({len(errors)}):", file=sys.stderr)
        for e in errors:
            print(f"  - {e}", file=sys.stderr)
        return 1

    print("\nAll checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
