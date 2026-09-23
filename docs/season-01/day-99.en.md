<p align="center"><a href="day-99.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 99 · Full rerun

[Phase I · Models](../../README.en.md) · runs

What you learn today: Full rerun MSE 0.000081, direction wrong 3, matches day 51 and day-70 manifest

## Plain-language account

Integration rerun: line test MSE 0.000081, direction wrong 3, matches day 51 true, manifest matches day 70 true. Gate before merging changes to run_day or panel paths.

## Core

```text
full run line test MSE = 0.000081
full run direction wrong days = 3
full run matches day 51 test MSE = true
manifest matches day 70 ten lines = true
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
python3 days/99-full-rerun/full_rerun.py
```

Or: `python3 -c "from days.run_day import main; main(99)"`.

Source: [`full_rerun.py`](../../days/99-full-rerun/full_rerun.py)。Keep the ```text``` block identical to stdout.
