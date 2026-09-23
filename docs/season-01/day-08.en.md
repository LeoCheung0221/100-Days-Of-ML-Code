<p align="center"><a href="day-08.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 8 · A three-session window

[Phase I · Models](../../README.en.md) · runs

What you learn today: the window slides from `{1, 2, 3}` to `{2, 3, 4}` and the slope moves from 2.0500 to 8.0500, an increase of 6.0000. The two residual sums of squares, 0.0417 and 22.0417, are not a ranking across windows.

## Plain-language account

Once a sample set is fixed, ordinary least squares writes every point in that set into the normal equations. Today the set is cut down to three consecutive sessions and then slid forward once. A session that slides out does not receive a smaller weight. Its weight becomes 0. It no longer contributes to the coefficients.

The first window is sessions 1, 2, and 3, closes 2.1, 3.9, and 6.2. Those three days nearly lie on a line: `ŷ = 2.0500x − 0.0333`, with a sum of squares of only 0.0417. Session 4's close of 20 has not entered the information set, so it neither lifts the slope nor enters this sum of squares.

Slide forward one session. The window is now sessions 2, 3, and 4, closes 3.9, 6.2, and 20.0. Session 1 leaves and session 4 enters. The slope becomes 8.0500, the intercept −14.1167, and the sum of squares 22.0417. The slope increases by 6.0000. The sum of squares is larger because the new trio contains an outlying close and the estimate must minimize the sum of squares on those three days. This is not the same line getting worse. The days inside the sum changed, so the domain of the sum changed.

Session 5 is in neither window and is not used as a score. Today is not the holdout exam of day 7. The object is two window lines, and the change in slope across one slide.

The intercept jump to −14.1167 pairs with slope 8.0500 so the line still passes near session 2's close. Report slope and intercept together.

Day 9 keeps all five sessions and only permutes rows; slopes stay at 3.2700 up to float noise. Today's delta 6.0000 is an information-set effect, not shuffle noise.

## Core

Window `t = 1, 2, 3`:

```text
ŷ = 2.0500x − 0.0333
RSS = 0.0417
```

Window `t = 2, 3, 4`:

```text
ŷ = 8.0500x − 14.1167
RSS = 22.0417
```

| Window | Information set | Slope | RSS |
|---|---|---:|---:|
| Before the slide | {1, 2, 3} | 2.0500 | 0.0417 |
| After the slide | {2, 3, 4} | 8.0500 | 22.0417 |

The difference in slopes is 6.0000. The full-sample slope 3.27 can be read as a compromise among five points. A window estimate is not that line with a discount, and it is not a smaller weight on early prices. A point outside the window has weight 0. The normal equations sum only over rows inside the window. Replacing `{1, 2, 3}` with `{2, 3, 4}` is another call to `lstsq`.

Day 5 removed session 4 from the full sample. Today never put all five sessions into the equation, and the second fit also removes session 1. The pair 0.0417 and 22.0417 shows that the loss changed its domain when the information set changed. It is not a cross-window ranking of the two lines.

| Operation | Sample set | β̂ changes? | Cross-window RSS rank? |
|---|---|---|---|
| Day 8 slide | yes | yes (6.0000) | forbidden |
| Day 9 shuffle | no | no (~0) | same as day 1 RSS |

## Further out

A rolling regression lets coefficients follow a recent sample. A short window gives a new day a large role because an old day is dropped as a whole row. A long window is harder for one arrival and one departure to overturn. Dropping session 1 and admitting session 4 moves the slope from 2.0500 to 8.0500. That is the sensitivity of a short window.

Sensitivity is not accuracy. The two sums of squares are defined on different points, so 22.0417 being larger than 0.0417 does not declare the second line a failure. A common trading mistake ranks in-sample fit across windows and then trades the window with the smallest number. Those numbers do not share a domain. Comparing windows requires the same held-out dates, chosen in advance. Today does not make that comparison. It records which rows entered, which rows left, and that the slope moved by 6.0000.

Hard-cut windows differ from exponential weighting: outside rows contribute zero to `XᵀX`, not small weights. Only one slide is in scope; sliding further to `{3,4,5}` is a different experiment.

## What the run showed

```bash
python days/08-three-day-window/three_day_window.py
```

The script should print `y = 2.0500 x + -0.0333`, the slope `8.0500` after the slide, and `delta slope = 6.0000`. The implementation is [`three_day_window.py`](../../days/08-three-day-window/three_day_window.py).

Hand in one change of information set and the change in slope. The two sums of squares are not a ranking. Day 9 keeps the set fixed and only shuffles the order of the five rows, to see whether batch least squares follows row order.

Self-check: delta slope 6.0000? Both windows named? RSS not used as a leaderboard? Session 5 excluded from both windows?
