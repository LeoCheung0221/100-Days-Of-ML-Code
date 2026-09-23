<p align="center"><a href="day-89.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 89 · Talk three models

[Phase I · Models](../../README.en.md) · runs

What you learn today: Talk track: zero MSE 0.000101, line 0.000081, tree 0.000174

## Plain-language account

Day 89 prepares talk track MSE lines: zero baseline 0.000101, frozen line 0.000081, frozen stump 0.000174, plus `numbers must match script stdout`. Hold-out frozen scoring only; tree loses to line on MSE.

## Core

```text
talk baseline = predict zero return
talk baseline test MSE = 0.000101
talk line = five lag OLS frozen
talk line test MSE = 0.000081
talk tree = single lag stump frozen
talk tree test MSE = 0.000174
numbers must match script stdout
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
python3 days/89-talk-three-models/talk_three_models.py
```

Or: `python3 -c "from days.run_day import main; main(89)"`.

Source: [`talk_three_models.py`](../../days/89-talk-three-models/talk_three_models.py)。Keep the ```text``` block identical to stdout.
