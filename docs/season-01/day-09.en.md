<p align="center"><a href="day-09.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 9 · Shuffle the row order

[Phase I · Models](../../README.en.md) · runs

Day 8 changed the set that enters the normal equations, and the slope moved from 2.0500 to 8.0500. Today the set does not change. The five pairs stay intact. Only their row order in the table is permuted, and batch OLS is run again.

The coefficients and the residual sum of squares do not move. The normal equations sum over pairs. Row order is not an argument. The fit does not use presentation order. That does not mean the abscissa contains no time. Time is written in `x_t`.

---

## Rows move, pairs do not

On the original order the line is still

```text
ŷ = 3.2700x − 1.2900
RSS = 96.3390
```

The fixed row order is `[2, 4, 3, 0, 1]`, zero-based, so the table is read as the original rows 3, 5, 4, 1, 2. The order is written down in advance. It is not chosen after looking at the fit. Each row moves as a pair `(x, y)`.

A second `lstsq` returns

```text
ŷ = 3.2700x − 1.2900
RSS = 96.3390
Δβ₁ = 1.332e-15
ΔRSS = 1.421e-14
```

The difference is floating-point noise. Batch OLS under squared loss is a function of the multiset of pairs. Changing the order of summation does not change the sum. Every row permutation therefore returns the same `β̂`, up to rounding.

---

## What the invariance is

Reading the table from top to bottom, or in another order, yields the same estimate whenever the five pairs are the same pairs. A day-8 window keyed by the calendar index `t` is likewise unchanged by a row permutation, because the pairs inside the window do not change. Every estimator that sums over `t` has this invariance.

Three nearby claims do not follow.

First, `x` is not an ignored column. `x_t = t` is still the first column of the design. Permuting rows does not remove the date from the pair.

Second, this is not a license to treat the score as insensitive to time. Reassigning closes to different dates breaks the pairs, and the `RSS` generally changes. That is a different experiment. Today's script does not break the pairs, and it does not report that other number.

Third, a recursive estimator that updates in order of arrival does not have this invariance. Today's estimator is not recursive. It reads the five rows at once. Order exists in the file. It does not exist in the objective.

The loose claim that the fit "does not know time" is tightened to a sentence that can be checked: batch squared loss does not know row order. The calendar coordinate is still in the model.

---

## Reproduce

```bash
python days/09-row-order/row_order.py
```

The script should print `y = 3.2700 x + -1.2900` twice, `RSS = 96.3390` twice, and a `delta RSS` on the order of `1e-14`. The implementation is [`row_order.py`](../../days/09-row-order/row_order.py).

---

## What this day is not

The invariant object is the sum of squared level residuals. The next day reports a second functional of the same line: the direction of the one-day move in the close. A smaller price residual can still have the wrong sign. Both scores are due. Invariance to row order does not answer the direction score.
