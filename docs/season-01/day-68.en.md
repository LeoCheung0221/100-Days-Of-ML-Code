<p align="center"><a href="day-68.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 68 · One entry point

[Phase I · Models](../../README.en.md) · runs

What you learn today: pipeline(name): AAA 0.000081, BBB 0.000105

## Plain-language account

Day 68's numbers come from script stdout, not hand-filled values. pipeline 封装第 65 天逻辑. entry 行标记入口. 换 name 只改参数. 

The panel is days/data/panel.csv, name AAA, simple returns from adjusted close. Train is the first seventy-five percent in time order unless this script changes the cut. Hold-out rows score MSE only; coefficients are not re-fit there. Same-bar high, low, close are not features; same-day market is not a result.

Separate train from test: parameters on train, MSE on hold-out mean squared error. pipeline(name): AAA 0.000081, BBB 0.000105

Return MSE is not price-level SSE from days 45–46. Claims serve this print only.

## Core

```text
entry = pipeline(name)
AAA test MSE = 0.000081
BBB test MSE = 0.000105
```

## Further out

Cross-check stdout against the page: key names, signs, and six decimals should match the terminal. pipeline(name): AAA 0.000081, BBB 0.000105

Keep forbidden rules beside MSE in the lab notebook. If the next lesson changes the cut or target, open a new log row instead of overwriting today's numbers.

## What the run showed

```bash
python days/68-one-entry/one_entry.py
```

The script should print stdout lines matching the core block. The implementation is [`one_entry.py`](../../days/68-one-entry/one_entry.py).

Hand in the printed numbers and rule lines for day 68. Keep the script path for reruns.
