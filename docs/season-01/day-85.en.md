<p align="center"><a href="day-85.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 85 · Pick model on table

[Phase I · Models](../../README.en.md) · runs

What you learn today: High-vol weeks: line test MSE 0.000094 vs tree 0.000146; model kept = line

## Plain-language account

After day 84’s cross-tab, day 85 prespecifies a decision cell on high-volatility weeks: compare line vs stump test MSE and print `model kept`. Line wins 0.000094 versus 0.000146. The rule is MSE-based, not billing (day 79) and not direction counts (zero wrong in high vol per day 84).

## Core

```text
decision cell = high volatility weeks test MSE
line test MSE high vol weeks = 0.000094
tree test MSE high vol weeks = 0.000146
model kept = line
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
python3 days/85-pick-model/pick_model.py
```

Or: `python3 -c "from days.run_day import main; main(85)"`.

Source: [`pick_model.py`](../../days/85-pick-model/pick_model.py)。Keep the ```text``` block identical to stdout.
