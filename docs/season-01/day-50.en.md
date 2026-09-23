<p align="center"><a href="day-50.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 50 · A vote of three models

[Phase I · Models](../../README.en.md) · runs

What you learn today: on the later stretch, at the step dated 2024-03-29, the line is wrong, ridge is wrong, the tree is wrong, and the vote is wrong. There are 8 such days. A majority of three wrong directions is still that wrong direction.

## Plain-language account

The three models are fit on the first 59 adjusted closes, as on day 46. The line is ordinary least squares. Ridge uses λ = 20000 on the slope only, with the intercept free. The tree is depth 2, and a child splits only with at least 8 sessions. On the sessions after the cut, each model produces a path of fitted levels. The predicted direction of a step is the sign of the difference between two adjacent fitted levels. The actual direction is the sign of the difference between two adjacent adjusted closes. Different signs mark the step wrong.

The vote is the sign of the sum of the three signs. When the three signs agree, the sign of the sum is their sign, and the majority repeats that direction. When two of the three agree, the majority is that pair's direction. On the step dated 2024-03-29 the line is wrong, ridge is wrong, the tree is wrong, and the vote is wrong. All four flags are true. The three models' signs on this step are not the sign of the actual direction. They agree with each other on the wrong side, so the sign of the sum points to that side, and the vote differs from the actual direction.

On the later stretch, the number of days on which all four flags are wrong is 8. 2024-03-29 is one of those days, the one the script prints, not a day outside the count of 8. The majority did not turn that day's three errors into a correct direction. Three wrong signs that already agree are still that sign when the vote reads them.

The claim stops at this count. On 2024-03-29 all four flags are true. The same pattern occurs on 8 days. The vote is the majority of the three signs. When all three signs are wrong, the majority is the wrong side.

## Core

The direction comparison is on one-step differences along the later stretch, not on the SSE of the price level. Day 46's later SSE is a different column: line 2.9263, ridge 3.2545, tree 2.1488. That column does not decide whether the sign on 2024-03-29 is right. The sign reads a difference. SSE reads a level.

```text
later date = 2024-03-29
line wrong = true
ridge wrong = true
tree wrong = true
vote wrong = true
days all three and the vote are wrong = 8
```

The vote is `sign(sign₁ + sign₂ + sign₃)`. When all three signs equal the opposite of the actual direction, the sum equals three times that opposite sign, the vote's sign matches the three, and the vote is wrong. 8 is the number of such days. The count adds the rows on the later stretch that meet the condition.

Ridge's slope here is not the full-sample 0.0201 from day 42 or day 49. Those days use 79 points. Today's ridge, like the line and the tree, is estimated on the first 59 rows and then differenced on the later stretch. The value of λ is still 20000, still on the slope entry. Do not write 0.0201 into this day's direction.

Four true flags are not the reverse of day 46's statement that the tree has the smallest later SSE. The tree can have later SSE 2.1488, smaller than the line and ridge, and still be wrong on the sign of one step. 2024-03-29 is such a step: the tree is wrong, the other two are wrong, and the vote is wrong. The ranking of sums of squares and the step-by-step signs are two tables.

## Further out

A majority vote has no third answer available when all three members point to the same wrong direction. An odd count keeps the sum from sitting at zero in the usual split, but the direction of the sum is decided by the members. If the members are already wrong together, the majority writes that agreement down again. 8 is how many times that rewriting happens. It does not count how often the vote is right on the other days. Hit counts for the other days are not in this run, and today's page does not fill in a hit rate.

Taking the difference of a level model as a direction keeps the distinction from day 10: a price residual and the sign of the move are not the same score. The label here is the one-step sign of adjusted close on the later stretch. The prediction is the one-step sign of each fitted path. On 2024-03-29 the script does not add a residual for how close the level sat to the close. It gives four wrong flags, all true.

The information set of each estimate stops at the first 59 rows. Directions on the later stretch do not flow back into the slope or the leaves. The vote does not flow back either. It sums three signs that have already been computed. The sum cannot create a sign that none of the three members produced. When the three members produce the wrong sign, the sum produces the wrong sign. That is the case on the 8 days, and it is the case on 2024-03-29.

## What the run showed

```bash
python days/50-vote/vote.py
```

The script should print `later date = 2024-03-29`, with the line, ridge, the tree, and the vote all `true`, and `days all three and the vote are wrong = 8`. The implementation is [`vote.py`](../../days/50-vote/vote.py).

Hand in these 8 days: a majority did not turn three wrong directions into a correct direction. The next lesson changes the feature to the past five daily returns. Today stops at the vote of these three models.
