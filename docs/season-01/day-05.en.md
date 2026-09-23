<p align="center"><a href="day-05.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 5 · Refit without session 4

[Phase I · Models](../../README.en.md) · runs

What you learn today: after `(4, 20)` is removed and the normal equations are solved again, the slope falls from 3.2700 to 2.0971, a change of −1.1729. That is a displacement of the whole line, not an exam score for session 4.

## Plain-language account

Day 3 put 0.6997 of the sum of squares on session 4. Day 4's chord ignored that point when choosing coefficients, but still scored all five points. Today does something else. Remove `(4, 20)` from the estimation sample, refit on sessions 1, 2, 3, and 5, and record how far the line moves.

The full-sample line is `ŷ = 3.2700x − 1.2900`. Without session 4 it is `ŷ = 2.0971x − 0.1171`. The slope falls by 1.1729 and the intercept rises by 1.1729. At full precision those two moves are opposites, so the displacement of the fitted value is proportional to `(x − 1)` and is 0 at session 1. The four-decimal table is rounded cell by cell. Multiplying the printed −1.1729 by `(x − 1)` does not recover every cell. The printed displacement at session 3 is −2.3457, not −2.3458. The cancellation is a fact about this sample. It is not a theorem that an endpoint must stay fixed after a deletion.

At the deleted abscissa the fitted value falls from 11.7900 to 8.2714, a displacement of −3.5186. The gap from the label 20.0 to 8.2714 is 11.7286. That gap is not today's score. The point was removed in order to watch its influence, and the removal already used how large 20 is. `x = 4` also remains inside the convex hull of `{1, 2, 3, 5}`. This is influence at an interior location, not extrapolation past the support.

## Core

Full sample:

```text
ŷ = 3.2700x − 1.2900
```

Refit on `t ∈ {1, 2, 3, 5}`:

```text
ŷ = 2.0971x − 0.1171
```

```text
Δβ₁ = −1.1729
Δβ₀ = 1.1729
```

| t | full-sample ŷ | refit ŷ | displacement |
|---:|---:|---:|---:|
| 1 | 1.9800 | 1.9800 | 0.0000 |
| 2 | 5.2500 | 4.0771 | −1.1729 |
| 3 | 8.5200 | 6.1743 | −2.3457 |
| 4 | 11.7900 | 8.2714 | −3.5186 |
| 5 | 15.0600 | 10.3686 | −4.6914 |

At full precision the displacement is proportional to `(x − 1)` and is 0 at `t = 1`. Multiplying the printed coefficient back does not reproduce −2.3457 at session 3. Report the table, not the product of the printed coefficient.

The share 0.6997 says session 4 is heavy in the sum of squares. The slope change −1.1729 says how far that point moved the line. The gap 11.7286 is not a score. A holdout that voids the training residual is day 7, and the held-out point there is session 5, not a point removed after it was seen.

## Further out

An influence calculation asks how far a coefficient moves when one observation is deleted. It answers dependence of the estimate on that point. It does not answer a forecast score at that point. The same separation applies to a single day's return. One sentence is the day's share of the loss. A second is how far beta or the intercept moves when the day is removed. A third, and only a third, is the holdout error if the day was set aside before looking. The information sets differ.

Today has the old share and the new displacement. 0.6997 is the full-sample squared share. −1.1729 is the slope change after deletion. 11.7286 looks like a large error, but the deletion used the size of 20, so it is not an out-of-sample score. `x = 4` is still inside the convex hull of `{1, 2, 3, 5}`, so it is not an extrapolation error either. Extrapolation waits until the query leaves the support. That is day 6.

## What the run showed

```bash
python days/05-without-day-4/without_day4.py
```

The script should print `delta slope = -1.1729` and the displacement `-3.5186` at `x = 4`. The implementation is [`without_day4.py`](../../days/05-without-day-4/without_day4.py).

The full-sample line is not discarded. It is the line the refit is compared with. The in-sample `RSS = 96.339` is still the day-1 sum of squares, not today's result. Today's result is the displacement. Day 6 places the query at `x = 6`, where there is no label and the residual is undefined.
