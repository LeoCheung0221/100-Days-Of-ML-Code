<p align="center"><a href="day-90.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 90 · Three failure days

[Phase I · Models](../../README.en.md) · runs

What you learn today: top three hold-out days by |error| with reasons (two jump horizontal misses, one direction wrong)

## Plain-language account

Day 90 lists the three largest |r−ŷ| hold-out days with reasons. Ranks one and two (2024-04-03, 2024-04-18) are jump-day horizontal misses; rank three (2024-04-22) is direction wrong. Ex post ordering, not a prespec deletion rule.

## Core

```text
fail rank 1 date = 2024-04-03 reason = jump day horizontal miss
fail rank 2 date = 2024-04-18 reason = jump day horizontal miss
fail rank 3 date = 2024-04-22 reason = direction wrong
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
python3 days/90-three-failures/three_failures.py
```

Or: `python3 -c "from days.run_day import main; main(90)"`.

Source: [`three_failures.py`](../../days/90-three-failures/three_failures.py)。Keep the ```text``` block identical to stdout.
