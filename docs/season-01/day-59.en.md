<p align="center"><a href="day-59.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 59 · Zero-return baseline

[Phase I · Models](../../README.en.md) · runs

What you learn today: baseline MSE 0.000101; line 0.000081

## Plain-language account

Predict zero every day: baseline test MSE 0.000101. The line at 0.000081 beats doing nothing on squared error.

The 0.000020 gap is named on day 60; keep both scores on the page.

Zero baseline is a level forecast, not a direction oracle.

Data come from name AAA in days/data/panel.csv: simple returns from adjusted close ratios minus one. Usable rows start after the fifth return, so five fewer rows than the raw panel. The default split is the first seventy-five percent of those rows in time order for train and the rest for test (often fifty-four train, nineteen test). Same-bar high, low, and close must not explain same-day return; same-day market return is not a valid feature or label unless the day script says otherwise.

## Core

```text
baseline predict return = 0 every day
baseline test MSE = 0.000101
line test MSE = 0.000081
```


Test MSE on returns is not the price-level SSE from days 45–46. Hold-out rows are the only score set; coefficients and thresholds are fit on train only.

| Idea | Changes this day? | Note |
|---|---|---|
| Five-lag line coeffs | Usually frozen | From day 51 train |
| test MSE 0.000081 | Reprinted on MSE days | Diagnostics use MAE/direction/bill |
| forbidden OHLC/market | Contract holds | See days 56–57, 67 |
| train/test rows | Default 54/19 | Day 58 calendar cut excepted |

## Core block, line by line

Day 59 prints 3 contract lines:

- `baseline predict return = 0 every day`: match the terminal verbatim—keys, spacing, signs, six decimals.
- `baseline test MSE = 0.000101`: match the terminal verbatim—keys, spacing, signs, six decimals.
- `line test MSE = 0.000081`: match the terminal verbatim—keys, spacing, signs, six decimals.

Lag-5 anchors: line test MSE 0.000081, volume helped false (day 54), total bill line −18.0000 (days 75 and 79). Do not paste anchors on days that do not print them; do not round or drop signs when they appear. Day 58’s 0.000782 belongs to the calendar split, not the 0.000081 ruler. BBB 0.000105 stays beside AAA—no auto-transfer.

## Further out

Report baseline and line together.

Day 60 prints improvement and the smallest-error day index.

## How this day connects

Zero baseline 0.000101 versus line 0.000081. Day 60 names improvement 0.000020 and index 13 absolute error.

Engineer reading order: run today's script first, then read the page; do not skip day 51 before diagnostics or the frozen coefficients lose context. Unit tests should assert hold-out scores against printed literals; common failures mix train rows or tickers. Screenshots should show English keys and six-decimal scores. Use python3; tiny float noise is fine, but contract integers like quiet=10, jump=5, and direction wrong=3 must not drift.

## What the run showed

```bash
python3 days/59-zero-baseline/zero_baseline.py
```

The script should print stdout matching the core block. Implementation: [`zero_baseline.py`](../../days/59-zero-baseline/zero_baseline.py).



Checklist: train/test counts match the script; English keys, signs, and six-decimal literals match the terminal; FORBIDDEN and not-a-result lines stay verbatim; do not swap line versus tree MSE or bill columns; lag-5 anchors (MSE 0.000081, volume helped false, bill −18) stay untouched unless you re-run and update the whole contract.
