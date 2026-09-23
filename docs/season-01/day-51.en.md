<p align="center"><a href="day-51.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 51 · Linear weights on five lags

[Phase I · Models](../../README.en.md) · runs

What you learn today: On AAA, five lagged simple returns predict same-day return. OLS: lag1=−0.1359, lag2=0.0829, lag3=0.1094, lag4=−0.1726, lag5=−0.0803, intercept=0.0023. Min −0.1726, max 0.1094, test MSE=0.000081. Same magnitude, not equal weights.

## Plain-language account

Day 50 still scored price-level directions; from here the label is same-day simple return and the features are five lagged simple returns. That is a finite-order AR structure on \(r_t\): estimate on the first seventy-five percent of time-ordered rows, score on the last nineteen hold-out rows only.

Campbell, Lo, and MacKinlay (1997, *The Econometrics of Financial Markets*) frame short-horizon predictability as a statement about the information set and the hold-out contract—not as proof of economic alpha on seventy-three usable days. We report \(\hat\beta\) and test MSE under a fixed split; we do not refit on test.

Weights are not 0.2 each. lag4=−0.1726 has the largest magnitude; lag3=0.1094 is the largest positive; lag1=−0.1359 is also material. Alternating signs mean the forecast is a blend, not a single-lag story. The intercept 0.0023 adjusts the conditional mean; it is not a sixth lag.

Test MSE 0.000081 is \(\frac{1}{19}\sum (r_t-\hat y_t)^2\) with frozen train coefficients. Same-bar OHLC and same-day market do not belong in \(X_t\) (days 56–57, 67 make that explicit later). This score is not price SSE from days 45–46 and not day 58’s calendar-split 0.000782.

## Core

```text
lags = 1 through 5
weight lag 1 = -0.1359
weight lag 2 = 0.0829
weight lag 3 = 0.1094
weight lag 4 = -0.1726
weight lag 5 = -0.0803
intercept = 0.0023
weight min = -0.1726 weight max = 0.1094
test MSE = 0.000081
```

Train stacks \(X\in\mathbb{R}^{54\times 6}\) (five lags plus intercept); `lstsq` on train only. Test rows enter the score, not \(X'X\). Shuffling train row order leaves \(\hat\beta\) unchanged (day 9); shuffling time before building lags breaks the design.

| Quantity | Role |
|---|---|
| \(\hat w_1,\ldots,\hat w_5,\hat b\) | Frozen after train for most of the lag-5 arc |
| test MSE 0.000081 | Hold-out mean squared error on returns |
| Price-tree SSE | Different label and units—do not paste here |

## Further

Lo and MacKinlay (1988, *Review of Financial Studies*) discuss return predictability on broader panels; treat 0.000081 as a teaching benchmark, not a significance claim. Newey and West (1987, *Econometrica*) matter once you attach t-stats to lag regressions—this season reports MSE only.

Harvey, Liu, and Zhu (2016) warn that each new feature search raises the bar for out-of-sample claims; log the prespecified AR(5) before comparing trees or volume (days 52–54). Hamilton (1994, *Time Series Analysis*) links stable AR estimation to well-ordered lags—never shuffle dates when constructing \(r_{t-j}\).

Day 52 places a regression stump on the same table; memorize these weights, especially lag4 versus lag3, before reading tree splits.

## Lab summary

```bash
python3 days/51-five-lag-weights/five_lag_weights.py
```

Or: `python3 -c \"from days.run_day import main; main(51)\"`.

Implementation: [`five_lag_weights.py`](../../days/51-five-lag-weights/five_lag_weights.py). Diff stdout against the ```text``` block verbatim. Next: one stump on the same five lags.
