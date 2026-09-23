<p align="center"><a href="day-60.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 60 · Line vs baseline

[Phase I · Models](../../README.en.md) · runs

What you learn today: baseline 0.000101, line 0.000081, improvement 0.000020; index 13 error 0.000214

## Plain-language account

Improvement 0.000020 is baseline minus line on test MSE.

Index 13 is a test-segment row index, not a calendar date; absolute error 0.000214 is not comparable to MSE as a single-number contest.

Map index to dates offline; the script prints row order only.

Data come from name AAA in days/data/panel.csv: simple returns from adjusted close ratios minus one. Usable rows start after the fifth return, so five fewer rows than the raw panel. The default split is the first seventy-five percent of those rows in time order for train and the rest for test (often fifty-four train, nineteen test). Same-bar high, low, and close must not explain same-day return; same-day market return is not a valid feature or label unless the day script says otherwise.

## Core

```text
baseline test MSE = 0.000101
line test MSE = 0.000081
MSE improvement over baseline = 0.000020
smallest line error day index on test = 13
that day line error = 0.000214
```


Test MSE on returns is not the price-level SSE from days 45–46. Hold-out rows are the only score set; coefficients and thresholds are fit on train only.

| Idea | Changes this day? | Note |
|---|---|---|
| Five-lag line coeffs | Usually frozen | From day 51 train |
| test MSE 0.000081 | Reprinted on MSE days | Diagnostics use MAE/direction/bill |
| forbidden OHLC/market | Contract holds | See days 56–57, 67 |
| train/test rows | Default 54/19 | Day 58 calendar cut excepted |

## Core block, line by line

Day 60 prints 5 contract lines:

- `baseline test MSE = 0.000101`: match the terminal verbatim—keys, spacing, signs, six decimals.
- `line test MSE = 0.000081`: match the terminal verbatim—keys, spacing, signs, six decimals.
- `MSE improvement over baseline = 0.000020`: match the terminal verbatim—keys, spacing, signs, six decimals.
- `smallest line error day index on test = 13`: match the terminal verbatim—keys, spacing, signs, six decimals.
- `that day line error = 0.000214`: match the terminal verbatim—keys, spacing, signs, six decimals.

Lag-5 anchors: line test MSE 0.000081, volume helped false (day 54), total bill line −18.0000 (days 75 and 79). Do not paste anchors on days that do not print them; do not round or drop signs when they appear. Day 58’s 0.000782 belongs to the calendar split, not the 0.000081 ruler. BBB 0.000105 stays beside AAA—no auto-transfer.

## Further out

Day 61 applies the same baseline to the tree; improvement goes negative.

Smallest error day is not necessarily the best economic day.

## How this day connects

Improvement on MSE versus absolute error on row index 13—different units. Day 61 applies baseline to the tree with negative improvement.

Engineer reading order: run today's script first, then read the page; do not skip day 51 before diagnostics or the frozen coefficients lose context. Unit tests should assert hold-out scores against printed literals; common failures mix train rows or tickers. Screenshots should show English keys and six-decimal scores. Use python3; tiny float noise is fine, but contract integers like quiet=10, jump=5, and direction wrong=3 must not drift.

## What the run showed

```bash
python3 days/60-line-vs-baseline/line_vs_baseline.py
```

The script should print stdout matching the core block. Implementation: [`line_vs_baseline.py`](../../days/60-line-vs-baseline/line_vs_baseline.py).



Checklist: train/test counts match the script; English keys, signs, and six-decimal literals match the terminal; FORBIDDEN and not-a-result lines stay verbatim; do not swap line versus tree MSE or bill columns; lag-5 anchors (MSE 0.000081, volume helped false, bill −18) stay untouched unless you re-run and update the whole contract.
