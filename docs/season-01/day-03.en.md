<p align="center"><a href="day-03.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 3 · The five residuals side by side

[Phase I · Models](../../README.en.md) · runs

What you learn today: the sum of squares 96.339 is one scalar. The five squared shares are 0.0001, 0.0189, 0.0559, 0.6997, and 0.2254. Sessions 4 and 5 together are 0.9251. The first three sessions are 0.0749.

## Plain-language account

Day 2 collapsed five residuals into 16.66 and 96.339. A sum of squares is easy to treat as "the error of the line." Many different five-tuples add to the same number. Five mediocre days and two bad days plus three days almost on the line can produce one total. The total does not say which story you have.

Divide each squared residual by 96.339. Session 1 is 0.0001, not 0. Three decimal places would print 0.000 and turn a tiny positive share into an absence. Session 2 is 0.0189, session 3 is 0.0559, session 4 is 0.6997, session 5 is 0.2254. The first three add to 0.0749. The last two add to 0.9251. Squared loss sits almost entirely on sessions 4 and 5. The early residuals are not zero. They are small enough that, after squaring, they are not the main part of the total.

The result today is not another printing of 96.339. It is the five shares, and the cut 0.9251 against 0.0749.

If someone averages 96.339 across five days, sessions 1 and 4 look equally important. The share table says otherwise: more than nine tenths of squared loss sits on the last two sessions. Collapsing a vector to a scalar, then calling the scalar "typical error," drops the coordinate picture.

Day 2's 0.6997 for session 4 must match π₄ here. Day 8's window RSS values sum over three days only—they are not comparable to this five-day decomposition.

## Core

The residuals are still those of the day-1 line. The sum of squares maps a five-dimensional vector to a scalar:

```text
π_t = r_t² / RSS,    RSS = Σ r_t²
```

`RSS = 96.339`. The shares sum to 1. At four decimals:

| t | r | r² | share |
|---:|---:|---:|---:|
| 1 | 0.12 | 0.0144 | 0.0001 |
| 2 | −1.35 | 1.8225 | 0.0189 |
| 3 | −2.32 | 5.3824 | 0.0559 |
| 4 | 8.21 | 67.4041 | 0.6997 |
| 5 | −4.66 | 21.7156 | 0.2254 |

The session-4 share is the same 0.6997 as the `L2` share on day 2. The session-1 share stays at four decimals. Writing 0 would claim a positive squared residual does not exist. Report both 0.9251 and 0.0749. The largest day alone would hide that session 5 is still more than a fifth of the sum.

A large share says the day is heavy inside squared loss. It does not say the day should be deleted, and it is not a verdict that the day is an outlier. Deleting it moves the whole line. That calculation is day 5. Today only returns the scalar to its coordinates.

| Output | Sees which days matter? |
|---|---|
| RSS = 96.339 alone | no |
| five π_t | yes |
| only π₄ | hides 0.2254 on session 5 |

## Further out

A cross-sectional or time-series mean squared error is the same kind of scalar. A falling training loss can mean most observations moved closer, or it can mean one or two squared residuals collapsed while the rest barely moved. Without the residual vector, the two stories look identical on a report.

A strategy's daily squared error and a factor's residual variance have the same problem when only one number is shown. This table is the small version: five coordinates, one sum, and 0.9251 on the last two days. When a fit "improves," split the sum of squares by time or by name and see which cell moved. A drop that lives in one session is not the same evidence as a drop spread across the sample.

Persist the five residuals—or these shares—as metadata for the full-sample OLS baseline. After deleting session 4 or changing the window, recompute on the new vector; do not rank 22.0417 from day 8 against π₄ here.

Day 9 shuffling intact pairs leaves these shares unchanged. Breaking pairs would change them. Day 7's training RSS 42.05 is a different domain (four fit points).

## What the run showed

```bash
python days/03-residual-vector/residual_vector.py
```

The script should print the shares `0.0001 0.0189 0.0559 0.6997 0.2254`, the sessions 4+5 total `0.9251`, and the first-three total `0.0749`. The implementation is [`residual_vector.py`](../../days/03-residual-vector/residual_vector.py).

This is still in sample. Neither 96.339 nor the shares is a holdout score. Hand in the coordinate split of the sum of squares. Day 4 changes the line inside the same affine class and asks whether `L1` and `L2` rank the two fits the same way. Day 5 deletes session 4 and records how far the line itself moves. The share says the day is heavy. The displacement says how far it moved the line. Those are two statements.
