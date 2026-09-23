<p align="center"><a href="day-07.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 7 · Hold out session 5

[Phase I · Models](../../README.en.md) · runs

What you learn today: the fit uses only the first four sessions. The line at session 5 is 22.05, residual −11.65. The nearest neighbor copies session 4's 20.0, residual −9.6. The training residual sum of squares 42.05 may be printed. It is not the score.

## Plain-language account

Day 6 had no label on session 6, so nothing could be scored. Today a label is available, under a rule: the close 10.4 does not enter the normal equations and does not enter the neighbor's candidates. The fit sees only `(1, 2.1)`, `(2, 3.9)`, `(3, 6.2)`, and `(4, 20.0)`. The only exam is session 5.

Among those four points, the close 20 is heavy. It lifts the line to `ŷ = 5.60x − 5.95`. At session 5 that is 22.05. The residual `10.4 − 22.05` is −11.65. The neighbor's nearest training abscissa to 5 is 4, whose label is 20.0, so its residual is −9.6. On this one held-out point the neighbor's absolute error is smaller.

That one comparison does not become "the neighbor is the better class." A neighbor can show a zero residual on a training point because it copies the label. The line's residual sum of squares on the first four sessions is 42.05. The number may be printed so the tightness on the training stretch is visible. It is not the score. The score is only the residual on session 5. Treating a drop in 42.05 as improvement grades points the fit has already seen.

Both estimators overshoot: negative residuals mean predictions above 10.4. The line overshoots more on this single point; that is not yet a class ranking.

Holdout is not the same as day 5's deletion diagnostic: session 4 still enters today's fit. Day 8's windows never score session 5.

## Core

```text
fit: (1, 2.1), (2, 3.9), (3, 6.2), (4, 20.0)
exam: (5, 10.4)
```

Ordinary least squares on the first four sessions is `ŷ = 5.60x − 5.95`. The training residual sum of squares is 42.05 and does not count today.

| Estimator | Value at x = 5 | Holdout residual |
|---|---:|---:|
| Nearest neighbor, copy of t = 4 | 20.0 | −9.6 |
| Ordinary least squares | 22.05 | −11.65 |

Both residuals are `10.4` minus the estimate. A negative sign means the estimate is above the close. The absolute error 9.6 is smaller than 11.65 only on this one point. It does not say the neighbor will be closer on another held-out point, and it does not say the neighbor should replace the line. Comparing classes needs a scoring point chosen in advance and enough repetition. Today there is one scoring point.

Session 5 lies outside the support `[1, 4]` of the fit, so the line's step is also an extrapolation. That is not the same as tomorrow's window. Tomorrow changes the length of the information set. Today changes which point is allowed into the loss.

| Contrast | Day 6 x = 6 | Day 7 x = 5 |
|---|---|---|
| Label | none | 10.4 |
| Score | none | −9.6 / −11.65 |
| Training RSS as score | — | no (42.05) |

## Further out

"Out of sample" is often attached to a falling training loss. A falling training loss only says the function moved closer to labels that already entered the loss. A holdout needs two things: the label at the scoring point does not enter the estimate, and the point was marked before the result was seen. Session 5 was set aside as the last day in advance. It was not picked as the worst residual after all five were inspected.

In a backtest, tuning on the whole sample and then reporting a Sharpe ratio on that same sample is the move that treats 42.05 as the score. The matching report estimates parameters on an earlier stretch and records the later residual alone. With one later day, the conclusion stays on that day. −9.6 and −11.65 are the two residuals on that day. They are not "the neighbor beat the regression." A smaller absolute error on one point is not yet a ranking of classes.

Do not cherry-pick which day to hold out after seeing residuals. Day 26 extends holdout to many rows; day 37's pooled splits are a different leakage class.

## What the run showed

```bash
python days/07-holdout-day-5/holdout_day5.py
```

The script should print training `RSS = 42.05` and mark it as not the score, then the holdout residuals `-9.6` and `-11.65`. The implementation is [`holdout_day5.py`](../../days/07-holdout-day-5/holdout_day5.py).

Hand in the holdout residuals, not the training sum of squares. The neighbor's smaller absolute error on this one point stays in the table and is not promoted to a ranking of classes. Day 8 uses a three-session window, slides it once, and watches the slope follow the information set. That is not another holdout exam.

Self-check: script says training RSS is not the score? Signed residuals reported? 22.05 not confused with full-sample fit at session 5?
