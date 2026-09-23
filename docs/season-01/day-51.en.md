<p align="center"><a href="day-51.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 51 · Linear weights on five lags

[Phase I · Models](../../README.en.md) · runs

What you learn today: On AAA, five lagged simple returns predict same-day return. OLS: lag1=−0.1359, lag2=0.0829, lag3=0.1094, lag4=−0.1726, lag5=−0.0803, intercept=0.0023. Min −0.1726, max 0.1094, test MSE=0.000081. Same magnitude, not equal weights.

## Plain-language account

Day 50 still voted on price-level directions; from today the feature chain is five lagged simple returns predicting same-day return.

Each row is a card: five lags on the left, same-day return on the right. Train is the first seventy-five percent in time order; the line minimizes train squared error.

Weights are not 0.2 each. lag4=−0.1726 has largest magnitude; lag3=0.1094 is largest positive; lag1=−0.1359 is also material.

Test MSE 0.000081 uses frozen train coefficients on nineteen hold-out rows. The min–max gap near 0.28 rejects equal weights; alternating signs mean a blend, not lag1 only.

When checking by hand, pair lag4 and lag3 in one table: one pulls predictions down, one up. Re-fit on test and the score moves—that is a split mistake, not economics.

Data come from name AAA in days/data/panel.csv: simple returns from adjusted close ratios minus one. Usable rows start after the fifth return, so five fewer rows than the raw panel. The default split is the first seventy-five percent of those rows in time order for train and the rest for test (often fifty-four train, nineteen test). Same-bar high, low, and close must not explain same-day return; same-day market return is not a valid feature or label unless the day script says otherwise.

## Core

```text
weight lag 1 = -0.1359
weight lag 2 = 0.0829
weight lag 3 = 0.1094
weight lag 4 = -0.1726
weight lag 5 = -0.0803
intercept = 0.0023
weight min = -0.1726  weight max = 0.1094
test MSE = 0.000081
```


Test MSE on returns is not the price-level SSE from days 45–46. Hold-out rows are the only score set; coefficients and thresholds are fit on train only.

| Idea | Changes this day? | Note |
|---|---|---|
| Five-lag line coeffs | Usually frozen | From day 51 train |
| test MSE 0.000081 | Reprinted on MSE days | Diagnostics use MAE/direction/bill |
| forbidden OHLC/market | Contract holds | See days 56–57, 67 |
| train/test rows | Default 54/19 | Day 58 calendar cut excepted |

## Core block, line by line

Day 51 prints 8 contract lines:

- `weight lag 1 = -0.1359`: match the terminal verbatim—keys, spacing, signs, six decimals.
- `weight lag 2 = 0.0829`: match the terminal verbatim—keys, spacing, signs, six decimals.
- `weight lag 3 = 0.1094`: match the terminal verbatim—keys, spacing, signs, six decimals.
- `weight lag 4 = -0.1726`: match the terminal verbatim—keys, spacing, signs, six decimals.
- `weight lag 5 = -0.0803`: match the terminal verbatim—keys, spacing, signs, six decimals.
- `intercept = 0.0023`: match the terminal verbatim—keys, spacing, signs, six decimals.
- `weight min = -0.1726  weight max = 0.1094`: match the terminal verbatim—keys, spacing, signs, six decimals.
- `test MSE = 0.000081`: match the terminal verbatim—keys, spacing, signs, six decimals.

Lag-5 anchors: line test MSE 0.000081, volume helped false (day 54), total bill line −18.0000 (days 75 and 79). Do not paste anchors on days that do not print them; do not round or drop signs when they appear. Day 58’s 0.000782 belongs to the calendar split, not the 0.000081 ruler. BBB 0.000105 stays beside AAA—no auto-transfer.

## Further out

In matrix form each row is [lag1,…,lag5,1] with same-day return as y. β̂ is fit on train; test rows only score predictions.

Compatible with day-9 row-order invariance on a fixed design, but never shuffle time when building lags.

Day 52 adds a stump on the same table; 0.000081 is the line ruler on the hold-out stretch, not a direction hit rate.

Log forbidden rules, split, and test MSE together; stdout is authoritative for six-decimal literals.

## How this day connects

Day 50 still voted on price-level directions; today starts the return chain with five lagged simple returns and test MSE 0.000081 as the ruler. Day 52 adds a lag4 stump—memorize weights, especially lag4 versus lag3. Do not paste price SSE from days 45–46. Split roles: one person copies stdout, one explains signs, one verifies the seventy-five percent split counts.

Engineer reading order: run today's script first, then read the page; do not skip day 51 before diagnostics or the frozen coefficients lose context. Unit tests should assert hold-out scores against printed literals; common failures mix train rows or tickers. Screenshots should show English keys and six-decimal scores. Use python3; tiny float noise is fine, but contract integers like quiet=10, jump=5, and direction wrong=3 must not drift.

## What the run showed

```bash
python3 days/51-five-lag-weights/five_lag_weights.py
```

The script should print stdout matching the core block. Implementation: [`five_lag_weights.py`](../../days/51-five-lag-weights/five_lag_weights.py).

Hand in five lag weights and test MSE 0.000081. Next: one stump on the same lags.

Checklist: train/test counts match the script; English keys, signs, and six-decimal literals match the terminal; FORBIDDEN and not-a-result lines stay verbatim; do not swap line versus tree MSE or bill columns; lag-5 anchors (MSE 0.000081, volume helped false, bill −18) stay untouched unless you re-run and update the whole contract.
