<p align="center"><a href="day-08.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 8 · A three-day window

[Phase I · Models](../../README.en.md) · runs

The ordinary least squares fits of the first seven days, once the sample set is fixed, write every abscissa in that set into the normal equations. Today the set is cut down to three consecutive sessions and then slid forward once. After the slide, an earlier price is absent from the equations, so it no longer contributes to the coefficients.

This is not the holdout of day 7. Session 5 is in neither window, and it is not scored. The objects today are the two window lines, and the change in slope across one slide.

---

## Two fits

On `t = 1, 2, 3`, with closes `2.1, 3.9, 6.2`:

```text
ŷ = 2.0500x − 0.0333
RSS = 0.0417
```

The first three sessions are nearly collinear. The close at 20 has not entered the information set, so it neither lifts the slope nor enters this `RSS`.

Slide forward once. The window is now `t = 2, 3, 4`, with closes `3.9, 6.2, 20.0`:

```text
ŷ = 8.0500x − 14.1167
RSS = 22.0417
```

Session 1 leaves the information set. Session 4 enters. The slope rises by **6.0000**. The sum of squares rises from 0.0417 to 22.0417 because the new set contains the pulled-up close, and the fit has to minimize squared error on these three sessions.

| Window | Information set | Slope | RSS |
|---|---|---:|---:|
| Before the slide | {1, 2, 3} | 2.0500 | 0.0417 |
| After the slide | {2, 3, 4} | 8.0500 | 22.0417 |

---

## What is dropped is a row, not a soft weight

The full-sample slope 3.27 can be read as a compromise among five points. A window fit is not a discount on that line, and it is not a smaller weight on early prices. A point outside the window has weight 0. The sum in the normal equations runs only over the rows inside the window.

A slide is therefore not a second report of the same `β̂`. Replacing `{1, 2, 3}` with `{2, 3, 4}` is another call to `lstsq`. Day 5 deleted session 4 from the full sample. Today the five sessions are never in the equation together, and the second fit drops session 1 as well.

The two residual sums of squares are not a ranking across windows. The sums run over different samples, so they are not the same functional. Putting 0.0417 next to 22.0417 shows that the loss changed its domain when the information set changed. It does not crown one window over the other.

---

## Reproduce

```bash
python days/08-three-day-window/three_day_window.py
```

The script should print `y = 2.0500 x + -0.0333`, then `y = 8.0500 x + -14.1167`, and `delta slope = 6.0000`. The implementation is [`three_day_window.py`](../../days/08-three-day-window/three_day_window.py).

---

## What this day is not

The window is selected by three consecutive calendar sessions. Permuting the row order of the table, while keeping each pair `(x_t, y_t)` intact, does not change a window that is keyed by `t`. The next day does that permutation on purpose: the rows are reordered, the pairs stay intact, and the batch OLS coefficients and `RSS` do not move. What fails to move is the presentation order, not the calendar coordinate.
