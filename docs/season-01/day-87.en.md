<p align="center"><a href="day-87.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 87 · Column policy

[Phase I · Models](../../README.en.md) · runs

What you learn today: Ten-line column policy: allowed lags, forbidden OHLC/market, train fit / test score

## Plain-language account

Day 87 restates column policy in ten lines: allowed lag1–5 plus intercept; forbidden same-row OHLC and same-day market; volume only when a day script adds it; train fits, test scores frozen parameters; panel is not a live feed. Matches days 56–57 for diffable compliance review.

## Core

```text
allowed = lag1 lag2 lag3 lag4 lag5 intercept
target = same-day simple return
forbidden = same-row high low close
forbidden = same-day market return as feature
volume = only when day script adds next-bar volume
label never uses future row
train fits coefficients thresholds only
test scores frozen parameters only
panel = days/data/panel.csv not live feed
reject list matches day 56 through 57 stdout
```

Match stdout line order and spacing. Booleans lower-case. Six-decimal floats where printed.

## Further reading

**Disclosure.** Treat ```text``` as audit anchors (Harvey et al., 2016).

**Leakage.** Same-day market MSE 0.000094 is invalid; lags-only 0.000081 is valid (days 67, 91, 98).

**Execution.** Close fill and zero slippage (day 92); no PnL in scripts.

**Splits.** Day-58 calendar cut uses a different MSE ruler—do not overwrite 0.000081 literals.

**Next steps.** Follow the phase-I README chain; re-run `main(day)` after any panel or split change.

## Lab summary

```bash
python3 days/87-ten-lines-columns/ten_lines_columns.py
```

Or: `python3 -c "from days.run_day import main; main(87)"`.

Source: [`ten_lines_columns.py`](../../days/87-ten-lines-columns/ten_lines_columns.py)。Keep the ```text``` block identical to stdout.
