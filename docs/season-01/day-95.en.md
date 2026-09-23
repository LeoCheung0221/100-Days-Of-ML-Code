<p align="center"><a href="day-95.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 95 · Second name again

[Phase I · Models](../../README.en.md) · runs

What you learn today: Day-68 pipeline: AAA 0.000081, BBB 0.000105

## Plain-language account

Reuse day-68 pipeline function: AAA test MSE 0.000081, BBB 0.000105. Regression test across tickers with identical lag contract—no automatic transfer of AAA conclusions to BBB.

## Core

```text
entry = same pipeline function as day 68
AAA test MSE = 0.000081
BBB test MSE = 0.000105
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
python3 days/95-second-name-again/second_name_again.py
```

Or: `python3 -c "from days.run_day import main; main(95)"`.

Source: [`second_name_again.py`](../../days/95-second-name-again/second_name_again.py)。Keep the ```text``` block identical to stdout.
