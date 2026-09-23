<p align="center"><a href="day-96.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 96 · One-page four titles

[Phase I · Models](../../README.en.md) · runs

What you learn today: Four one-page titles: task, split, baseline, errors vocabulary

## Plain-language account

Four one-line slide titles: task, split, baseline, errors vocabulary—structure without reprinting every metric. Pairs with day-100 narrative.

## Core

```text
one page title task = predict AAA return from five lags
one page title split = seventy-five percent train time order
one page title baseline = zero return on hold-out
one page title errors = quiet jump direction wrong plus bill
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
python3 days/96-one-page-four/one_page_four.py
```

Or: `python3 -c "from days.run_day import main; main(96)"`.

Source: [`one_page_four.py`](../../days/96-one-page-four/one_page_four.py)。Keep the ```text``` block identical to stdout.
