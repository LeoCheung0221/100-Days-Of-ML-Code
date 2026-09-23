<p align="center"><a href="day-92.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 92 · Fill assumptions

[Phase I · Models](../../README.en.md) · runs

What you learn today: Three fill lines: close signal, zero slippage, errors/bills only

## Plain-language account

Three fill assumptions: signal at close from adj_close, no orders and zero slippage in script, no PnL—errors and bills only. Research protocol boundary before any live execution discussion.

## Core

```text
fill row 1 = signal at close uses adj_close that day
fill row 2 = no order sent slippage zero in script
fill row 3 = PnL not computed only errors and bills
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
python3 days/92-fill-three-lines/fill_three_lines.py
```

Or: `python3 -c "from days.run_day import main; main(92)"`.

Source: [`fill_three_lines.py`](../../days/92-fill-three-lines/fill_three_lines.py)。Keep the ```text``` block identical to stdout.
