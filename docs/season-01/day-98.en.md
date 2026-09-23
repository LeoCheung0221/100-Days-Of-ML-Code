<p align="center"><a href="day-98.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 98 · Patch the leak

[Phase I · Models](../../README.en.md) · runs

What you learn today: After patch: valid MSE 0.000081 vs leak 0.000094; valid worse than leak = false

## Plain-language account

Patch verification: drop market from design—valid MSE 0.000081, invalid leak 0.000094, `valid score worse than leak = false` because compliance score need not beat leak MSE.

## Core

```text
patch applied = drop same-day market from design
valid test MSE after patch = 0.000081
invalid test MSE with leak = 0.000094
valid score worse than leak = false
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
python3 days/98-patch-leak/patch_leak.py
```

Or: `python3 -c "from days.run_day import main; main(98)"`.

Source: [`patch_leak.py`](../../days/98-patch-leak/patch_leak.py)。Keep the ```text``` block identical to stdout.
