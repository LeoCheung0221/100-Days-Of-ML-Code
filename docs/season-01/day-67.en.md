<p align="center"><a href="day-67.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 67 · Same-day market forbidden

[Phase I · Models](../../README.en.md) · runs

What you learn today: lags only 0.000081; with same-day market 0.000094; FORBIDDEN; lower MSE is not a result

## Plain-language account

Same-day market can lower MSE to 0.000094 but is FORBIDDEN; that score is not a result.

Only lags only 0.000081 counts.

Data come from name AAA in days/data/panel.csv: simple returns from adjusted close ratios minus one. Usable rows start after the fifth return, so five fewer rows than the raw panel. The default split is the first seventy-five percent of those rows in time order for train and the rest for test (often fifty-four train, nineteen test). Same-bar high, low, and close must not explain same-day return; same-day market return is not a valid feature or label unless the day script says otherwise.

## Core

```text
test MSE lags only = 0.000081
test MSE lags and same-day market = 0.000094
same-day market column = FORBIDDEN
a lower MSE with same-day market is not a result
```


Test MSE on returns is not the price-level SSE from days 45–46. Hold-out rows are the only score set; coefficients and thresholds are fit on train only.

| Idea | Changes this day? | Note |
|---|---|---|
| Five-lag line coeffs | Usually frozen | From day 51 train |
| test MSE 0.000081 | Reprinted on MSE days | Diagnostics use MAE/direction/bill |
| forbidden OHLC/market | Contract holds | See days 56–57, 67 |
| train/test rows | Default 54/19 | Day 58 calendar cut excepted |

## Core block, line by line

Day 67 prints 4 contract lines:

- `test MSE lags only = 0.000081`: match the terminal verbatim—keys, spacing, signs, six decimals.
- `test MSE lags and same-day market = 0.000094`: match the terminal verbatim—keys, spacing, signs, six decimals.
- `same-day market column = FORBIDDEN`: match the terminal verbatim—keys, spacing, signs, six decimals.
- `a lower MSE with same-day market is not a result`: match the terminal verbatim—keys, spacing, signs, six decimals.

Lag-5 anchors: line test MSE 0.000081, volume helped false (day 54), total bill line −18.0000 (days 75 and 79). Do not paste anchors on days that do not print them; do not round or drop signs when they appear. Day 58’s 0.000782 belongs to the calendar split, not the 0.000081 ruler. BBB 0.000105 stays beside AAA—no auto-transfer.

## Further out

Day 68 centralizes the legal path in pipeline(name).

Production beta uses prior-day market or rolling estimates—not same-day leakage.

## How this day connects

FORBIDDEN same-day market: 0.000094 is not a result. Legal score stays lags only 0.000081.

Engineer reading order: run today's script first, then read the page; do not skip day 51 before diagnostics or the frozen coefficients lose context. Unit tests should assert hold-out scores against printed literals; common failures mix train rows or tickers. Screenshots should show English keys and six-decimal scores. Use python3; tiny float noise is fine, but contract integers like quiet=10, jump=5, and direction wrong=3 must not drift.

## What the run showed

```bash
python3 days/67-market-lag/market_lag.py
```

The script should print stdout matching the core block. Implementation: [`market_lag.py`](../../days/67-market-lag/market_lag.py).



Checklist: train/test counts match the script; English keys, signs, and six-decimal literals match the terminal; FORBIDDEN and not-a-result lines stay verbatim; do not swap line versus tree MSE or bill columns; lag-5 anchors (MSE 0.000081, volume helped false, bill −18) stay untouched unless you re-run and update the whole contract.
