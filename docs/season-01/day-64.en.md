<p align="center"><a href="day-64.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 64 · Drop the best month

[Phase I · Models](../../README.en.md) · runs

What you learn today: Best month 2024-04 mean 0.006887; all months 0.006980; without it 0.007770 (March only)

## Plain-language account

April 2024 is the lowest monthly MAE; dropping it leaves March only at 0.007770 versus 0.006980 overall.

Aggregate scores can be dominated by the large month; name the dropped month.

Data come from name AAA in days/data/panel.csv: simple returns from adjusted close ratios minus one. Usable rows start after the fifth return, so five fewer rows than the raw panel. The default split is the first seventy-five percent of those rows in time order for train and the rest for test (often fifty-four train, nineteen test). Same-bar high, low, and close must not explain same-day return; same-day market return is not a valid feature or label unless the day script says otherwise.

## Core

```text
month with smallest mean abs error = 2024-04
mean abs error that month = 0.006887
test mean abs error all months = 0.006980
test mean abs error without that month = 0.007770
```


Test MSE on returns is not the price-level SSE from days 45–46. Hold-out rows are the only score set; coefficients and thresholds are fit on train only.

| Idea | Changes this day? | Note |
|---|---|---|
| Five-lag line coeffs | Usually frozen | From day 51 train |
| test MSE 0.000081 | Reprinted on MSE days | Diagnostics use MAE/direction/bill |
| forbidden OHLC/market | Contract holds | See days 56–57, 67 |
| train/test rows | Default 54/19 | Day 58 calendar cut excepted |

## Core block, line by line

Day 64 prints 4 contract lines:

- `month with smallest mean abs error = 2024-04`: match the terminal verbatim—keys, spacing, signs, six decimals.
- `mean abs error that month = 0.006887`: match the terminal verbatim—keys, spacing, signs, six decimals.
- `test mean abs error all months = 0.006980`: match the terminal verbatim—keys, spacing, signs, six decimals.
- `test mean abs error without that month = 0.007770`: match the terminal verbatim—keys, spacing, signs, six decimals.

Lag-5 anchors: line test MSE 0.000081, volume helped false (day 54), total bill line −18.0000 (days 75 and 79). Do not paste anchors on days that do not print them; do not round or drop signs when they appear. Day 58’s 0.000782 belongs to the calendar split, not the 0.000081 ruler. BBB 0.000105 stays beside AAA—no auto-transfer.

## Further out

Day 65 adds ticker BBB with a different MSE.

Worse MAE after dropping April is a sample change, not a parameter shift.

## How this day connects

Dropping April raises monthly MAE—sample change, not parameter change. Day 65 adds BBB MSE 0.000105.

Engineer reading order: run today's script first, then read the page; do not skip day 51 before diagnostics or the frozen coefficients lose context. Unit tests should assert hold-out scores against printed literals; common failures mix train rows or tickers. Screenshots should show English keys and six-decimal scores. Use python3; tiny float noise is fine, but contract integers like quiet=10, jump=5, and direction wrong=3 must not drift.

## What the run showed

```bash
python3 days/64-drop-month/drop_month.py
```

The script should print stdout matching the core block. Implementation: [`drop_month.py`](../../days/64-drop-month/drop_month.py).



Checklist: train/test counts match the script; English keys, signs, and six-decimal literals match the terminal; FORBIDDEN and not-a-result lines stay verbatim; do not swap line versus tree MSE or bill columns; lag-5 anchors (MSE 0.000081, volume helped false, bill −18) stay untouched unless you re-run and update the whole contract.
