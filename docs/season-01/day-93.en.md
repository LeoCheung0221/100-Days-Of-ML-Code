<p align="center"><a href="day-93.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 93 · One-tick slippage

[Phase I · Models](../../README.en.md) · runs

What you learn today: One-tick slippage 0.0001; direction wrong stays 3; rank changed = false

## Plain-language account

One-tick slippage 0.0001 on predictions leaves direction-wrong count at three before and after; `rank changed = false` on this panel. Sensitivity probe, not a full cost model.

## Core

```text
slippage one tick = 0.0001
direction wrong before slippage = 3
direction wrong after slippage = 3
rank changed = false
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
python3 days/93-slippage-tick/slippage_tick.py
```

Or: `python3 -c "from days.run_day import main; main(93)"`.

Source: [`slippage_tick.py`](../../days/93-slippage-tick/slippage_tick.py)。Keep the ```text``` block identical to stdout.
