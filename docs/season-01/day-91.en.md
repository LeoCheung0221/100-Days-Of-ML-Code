<p align="center"><a href="day-91.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 91 · Reject a feature

[Phase I · Models](../../README.en.md) · runs

What you learn today: Reject same-day market: leak MSE 0.000094 vs lags-only 0.000081; reject stands

## Plain-language account

Day 91 quantifies forbidden same-day market return: leak MSE 0.000094 versus lags-only 0.000081 after reject. `reject stands even if MSE rises = true`—compliance beats score. Valid reporting uses 0.000081 only.

## Core

```text
feature rejected = same-day market return
rank before reject = line with leak MSE 0.000094
rank after reject = lags only MSE 0.000081
reject stands even if MSE rises = true
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
python3 days/91-reject-feature/reject_feature.py
```

Or: `python3 -c "from days.run_day import main; main(91)"`.

Source: [`reject_feature.py`](../../days/91-reject-feature/reject_feature.py)。Keep the ```text``` block identical to stdout.
