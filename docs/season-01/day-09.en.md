<p align="center"><a href="day-09.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 9 · Shuffle the row order

[Phase I · Models](../../README.en.md) · runs

What you learn today: the five pairs stay intact and only the row order changes, to `[2, 4, 3, 0, 1]`. The slope and the residual sum of squares stay `3.2700x − 1.2900` and 96.3390. That is invariance of batch least squares to row order. It is not a model that ignores time.

## Plain-language account

Day 8 changed the set inside the equation, and the slope moved from 2.0500 to 8.0500. Today the set stays. The five pairs of session index and close stay intact. Only their vertical order in the table is shuffled, and batch least squares is run again.

The new order, in zero-based indices, is `[2, 4, 3, 0, 1]`. The third row moves to the top, and that row is still session 3 paired with 6.2. The close of session 3 is not attached to another day. The normal equations sum over rows. A sum does not depend on the order of its terms, so the coefficients should not change. The printed line is still `ŷ = 3.2700x − 1.2900` and the sum of squares is still 96.3390. The slope differs by `1.332e-15` and the sum of squares by `1.421e-14`. That is floating-point noise, not a new line.

It is easy to call this "the model ignores time." That sentence is wrong. The abscissa is still `x_t = t`. Session 1 and session 5 are not the same number in the design matrix. Time entered the equation. What did not enter is the typography of the table. Breaking the pairs, so that session 5's close is tied to session 1's abscissa, is a different problem and is not done today. Pairs stay whole.

## Core

Batch least squares in the original order:

```text
ŷ = 3.2700x − 1.2900
RSS = 96.3390
```

After the row order becomes `[2, 4, 3, 0, 1]`, the equations are solved again. The differences are:

```text
Δslope = 1.332e-15
ΔRSS = 1.421e-14
```

Each design row is still `[t, 1]` and the label is still the close at that `t`. Swapping rows swaps terms in a sum. `XᵀX` and `Xᵀy` are unchanged in exact arithmetic, so the `lstsq` coefficients are unchanged. A floating-point gap around `1e-14` is not "the slope moved a little after the shuffle."

Day 8's window also collects rows by date, not by their current position in the table. If the pairs stay intact, swapping the three rows of a window does not change that window's coefficients. Do not say that shuffling rows would move day 8's slope off 2.0500. The window changed because the set changed from `{1, 2, 3}` to `{2, 3, 4}`. A new row order with the pairs intact leaves the set alone.

## Further out

Panel and tick data are sorted before a regression: by time, by name, by trade. The sort keeps lags, rolling windows, and session alignment from being written against the wrong neighbor. The sort itself is not a feature. Batch least squares reads the pair `(x, y)`. It does not read "this row is now in position k." The estimate changes if the sort is fed back in as a column, or if the shuffle separates labels from features.

A time-series model can depend on order somewhere else. A lag `y_{t-1}` must take the previous label in time, not the previous row after a shuffle. Today's abscissa is the session index already stored inside the row, so exchanging rows does not exchange information. If the feature were "the close in the row above," a shuffle would replace yesterday with an unrelated day. That is a change in the definition of the feature, not least squares suddenly reading row order. Before building a lag, sort by time, then take the previous row. Today does not build that lag column.

## What the run showed

```bash
python days/09-row-order/row_order.py
```

The script should print the line after the shuffle as `3.2700 x + -1.2900`, `RSS = 96.3390`, and the two near-zero differences. The implementation is [`row_order.py`](../../days/09-row-order/row_order.py).

Hand in invariance to row order. Time is still in the design matrix. Day 10 keeps this full-sample line and changes the score from the price level to the direction of the move. A direction hit and a small absolute residual need not fall on the same day.
