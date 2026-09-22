<p align="center"><a href="day-03.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 3 · The five residuals, side by side

[Phase I · Models](../../README.en.md) · runs

`L2 = 96.339` is a scalar. The residual is a vector in five coordinates. The sum of squares is a many-to-one map from that vector to a scalar: the same sum can come from entirely different coordinates. Today the sum is opened, and the session that holds the squared loss is named.

---

## Shares

The line is still `ŷ = 3.27x − 1.29`. The share of session `t` in the residual sum of squares is

```text
π_t = r_t² / RSS,    RSS = Σ r_t²
```

| t | r | r² | π |
|---:|---:|---:|---:|
| 1 | 0.12 | 0.0144 | 0.0001 |
| 2 | −1.35 | 1.8225 | 0.0189 |
| 3 | −2.32 | 5.3824 | 0.0559 |
| **4** | **8.21** | **67.4041** | **0.6997** |
| 5 | −4.66 | 21.7156 | 0.2254 |

Sessions 4 and 5 together are **0.9251**. The first three sessions together are **0.0749**. The largest squared residual is at `t = 4`.

Reporting 96.339 alone lets a reader treat the first three sessions, under a tenth of the loss, as the same kind of fit as the last two. Once the vector is on the page, the concentration is computed.

---

## A scalar does not keep the coordinates

The level set of `r ↦ Σ r_t²` is a sphere. Points on that sphere share an `RSS` and need not share an `argmax`. The scalar is therefore not a substitute for the residual table. Day 2 required the absolute sum and the squared sum together. Today the squared sum itself has to be indexed by session.

Shares are printed to four decimals. The share on session 1 is 0.0001, not 0. Printing it as 0 would turn a small positive contribution into an absence.

The sign stays. Session 4 is positive and session 5 is negative. A squared share cannot show that. What is reported side by side is the signed `r_t` and the `π_t` computed from it, not another collapsed total.

---

## Reproduce

```bash
python days/03-residual-vector/residual_vector.py
```

The script should print `RSS = 96.339`, a session-4 share of `0.6997`, a combined share of `0.9251` for sessions 4 and 5, and `0.0749` for the first three. The implementation is [`residual_vector.py`](../../days/03-residual-vector/residual_vector.py).

---

## What this day is not

This is a decomposition of one in-sample fit. It is not a second line, and it is not a holdout score. Knowing that the loss sits on session 4 does not say how far the line moves once that point is deleted. That is day 5. Day 4 first brings in an affine competitor that does not minimize `RSS`.
