#!/usr/bin/env python3
"""Helpers for incremental season-01 publishing (local full tree, remote 1–2 days per run)."""
from __future__ import annotations

import ast
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LOCAL_RUN_DAY = ROOT / "days" / "run_day.py"

# Function order on origin/master through day 80 (before day_50 and DAYS).
RUN_DAY_ORDER_THROUGH_80: tuple[str, ...] = (
    "_five_returns",
    "_sigmoid",
    "_aaa",
    "_complete",
    "_panel_pair",
    "day_11",
    "day_12",
    "day_13",
    "day_14",
    "day_15",
    "day_16",
    "day_17",
    "day_18",
    "day_19",
    "day_20",
    "day_21",
    "day_22",
    "day_23",
    "day_24",
    "day_25",
    "_split_score",
    "_lag_xy",
    "day_26",
    "day_27",
    "day_28",
    "day_29",
    "day_30",
    "day_31",
    "day_32",
    "day_33",
    "day_34",
    "day_35",
    "day_36",
    "day_37",
    "day_38",
    "day_39",
    "day_40",
    "_level",
    "_train_test",
    "day_41",
    "day_42",
    "day_43",
    "day_44",
    "day_45",
    "day_46",
    "day_47",
    "day_48",
    "day_49",
    "_lag5_xy",
    "_ols_design",
    "_predict_design",
    "_mse",
    "_ridge_design",
    "_best_stump",
    "_predict_stump_col",
    "day_51",
    "day_52",
    "day_53",
    "day_54",
    "day_55",
    "day_56",
    "day_57",
    "day_58",
    "day_59",
    "day_60",
    "_lag5_for_rows",
    "day_61",
    "day_62",
    "day_63",
    "day_64",
    "day_65",
    "day_66",
    "day_67",
    "day_68",
    "day_69",
    "day_70",
    "_lag5_line_test",
    "day_71",
    "day_72",
    "day_73",
    "day_74",
    "day_75",
    "day_76",
    "day_77",
    "day_78",
    "day_79",
    "day_80",
)

EXTENSION_HELPERS: tuple[str, ...] = (
    "_iso_week",
    "_week_vol_high_low",
    "_lag5_depth2_on_best_col",
)


def git_show(rev_path: str) -> str:
    proc = subprocess.run(
        ["git", "show", rev_path],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr.strip() or f"git show {rev_path} failed")
    return proc.stdout


def parse_function_sources(source: str) -> dict[str, str]:
    tree = ast.parse(source)
    out: dict[str, str] = {}
    for node in tree.body:
        if isinstance(node, ast.FunctionDef):
            seg = ast.get_source_segment(source, node)
            if seg:
                out[node.name] = seg.rstrip() + "\n\n"
    return out


def run_day_header(upto: int) -> str:
    return (
        f'"""Days 11–{upto}. Each day_xx prints the numbers its note quotes."""\n\n'
        "from __future__ import annotations\n\n"
        "import datetime as dt\n\n"
        "import numpy as np\n\n"
        "from days.course import (\n"
        "    FIVE_V,\n"
        "    FIVE_X,\n"
        "    FIVE_Y,\n"
        "    PANEL_PATH,\n"
        "    accuracy,\n"
        "    column,\n"
        "    fmt,\n"
        "    load_panel,\n"
        "    name_rows,\n"
        "    ols,\n"
        "    predict_stump,\n"
        "    predict_tree,\n"
        "    returns,\n"
        "    ridge_slope,\n"
        "    sign_hit,\n"
        "    stump,\n"
        "    tree_depth2,\n"
        ")\n\n\n"
    )


def build_run_day_upto(upto: int) -> str:
    if upto < 81:
        raise ValueError("build_run_day_upto expects upto >= 81")
    local = LOCAL_RUN_DAY.read_text(encoding="utf-8")
    funcs = parse_function_sources(local)
    parts = [run_day_header(upto)]
    for name in RUN_DAY_ORDER_THROUGH_80:
        if name not in funcs:
            raise KeyError(f"missing {name} in local run_day.py")
        parts.append(funcs[name])
    for name in EXTENSION_HELPERS:
        parts.append(funcs[name])
    for n in range(81, upto + 1):
        key = f"day_{n}"
        if key not in funcs:
            raise KeyError(key)
        parts.append(funcs[key])
    parts.append(funcs["day_50"])
    parts.append(f"DAYS = {{i: globals()[f\"day_{{i}}\"] for i in range(11, {upto + 1})}}\n\n\n")
    parts.append(
        "def main(day: int) -> None:\n"
        "    DAYS[day]()\n"
    )
    return "".join(parts)


def find_runner_dir(day: int) -> Path | None:
    prefix = f"{day}-"
    for d in sorted((ROOT / "days").iterdir()):
        if d.is_dir() and d.name.startswith(prefix):
            return d
    return None


def day_doc_paths(day: int) -> list[Path]:
    return [
        ROOT / "docs" / "season-01" / f"day-{day:02d}.md",
        ROOT / "docs" / "season-01" / f"day-{day:02d}.en.md",
    ]


def lesson_title(day: int) -> str:
    zh = (ROOT / "docs" / "season-01" / f"day-{day:02d}.md").read_text(encoding="utf-8")
    m = re.search(r"^# 第 \d+ 天 · (.+)$", zh, re.MULTILINE)
    return m.group(1).strip() if m else f"day {day}"


def commit_subject(day: int) -> str:
    title = lesson_title(day)
    if re.search(r"[\u4e00-\u9fff]", title):
        return f"Day {day}: {title}"
    return f"Day {day}: notes on {title.lower()}"


def zh_day_label(n: int) -> str:
    ones = ["", "一", "二", "三", "四", "五", "六", "七", "八", "九"]
    if n == 100:
        return "第一百天"
    if n <= 10:
        return "第十天" if n == 10 else f"第{ones[n]}天"
    if n < 20:
        return f"第十{ones[n - 10]}天"
    if n % 10 == 0:
        return f"第{ones[n // 10]}十天"
    return f"第{ones[n // 10]}十{ones[n % 10]}天"


def extract_root_readme_link_line(
    local_readme: str, day: int, *, english: bool = False
) -> str | None:
    label = f"Day {day}" if english else zh_day_label(day)
    for line in local_readme.splitlines():
        if line.startswith(f"- [{label}　"):
            return line
    for line in local_readme.splitlines():
        if re.match(rf"^- \[\*\*{day}\s", line) or re.match(rf"^- \[\*\*{day:02d}\s", line):
            return line
    return None


def patch_root_readme(
    head: str, day: int, local_readme: str, *, bump_runnable: bool, english: bool = False
) -> str:
    out = head
    if bump_runnable:
        out = re.sub(
            r"第 1 日至第 \d+ 日已可运行",
            f"第 1 日至第 {day} 日已可运行",
            out,
            count=1,
        )
        out = re.sub(
            r"Days 1 through \d+ run",
            f"Days 1 through {day} run",
            out,
            count=1,
        )
        out = re.sub(
            r"Days 1–\d+ are runnable",
            f"Days 1–{day} are runnable",
            out,
            count=1,
        )
    link = extract_root_readme_link_line(local_readme, day, english=english)
    if not link:
        return out
    label = f"Day {day}" if english else zh_day_label(day)
    for plain in (
        re.compile(rf"^- \*\*{day}\s"),
        re.compile(rf"^- \*\*{day:02d}\s"),
        re.compile(rf"^- \[{re.escape(label)}　[^\]]+\]\("),  # already linked
    ):
        if plain.pattern.endswith(r"\("):
            if plain.search(out):
                return out
            continue
        if plain.search(out):
            return plain.sub(link, out, count=1)
    return out


def patch_season_readme(head: str, day: int, local_season: str, *, bump_runnable: bool) -> str:
    out = head
    if bump_runnable:
        out = re.sub(
            r"说明：第 1 日至第 \d+ 日已有笔记",
            f"说明：第 1 日至第 {day} 日已有笔记",
            out,
            count=1,
        )
        out = re.sub(
            r"Days 1–\d+ have notes",
            f"Days 1–{day} have notes",
            out,
            count=1,
        )
        out = out.replace("其余各日只有标题。", "链在表内。")
        out = out.replace("Other days are titles only.", "Links are in the tables.")
    row_link = None
    for line in local_season.splitlines():
        if line.startswith(f"| [{day} "):
            row_link = line
            break
    if row_link:
        plain = re.compile(rf"^\| {day} \|")
        out = plain.sub(row_link, out, count=1)
    return out
