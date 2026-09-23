<p align="center"><a href="day-81.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 81 · Volatility weeks

[Phase I · Models](../../README.en.md) · runs

What you learn today: ISO-week volatility split on hold-out rows; MAE 0.007341 vs 0.006362

## Plain-language account

From day 71 onward most lessons score the same frozen five-lag OLS line fit on fifty-four train rows. Day 81 adds a calendar regime: for each ISO week present in the nineteen test dates, compute the sample standard deviation of same-day simple returns on test rows in that week (a one-day week uses |r|). Weeks at or above the median weekly std are “high volatility”; others are low. Twelve test days fall in high-vol weeks, seven in low.

The line coefficients are not re-estimated. Mean absolute error |r−ŷ| averages 0.007341 on the twelve high-vol days and 0.006362 on the seven low-vol days—same β̂, different level accuracy. That pattern aligns with volatility clustering (Andersen and Bollerslev, 1998) but here we use a minimal realized-vol slice, not GARCH. Nineteen points forbid strong claims; the point is disclosure: a single full-sample MAE can hide regime shape.

Week-vol differs from day-71 jumps: jumps use the 75th percentile of |r| on all test rows; week vol uses within-week dispersion. Day 84 will cross the two axes. Diff stdout literally—median 0.009415, counts 12/7, two MAE lines.

## Core

```text
volatility = std of same-day returns within ISO week on test rows
week volatility median = 0.009415
high volatility week days = 12
low volatility week days = 7
mean abs error high vol weeks = 0.007341
mean abs error low vol weeks = 0.006362
```

`_week_vol_high_low()` groups test indices by ISO week, compares each week’s std to the cross-week median, and splits MAE on |y−ŷ| from `_lag5_line_test()`.

| Line | Role |
|---|---|
| week volatility median | Threshold on weekly return std |
| 12 / 7 | Test-row counts summing to 19 |
| Two MAE values | Level error, not MSE 0.000081 |

Contract: AAA returns from `adj_close`, default 75/25 split; forbidden same-bar OHLC and same-day market (days 56–57, 87). Changing split or ticker requires re-running regime logic.

## Further reading

**Information set.** Estimating vol thresholds on train and applying frozen rules to test is the production pattern; this script uses test-only weekly stds as a teaching simplification—avoid leaking train shape into regime labels when writing memos.

**MAE vs MSE.** Day 51 uses MSE to pick β̂; this day uses MAE for typical level miss. High-vol MAE need not move direction-wrong counts (Christoffersen and Diebold, 2006).

**Next days.** Day 82: jumps inside high-vol weeks. Days 83–85: trees and model choice by regime. Days 86–87: manifest lines for data and columns.

**Reporting.** Always state regime definition, subsample n, and metric (MAE vs MSE). Harvey et al. (2016) treat literals as audit anchors.

## Lab summary

```bash
python3 days/81-vol-weeks/vol_weeks.py
```

Or: `python3 -c "from days.run_day import main; main(81)"`.

Source: [`vol_weeks.py`](../../days/81-vol-weeks/vol_weeks.py). ```text``` block must match stdout verbatim.
