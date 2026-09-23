<p align="center"><a href="day-88.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 88 · Alt entry check

[Phase I · Models](../../README.en.md) · runs

What you learn today: Alt entry `python3 -m days.run_day 88`; two- vs six-decimal MSE match

## Plain-language account

Day 88 validates entry and rounding: `python3 -m days.run_day 88`, two-decimal MSE 0.00 versus six-decimal 0.000081, and `match required to two decimals = true`. Same estimand as day 51; different print contract.

## Core

```text
entry = python3 -m days.run_day 88
line test MSE two decimals = 0.00
line test MSE six decimals = 0.000081
match required to two decimals = true
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
python3 days/88-alt-entry/alt_entry.py
```

Or: `python3 -c "from days.run_day import main; main(88)"`.

Source: [`alt_entry.py`](../../days/88-alt-entry/alt_entry.py)。Keep the ```text``` block identical to stdout.
