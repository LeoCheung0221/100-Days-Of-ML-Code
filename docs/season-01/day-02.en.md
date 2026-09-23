<p align="center"><a href="day-02.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 2 · Absolute error and squared error

[Phase I · Models](../../README.en.md) · runs

What you learn today: the same line and the same residuals must be reported as both absolute loss and squared loss. Session 4 is 0.4928 of the absolute loss and 0.6997 of the squared loss.

## Plain-language account

Day 1 left five residuals: 0.12, −1.35, −2.32, 8.21, −4.66. Saying "session 4 missed by 8.2" names one distance. Saying "the sum of squares is 96.339" names one total. Neither says how large session 4 is inside each total. Add the absolute residuals and the sum is 16.66. Session 4's 8.21 is 0.4928 of that, under half. Square them first and the sum is 96.339. Session 4's square is 67.4041, which is 0.6997 of the total, close to seven tenths. The point did not become more important. Squaring lifts a residual whose absolute value is above 1 and shrinks one whose absolute value is below 1. The first day's 0.12 becomes 0.0144.

One number is not enough. 8.2 does not say whether it is an absolute residual, a squared residual, or an average. 16.66 or 96.339 alone does not say how far session 4 was amplified.

## Core

The line is still `ŷ = 3.27x − 1.29`. With `r = y − ŷ`:

```text
L1 = Σ |r_t|
L2 = Σ r_t²
```

| t | y | ŷ | r | \|r\| | r² |
|---:|---:|---:|---:|---:|---:|
| 1 | 2.1 | 1.98 | 0.12 | 0.12 | 0.0144 |
| 2 | 3.9 | 5.25 | −1.35 | 1.35 | 1.8225 |
| 3 | 6.2 | 8.52 | −2.32 | 2.32 | 5.3824 |
| 4 | 20.0 | 11.79 | 8.21 | 8.21 | 67.4041 |
| 5 | 10.4 | 15.06 | −4.66 | 4.66 | 21.7156 |
| sum | | | | 16.66 | 96.339 |

Session 4's share of `L1` is 0.4928 and of `L2` is 0.6997, printed to four decimals so the split lines up with day 3. Ordinary least squares from day 1 minimizes the sum of squares, not the sum of absolute residuals:

```text
β̂_L2 = argmin_β Σ (y_t − β₁ x_t − β₀)²
```

The printed slope 3.27 and intercept −1.29 are that minimizer. The absolute-loss minimizer is a different problem and is not solved today. Today only requires both norms, and both shares, on the line already fit. Changing the loss can change the minimizer. The endpoint chord on day 4 is where that shows up.

## Further out

Mean squared error and mean absolute error are often treated as interchangeable ways of saying "the error got smaller." They do not select the same point. Squared loss lets a few large residuals dominate a fit, so one jump, one bad print, or one unadjusted corporate action can own the objective. Absolute loss still sees those points, but it does not let them grow with the square.

In a factor regression or a portfolio objective, changing the norm can change the solution. An "error" that does not name its norm hides how much one session was amplified. These five points make the arithmetic visible: the same residual vector, shares 0.4928 and 0.6997. When a mean squared error falls, ask whether one or two squared outliers produced the fall.

## What the run showed

From the repository root, still on `numpy==1.24.4`:

```bash
python days/02-two-losses/two_losses.py
```

The script should print `L1 = sum |r| = 16.66`, `L2 = sum r^2 = 96.339`, and session-4 shares `0.4928` and `0.6997`. The implementation is [`two_losses.py`](../../days/02-two-losses/two_losses.py). The line still comes from `numpy.linalg.lstsq`.

Both losses are in sample. Neither is a holdout score. Hand in the two norms and the two shares. Day 3 splits the sum of squares back into each session. Day 4 compares this line with the endpoint chord, where the two losses can rank the fits in opposite order.
