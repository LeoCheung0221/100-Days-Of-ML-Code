<p align="center"><a href="day-06.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 6 · A query off the training support

[Phase I · Models](../../README.en.md) · runs

The training abscissae are `{1, 2, 3, 4, 5}`, so the support is the closed interval `[1, 5]`. Today's query is `x = 6`. There is no sixth close in the sample. Without a label there is no residual.

Each estimator still returns a number. The nearest neighbor can only copy a label it has already seen. Ordinary least squares evaluates the affine function outside the support. That is extrapolation. The gap between the two numbers is a gap between estimates, not a miss.

---

## Support

A query lies in the training support when it lies in the convex hull of the training abscissae. `x = 4` is inside that hull, which is why the day-1 neighbor can land on a training point and why its residual can be 0. `x = 6` is outside the hull. The nearest training abscissa is `5`, not `6`.

```text
î = argmin_i |x_i − 6| = 5
ŷ_NN = y_5 = 10.4
```

This 10.4 does not use a new observation at `x = 6`. Outside the support the estimator has no local label, and the output falls back to the nearest observed close on the boundary.

OLS keeps the day-1 coefficients. Substitute outside the support:

```text
ŷ(6) = 3.27 × 6 − 1.29 = 18.33
```

| | Value |
|---|---:|
| Nearest neighbor | 10.4 |
| OLS | 18.33 |
| Gap | 7.93 |

Both sides of 7.93 are estimates. Neither side is `y_6`. Calling 18.33 a residual, or calling 10.4 a hit on session 6, replaces an unobserved label with another estimate.

---

## Extrapolation uses the class, not new data

The affine class is defined on the whole real line, so substituting `x = 6` is arithmetically legal. Legal is not the same as scored. A score needs `y_6 − ŷ(6)`. That difference is undefined because `y_6` is not in the sample.

The slope outside the support is still 3.27. The line does not switch to the neighbor rule when it passes the last training point, and it does not clip the extrapolated value to the range of observed closes. That range is 10.4 to 20.0. The value 18.33 happens to sit inside it. That is a fact about these five numbers and this slope, not a bound the estimator promised.

The neighbor has no slope outside the support. Its output is 10.4 for every `x > 5`, until a closer training point exists. None does today.

---

## Reproduce

```bash
python days/06-off-support/off_support.py
```

The script should print the neighbor `10.4`, the extrapolated value `18.33`, the gap `7.93`, and `residual is undefined`. The implementation is [`off_support.py`](../../days/06-off-support/off_support.py).

---

## What this day is not

No fictional sixth close is invented in order to manufacture a residual. That would turn extrapolation back into an in-sample score. The next session does have a label, and that label is kept out of the fit: session 5 is held out, and the training residual stops being the score.
