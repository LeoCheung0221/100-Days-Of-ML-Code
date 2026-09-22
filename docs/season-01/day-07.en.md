<p align="center"><a href="day-07.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 7 · Hold out session 5

[Phase I · Models](../../README.en.md) · runs

The fit uses `t = 1, 2, 3, 4` only. The close 10.4 on session 5 does not enter the normal equations, and it is not a candidate label for the nearest neighbor. The score is the residual on session 5. The residual sum of squares on the fitting sessions may be printed. It does not count.

Day 5 deleted session 4 in order to measure a displacement. Today the last session is held out in order to separate the point that is scored from the points that are estimated.

---

## Information set

```text
Fit:  (1, 2.1), (2, 3.9), (3, 6.2), (4, 20.0)
Exam: (5, 10.4)
```

On those four points the affine OLS line is

```text
ŷ = 5.60x − 5.95
```

The close at 20 is still inside the fit, and the slope rises from the full-sample 3.27 to 5.60. The training residual sum of squares is **42.05**. It says how closely the line sits on the four points it was allowed to see. It does not say how closely it sits on session 5.

---

## The score

| Estimator | Value at x = 5 | Residual 10.4 − value |
|---|---:|---:|
| OLS | 22.05 | −11.65 |
| Nearest neighbor | 20.0 | −9.6 |

The neighbor's candidates are the first four sessions. The nearest abscissa to `x = 5` is `x = 4`, so the estimate copies 20.0. The day-1 residual of 0 required the query to coincide with a training point. Once that coincidence is removed by the holdout, the retrieved object is the neighbor's label. The neighbor is the outlier.

OLS carries the slope 5.60 out to `x = 5` and returns 22.05, farther from 10.4 than the copied outlier is. On this single held-out point the absolute residual is smaller for the neighbor. That does not promote the neighbor to the better model class. It says that a ranking by training `RSS` does not automatically become the holdout ranking. On the full sample, OLS has a smaller in-sample sum of squares than any other affine function. The sum in that inequality runs over the five training points, not over this held-out point.

The numbers that may be written as the score are −11.65 and −9.6. The value 42.05 is printed in order to mark it as excluded.

---

## Reproduce

```bash
python days/07-holdout-day-5/holdout_day5.py
```

The script should print `training RSS = 42.05`, `training RSS is not the score`, an OLS residual of `-11.65`, and a neighbor residual of `-9.6`. The implementation is [`holdout_day5.py`](../../days/07-holdout-day-5/holdout_day5.py).

---

## What this day is not

One held-out point is not an out-of-sample distribution. It only removes the convenience of treating the training residual as the score. Session 5 still sits against the right edge of the fitting support. The query is not the unlabeled extrapolation of day 6. The next day changes the length of the information set: a window of three sessions, slid forward once, so that earlier prices have to leave the fit.
