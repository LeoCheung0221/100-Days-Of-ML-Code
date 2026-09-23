<p align="center"><a href="day-60.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 60 · Line vs baseline

[Phase I · Models](../../README.en.md) · runs

What you learn today: baseline 0.000101, line 0.000081, improvement 0.000020; index 13 error 0.000214

## Plain-language account

Day 60's numbers come from script stdout, not hand-filled values. improvement=baseline−line=0.000020. index 13 是 test 上 |y−ŷ| 最小日，误差 0.000214. 

The panel is days/data/panel.csv, name AAA, simple returns from adjusted close. Train is the first seventy-five percent in time order unless this script changes the cut. Hold-out rows score MSE only; coefficients are not re-fit there. Same-bar high, low, close are not features; same-day market is not a result.

Separate train from test: parameters on train, MSE on hold-out mean squared error. baseline 0.000101, line 0.000081, improvement 0.000020; index 13 error 0.000214

Return MSE is not price-level SSE from days 45–46. Claims serve this print only.

## Core

```text
baseline test MSE = 0.000101
line test MSE = 0.000081
MSE improvement over baseline = 0.000020
smallest line error day index on test = 13
that day line error = 0.000214
```

## Further out

Cross-check stdout against the page: key names, signs, and six decimals should match the terminal. baseline 0.000101, line 0.000081, improvement 0.000020; index 13 error 0.000214

Keep forbidden rules beside MSE in the lab notebook. If the next lesson changes the cut or target, open a new log row instead of overwriting today's numbers.

## What the run showed

```bash
python days/60-line-vs-baseline/line_vs_baseline.py
```

The script should print stdout lines matching the core block. The implementation is [`line_vs_baseline.py`](../../days/60-line-vs-baseline/line_vs_baseline.py).

Hand in the printed numbers and rule lines for day 60. Keep the script path for reruns.
