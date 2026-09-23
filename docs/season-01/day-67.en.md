<p align="center"><a href="day-67.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 67 · Same-day market column

[Phase I · Models](../../README.en.md) · runs

What you learn today: lags only 0.000081; same-day market 0.000094; FORBIDDEN; lower MSE not a result

## Plain-language account

Day 67's numbers come from script stdout, not hand-filled values. FORBIDDEN 与 not a result 句同脚本. 此处 0.000094>0.000081，同日 market hurt. 

The panel is days/data/panel.csv, name AAA, simple returns from adjusted close. Train is the first seventy-five percent in time order unless this script changes the cut. Hold-out rows score MSE only; coefficients are not re-fit there. Same-bar high, low, close are not features; same-day market is not a result.

Separate train from test: parameters on train, MSE on hold-out mean squared error. lags only 0.000081; same-day market 0.000094; FORBIDDEN; lower MSE not a result

Return MSE is not price-level SSE from days 45–46. Claims serve this print only.

## Core

```text
test MSE lags only = 0.000081
test MSE lags and same-day market = 0.000094
same-day market column = FORBIDDEN
a lower MSE with same-day market is not a result
```

## Further out

Cross-check stdout against the page: key names, signs, and six decimals should match the terminal. lags only 0.000081; same-day market 0.000094; FORBIDDEN; lower MSE not a result

Keep forbidden rules beside MSE in the lab notebook. If the next lesson changes the cut or target, open a new log row instead of overwriting today's numbers.

## What the run showed

```bash
python days/67-market-lag/market_lag.py
```

The script should print stdout lines matching the core block. The implementation is [`market_lag.py`](../../days/67-market-lag/market_lag.py).

Hand in the printed numbers and rule lines for day 67. Keep the script path for reruns.
