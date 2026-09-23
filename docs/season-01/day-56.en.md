<p align="center"><a href="day-56.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 56 · Next-day return task

[Phase I · Models](../../README.en.md) · runs

What you learn today: task lines declare lags 1–5 on AAA; train=54, test=19, test MSE=0.000081

## Plain-language account

Day 56's numbers come from script stdout, not hand-filled values. stdout 写清 target 与 forbidden OHLC. 54+19 对应 75% 切分. MSE 与第 51 天直线相同. 

The panel is days/data/panel.csv, name AAA, simple returns from adjusted close. Train is the first seventy-five percent in time order unless this script changes the cut. Hold-out rows score MSE only; coefficients are not re-fit there. Same-bar high, low, close are not features; same-day market is not a result.

Separate train from test: parameters on train, MSE on hold-out mean squared error. task lines declare lags 1–5 on AAA; train=54, test=19, test MSE=0.000081

Return MSE is not price-level SSE from days 45–46. Claims serve this print only.

## Core

```text
task = predict today's return from lags 1 through 5 on AAA adj_close
target = same-day simple return on adjusted close
forbidden = same-row high low close as features
train rows = 54  test rows = 19
test MSE = 0.000081
```

## Further out

Cross-check stdout against the page: key names, signs, and six decimals should match the terminal. task lines declare lags 1–5 on AAA; train=54, test=19, test MSE=0.000081

Keep forbidden rules beside MSE in the lab notebook. If the next lesson changes the cut or target, open a new log row instead of overwriting today's numbers.

## What the run showed

```bash
python days/56-next-day-task/next_day_task.py
```

The script should print stdout lines matching the core block. The implementation is [`next_day_task.py`](../../days/56-next-day-task/next_day_task.py).

Hand in the printed numbers and rule lines for day 56. Keep the script path for reruns.
