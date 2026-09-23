<p align="center"><a href="day-74.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 74 · Top five errors

[Phase I · Models](../../README.en.md) · runs

What you learn today: Top five: 2024-04-03 err=0.019717 jump right; 04-18 0.017449 jump right; 04-22 0.014328 mid wrong; 03-28 0.013401 jump right; 04-02 0.009609 jump right.

## Plain-language account

Day 74's numbers come from script stdout, not hand-filled values. 排序键是 |y−ŷ|，不是账单. 前五里四个 jump、一个 mid；仅 rank3 方向错. 最大误差日可以方向对——直线猜对涨跌仍可能离 y 很远. 

日期与六位 error 必须逐字对齐 stdout；class 与 direction 是脚本对同一行的附加标签. 

The panel is days/data/panel.csv, name AAA, simple returns from adjusted close. Train is the first seventy-five percent in time order unless this script changes the cut. Hold-out rows are scored only; the five-lag line is not re-fit there. Same-bar high, low, close are not features; same-day market is not a result.

Separate train from test: coefficients on train, counts and MAE on nineteen hold-out rows. Top five: 2024-04-03 err=0.019717 jump right; 04-18 0.017449 jump right; 04-22 0.014328 mid wrong; 03-28 0.013401 jump right; 04-02 0.009609 jump right.

Return scores here are not price-level SSE from days 45–46. Claims serve this print only.

## Core

```text
rank 1 date = 2024-04-03 error = 0.019717 class = jump direction = right
rank 2 date = 2024-04-18 error = 0.017449 class = jump direction = right
rank 3 date = 2024-04-22 error = 0.014328 class = mid direction = wrong
rank 4 date = 2024-03-28 error = 0.013401 class = jump direction = right
rank 5 date = 2024-04-02 error = 0.009609 class = jump direction = right
```

## Further out

Cross-check stdout against the page: key names, signs, and decimals should match the terminal. Top five: 2024-04-03 err=0.019717 jump right; 04-18 0.017449 jump right; 04-22 0.014328 mid wrong; 03-28 0.013401 jump right; 04-02 0.009609 jump right.

Keep billing rules beside direction counts in the lab notebook. If the next lesson changes the cut or target, open a new log row instead of overwriting today's numbers.

## What the run showed

```bash
python days/74-top-five-errors/top_five_errors.py
```

The script should print stdout lines matching the core block. The implementation is [`top_five_errors.py`](../../days/74-top-five-errors/top_five_errors.py).

Hand in the printed numbers and rule lines for day 74. Keep the script path for reruns.
