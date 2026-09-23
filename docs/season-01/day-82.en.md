<p align="center"><a href="day-82.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 82 · Jumps inside high-vol weeks

[Phase I · Models](../../README.en.md) · runs

What you learn today: four jump days inside high-volatility ISO weeks; frozen line MAE 0.015044 on that intersection

## Plain-language account

Day 81 split the nineteen hold-out rows by ISO-week return volatility. Day 82 intersects that high-volatility subset with the day-71 jump rule: on the test stretch, a day is a jump when same-day absolute return meets or exceeds the 75th percentile of |r| on those nineteen rows. Four days lie in both sets. The script reports mean absolute error of the frozen five-lag OLS line on those four days only—0.015044—not a refit on tail events.

That number sits above the high-vol-week MAE from day 81 (0.007341 on twelve days). The lesson is shape, not a new model: tail days inside a volatile week drive much of the level error, while direction diagnostics may still look fine in that regime (see day 84’s table). Coefficients remain the day-51 train estimate; scoring uses `_lag5_line_test()` predictions on hold-out rows only.

Jump geometry differs from week volatility. Jump is a cross-sectional threshold on |r|; week vol is dispersion within an ISO week. The first stdout line fixes the subpopulation (`regime = high volatility ISO weeks on test stretch`) so you do not confuse four high-vol jumps with five test-wide jumps from day 71.

Treat 0.015044 as a protocol snapshot with n=4—no inferential claim. Harvey et al. (2016) treat such disclosures as audit anchors, not deflated alpha. Christoffersen and Diebold (2006) separate level MAE from direction counts; this day prints level error only.

## Core

```text
regime = high volatility ISO weeks on test stretch
jump days in high vol weeks = 4
line mean abs error on those jump days = 0.015044
```

Implementation intersects `_week_vol_high_low` high indices with the test |r| p75 mask, then averages |y−ŷ| on the frozen line. If the intersection were empty, stdout would read `not defined`; this panel yields four days.

| Quantity | Reading |
|---|---|
| 4 | Intersection count, not five test-wide jumps |
| 0.015044 | MAE on intersection; higher than 0.007341 on all high-vol days |
| Regime line | Declares estimand before the numeric rows |

Contract: AAA simple returns from `adj_close`, default 75/25 time split, forbidden same-bar OHLC and same-day market (days 56–57, 87). Changing the day-58 cut or ticker requires a full re-run; do not hand-edit literals.

## Further reading

**Subsample estimand.** Reporting MAE on a prespecified intersection is descriptive. Refitting OLS on jump days would be a new experiment. Bailey and Lopez de Prado (2014) warn about implicit mining when subgroups are chosen ex post; here the rules are frozen from days 71 and 81.

**Execution gap.** Days 69 and 92 assume close fill, zero slippage, no PnL—Almgren and Chriss (2000) remind that real trading changes effective alpha. Billing on jumps (days 75, 79) is separate from this MAE.

**Cross-day context.** Day 84 crosses quiet/jump/direction with vol regimes; day 85 picks line vs stump on high-vol MSE. Cite those rows when comparing models, not this MAE alone.

**HAC.** Newey and West (1987) matters if you infer coefficient differences; four-day MAE is a point disclosure only.

## Lab summary

```bash
python3 days/82-jumps-high-vol/jumps_high_vol.py
```

Or: `python3 -c "from days.run_day import main; main(82)"`.

Source: [`jumps_high_vol.py`](../../days/82-jumps-high-vol/jumps_high_vol.py). Keep the ```text``` block byte-identical to stdout.
