<p align="center"><a href="day-86.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 86 · Sample manifest

[Phase I · Models](../../README.en.md) · runs

What you learn today: Ten-line data manifest: panel.csv, AAA, dates, 79 complete rows, 75/25 split

## Plain-language account

Day 86 prints a ten-line data manifest: panel path, AAA, adj_close, date range through 2024-04-23, seventy-nine complete rows, same-day simple returns, lags one through five, seventy-five/twenty-five time-ordered split. No new fit—audit onboarding for the whole phase.

## Core

```text
source = days/data/panel.csv
name = AAA
price column = adj_close
first date = 2024-01-02
last date = 2024-04-23
complete rows = 79
return = same-day simple from adj_close
lags = 1 through 5 of that return
split = first seventy-five percent train time-ordered
hold-out = remaining twenty-five percent
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
python3 days/86-ten-lines-dates/ten_lines_dates.py
```

Or: `python3 -c "from days.run_day import main; main(86)"`.

Source: [`ten_lines_dates.py`](../../days/86-ten-lines-dates/ten_lines_dates.py)。Keep the ```text``` block identical to stdout.
