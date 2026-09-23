<p align="center"><a href="day-62.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 62 · Top tenth by confidence

[Phase I · Models](../../README.en.md) · runs

What you learn today: test=19, top=2, top MAE 0.007193, rest 0.006955; top tenth NOT more accurate

## Plain-language account

Day 62's numbers come from script stdout, not hand-filled values. 置信=|ŷ|. 最高 tenth 仅 2 行. top MAE>rest，大 |ŷ| 不等于小误差. 

The panel is days/data/panel.csv, name AAA, simple returns from adjusted close. Train is the first seventy-five percent in time order unless this script changes the cut. Hold-out rows score MSE only; coefficients are not re-fit there. Same-bar high, low, close are not features; same-day market is not a result.

Separate train from test: parameters on train, MSE on hold-out mean squared error. test=19, top=2, top MAE 0.007193, rest 0.006955; top tenth NOT more accurate

Return MSE is not price-level SSE from days 45–46. Claims serve this print only.

## Core

```text
test rows = 19
top tenth count = 2
top tenth mean absolute error = 0.007193
rest mean absolute error = 0.006955
```

## Further out

Cross-check stdout against the page: key names, signs, and six decimals should match the terminal. test=19, top=2, top MAE 0.007193, rest 0.006955; top tenth NOT more accurate

Keep forbidden rules beside MSE in the lab notebook. If the next lesson changes the cut or target, open a new log row instead of overwriting today's numbers.

## What the run showed

```bash
python days/62-top-tenth/top_tenth.py
```

The script should print stdout lines matching the core block. The implementation is [`top_tenth.py`](../../days/62-top-tenth/top_tenth.py).

Hand in the printed numbers and rule lines for day 62. Keep the script path for reruns.
