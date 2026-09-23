<p align="center"><a href="day-38.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 38 · Lag the signal one day

[Phase I · Models](../../README.en.md) · runs

What you learn today: line up the sign of the market return with the sign of AAA's adjusted return. Same-day accuracy is 0.6795. Lagged one day it is 0.4026. The 0.2769 that disappeared was simultaneous. 0.4026 is below 0.5 and is not a usable forecast.

## Plain-language account

AAA's adjusted return and the market return are both simple returns. The score keeps only whether the signs match. With the market sign taken on the same day, accuracy against AAA's sign is 0.6795. Shift the market sign back by one session, and yesterday's market sign is compared with today's AAA sign. Accuracy is 0.4026.

0.6795 minus 0.4026 equals 0.2769. That 0.2769 is present before the lag and absent after it. It depends on a market return and a name return that were realized together on the same session. The day's market return is complete at that close, and AAA's return that day is complete at that same close. Aligning one with the other uses two numbers known at the same time. After the one-day shift, the accuracy that remains is 0.4026. 0.4026 is below 0.5. A sign match with no information sits on the side of one half. The print is below that. This column of lagged market signs does not give a usable forecast. 0.6795 stays on the row that was aligned at the same time.

## Core

```text
same-day market sign accuracy = 0.6795
lagged-one-day market sign accuracy = 0.4026
what disappeared was simultaneous
```

Accuracy is the fraction of matching signs. The lag uses the previous item of the market series itself. The label starts at the second item, and the two lengths match.

The information set of 0.6795 includes today's market return. The information set of 0.4026 stops at yesterday's market return. The difference of the two accuracies is 0.2769, and that piece disappears with today's market return. What remains, 0.4026, is the hit rate of the lagged rule on this table. It is below 0.5. A sign hit below one half is not a forecast that becomes usable by widening a threshold. Today's rule was written in advance as "the market sign lagged one day," and the print is 0.4026.

Yesterday's 0.7234 also used the same-day market, and it also allowed one date to appear on both sides of the split across names. Today the question is sign alignment on one name. The same day still scores 0.6795. Lagged one day, 0.4026 remains. Set side by side, the higher number stays on the column that was completed at the same time.

## Further out

A market quantity known before the close and a market return completed only at the close are not the same column. An intraday return already realized, yesterday's close, and the overnight gap each have their own time of becoming known. The series lagged today is the full-day market return. The one-day lag puts the whole signal on the session before the label. After that, the hit rate is 0.4026. The sign of the full-day market return, lagged one day, lines up with AAA's next-day sign on less than half the rows. Using a partial intraday quantity requires cutting that column at the time it is actually known. The full-day return cannot stand in for it, with the accuracy written back as 0.6795.

0.4026 is not written up as the score of the reversed rule. Reversing swaps hits and misses, and that is a different rule, available only after 0.4026 has been seen. Today does not search for another rule. Next, a position written down in advance is applied to the return, a round-trip cost written down in advance is subtracted, and the sign of the gross mean is read before the cost.

How much of 0.6795 comes from one session that has already finished can be read by subtraction. Removing the simultaneous alignment takes away 0.2769 and leaves 0.4026. The remainder is below one half. On this table, yesterday's market sign and today's AAA adjusted-return sign disagree on more rows than they agree. Disagreement is not a forecast to send as an order. The simultaneous 0.6795 describes the alignment after the day's market and the day's name have both been realized. Printing the two accuracies together keeps 0.2769 on the word "simultaneous."

Same-day market sign accuracy 0.6795; lagged 0.4026; 0.2769 was simultaneous. 0.4026 below 0.5 is not a tradable forecast.

Do not treat 0.6795 as out-of-sample alpha; lagged 0.4026 is the honest tradable-signal read for whole-day market return.

**Simultaneity.** Same-day market 0.6795 vs lagged 0.4026—what disappeared was simultaneous alignment.

## What the run showed

```bash
python days/38-lag-signal/lag_signal.py
```

The script should print same-day market-sign accuracy 0.6795 and lagged-one-day accuracy 0.4026. The implementation is [`lag_signal.py`](../../days/38-lag-signal/lag_signal.py).

Hand in the two accuracies. The 0.2769 that dropped out was simultaneous. What remains, 0.4026, is below 0.5 and is not a usable forecast.
