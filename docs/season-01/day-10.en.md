<p align="center"><a href="day-10.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 10 · Up or down

[Phase I · Models](../../README.en.md) · runs

The losses of the first nine days act on the price level, `y_t − ŷ_t`. The other number a fill has to meet is direction: whether the close rose or fell from the previous session. Both functionals use the same line. Their rankings need not agree.

Today still uses the full-sample line `ŷ = 3.27x − 1.29`. No classifier is introduced. Direction is read off the one-day difference of this affine function.

---

## Level residuals and the one-day difference

An affine fit in time has a constant slope, so the one-step difference of the fitted path is the same constant:

```text
Δŷ_t = ŷ_t − ŷ_{t−1} = β₁ = 3.27,    t = 2, 3, 4, 5
```

The realized difference `Δy_t = y_t − y_{t−1}` is not constant. A hit means `sign(Δy_t) = sign(Δŷ_t)`.

| t | y | ŷ | r | Δy | Δŷ | Hit |
|---:|---:|---:|---:|---:|---:|---:|
| 2 | 3.9 | 5.25 | −1.35 | 1.8 | 3.27 | 1 |
| 3 | 6.2 | 8.52 | −2.32 | 2.3 | 3.27 | 1 |
| 4 | 20.0 | 11.79 | 8.21 | 13.8 | 3.27 | 1 |
| 5 | 10.4 | 15.06 | −4.66 | −9.6 | 3.27 | 0 |

Three of the four steps hit. The only decline is session 5. The fitted difference is positive on every step, so the direction on session 5 is wrong by construction.

The absolute residual on session 4 is **8.21**, and the direction hits. The absolute residual on session 5 is **4.66**, smaller than on session 4, and the direction misses. The session with the smaller price loss has the wrong sign. Handing in only `L1`, or only the hit count, hides the other column.

---

## Three out of four does not recognize a path

When `β₁ > 0`, `sign(Δŷ_t)` equals `+1` at every `t`. The direction rule collapses to "call every step an up move." The first three steps in the sample did rise, so any affine fit with a positive slope hits those three steps. The count 3/4 does not use the shape of the path beyond the price residuals. It uses the sign of the slope, and that sign is a byproduct of least squares on the level.

On session 5, `Δy = −9.6` and `Δŷ = 3.27` have opposite signs. The level residual −4.66 says only that the fitted value 15.06 lies above the close 10.4. It does not say that the step's direction was called correctly. Direction is a property of the difference, not of the level.

What is handed in is therefore two columns: the level residual on each session, and the direction hit from session 2 onward. The ratio 3/4 is not an accuracy that can be carried off by itself.

---

## Reproduce

```bash
python days/10-direction/direction.py
```

The script should print `fitted one-day move = 3.27 on every step`, `direction hits = 3 / 4`, a session-4 absolute residual of `8.21` with a hit, and a session-5 absolute residual of `4.66` with a miss. The implementation is [`direction.py`](../../days/10-direction/direction.py).

---

## What this day is not

Direction is not yet the target of estimation. The line is still least squares on the price level, and the sign is read off afterwards. The next session turns the move into a label and stops accepting a distance such as 8.21 as the loss on that label. A directional hit on a holdout is not reported today either. The hits in the table are the full-sample fit scoring its own path, the same kind of object as the training `RSS` that day 7 refused to count.
