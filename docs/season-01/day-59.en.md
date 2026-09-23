<p align="center"><a href="day-59.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 59 · Zero-return baseline

[Phase I · Models](../../README.en.md) · runs

What you learn today: baseline MSE 0.000101; line 0.000081

## Plain-language account

Day 59's numbers come from script stdout, not hand-filled values. 恒零预测是 return 最简基准. 直线 beat 零：0.000081<0.000101. 

The panel is days/data/panel.csv, name AAA, simple returns from adjusted close. Train is the first seventy-five percent in time order unless this script changes the cut. Hold-out rows score MSE only; coefficients are not re-fit there. Same-bar high, low, close are not features; same-day market is not a result.

Separate train from test: parameters on train, MSE on hold-out mean squared error. baseline MSE 0.000101; line 0.000081

Return MSE is not price-level SSE from days 45–46. Claims serve this print only.

## Core

```text
baseline predict return = 0 every day
baseline test MSE = 0.000101
line test MSE = 0.000081
```

## Further out

Cross-check stdout against the page: key names, signs, and six decimals should match the terminal. baseline MSE 0.000101; line 0.000081

Keep forbidden rules beside MSE in the lab notebook. If the next lesson changes the cut or target, open a new log row instead of overwriting today's numbers.

## What the run showed

```bash
python days/59-zero-baseline/zero_baseline.py
```

The script should print stdout lines matching the core block. The implementation is [`zero_baseline.py`](../../days/59-zero-baseline/zero_baseline.py).

Hand in the printed numbers and rule lines for day 59. Keep the script path for reruns.
