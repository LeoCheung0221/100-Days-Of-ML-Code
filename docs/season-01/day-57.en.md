<p align="center"><a href="day-57.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 57 · Refuse same-bar prices

[Phase I · Models](../../README.en.md) · runs

What you learn today: high, low, close FORBIDDEN same-bar; five lags allowed; test MSE=0.000081

## Plain-language account

Day 57's numbers come from script stdout, not hand-filled values. 三列 OHLC 都印 FORBIDDEN. feature build rejects same-row OHLC=true. 合法特征仍五 lag. 

The panel is days/data/panel.csv, name AAA, simple returns from adjusted close. Train is the first seventy-five percent in time order unless this script changes the cut. Hold-out rows score MSE only; coefficients are not re-fit there. Same-bar high, low, close are not features; same-day market is not a result.

Separate train from test: parameters on train, MSE on hold-out mean squared error. high, low, close FORBIDDEN same-bar; five lags allowed; test MSE=0.000081

Return MSE is not price-level SSE from days 45–46. Claims serve this print only.

## Core

```text
column high = FORBIDDEN same-bar
column low = FORBIDDEN same-bar
column close = FORBIDDEN same-bar
feature build rejects same-row OHLC = true
allowed features = five lagged returns only
test MSE = 0.000081
```

## Further out

Cross-check stdout against the page: key names, signs, and six decimals should match the terminal. high, low, close FORBIDDEN same-bar; five lags allowed; test MSE=0.000081

Keep forbidden rules beside MSE in the lab notebook. If the next lesson changes the cut or target, open a new log row instead of overwriting today's numbers.

## What the run showed

```bash
python days/57-refuse-today/refuse_today.py
```

The script should print stdout lines matching the core block. The implementation is [`refuse_today.py`](../../days/57-refuse-today/refuse_today.py).

Hand in the printed numbers and rule lines for day 57. Keep the script path for reruns.
