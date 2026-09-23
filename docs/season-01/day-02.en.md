<p align="center"><a href="day-02.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 2 · Absolute error and squared error

[Phase I · Models](../../README.en.md) · runs

One affine fit, one residual vector. A single error number is no longer accepted. Absolute loss and squared loss are two norms of that vector, and session 4 does not have the same share in both.

The ordinary least squares line from day 1 minimizes the sum of squares, not the sum of absolute residuals. Change the loss, and the minimizer is allowed to change.

---

## Two norms

The five closes are unchanged, and so is the line

```text
ŷ = 3.27x − 1.29
```

Write `r = y − ŷ`. The two in-sample losses are

```text
L1 = Σ |r_t|
L2 = Σ r_t²
```

| t | y | ŷ | r | \|r\| | r² |
|---:|---:|---:|---:|---:|---:|
| 1 | 2.1 | 1.98 | 0.12 | 0.12 | 0.0144 |
| 2 | 3.9 | 5.25 | −1.35 | 1.35 | 1.8225 |
| 3 | 6.2 | 8.52 | −2.32 | 2.32 | 5.3824 |
| **4** | **20.0** | **11.79** | **8.21** | **8.21** | **67.4041** |
| 5 | 10.4 | 15.06 | −4.66 | 4.66 | 21.7156 |
| Total | | | | **16.66** | **96.339** |

Session 4 is **0.4928** of `L1` and **0.6997** of `L2`. Under the absolute norm it is less than half the loss. After squaring it is about seven tenths. For `|r| > 1`, the square amplifies the outlier. For `|r| < 1`, the square shrinks it. The absolute residual 0.12 on session 1 contributes 0.0144 to the sum of squares.

This is the shape of `x ↦ x²`, not a narrative ranking of the sessions.

---

## The minimizer follows the loss

```text
β̂_L2 = argmin_β Σ (y_t − β₁ x_t − β₀)²
```

The printed slope and intercept are this minimizer. They are not the minimizer of `L1`. Finding the absolute-loss line is a different calculation, and it is not done today. What is required is that the line already in hand be reported under both numbers.

A lone 8.2 does not say whether it is an absolute residual, a squared residual, or an average. A lone 16.66 or a lone 96.339 does not say how hard session 4 was amplified. The shares are visible only when the two totals sit side by side.

---

## Reproduce

Same dependency as day 1, `numpy==1.24.4`. From the repository root:

```bash
python days/02-two-losses/two_losses.py
```

The script should print `L1 = sum |r| = 16.66`, `L2 = sum r^2 = 96.339`, and session-4 shares `0.4928` and `0.6997`. The implementation is [`two_losses.py`](../../days/02-two-losses/two_losses.py). The line is still the `numpy.linalg.lstsq` solution.

---

## What this day is not

Both losses are in-sample. The query is still inside the training set. Neither number is a holdout score.

| Later | The new restriction |
|---|---|
| Day 3 | The scalar `L2` is no longer enough. The sum of squares has to be opened by session |
| Day 4 | The endpoint chord is scored against this OLS line. The two losses can rank them in opposite orders |
