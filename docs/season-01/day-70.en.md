<p align="center"><a href="day-70.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 70 · Ten-line recap

[Phase I · Models](../../README.en.md) · runs

What you learn today: Ten stdout recap lines including line test MSE 0.000081, verbatim

## Plain-language account

Day 70 compresses the season contract to ten stdout lines without a new fit.

Line test MSE 0.000081 must match day 51; volume line matches day 54.

Recap does not replace per-day scripts.

Data come from name AAA in days/data/panel.csv: simple returns from adjusted close ratios minus one. Usable rows start after the fifth return, so five fewer rows than the raw panel. The default split is the first seventy-five percent of those rows in time order for train and the rest for test (often fifty-four train, nineteen test). Same-bar high, low, and close must not explain same-day return; same-day market return is not a valid feature or label unless the day script says otherwise.

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


Test MSE on returns is not the price-level SSE from days 45–46. Hold-out rows are the only score set; coefficients and thresholds are fit on train only.

| Idea | Changes this day? | Note |
|---|---|---|
| Five-lag line coeffs | Usually frozen | From day 51 train |
| test MSE 0.000081 | Reprinted on MSE days | Diagnostics use MAE/direction/bill |
| forbidden OHLC/market | Contract holds | See days 56–57, 67 |
| train/test rows | Default 54/19 | Day 58 calendar cut excepted |

## Core block, line by line

Day 70 prints 10 contract lines:

- `data = days/data/panel.csv name AAA adj_close`: match the terminal verbatim—keys, spacing, signs, six decimals.
- `task = predict return from five lagged returns`: match the terminal verbatim—keys, spacing, signs, six decimals.
- `split = first seventy-five percent train time-ordered`: match the terminal verbatim—keys, spacing, signs, six decimals.
- `baseline = predict zero return`: match the terminal verbatim—keys, spacing, signs, six decimals.
- `forbidden = same-row high low close and same-day market`: match the terminal verbatim—keys, spacing, signs, six decimals.
- `line test MSE = 0.000081`: match the terminal verbatim—keys, spacing, signs, six decimals.
- `tree splits one lag column on a subsample`: match the terminal verbatim—keys, spacing, signs, six decimals.
- `volume on this stretch did not help test MSE`: match the terminal verbatim—keys, spacing, signs, six decimals.
- `fill = close to close slippage zero`: match the terminal verbatim—keys, spacing, signs, six decimals.
- `no live order leaves this script`: match the terminal verbatim—keys, spacing, signs, six decimals.

Lag-5 anchors: line test MSE 0.000081, volume helped false (day 54), total bill line −18.0000 (days 75 and 79). Do not paste anchors on days that do not print them; do not round or drop signs when they appear. Day 58’s 0.000782 belongs to the calendar split, not the 0.000081 ruler. BBB 0.000105 stays beside AAA—no auto-transfer.

## Further out

From day 71 onward emphasizes direction and quiet/jump diagnostics.

Use the ten lines as onboarding before deep dives.

## How this day connects

Ten-line contract recap including line MSE 0.000081 and volume did not help. Day 71 starts quiet/jump/direction diagnostics.

Engineer reading order: run today's script first, then read the page; do not skip day 51 before diagnostics or the frozen coefficients lose context. Unit tests should assert hold-out scores against printed literals; common failures mix train rows or tickers. Screenshots should show English keys and six-decimal scores. Use python3; tiny float noise is fine, but contract integers like quiet=10, jump=5, and direction wrong=3 must not drift.

## What the run showed

```bash
python3 days/70-ten-lines/ten_lines.py
```

The script should print stdout matching the core block. Implementation: [`ten_lines.py`](../../days/70-ten-lines/ten_lines.py).



Checklist: train/test counts match the script; English keys, signs, and six-decimal literals match the terminal; FORBIDDEN and not-a-result lines stay verbatim; do not swap line versus tree MSE or bill columns; lag-5 anchors (MSE 0.000081, volume helped false, bill −18) stay untouched unless you re-run and update the whole contract.
