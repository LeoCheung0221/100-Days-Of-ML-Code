<p align="center"><a href="day-63.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 63 · Monthly MAE

[Phase I · Models](../../README.en.md) · runs

What you learn today: 2024-03 mean 0.007770 days=2; 2024-04 mean 0.006887 days=17

## Plain-language account

Monthly MAE on test: March two days at 0.007770, April seventeen days at 0.006887.

Tiny March sample is unstable.

Whole-test MAE 0.006980 is a weighted blend.

Data come from name AAA in days/data/panel.csv: simple returns from adjusted close ratios minus one. Usable rows start after the fifth return, so five fewer rows than the raw panel. The default split is the first seventy-five percent of those rows in time order for train and the rest for test (often fifty-four train, nineteen test). Same-bar high, low, and close must not explain same-day return; same-day market return is not a valid feature or label unless the day script says otherwise.

## Core

```text
month 2024-03 mean abs error = 0.007770 days = 2
month 2024-04 mean abs error = 0.006887 days = 17
```


Test MSE on returns is not the price-level SSE from days 45–46. Hold-out rows are the only score set; coefficients and thresholds are fit on train only.

| Idea | Changes this day? | Note |
|---|---|---|
| Five-lag line coeffs | Usually frozen | From day 51 train |
| test MSE 0.000081 | Reprinted on MSE days | Diagnostics use MAE/direction/bill |
| forbidden OHLC/market | Contract holds | See days 56–57, 67 |
| train/test rows | Default 54/19 | Day 58 calendar cut excepted |

## Core block, line by line

Day 63 prints 2 contract lines:

- `month 2024-03 mean abs error = 0.007770 days = 2`: match the terminal verbatim—keys, spacing, signs, six decimals.
- `month 2024-04 mean abs error = 0.006887 days = 17`: match the terminal verbatim—keys, spacing, signs, six decimals.

Lag-5 anchors: line test MSE 0.000081, volume helped false (day 54), total bill line −18.0000 (days 75 and 79). Do not paste anchors on days that do not print them; do not round or drop signs when they appear. Day 58’s 0.000782 belongs to the calendar split, not the 0.000081 ruler. BBB 0.000105 stays beside AAA—no auto-transfer.

## Further out

Day 64 drops the best month and recomputes.

Always pair monthly means with day counts.

## How this day connects

Monthly MAE with March two days versus April seventeen days. Day 64 drops the best month.

Engineer reading order: run today's script first, then read the page; do not skip day 51 before diagnostics or the frozen coefficients lose context. Unit tests should assert hold-out scores against printed literals; common failures mix train rows or tickers. Screenshots should show English keys and six-decimal scores. Use python3; tiny float noise is fine, but contract integers like quiet=10, jump=5, and direction wrong=3 must not drift.

## What the run showed

```bash
python3 days/63-monthly-residuals/monthly_residuals.py
```

The script should print stdout matching the core block. Implementation: [`monthly_residuals.py`](../../days/63-monthly-residuals/monthly_residuals.py).



Checklist: train/test counts match the script; English keys, signs, and six-decimal literals match the terminal; FORBIDDEN and not-a-result lines stay verbatim; do not swap line versus tree MSE or bill columns; lag-5 anchors (MSE 0.000081, volume helped false, bill −18) stay untouched unless you re-run and update the whole contract.
