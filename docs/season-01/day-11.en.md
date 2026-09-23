<p align="center"><a href="day-11.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 11 · Direction labels

[Phase I · Models](../../README.en.md) · runs

What you learn today: the score is direction hits 3/4. The day-4 absolute price residual is 8.21, and that residual is not the score. The day-5 absolute residual is 4.66 and the direction misses. The slope is positive, so 3/4 is the rule that calls up on every step.

## Plain-language account

The five closes are still 2.1, 3.9, 6.2, 20.0, and 10.4, and the line through them is still `ŷ = 3.27x − 1.29`. Direction does not read the vertical distance from a close to the line. It reads which of two neighboring days is higher. Subtracting consecutive closes gives the four actual moves 1.8, 2.3, 13.8, and −9.6. The first three steps rise. The fifth step falls from 20.0 to 10.4.

The slope of this line is a positive constant. The one-day change of an affine path equals the slope, so every fitted move is 3.27 and every fitted move points up. The signs of 1.8, 2.3, and 13.8 agree with 3.27. The sign of −9.6 does not. Three of the four steps hit. The score is 3/4.

The absolute price residuals sit on the same rows. On day 4 the close 20.0 is 8.21 away from the line, the large gap on the price axis, and the direction still hits: the price rose and the line rose. On day 5 the close is 4.66 away from the line, shorter than 8.21, and the direction misses: the price fell and the line kept rising. The day that sits closer in price can be the day whose direction is wrong. From today the column that is handed in is 3/4. The value 8.21 stays in the price-residual column. It measures how far the day-4 close sits from the line, and it is not the score. The value 4.66 stays in that same column. It measures the day-5 distance, and it does not turn the day-5 direction into a hit.

The sign of the slope does not change from step to step. The direction rule never reads the size of the move. It reads that positive sign, and the positive sign means: call up on every step. Three of the four steps did rise, so calling up on every step scores 3/4. The score uses the sign of the slope, and that sign is a byproduct of least squares on the level. The chapter that never looks at price and writes always-up as its own control is day 14. Today needs that one sentence, and it does not unfold the baseline table.

## Core

The score is the direction hit. The price distance is kept, and it does not enter the score.

```text
score = direction hits 3/4
day 4 absolute price residual = 8.21
that residual is not the score
day 5 absolute residual = 4.66, direction miss
```

```text
Δŷ_t = ŷ_t − ŷ_{t−1} = 3.27,    t = 2, 3, 4, 5
```

A hit means `sign(Δy_t) = sign(Δŷ_t)`. When `β₁ > 0`, the right-hand side is positive on every step, and the direction rule is the same rule as "call up on every step."

| t | close | Δy | Δŷ | absolute price residual | direction hit |
|---:|---:|---:|---:|---:|---:|
| 2 | 3.9 | 1.8 | 3.27 | 1.35 | 1 |
| 3 | 6.2 | 2.3 | 3.27 | 2.32 | 1 |
| 4 | 20.0 | 13.8 | 3.27 | 8.21 | 1 |
| 5 | 10.4 | −9.6 | 3.27 | 4.66 | 0 |

Day 4 contributes a 1 to the numerator of the score and contributes 8.21 to the price column. Day 5 contributes a 0 to the numerator and contributes 4.66 to the price column. On absolute residual, 4.66 is smaller than 8.21. On direction, day 5 is the only miss. The two columns answer two questions: how far the close sits from `ŷ = 3.27x − 1.29`, and whether the signs of the differences agree. The score 3/4 is the number of agreements in the second column, divided by four steps. Putting 8.21 or 4.66 into the score column copies the answer of the distance question into the sign question.

The line is estimated on all five closes, and the four direction labels are the differences of those same closes. The 3/4 is the sign count of this already fitted line on the same sample. It answers how many steps the positive slope covers. It does not answer what a rule would score before it had seen day 5. Because the slope is positive, the direction hit 3/4 and the rule that calls up on every step are the same rule, and 8.21 is not that rule's score.

## Further out

A research note often keeps a single direction hit rate. Before reading that number, check whether the predicted sign is constant. If the predicted sign is the same every day, the hit rate is the share of the current labels that match "always call this sign." The rule has not changed its call with the shape of the path. The shape is in the differences: the fourth actual move is 13.8, the fifth is −9.6, and the fitted move is 3.27 on both steps. The size never enters the direction rule. Writing the slope as 3.27 or as any other positive number leaves the four direction cells unchanged. What changes the direction table is the sign of the slope, or the definition of the label.

A price model and a direction label use different coordinates. Squared loss penalizes the level residual. A direction record looks at the sign of the next step. Day 4 shows that an absolute residual of 8.21 can sit next to a hit. Day 5 shows that an absolute residual of 4.66 can sit next to a miss. When this fit is cited later, 8.21, 4.66, and 3/4 stay in separate columns. Distance does not underwrite the sign count, and the sign count does not underwrite the distance.

The number of up steps in the sample itself raises the hit rate of "call up on every step." With three rises and one fall, any affine fit with a positive slope scores the same 3/4 on direction, as long as its one-day difference stays positive. The next change of definition starts on day 12: a return is compared with a threshold that is written into the label, and the sign by itself is no longer the label. Day 14 is the chapter that writes the constant rule, the rule that looks at no price, as the control. Today's score column changes definition first: the direction hit enters the score, and the absolute price residual leaves it.

Today changes the score column, not the line. `8.21` stays a level residual and is explicitly not the score; `3/4` is. That reporting split persists when threshold labels arrive on day 12 and when sigmoid scores arrive on day 16–17.

Because `β₁ > 0`, the direction rule coincides with always-up on symbol labels—the same 3/4 as day 14's 0.75 benchmark, but here the slope was estimated from prices. Full-sample fit then full-sample direction counts mirror day 7's warning about training objects that already saw the labels.

Verify `labels.py` against day 10's table; anchor words: `not the score`, 8.21, 4.66, 3/4.
Score column vs diagnostic column: 3/4 vs 8.21/4.66. The stdout line `not the score` is part of the specification—do not drop it in slides. Threshold days change labels, not this fitted line.
Treat `not the score` as part of the spec alongside 3/4. Changing metrics without refitting is deliberate pedagogy for later train vs holdout splits and for day-25's two-score report.
## What the run showed

```bash
python days/11-direction-labels/labels.py
```

The script prints `score = direction hits 3/4` and `day 4 absolute price residual = 8.21`, and it states that this residual is not the score. The day-5 absolute residual is 4.66, and the direction misses. The implementation is [`labels.py`](../../days/11-direction-labels/labels.py).

The line is still `ŷ = 3.27x − 1.29` on the five closes. What changes today is the score column: the direction hit 3/4 enters the score, and 8.21 leaves it. Because the slope is positive, the printed 3/4 is the rule that calls up on every step.

