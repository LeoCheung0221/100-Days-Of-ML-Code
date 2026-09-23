<p align="center"><a href="day-35.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 35 · The gap after a halt

[Phase I · Models](../../README.en.md) · runs

What you learn today: row numbers 35 and 36 are adjacent. The dates are 2024-02-20 and 2024-02-22. The business-day gap from `np.busday_count` is 2, so one business day is missing. Weekend pairs have a business-day gap of 1. A row difference of 1 is not a time difference of 1.

## Plain-language account

Read AAA down the file. Rows 35 and 36 sit next to each other, with no row between them. Their dates are 2024-02-20 and 2024-02-22. The row numbers differ by 1, which looks like the next print. Hand the two dates to `np.busday_count`. The function counts business days from the start date up to, and not including, the end date. The count is 2. A gap of 2 means one business day is missing between these rows. That day is not in the table, so the rows are still adjacent and the sessions are not.

Weekends are a separate case. Friday and the following Monday can also be adjacent rows. Saturday and Sunday sit on the calendar between them, and `np.busday_count` returns a business-day gap of 1. A gap of 1 means the two sessions are neighbors on the default Monday-to-Friday calendar. The weekend did not create a missing business day. Rows 35 and 36 have gap 2, so they are not that kind of weekend pair. The measure is the business-day gap, not the number of calendar days obtained by subtracting the two dates. A row difference of 1 only says the file did not insert another row.

## Core

```text
row numbers 35 36
dates 2024-02-20 2024-02-22
business-day gap = 2
adjacent rows are not adjacent sessions
```

The script walks forward through the dates, finds the first adjacent pair whose business-day gap is greater than 1, prints the row numbers, the two dates, and the gap, and then stops.

`np.busday_count(2024-02-20, 2024-02-22)` equals 2. The half-open interval contains two weekdays, the end date 2024-02-22 is excluded, and the business day between the rows never became a row. If the next row were the next session, the same function would return 1. A weekend pair returns 1, because Saturday and Sunday do not enter the count. "The row numbers differ by 1" and "the business-day gap is 1" are two predicates. This pair meets the first. The printed gap is 2, so it does not meet the second.

A lag taken by row treats the previous row as yesterday. On row 36 the previous row is dated 2024-02-20, and one business day is missing in between. The lag steps over that missing session and still moves only one row in the file. If a return uses the previous row's close in the denominator, the holding period is not one session. Putting that return into the same regression as an ordinary one-day return writes two holding periods under one time index.

## Further out

A business-day count and a calendar-day count separate on weekends. Friday to the next Monday crosses two days off, and the business-day gap is still 1. From 2024-02-20 to 2024-02-22 the business-day gap is 2. The missing day is a weekday, not a weekend. `np.busday_count` uses the default Monday-to-Friday week. If an exchange calendar marks a weekday as closed, the default count still treats that day as a business day and the gap is understated. The printed 2 is the count on this default calendar. It is already enough to show that 2024-02-20 and 2024-02-22 are not adjacent sessions. A finer holiday table would change the gap on other dates. It would not turn "row difference 1" into a time difference of 1.

A rolling window, a volatility, or a volume average that takes "the last twenty rows" will, after this pair, treat 2024-02-20 as the day before 2024-02-22. Aligning by session needs a business calendar first, and then a decision: leave the missing day blank, fill it with a close already known, or drop the interval from the sample. Yesterday's 9.8971 already says a fill may use only a close known at the time. Today's fact is the one that remains when nothing is filled: adjacent rows are not adjacent sessions. Rows 35 and 36 differ by 1. The dates are 2024-02-20 and 2024-02-22. The business-day gap is 2.

A halt check asks whether the business-day gap of the pair is greater than 1. It does not ask whether the row numbers are consecutive. The first adjacent pair with a gap greater than 1 is rows 35 and 36. The script stops there, and later rows are not printed. Next, one return is computed on the adjusted close and one on the unadjusted close, so the size of a corporate action in the unadjusted return can be read.

Rows 35–36, dates 2024-02-20 and 2024-02-22, business-day gap 2. Adjacent rows are not adjacent sessions.

Lag by row index after a halt spans the missing session; gap counting uses np.busday_count on printed dates.

**Rows vs sessions.** Adjacent row numbers can span a two business-day gap—build lags on dates, not row index alone.

## What the run showed

```bash
python days/35-halt-gap/halt_gap.py
```

The script should print row numbers 35 and 36, the dates 2024-02-20 and 2024-02-22, and a business-day gap of 2. The implementation is [`halt_gap.py`](../../days/35-halt-gap/halt_gap.py).

Hand in this one pair of adjacent rows. The business-day gap is 2, so one business day is missing. Weekend neighbors have a business-day gap of 1. A row difference of 1 is not a time difference of 1.
