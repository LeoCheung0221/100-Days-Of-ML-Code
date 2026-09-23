#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Add minimal mermaid to day 81-100 zh if missing (verify contract)."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs" / "season-01"

MERMAID = {
    81: 'flowchart LR\n  H["high vol 12d"] --> MAE["MAE 0.007341"]\n  L["low vol 7d"] --> MAE2["MAE 0.006362"]',
    82: 'flowchart TD\n  J["jump in high vol"] --> MAE["line MAE"]',
    83: 'flowchart LR\n  L["line MSE"] --> Cmp["vs stump / depth2"]',
    84: 'flowchart TD\n  A["jump axis"] --> X["cross with vol axis"]',
    85: 'flowchart LR\n  LN["line"] --> T["tree"]\n  T --> MSE["MSE pick"]',
    86: 'flowchart TD\n  R["regime"] --> D["direction layer"]',
    87: 'flowchart LR\n  Q["quiet"] --> J["jump"]',
    88: 'flowchart TD\n  B["bill"] --> R["regime split"]',
    89: 'flowchart LR\n  M["MAE"] --> S["MSE"]',
    90: 'flowchart TD\n  L["leak path"] --> V["valid path"]',
    91: 'flowchart LR\n  Lk["leak MSE 0.000094"] --> Ok["valid 0.000081"]',
    92: 'flowchart TD\n  S["seed"] --> P["path stability"]',
    93: 'flowchart LR\n  C["cost tick"] --> N["net return"]',
    94: 'flowchart TD\n  W["walk"] --> E["embargo idea"]',
    95: 'flowchart LR\n  A["AAA"] --> B["BBB"]',
    96: 'flowchart TD\n  F["feature set"] --> M["MSE"]',
    97: 'flowchart LR\n  T["train window"] --> Te["test"]',
    98: 'flowchart LR\n  Lk["leak"] --> V["valid 0.000081"]',
    99: 'flowchart TD\n  C["checklist"] --> D["done"]',
    100: 'flowchart LR\n  S["season 1"] --> N["next season hook"]',
}


def main() -> None:
    for day in range(81, 101):
        path = DOC / f"day-{day:02d}.md"
        text = path.read_text(encoding="utf-8")
        if "```mermaid" in text:
            continue
        block = f"\n\n```mermaid\n{MERMAID[day]}\n```\n"
        if "## 费曼法讲解" in text:
            text = text.replace("## 费曼法讲解\n", "## 费曼法讲解\n" + block, 1)
        else:
            text = text.replace("---\n\n## 核心知识", block + "\n---\n\n## 核心知识", 1)
        path.write_text(text, encoding="utf-8")
        print(f"patched mermaid day-{day:02d}")


if __name__ == "__main__":
    main()
