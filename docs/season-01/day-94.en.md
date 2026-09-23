<p align="center"><a href="day-94.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 94 · Drop best month

[Phase I · Models](../../README.en.md) · runs

What you learn today: Drop 2024-03 month; line MSE 0.000080 vs tree 0.000170; model kept = line

## Plain-language account

Drop the hold-out month with highest mean |error| (2024-03), then compare line MSE 0.000080 vs tree 0.000170; `model kept after drop = line`. Stress estimand—stdout names the dropped month explicitly.

## Core

```text
month dropped = 2024-03
line test MSE without that month = 0.000080
tree test MSE without that month = 0.000170
model kept after drop = line
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
python3 days/94-drop-best-month/drop_best_month.py
```

Or: `python3 -c "from days.run_day import main; main(94)"`.

Source: [`drop_best_month.py`](../../days/94-drop-best-month/drop_best_month.py)。Keep the ```text``` block identical to stdout.
