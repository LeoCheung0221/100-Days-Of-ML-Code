<p align="center"><a href="day-64.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 64 · Drop the easy month

[Phase I · Models](../../README.en.md) · runs

What you learn today: smallest-error month 2024-04 mean 0.006887; all 0.006980; without 0.007770 (March only)

## Plain-language account

Day 64's numbers come from script stdout, not hand-filled values. drop 最小 mean 月 2024-04. 去掉后只剩 March 两行，均值升到 0.007770. 

The panel is days/data/panel.csv, name AAA, simple returns from adjusted close. Train is the first seventy-five percent in time order unless this script changes the cut. Hold-out rows score MSE only; coefficients are not re-fit there. Same-bar high, low, close are not features; same-day market is not a result.

Separate train from test: parameters on train, MSE on hold-out mean squared error. smallest-error month 2024-04 mean 0.006887; all 0.006980; without 0.007770 (March only)

Return MSE is not price-level SSE from days 45–46. Claims serve this print only.

## Core

```text
month with smallest mean abs error = 2024-04
mean abs error that month = 0.006887
test mean abs error all months = 0.006980
test mean abs error without that month = 0.007770
```

## Further out

Cross-check stdout against the page: key names, signs, and six decimals should match the terminal. smallest-error month 2024-04 mean 0.006887; all 0.006980; without 0.007770 (March only)

Keep forbidden rules beside MSE in the lab notebook. If the next lesson changes the cut or target, open a new log row instead of overwriting today's numbers.

## What the run showed

```bash
python days/64-drop-month/drop_month.py
```

The script should print stdout lines matching the core block. The implementation is [`drop_month.py`](../../days/64-drop-month/drop_month.py).

Hand in the printed numbers and rule lines for day 64. Keep the script path for reruns.
