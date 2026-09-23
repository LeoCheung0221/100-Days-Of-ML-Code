<p align="center"><a href="day-01.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 1 · In-sample nearest neighbor and ordinary least squares

[Phase I · Models](../../README.en.md) · runs

What you learn today: when the query lies on a training point, a nearest-neighbor residual of 0 is retrieval. The ordinary-least-squares residual of 8.2 is the approximation error of the affine class.

## Plain-language account

Five closes sit in a table: 2.1, 3.9, 6.2, 20.0, 10.4. Someone asks for session 4. One answer turns to that row and reads 20. That is the nearest neighbor. The query abscissa equals a training abscissa, so the neighbor is the row itself, the estimate equals the label, and the residual is 0. The 0 does not use the other four closes. It only shows that the question was already in the table.

The other answer refuses to copy a row. It may draw only a straight line, slope times the session index plus an intercept, and it must make the sum of squared vertical distances as small as possible. The line is `ŷ = 3.27x − 1.29`. At session 4 that is 11.79. The gap from 20 is 8.21, printed as an absolute residual of 8.2. Lifting the line through 20 would push the other four points farther away and raise the sum of squares. 11.79 is the compromise. 8.2 is what session 4 pays for it.

Zero and 8.2 are not "accurate" and "inaccurate" in the same sense. Zero is lookup. 8.2 is what this shape of function cannot avoid. If the function class were "copy the nearest row," in-sample residuals could all be zero on training abscissae. That would still not be the same object as a fitted line.

Picture five cards: the front shows session `t`, the back shows close `y`. At `x = 4` the neighbor flips to session 4 and reads 20.0. Ordinary least squares uses all five cards in the sums that build `XᵀX` and `Xᵀy`, then solves for slope 3.27 and intercept −1.29. Row order is not shuffled today—that is day 9. Today only asks what each estimator says at one query inside the support.

Day 6 moves the query to `x = 6` with no label; residuals are undefined there. Day 7 holds out session 5 and stops treating training RSS as the score. Do not read today's 0 or 8.2 as holdout performance.

## Core

Let `y_t` be the close on session `t`, with `x_t = t`. The query `x = 4` lies in the convex hull of `{1,2,3,4,5}` and coincides with a training point. This is not a holdout.

```text
î = argmin_i |x_i − x|
ŷ = y_î
```

At `x = 4`, `ŷ = 20.0` and the residual is 0.

OLS restricts the estimate to `ŷ = β₁x + β₀`. The design row is `[x_i, 1]`. The coefficient minimizes `||y − Xβ||²`. `numpy.linalg.lstsq` returns the closed form. Printed to two decimals, the slope is 3.27 and the intercept is −1.29. Fitted values are 1.98, 5.25, 8.52, 11.79, 15.06. Residuals are 0.12, −1.35, −2.32, 8.21, −4.66. Signs differ. The line has no extra rule that excuses one point. It simply cannot zero five residuals at once. Session 4 is the largest because it sits farthest from the slope supported by the other four.

| Estimator | Value at x = 4 | In-sample residual | Where the residual comes from |
|---|---:|---:|---|
| Nearest neighbor | 20.0 | 0 | The query coincides with a training point |
| OLS | 11.79 | 8.2 | Minimum residual sum of squares in the affine class |

| Dimension | Day 1 (today) | Day 6 | Day 7 |
|---|---|---|---|
| Query | `x = 4`, in support | `x = 6`, off support | `x = 5`, holdout |
| Label used in score | yes (20.0) | no | yes (10.4), not in fit |
| Neighbor behavior | copy training point | copy 10.4 at boundary | copy 20.0 from t = 4 |

In normal-equation language, `β̂ = (XᵀX)⁻¹Xᵀy`. With only five points the course calls `lstsq` directly. The season pins `numpy==1.24.4`; report 3.27 and −1.29 as printed, not hand-rounded substitutes.

## Further out

The same pair of answers returns in quantitative work under other names. Reporting tomorrow from "the historical day that looks most like today" can look perfect in sample, because similarity was defined on days already seen. A linear factor model instead limits the return to a short list of exposures. What the class cannot reach stays in the residual. A large residual can mean the class is narrow. A zero residual can mean the query landed on a training point.

Before a cross-sectional regression or a search for similar history, ask whether the query is inside the training support. On the support, a neighbor's zero is not out-of-sample skill. A line's nonzero residual compares function classes. It does not certify performance off the sample. Costs, limits, and live orders are outside today. The animation draws the five points and the line. It does not emit an order.

A common backtest mistake averages neighbor errors on rows that already have labels, then sells the average as alpha. That repeats today's lookup at every training abscissa. Treating 8.2 as "OLS failed" while ignoring the other four signed residuals misreads the in-sample vector. Day 4's endpoint chord lives in the same affine class with a different coefficient rule. Day 5 deletes session 4 and moves the slope by −1.1729—an information-set change, not a rename of the estimator.

## What the run showed

From the repository root:

```bash
python days/01-line-that-misses/fit_line.py
```

The script should print `y = 3.27 x + -1.29`, a nearest-neighbor residual of `0.0`, and a line residual of `8.2`. The implementation is [`fit_line.py`](../../days/01-line-that-misses/fit_line.py). The same numbers are drawn in [`site`](../../site).

Hand in only this comparison. The query belongs to the training set. The neighbor's 0 is not "the model works." The line's 8.2 is not "discard the line." It is the minimum squared residual of the affine class on these five points. Day 2 reports the same residual as both absolute loss and squared loss. Day 6 moves the query off the support. Day 7 holds out session 5 and stops treating the training residual as the score.

Self-check without changing digits: Did you call 0 "predictive accuracy"? Did you call 8.2 a failure instead of the affine optimum at that query? Did you mix holdout language from day 7? Run the script before editing notes; assert NN output 20.0 and `lstsq` coefficients match the printout.
