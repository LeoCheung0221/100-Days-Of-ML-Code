<p align="center"><a href="day-70.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 70 · Ten-line recap

[Phase I · Models](../../README.en.md) · runs

What you learn today: ten stdout recap lines including line test MSE 0.000081, verbatim

## Plain-language account

Day 70's numbers come from script stdout, not hand-filled values. 十行串起数据、任务、切分、基准、禁止项、线 MSE、树、volume、fill、无下单. 第 70 天只汇总 frozen 结论. 

The panel is days/data/panel.csv, name AAA, simple returns from adjusted close. Train is the first seventy-five percent in time order unless this script changes the cut. Hold-out rows score MSE only; coefficients are not re-fit there. Same-bar high, low, close are not features; same-day market is not a result.

Separate train from test: parameters on train, MSE on hold-out mean squared error. ten stdout recap lines including line test MSE 0.000081, verbatim

Return MSE is not price-level SSE from days 45–46. Claims serve this print only.

## Core

```text
data = days/data/panel.csv name AAA adj_close
task = predict return from five lagged returns
split = first seventy-five percent train time-ordered
baseline = predict zero return
forbidden = same-row high low close and same-day market
line test MSE = 0.000081
tree splits one lag column on a subsample
volume on this stretch did not help test MSE
fill = close to close slippage zero
no live order leaves this script
```

## Further out

Cross-check stdout against the page: key names, signs, and six decimals should match the terminal. ten stdout recap lines including line test MSE 0.000081, verbatim

Keep forbidden rules beside MSE in the lab notebook. If the next lesson changes the cut or target, open a new log row instead of overwriting today's numbers.

## What the run showed

```bash
python days/70-ten-lines/ten_lines.py
```

The script should print stdout lines matching the core block. The implementation is [`ten_lines.py`](../../days/70-ten-lines/ten_lines.py).

Hand in the printed numbers and rule lines for day 70. Keep the script path for reruns.
