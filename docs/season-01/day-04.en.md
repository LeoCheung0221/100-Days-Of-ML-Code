<p align="center"><a href="day-04.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 4 · The chord through the endpoints

[Phase I · Models](../../README.en.md) · runs

The chord uses session 1 and session 5 only. It belongs to the same affine class as ordinary least squares, `ŷ = β₁ x + β₀`. Same class, different loss, and the ranking is allowed to flip.

On squared loss the chord cannot beat OLS. OLS is the minimizer of `L2` inside this class. On absolute loss the chord can be smaller. The two norms from day 2 rank the two lines in opposite orders.

---

## The chord

Through `(1, 2.1)` and `(5, 10.4)`:

```text
β₁ = (10.4 − 2.1) / (5 − 1) = 2.075
β₀ = 2.1 − 2.075 × 1 = 0.025
ŷ = 2.075x + 0.025
```

Both endpoint residuals are 0. That is two-point interpolation, not a minimum of the residual sum of squares. The three middle sessions do not enter the coefficients. The close at 20 does not enter the coefficients.

| t | Chord ŷ | Chord residual | OLS ŷ | OLS residual |
|---:|---:|---:|---:|---:|
| 1 | 2.1000 | 0.0000 | 1.9800 | 0.1200 |
| 2 | 4.1750 | −0.2750 | 5.2500 | −1.3500 |
| 3 | 6.2500 | −0.0500 | 8.5200 | −2.3200 |
| 4 | 8.3250 | 11.6750 | 11.7900 | 8.2100 |
| 5 | 10.4000 | 0.0000 | 15.0600 | −4.6600 |

---

## Two losses, two rankings

| Estimator | L1 | L2 | Session 4 \|r\| |
|---|---:|---:|---:|
| Chord | 12.0000 | 136.3837 | 11.6750 |
| OLS | 16.6600 | 96.3390 | 8.2100 |

`136.3837 > 96.3390` is not an accident of this sample. Every affine function has an in-sample sum of squares at least as large as the OLS value. The chord is affine, so it does not win on `L2`.

`12.0000 < 16.6600` is also computed. The chord sets both endpoint residuals to 0 and piles the absolute error onto session 4. OLS refuses to zero the endpoints, because that would raise the sum of squares. Its absolute residual on session 4 is therefore smaller, and its total absolute loss is larger.

Until the loss is named, there is no answer to which line is better. Calling the chord cruder is a statement about squared loss.

---

## Reproduce

```bash
python days/04-endpoint-chord/endpoint_chord.py
```

The script should print the chord `y = 2.0750 x + 0.0250`, its `L2 = 136.3837`, and the OLS `L2 = 96.3390`. The implementation is [`endpoint_chord.py`](../../days/04-endpoint-chord/endpoint_chord.py). The chord uses the two-point formula, not `lstsq`.

---

## What this day is not

Both lines are scored on all five points. The chord ignores the middle points by keeping them out of the coefficients, then still scores them. That is not a refit after deletion. Delete session 4 and fit again, and the coefficients move. That is day 5.
