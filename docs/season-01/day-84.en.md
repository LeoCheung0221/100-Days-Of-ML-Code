<p align="center"><a href="day-84.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 84 · Regime cross-tab

[Phase I · Models](../../README.en.md) · runs

What you learn today: Eight-line table crossing vol regimes with quiet/jump/direction counts and MAE

## Plain-language account

Day 84 crosses volatility regimes (day 81) with quiet/jump labels and direction-wrong flags on the frozen line. High vol: six quiet, four jump, zero direction-wrong, MAE 0.007341. Low vol: four quiet, one jump, three direction-wrong, MAE 0.006362. Tail jumps cluster in high-vol weeks; sign errors cluster in low-vol weeks.

Diff eight `table ...` lines literally. This is counting and averaging only—no refit on test.

## Core

```text
table high vol quiet days = 6
table high vol jump days = 4
table high vol direction wrong days = 0
table high vol mean abs error = 0.007341
table low vol quiet days = 4
table low vol jump days = 1
table low vol direction wrong days = 3
table low vol mean abs error = 0.006362
```

Loops high/low indices from `_week_vol_high_low` with quiet/jump/wrong masks on test rows; prints four metrics per regime.

Integers and six-decimal MAE must match stdout. Full-sample MSE 0.000081 is not reprinted.

## Further reading

**Sparse cells.** Low-vol direction-wrong equals three of seven rows—disclose n in slides.

**Billing.** Jump counts relate to day-75 bills but are not identical estimands.

**Ex post labels.** Quiet/jump use realized |r|; fine for diagnostics, not prespec signals.

**Next.** Day 85 picks line vs stump on high-vol MSE using a separate decision cell.

## Lab summary

```bash
python3 days/84-regime-table/regime_table.py
```

Or: `python3 -c "from days.run_day import main; main(84)"`.

Source: [`regime_table.py`](../../days/84-regime-table/regime_table.py)。Keep the ```text``` block identical to stdout.
