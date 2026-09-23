<p align="center"><a href="day-09.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 9 · Shuffle the row order

[Phase I · Models](../../README.en.md) · runs

What you learn today: the five pairs stay intact and only the row order changes, to `[2, 4, 3, 0, 1]`. The slope and the residual sum of squares stay `3.2700x − 1.2900` and 96.3390. That is invariance of batch least squares to row order. It is not a model that ignores time.

## Plain-language account

Day 8 changed which sessions entered the equation. The window moved from `{1, 2, 3}` to `{2, 3, 4}`, and the slope jumped from 2.0500 to 8.0500 because the close of 20 on session 4 entered the information set. Today the set is fixed: the same five points `(1, 2.1)` through `(5, 10.4)`. Only the row order in the file changes.

Picture five cards: the front shows the session index, the back shows the close. Shuffling the deck changes stack order, not which back belongs to which front. The script order `[2, 4, 3, 0, 1]` means the old row 3 sits on top, still labeled session 3 with 6.2. Peeling a back and gluing it to another front would be a different experiment. Today does not break pairs.

Ordinary least squares accumulates sums. Each row contributes terms to `XᵀX` and `Xᵀy`. Addition is commutative, so permuting rows permutes terms inside those sums without changing the totals, as long as each row still carries its own `[t, 1]` and its own `y`. The printed line remains `ŷ = 3.2700x − 1.2900` and RSS remains 96.3390. Differences of `1.332e-15` on the slope and `1.421e-14` on RSS are floating-point noise at roughly `1e-14`. They are not an economic shift in the fit.

Calling this "the model ignores time" is misleading. Time enters through `x_t = t` in the design matrix. Session 1 and session 5 are different first-column entries. What does not enter is "this row is row k in the CSV." Row index is not a feature unless you put it in `X`. Today's design is only `[t, 1]`.

## Core

Original batch least squares:

```text
ŷ = 3.2700x − 1.2900
RSS = 96.3390
```

After the order `[2, 4, 3, 0, 1]`:

```text
Δslope = 1.332e-15
ΔRSS = 1.421e-14
```

With permutation matrix `P` that only reorders rows, `(PX)ᵀ(PX) = XᵀX` and `(PX)ᵀ(P y) = Xᵀy` in exact arithmetic, so the least-squares solution is unchanged. `numpy.linalg.lstsq` may show the tiny deltas above; treat them as zero in interpretation.

| Operation | Sample set | Design rows | β̂ and RSS |
|---|---|---|---|
| Day 8 slide window | Changes | Still `[t, 1]`, different t set | Changes (e.g. 2.0500 → 8.0500) |
| Day 9 shuffle rows | Same five t | Same `[t, 1]`, permuted order | Unchanged (up to float noise) |
| Break pairs (not today) | Five rows | t and y misaligned | Generally changes |

Day 1 already fit this line and RSS. Day 9 verifies that reordering rows does not refit a new story. Day 7 holdout removed a point from estimation; shuffle keeps all five points in the loss.

Day 10 will keep this line but score direction instead of level. Invariance today guarantees day 9 does not move day 10's line; day 10 changes the functional, not `β̂`.

## Further out

Three notions of "order" appear in research code: file row order, calendar order, and explicit `t` or `date` inside features. Batch OLS is invariant to the first when pairs are intact. It is sensitive to the second once features are defined as "previous row." It is sensitive to the third because that column is inside `X`. Sorting a panel by `date, symbol` before building lags is hygiene, not an extra regressor.

Shuffling rows after building correct lags is not the same as shuffling before building lags. Day 26's random split assigns rows to train or test; day 37's pooled names share dates across sides. Those are information-set issues, not the row-order invariance of a fixed design matrix.

A hand-check on five points: `β₁` is a ratio of sums of products `(t − t̄)(y − ȳ)`. Both numerator and denominator reorder unchanged when pairs stay intact. RSS is a sum of five squared residuals, each depending only on its own `(t, y)`. Breaking pairs changes cross-terms; shuffling intact pairs does not.

## What the run showed

```bash
python days/09-row-order/row_order.py
```

Expect `3.2700 x + -1.2900`, `RSS = 96.3390`, and the two near-zero deltas. Code: [`row_order.py`](../../days/09-row-order/row_order.py).

Hand in three checks: pairs intact; `β̂` and RSS match day 1; deltas at `1e-14` mean zero. Do not write "shuffle removes time"; write "time is in column t, not in row index." Day 10 reads direction from the same line; a large level residual and a direction miss can land on different sessions.

Before claiming "we shuffled the data," specify whether you permuted rows of a fixed design or destroyed time when constructing features. Those are different operations; only the first is what today's script demonstrates.
