<p align="center"><a href="day-34.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 34 · Two ways to fill a blank

[Phase I · Models](../../README.en.md) · runs

What you learn today: AAA's close on 2024-02-01 is blank. Filling from the previous close gives 10.1047. Filling from the next close gives 9.8971. Both numbers are printed. The next close sees the future.

## Plain-language account

AAA has a row dated 2024-02-01 whose close is not a finite number. The close on the previous row is 10.1047. The close on the next row is 9.8971. Both fills copy a number already printed on a neighboring row. After the copy, the blank is gone, and later calculations would treat the row as an ordinary sample.

10.1047 and 9.8971 are not the same price. A different fill changes that day's return and any lag that uses this close. 10.1047 is the close of the session before the blank. When the blank is found, that number is already on the table. 9.8971 is the close of the session after the blank. Using it on the 2024-02-01 row writes a later close into that date. The second fill sees the future. Both are printed so that 10.1047 and 9.8971 stand side by side, rather than leaving only one filled series.

## Core

```text
blank date = 2024-02-01
fill from the previous close = 10.1047
fill from the next close = 9.8971
the next close sees the future
```

The blank is located by a close that is not finite. The date prints as 2024-02-01. The fill does not estimate and does not interpolate between the two neighbors. It takes the adjacent close.

The previous-close fill places 10.1047 on 2024-02-01. The next-close fill places 9.8971 on the same row. If a backtest may use new information only after that session's close, the previous close is a price that has already happened, and the next close appears on the following session. Filling with 9.8971 puts the next session inside the blank day's inputs. This is the same kind of problem as yesterday's whole-sample scale: a number that was not yet allowed to be seen enters the input used to build the sample. Yesterday that number was hidden inside 0.002470 and 0.019265. Today the number is 9.8971.

The missing value can stay missing. This script does not hand the blank to a model. It prints the two candidate fills. Once the next close is chosen, the leak is complete at the fill step. A later mean squared error or a direction hit cannot take 9.8971 back out of the row.

## Further out

A blank close on a panel can come from a halt, a session with no trade, or a hole in the file. The research rule states the fill first, and then states the time at which that fill becomes known. If only closes from before that time are allowed, the blank stays missing, or it is replaced by a price already known, under an explicit rule. Copying the next row runs the calendar backward. A backward fill often makes the series look continuous. Continuity is not a reason to put that fill into the training sample.

Forward fill and backward fill are often two function names. The name does not decide the information set. The information set is decided by whether the copied close happened before the blank or after it. The two numbers copied today are 10.1047 and 9.8971. The gap between them is 0.2076, and it comes from the neighboring rows, not from an extra trade on the blank day. Next is another kind of break: the business-day gap between two adjacent rows can be more than one session. A row difference of 1 need not be a time difference of 1.

After 9.8971 is written onto 2024-02-01, the row is finite again, and a later simple return uses it in the numerator or the denominator. Filling 10.1047 puts a different price in the same place. The two filled series can diverge from this day on, and the source of the divergence is the time of the fill. If a backtest at the 2024-02-01 close does not yet know the next day's 9.8971, the second series cannot be built at that time. The script therefore does not emit a filled close column. It prints the date and the two candidate prices together, so the difference between 10.1047 and 9.8971 stays on the page.

Once the two candidate prices stand side by side, the blank day has not yet been written into a price path. 10.1047 is the close already printed on the previous row. 9.8971 is the close that appears only on the next row. A research note that keeps only the filled series shows a later reader a finite close and hides which row the fill came from. The script keeps the date and both prices so the choice on 2024-02-01 stays in the print. Choosing 10.1047 uses a price that has already happened. Choosing 9.8971 uses the next close. Both numbers are printed, and the second one sees the future.

Blank 2024-02-01: fill 10.1047 from previous close vs 9.8971 from next close; the next close sees the future.

**Fill direction.** Previous close 10.1047 is causal; next close 9.8971 sees the future.

## What the run showed

```bash
python days/34-two-fills/two_fills.py
```

The script should print the blank date 2024-02-01, the previous-close fill 10.1047, and the next-close fill 9.8971. The implementation is [`two_fills.py`](../../days/34-two-fills/two_fills.py).

Hand in the two fills. 10.1047 comes from the previous close. 9.8971 comes from the next close, and it sees the future.
