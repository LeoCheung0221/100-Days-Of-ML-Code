<p align="center"><a href="day-97.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 97 · Open leak ticket

[Phase I · Models](../../README.en.md) · runs

What you learn today: Open leak ticket: market column, patch owner = feature builder

## Plain-language account

Open leak ticket: same-day market lowers MSE but is forbidden; reference day 67; patch is lags-only train and hold-out score; symptom when column added; fix owner is feature builder before OLS.

## Core

```text
open leak = same-day market column lowers MSE but forbidden
reference day = 67
patch = fit lags only on train score hold-out
symptom = MSE changes when forbidden column added
fix owner = feature builder before OLS
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
python3 days/97-open-leak/open_leak.py
```

Or: `python3 -c "from days.run_day import main; main(97)"`.

Source: [`open_leak.py`](../../days/97-open-leak/open_leak.py)。Keep the ```text``` block identical to stdout.
