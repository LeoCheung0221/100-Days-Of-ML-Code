<p align="center"><a href="day-06.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 6 · A query outside the training support

[Phase I · Models](../../README.en.md) · runs

What you learn today: the query `x = 6` lies outside the training support `[1, 5]`. The nearest neighbor copies session 5's close, 10.4. The line extrapolates to 18.33. The gap is 7.93. There is no sixth close, so the residual is undefined.

## Plain-language account

The first five days asked questions inside the table. Today the question moves to session 6. The table has no sixth close. Both answers still produce a number, and neither number can be subtracted from a truth, because the truth is not in the sample.

The nearest neighbor may search only among abscissae it has seen. The closest to 6 is 5, and that close is 10.4, so it reports 10.4. The number uses no new observation at `x = 6`. Outside the support there is no local label, and the output falls back to the nearest close on the boundary. For every query past 5, until a closer training point exists, it reports 10.4.

The line does not stop at the boundary. The day-1 coefficients give `3.27 × 6 − 1.29 = 18.33`. An affine function is defined on the whole real line, so the substitution is legal arithmetic. Legal is not the same as scored. A score needs `y_6 − ŷ(6)`. There is no `y_6`, so the difference is undefined. 18.33 and 10.4 differ by 7.93. Both sides of 7.93 are estimates. Calling 18.33 a residual, or calling 10.4 a hit on session 6, replaces an unobserved label with another estimate. The average 14.365 is also just a function of estimates, not a sixth close.

Day 1 at `x = 4` had a label and defined residuals. Day 7 at `x = 5` has a label but excludes it from the fit. Today has no label at all.

## Core

The training abscissae are `{1, 2, 3, 4, 5}` and the support is the closed interval `[1, 5]`. A query is inside the support when it lies in the convex hull of those abscissae. `x = 4` is inside, which is why day 1's neighbor could land on a training point. `x = 6` is outside.

```text
î = argmin_i |x_i − 6| = 5
ŷ_NN = y_5 = 10.4
```

```text
ŷ(6) = 3.27 × 6 − 1.29 = 18.33
```

| | value |
|---|---:|
| Nearest neighbor | 10.4 |
| Ordinary least squares | 18.33 |
| Gap | 7.93 |

The slope outside the support is still 3.27. The line does not switch to the neighbor's rule when it passes the last training point, and it does not clip the extrapolation into the range of closes already seen. Those closes run from 10.4 to 20.0. 18.33 happens to sit inside that range. That is a result of these five numbers and this slope, not a bound the estimator promised. The neighbor has no slope outside the support.

Day 5's `x = 4` was still inside the convex hull of `{1, 2, 3, 5}`. That was influence at an interior point. Today's query is the first one to leave the support. The two questions are not one question about accuracy on unseen places. Today the unseen place has no label, so accuracy cannot be computed.

| Day | Query | Residual y − ŷ |
|---|---|---|
| 1 | 4 | defined |
| 6 | 6 | undefined |
| 7 | 5 | defined (holdout) |

## Further out

A time-series forecast of the next bar places the query outside the support by construction. A neighbor method copies the nearest state already seen. A linear trend keeps drawing the slope. Both can emit a number. Before the label arrives, the gap between those numbers is a gap between estimates, not an error.

Calling an extrapolation a residual usually means a close was filled in afterwards and the miss was computed backwards. That step leaves the information set in which the label was absent at query time. Today deliberately does not invent a sixth close. Inventing one would turn extrapolation back into an in-sample score. The minimum and maximum of prices already seen are not a legal bound on the extrapolation either. 18.33 happens to lie between 10.4 and 20.0. That does not mean the line stayed inside a promised range. The range is a range of labels, not the domain of the function.

Feature stores must as-of cut labels; otherwise off-support queries silently become in-sample lookups. Day 9 shuffling rows does not change 10.4, 18.33, or 7.93 when the design is unchanged.

## What the run showed

```bash
python days/06-off-support/off_support.py
```

The script should print the neighbor `10.4`, the extrapolation `18.33`, the gap `7.93`, and `residual is undefined`. The implementation is [`off_support.py`](../../days/06-off-support/off_support.py).

Hand in two estimates and the sentence that the residual is undefined. Do not write 7.93 as a miss. Day 7 is the first day with a label that does not enter the fit: session 5 is held out, and the training residual stops being the score.
