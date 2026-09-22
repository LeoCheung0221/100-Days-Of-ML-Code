<p align="center"><a href="day-05.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 5 · Refit without session 4

[Phase I · Models](../../README.en.md) · runs

Day 3 located the squared loss on session 4. Day 4 kept that close out of the chord's coefficients, then still scored every session. Today `(4, 20)` is removed from the estimation sample, the normal equations are solved again, and the displacement of the whole line is recorded.

The displacement is not an exam score. The label on session 4 is absent from the fit, and it is not treated as a holdout result. A holdout that voids the training residual is day 7, and the held-out session there is session 5.

---

## Two lines

On the full sample:

```text
ŷ = 3.2700x − 1.2900
```

After session 4 is deleted, refit on `t ∈ {1, 2, 3, 5}`:

```text
ŷ = 2.0971x − 0.1171
```

```text
Δβ₁ = −1.1729
Δβ₀ = 1.1729
```

At full precision the two moves are negatives of each other, so the displacement is proportional to `(x − 1)`. It is 0 at `t = 1` and grows with `x`. The four-decimal table rounds each cell on its own. Multiplying the printed −1.1729 by `(x − 1)` does not recover every cell. The cancellation is a fact about this sample. It is not a theorem that an endpoint fit must stay fixed after a deletion.

| t | Full-sample ŷ | Refit ŷ | Displacement |
|---:|---:|---:|---:|
| 1 | 1.9800 | 1.9800 | 0.0000 |
| 2 | 5.2500 | 4.0771 | −1.1729 |
| 3 | 8.5200 | 6.1743 | −2.3457 |
| 4 | 11.7900 | 8.2714 | −3.5186 |
| 5 | 15.0600 | 10.3686 | −4.6914 |

At the deleted abscissa the fitted value falls from 11.7900 to 8.2714. One point raised the slope by 1.1729. The share 0.6997 says that session 4 is heavy in the sum of squares. The displacement says how far it moved the line. Those are not the same sentence.

---

## The gap is not the score

The refit equals 8.2714 at `x = 4`. The gap from the label 20.0 to that value is 11.7286. It is not reported as a score.

There are two reasons. The point was removed in order to see its influence, and the removal looked at the size of `y_4`. And if a score is defined as a holdout residual, the information set used for fitting and the point used for scoring have to be separated in advance. Today's information set is the four points left after a temporary deletion. What is reported is the coefficients and the movement of `ŷ(x)`.

`x = 4` still lies in the convex hull of the remaining abscissae `{1, 2, 3, 5}`. This is influence at an interpolation site, not extrapolation past the support. Extrapolation is day 6.

---

## Reproduce

```bash
python days/05-without-day-4/without_day4.py
```

The script should print `delta slope = -1.1729` and a displacement of `-3.5186` at `x = 4`. The implementation is [`without_day4.py`](../../days/05-without-day-4/without_day4.py).

---

## What this day is not

The full-sample line is not discarded. It is the line the refit is compared with. The in-sample `RSS = 96.339` is still the sum of squares of the day-1 line. It is not today's result. Today's result is the displacement.
