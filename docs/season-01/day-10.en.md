<p align="center"><a href="day-10.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 10 · Direction of the move

[Phase I · Models](../../README.en.md) · runs

What you learn today: the one-day change in the same line is 3.27 on every step, and the direction hits are 3/4. Session 4 has absolute residual 8.21 and a hit. Session 5 has absolute residual 4.66 and a miss. Because the slope is positive, 3/4 is the rule "call up on every step."

## Plain-language account

The losses of the first nine days act on the price level. They ask how far the close sits from the line. A trade also has to report another number: relative to the previous close, was the move up or down. Both questions use the line `ŷ = 3.27x − 1.29`. Today does not build a new classifier. Direction is read from the one-day difference of this line.

The slope is constant, so the fitted path rises by 3.27 on every step. The closes do not. From 2.1 to 3.9 the rise is 1.8; then 2.3; then 13.8; then a fall of 9.6. The first three actual moves are up and the fit is up, so those are hits. The fifth actual move is down and the fit is still up, so that is a miss. Three of four steps hit.

Session 4's absolute residual is 8.21, the largest level error of the five days, and the direction is right. Session 5's absolute residual is 4.66, smaller than session 4, and the direction is wrong. The day that sits closer in price can be the day whose direction is wrong. Reporting only absolute loss hides the direction error on session 5. Reporting only 3/4 hides the long vertical gap on session 4.

## Core

```text
Δŷ_t = ŷ_t − ŷ_{t−1} = β₁ = 3.27,    t = 2, 3, 4, 5
```

The actual difference `Δy_t = y_t − y_{t−1}` is not constant. A hit means `sign(Δy_t) = sign(Δŷ_t)`.

| t | y | ŷ | r | Δy | Δŷ | hit |
|---:|---:|---:|---:|---:|---:|---:|
| 2 | 3.9 | 5.25 | −1.35 | 1.8 | 3.27 | 1 |
| 3 | 6.2 | 8.52 | −2.32 | 2.3 | 3.27 | 1 |
| 4 | 20.0 | 11.79 | 8.21 | 13.8 | 3.27 | 1 |
| 5 | 10.4 | 15.06 | −4.66 | −9.6 | 3.27 | 0 |

When `β₁ > 0`, `sign(Δŷ_t)` is positive on every step. The direction rule collapses to "call up every time." The first three steps in the sample do rise, so any affine fit with a positive slope hits those three steps. The score 3/4 does not recognize a path beyond the price residuals. It uses the sign of the slope, and that sign is a byproduct of least squares on the level.

On session 5, `Δy = −9.6` and `Δŷ = 3.27` have opposite signs. The level residual −4.66 only says the fitted value 15.06 is above the close 10.4. It does not say the direction of the step was called correctly. Direction looks at the difference, not at the level. Today therefore hands in two columns: the level residual on each day, and the direction hit from session 2 onward. The 3/4 cannot be carried off alone as an accuracy that has already been compared with a baseline. The chapter that never looks at price and always calls up is day 14. Today needs one sentence: because the slope is positive, 3/4 and always-up are the same rule.

## Further out

The loss of a price model and the loss of a trading decision are often different functionals. A regression minimizes squared level residuals. An order looks at the sign of the next move. A fit that is closer in mean square can be worse on sign, and a rule with a high hit rate can sit far from the price. Sessions 4 and 5 are the small example: 8.21 with a hit, 4.66 with a miss.

A direction accuracy means something only next to a baseline. When the sign of the fitted difference is constant, the accuracy equals the accuracy of "always call that sign." The model has not used the shape of the path. A later direction model that reports seventy-five percent should be checked for a prediction sign that is the same every day. If it is the same, the number is the hit rate of a constant rule, and the constant rule belongs beside it. Today does not unfold that baseline table. It puts the level residual and the direction hit in one table, so the two columns cannot stand in for each other.

Day 9 row-order invariance guarantees the same `β̂` feeds today's constant `Δŷ = 3.27`. Do not swap in the day-8 window slope 8.0500—that changes the sample set, not the scoring functional. Affine structure means `Δŷ_t = β₁` for every step; magnitude mismatches like 13.8 vs 3.27 do not enter the hit bit.

When reporting, sort by `|r|` and sort by direction hits give different rankings—session 5 can look "closer" yet miss direction. Keep both columns visible through day 11 and again on day 25 with returns. The 3/4 here is in-sample on the fitted path, not an out-of-sample directional forecast.

Hand in: positive slope ⇒ constant predicted up moves; 8.21 hit vs 4.66 miss; level and direction are not interchangeable. Re-run checks: four identical `Δŷ`, three hits, script strings unchanged.
Keep the prefix "in-sample after full fit" when citing 3/4. Level RSS and direction hits answer different functionals; session 5's smaller |r| with a miss is the canonical warning. Script strings and table numbers are the source of truth for hand-ins.
Re-read the chain: level OLS fixes β₁, affine diffs fix Δŷ, signs define hits. Common exam mistakes confuse 3.27 with a return threshold or 8.21 with a direction penalty—keep the table columns separate in notes and slides.
## What the run showed

```bash
python days/10-direction/direction.py
```

The script should print `fitted one-day move = 3.27 on every step`, `direction hits = 3 / 4`, a hit with absolute residual `8.21` on session 4, and a miss with absolute residual `4.66` on session 5. The implementation is [`direction.py`](../../days/10-direction/direction.py).

The line is still least squares on the price level. Direction is read off afterwards. The hits in the table are the full-sample fit scoring its own path, the same kind of object as the training sum of squares that did not count on day 7: the labels already entered the estimate. From day 11 the score becomes the direction hit, and 8.21 is explicitly no longer the score.

