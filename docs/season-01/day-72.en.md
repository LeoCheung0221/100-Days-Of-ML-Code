<p align="center"><a href="day-72.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 72 · Error on quiet days

[Phase I · Models](../../README.en.md) · runs

What you learn today: quiet=10; quiet MAE=0.003154; all-test MAE=0.006980.

## Plain-language account

Day 72's numbers come from script stdout, not hand-filled values. quiet 仍是 |y|≤中位数. quiet 上 MAE 0.003154 小于全段 0.006980，说明小波动日直线更贴标签；但 quiet 只有 10 行，均值方差都比 nineteen 行大. 

读 MAE 时不要与第 51 天 MSE 0.000081 直接比大小——MAE 是 |y−ŷ| 均值，MSE 是平方均值，量纲习惯不同. 

The panel is days/data/panel.csv, name AAA, simple returns from adjusted close. Train is the first seventy-five percent in time order unless this script changes the cut. Hold-out rows are scored only; the five-lag line is not re-fit there. Same-bar high, low, close are not features; same-day market is not a result.

Separate train from test: coefficients on train, counts and MAE on nineteen hold-out rows. quiet=10; quiet MAE=0.003154; all-test MAE=0.006980.

Return scores here are not price-level SSE from days 45–46. Claims serve this print only.

## Core

```text
quiet days = 10
mean abs error on quiet days = 0.003154
mean abs error all test days = 0.006980
```

## Further out

Cross-check stdout against the page: key names, signs, and decimals should match the terminal. quiet=10; quiet MAE=0.003154; all-test MAE=0.006980.

Keep billing rules beside direction counts in the lab notebook. If the next lesson changes the cut or target, open a new log row instead of overwriting today's numbers.

## What the run showed

```bash
python days/72-quiet-days/quiet_days.py
```

The script should print stdout lines matching the core block. The implementation is [`quiet_days.py`](../../days/72-quiet-days/quiet_days.py).

Hand in the printed numbers and rule lines for day 72. Keep the script path for reruns.
