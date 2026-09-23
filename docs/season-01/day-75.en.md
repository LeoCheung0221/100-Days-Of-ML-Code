<p align="center"><a href="day-75.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 75 · Billed errors

[Phase I · Models](../../README.en.md) · runs

What you learn today: total bill line=−18.0000; direction wrong 3; jump days 5. Rule: −1 per wrong direction, −3 per jump day, stack same day.

## Plain-language account

Day 75's numbers come from script stdout, not hand-filled values. 账单在测试段逐日累加：方向错扣 1，jump 扣 3，同一日两项都满足就扣 4. 3×(−1)+5×(−3)=−18，与打印一致. 

这是教学用的离散成本，不是 broker 对账单. jump 仍按 |y|≥p75 定义，与第 71 天 jump=5 一致. 

The panel is days/data/panel.csv, name AAA, simple returns from adjusted close. Train is the first seventy-five percent in time order unless this script changes the cut. Hold-out rows are scored only; the five-lag line is not re-fit there. Same-bar high, low, close are not features; same-day market is not a result.

Separate train from test: coefficients on train, counts and MAE on nineteen hold-out rows. total bill line=−18.0000; direction wrong 3; jump days 5. Rule: −1 per wrong direction, −3 per jump day, stack same day.

Return scores here are not price-level SSE from days 45–46. Claims serve this print only.

## Core

```text
total bill line = -18.0000
direction wrong count = 3
jump day count = 5
```

## Further out

Cross-check stdout against the page: key names, signs, and decimals should match the terminal. total bill line=−18.0000; direction wrong 3; jump days 5. Rule: −1 per wrong direction, −3 per jump day, stack same day.

Keep billing rules beside direction counts in the lab notebook. If the next lesson changes the cut or target, open a new log row instead of overwriting today's numbers.

## What the run showed

```bash
python days/75-billed-errors/billed_errors.py
```

The script should print stdout lines matching the core block. The implementation is [`billed_errors.py`](../../days/75-billed-errors/billed_errors.py).

Hand in the printed numbers and rule lines for day 75. Keep the script path for reruns.
