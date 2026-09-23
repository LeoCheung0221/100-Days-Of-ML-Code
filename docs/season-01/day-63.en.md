<p align="center"><a href="day-63.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 63 · Monthly residuals

[Phase I · Models](../../README.en.md) · runs

What you learn today: 2024-03 mean 0.007770 days=2; 2024-04 mean 0.006887 days=17

## Plain-language account

Day 63's numbers come from script stdout, not hand-filled values. test |y−ŷ| 按 yyyy-mm 聚合. 三月 2 天，四月 17 天；读均值必带 days. 

The panel is days/data/panel.csv, name AAA, simple returns from adjusted close. Train is the first seventy-five percent in time order unless this script changes the cut. Hold-out rows score MSE only; coefficients are not re-fit there. Same-bar high, low, close are not features; same-day market is not a result.

Separate train from test: parameters on train, MSE on hold-out mean squared error. 2024-03 mean 0.007770 days=2; 2024-04 mean 0.006887 days=17

Return MSE is not price-level SSE from days 45–46. Claims serve this print only.

## Core

```text
month 2024-03 mean abs error = 0.007770  days = 2
month 2024-04 mean abs error = 0.006887  days = 17
```

## Further out

Cross-check stdout against the page: key names, signs, and six decimals should match the terminal. 2024-03 mean 0.007770 days=2; 2024-04 mean 0.006887 days=17

Keep forbidden rules beside MSE in the lab notebook. If the next lesson changes the cut or target, open a new log row instead of overwriting today's numbers.

## What the run showed

```bash
python days/63-monthly-residuals/monthly_residuals.py
```

The script should print stdout lines matching the core block. The implementation is [`monthly_residuals.py`](../../days/63-monthly-residuals/monthly_residuals.py).

Hand in the printed numbers and rule lines for day 63. Keep the script path for reruns.
