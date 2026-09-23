#!/usr/bin/env python3
"""
Publish 1–2 season-01 days from the local full tree without bulk-pushing everything.

Keep writing all lessons locally; this script commits and pushes only the next day(s).
After each commit, README and run_day.py on disk are restored from backup so your
full local catalog (e.g. days 1–100 linked) stays intact while origin advances slowly.

Usage:
  python3 scripts/daily_publish.py --dry-run
  python3 scripts/daily_publish.py --count 2
  python3 scripts/daily_publish.py --human-time

Automated (06:00–22:00 random, no manual run):
  scripts/install-systemd-timer.sh   # once
  tail -f scripts/publish.log

State: scripts/publish_state.json (copy from publish_state.example.json).
"""
from __future__ import annotations

import argparse
import json
import os
import random
import subprocess
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STATE_PATH = ROOT / "scripts" / "publish_state.json"
TZ = timezone(timedelta(hours=8))

sys.path.insert(0, str(ROOT / "scripts"))
from publish_lib import (  # noqa: E402
    build_run_day_upto,
    commit_subject,
    day_doc_paths,
    find_runner_dir,
    git_show,
    patch_root_readme,
    patch_season_readme,
)


def load_state() -> dict:
    if STATE_PATH.exists():
        return json.loads(STATE_PATH.read_text(encoding="utf-8"))
    example = ROOT / "scripts" / "publish_state.example.json"
    if example.exists():
        return json.loads(example.read_text(encoding="utf-8"))
    return {
        "next_day": 1,
        "max_runnable_pushed": 80,
        "daily_cap": 2,
        "today": "",
        "today_count": 0,
    }


def save_state(state: dict) -> None:
    STATE_PATH.write_text(json.dumps(state, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def run_cmd(cmd: list[str], *, dry_run: bool, env: dict | None = None) -> None:
    print("+", " ".join(cmd))
    if not dry_run:
        subprocess.run(cmd, cwd=ROOT, check=True, env=env)


def verify_day(day: int) -> None:
    if day < 51:
        return
    proc = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "verify_season01_docs.py"), "--day", str(day)],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    if proc.returncode != 0:
        print(proc.stdout, proc.stderr, file=sys.stderr)
        raise SystemExit(f"verify failed for day {day}")


def backup(path: Path, store: dict[Path, bytes]) -> None:
    if path.is_file():
        store[path] = path.read_bytes()


def restore(store: dict[Path, bytes]) -> None:
    for path, data in store.items():
        path.write_bytes(data)


def publish_one_day(day: int, state: dict, args: argparse.Namespace) -> None:
    for p in day_doc_paths(day):
        if not p.exists():
            raise SystemExit(f"missing local doc: {p}")

    verify_day(day)

    bump_runnable = day >= 81 and day > int(state["max_runnable_pushed"])
    backups: dict[Path, bytes] = {}

    try:
        for p in day_doc_paths(day):
            run_cmd(["git", "add", str(p.relative_to(ROOT))], dry_run=args.dry_run)

        if day >= 81:
            runner = find_runner_dir(day)
            if runner is None:
                raise SystemExit(f"day {day} needs a days/NN-* runner directory")
            for py in sorted(runner.glob("*.py")):
                run_cmd(["git", "add", str(py.relative_to(ROOT))], dry_run=args.dry_run)

            run_day_path = ROOT / "days" / "run_day.py"
            backup(run_day_path, backups)
            published = build_run_day_upto(day)
            if not args.dry_run:
                run_day_path.write_text(published, encoding="utf-8")
            run_cmd(["git", "add", "days/run_day.py"], dry_run=args.dry_run)

        if bump_runnable:
            pairs = (
                ("README.md", "HEAD:README.md", ROOT / "README.md"),
                ("README.en.md", "HEAD:README.en.md", ROOT / "README.en.md"),
                (
                    "docs/season-01/README.md",
                    "HEAD:docs/season-01/README.md",
                    ROOT / "docs" / "season-01" / "README.md",
                ),
                (
                    "docs/season-01/README.en.md",
                    "HEAD:docs/season-01/README.en.md",
                    ROOT / "docs" / "season-01" / "README.en.md",
                ),
            )
            for _label, head_ref, path in pairs:
                backup(path, backups)
                local = path.read_text(encoding="utf-8")
                head = git_show(head_ref)
                if path.name == "README.md" or path.name == "README.en.md":
                    patched = patch_root_readme(
                        head,
                        day,
                        local,
                        bump_runnable=True,
                        english=path.name == "README.en.md",
                    )
                else:
                    patched = patch_season_readme(head, day, local, bump_runnable=True)
                if not args.dry_run:
                    path.write_text(patched, encoding="utf-8")
                run_cmd(["git", "add", str(path.relative_to(ROOT))], dry_run=args.dry_run)

        subject = commit_subject(day)
        env = None
        if args.human_time and not args.dry_run:
            hour = random.randint(19, 22)
            minute = random.randint(3, 57)
            when = datetime.now(TZ).replace(
                hour=hour, minute=minute, second=random.randint(0, 59), microsecond=0
            )
            iso = when.strftime("%Y-%m-%d %H:%M:%S +0800")
            env = {**os.environ, "GIT_AUTHOR_DATE": iso, "GIT_COMMITTER_DATE": iso}

        if args.dry_run:
            print(f"  would commit: {subject}")
            return

        subprocess.run(["git", "commit", "-m", subject], cwd=ROOT, check=True, env=env)
        if bump_runnable:
            state["max_runnable_pushed"] = day
    finally:
        if not args.dry_run and backups:
            restore(backups)


def main() -> int:
    parser = argparse.ArgumentParser(description="Publish 1–2 Quant ML season-01 days.")
    parser.add_argument("--count", type=int, default=1, choices=(1, 2), help="days this run")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--no-push", action="store_true")
    parser.add_argument("--force", action="store_true", help="ignore daily cap")
    parser.add_argument("--human-time", action="store_true", help="random evening author date")
    args = parser.parse_args()

    state = load_state()
    today = datetime.now(TZ).date().isoformat()
    if state.get("today") != today:
        state["today"] = today
        state["today_count"] = 0

    cap = int(state.get("daily_cap", 2))
    if not args.force and state["today_count"] + args.count > cap:
        print(
            f"Daily cap ({cap}) reached for {today} (count={state['today_count']}). "
            "Use --force or wait until tomorrow."
        )
        return 0

    start = int(state["next_day"])
    if start > 100:
        print("All 100 days already published (next_day > 100).")
        return 0

    for offset in range(args.count):
        day = start + offset
        if day > 100:
            break
        print(f"\n=== Day {day} ===")
        publish_one_day(day, state, args)
        state["next_day"] = day + 1
        if not args.dry_run:
            state["today_count"] = int(state["today_count"]) + 1

    if not args.dry_run:
        save_state(state)
        if not args.no_push:
            run_cmd(["git", "push", "origin", "HEAD"], dry_run=False)
    else:
        print("\n(dry-run: state not saved, no commit/push)")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
