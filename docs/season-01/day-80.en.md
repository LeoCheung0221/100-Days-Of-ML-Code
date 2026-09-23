<p align="center"><a href="day-80.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 80 · Acceptable mistake

[Phase I · Models](../../README.en.md) · runs

What you learn today: acceptable mistake=direction wrong at cost 1; wrong days=3; jump days billed at 3=5.

## Plain-language account

Day 80's numbers come from script stdout, not hand-filled values. 第 80 天不重算新账单，只命名：可接受失手列取 direction wrong，单价 1；jump 列单价 3 共 5 日. 与第 75 天 −18 分解一致. 

season 第一阶段在 return 直线诊断上收束：分类、MAE、方向、前五、账单、阈值、树线对比、列名约定. 

The panel is days/data/panel.csv, name AAA, simple returns from adjusted close. Train is the first seventy-five percent in time order unless this script changes the cut. Hold-out rows are scored only; the five-lag line is not re-fit there. Same-bar high, low, close are not features; same-day market is not a result.

Separate train from test: coefficients on train, counts and MAE on nineteen hold-out rows. acceptable mistake=direction wrong at cost 1; wrong days=3; jump days billed at 3=5.

Return scores here are not price-level SSE from days 45–46. Claims serve this print only.

## Core

```text
acceptable mistake = direction wrong at cost 1
direction wrong days = 3
jump days billed at 3 = 5
this choice names column direction wrong in the bill table
```

## Further out

Cross-check stdout against the page: key names, signs, and decimals should match the terminal. acceptable mistake=direction wrong at cost 1; wrong days=3; jump days billed at 3=5.

Keep billing rules beside direction counts in the lab notebook. If the next lesson changes the cut or target, open a new log row instead of overwriting today's numbers.

## What the run showed

```bash
python days/80-acceptable-mistake/acceptable_mistake.py
```

The script should print stdout lines matching the core block. The implementation is [`acceptable_mistake.py`](../../days/80-acceptable-mistake/acceptable_mistake.py).

Hand in the printed numbers and rule lines for day 80. Keep the script path for reruns.
