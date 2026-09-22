<p align="center"><a href="day-01.md">中文</a></p>

# Day 1 · In-sample nearest neighbor and ordinary least squares

[Phase I · Models](README.en.md) · runs

Two estimators, one query, in-sample residuals only. The series is five closing prices. The query `x = 4` lies inside the training set. It is not a holdout.

The nearest neighbor therefore repeats that point's label and the residual is 0. Ordinary least squares minimizes the residual sum of squares inside the affine class, cannot place the fitted value at 20, and leaves a residual of 8.2. A zero residual here is retrieval. A nonzero residual is the approximation error of the model class.

---

## Sample

Let `y_t` be the close on session `t`, for `t = 1,…,5`. Aside from session 4, the path rises by about 2 per day. The close at 20 is the observation with the largest pull on squared loss.

| t | Close y | OLS fit ŷ | Residual y − ŷ |
|---:|---:|---:|---:|
| 1 | 2.1 | 1.98 | 0.12 |
| 2 | 3.9 | 5.25 | −1.35 |
| 3 | 6.2 | 8.52 | −2.32 |
| **4** | **20.0** | **11.79** | **8.21** |
| 5 | 10.4 | 15.06 | −4.66 |

Fitted values are the script's two-decimal print. The session-4 residual is `20.0 − 11.79 = 8.21`, reported as **8.2**.

---

## Estimator 1 · Nearest neighbor

For a query `x`,

```text
î = argmin_i |x_i − x|
ŷ = y_î
```

with `x_i = i`. When the query coincides with a training abscissa, the neighbor is that point, the estimate equals the label, and the in-sample residual is identically 0.

At `x = 4`:

| | |
|---|---|
| Estimate | 20.0 |
| Residual | 0 |

That 0 does not use the other four closes. It records that the query sits on the training support and the label was retrieved. Outside that support the same rule can only copy the nearest observed label. That is day 6.

---

## Estimator 2 · Ordinary least squares

The hypothesis class is the affine map `ŷ = β₁ x + β₀`. Row `i` of the design matrix is `[x_i, 1]`. The coefficient is the minimizer of the residual sum of squares:

```text
β̂ = argmin_β || y − Xβ ||²
```

The closed form on these five points, printed to two decimals, is

```text
ŷ = 3.27x − 1.29
```

At the query: `3.27 × 4 − 1.29 = 11.79`.

| | |
|---|---|
| Estimate | 11.79 |
| Residual | 8.2 |

Squared loss weights the outlying close more than the points that already lie near a line. OLS still does not lift the whole line to 20. Doing so would increase the squared residuals of the other four points, and the total loss would rise. 11.79 is the compromise of one line across five points. 8.2 is the in-sample residual session 4 pays for that compromise.

The five residuals change sign. The line has no special rule that spares one point. An affine function cannot zero all five residuals at once. Session 4 has the largest residual because it sits farthest from the slope supported by the other four.

---

## Side by side

| Estimator | Output at x = 4 | In-sample residual | Why the residual is this number |
|---|---:|---:|---|
| Nearest neighbor | 20.0 | 0 | The query coincides with a training point, so the output is the label |
| OLS | 11.79 | 8.2 | Minimizer of residual sum of squares in the affine class |

> A parameterized mean is not a retrieval of the training label. On the training support the nearest-neighbor residual is zero. The residual of the line is the approximation error of the model class.

---

## Reproduce

From the repository root, Python 3.8 or newer:

```bash
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
python days/01-line-that-misses/fit_line.py
```

The script should print `y = 3.27 x + -1.29`, a nearest-neighbor residual of `0.0`, and a line residual of `8.2`. The implementation is [`fit_line.py`](../../days/01-line-that-misses/fit_line.py). It calls `numpy.linalg.lstsq` for the least squares above. There is no iteration.

The same `y` and fitted values are drawn in [`site`](../../site). From that directory, run `npm install`, then `npm run dev`. Session 4 sits at 20, the line passes through 11.79, and the vertical segment marks the residual 8.2. The page does not emit an order. Later backtests use historical prices, not a live book.

---

## What this day is not

This is not an out-of-sample evaluation. The query belongs to the training set. A zero nearest-neighbor residual does not transfer into a claim that the estimator works.

| Later | Convenience removed |
|---|---|
| Day 2 | The same residual must be reported as absolute loss and as squared loss. Squared loss raises the weight of session 4 further |
| Day 6 | Query a point outside the training support. The neighbor can only copy. The line must extrapolate |
| Day 7 | Hold out session 5. Residuals on the fitting set no longer count as the score |
