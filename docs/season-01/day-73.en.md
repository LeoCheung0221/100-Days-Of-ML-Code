<p align="center"><a href="day-73.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 73 · Wrong direction

[Phase I · Models](../../README.en.md) · runs

What you learn today: direction wrong on 3 days; 19 test days.

## Plain-language account

Day 73's numbers come from script stdout, not hand-filled values. 方向只看 sign(y) 与 sign(ŷ)，不看误差幅度. 3/19 约十六 percent 失手，与 MAE 或 MSE 不是同一分数. 

第 74 天会按 |y−ŷ| 列出前五名，其中可能方向对但误差大. 

The panel is days/data/panel.csv, name AAA, simple returns from adjusted close. Train is the first seventy-five percent in time order unless this script changes the cut. Hold-out rows are scored only; the five-lag line is not re-fit there. Same-bar high, low, close are not features; same-day market is not a result.

Separate train from test: coefficients on train, counts and MAE on nineteen hold-out rows. direction wrong on 3 days; 19 test days.

Return scores here are not price-level SSE from days 45–46. Claims serve this print only.

## Core

```text
direction wrong days = 3
test days = 19
```

## Further out

Cross-check stdout against the page: key names, signs, and decimals should match the terminal. direction wrong on 3 days; 19 test days.

Keep billing rules beside direction counts in the lab notebook. If the next lesson changes the cut or target, open a new log row instead of overwriting today's numbers.

## What the run showed

```bash
python days/73-wrong-direction/wrong_direction.py
```

The script should print stdout lines matching the core block. The implementation is [`wrong_direction.py`](../../days/73-wrong-direction/wrong_direction.py).

Hand in the printed numbers and rule lines for day 73. Keep the script path for reruns.
