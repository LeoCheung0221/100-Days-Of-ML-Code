<p align="center"><a href="day-13.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 13 · Threshold sensitivity

[Phase I · Models](../../README.en.md) · runs

What you learn today: the thresholds 0.50, 0.70, and 0.90 give constant-up accuracies 0.75, 0.50, and 0.25. The threshold rises by 0.40 and the accuracy falls by 0.50. Reporting one accuracy hides which cut it used.

## Plain-language account

The four returns are still 0.8571, 0.5897, 2.2258, and −0.4800. The prediction is still 1 on every step. Today only the horizontal line moves, and its height takes three values: 0.50, 0.70, and 0.90.

Draw the line at 0.50. The returns 0.8571, 0.5897, and 2.2258 sit above it, and −0.4800 sits below it. The labels are 1 1 1 0. Always-up hits the first three steps. The accuracy is 0.75.

Draw the line at 0.70. The return 0.5897 falls below the line, and the labels become 1 0 1 0. Always-up hits the first and the third step. The accuracy is 0.50. That is the single number from day 12.

Draw the line at 0.90. The return 0.8571 also falls below the line, and only 2.2258 remains above it. The labels are 0 0 1 0. Always-up hits only the third step. The accuracy is 0.25.

From 0.50 to 0.90 the threshold rises by 0.40. The accuracy goes from 0.75 to 0.25 and falls by 0.50. None of the four predicted 1s changed. The fall comes from fewer 1s in the label: first 0.5897 is not high enough, then 0.8571 is not high enough either. The return 2.2258 is above the line at all three heights. The return −0.4800 is below the line at all three heights. The two middle positive returns decide how the table moves.

A result that says only "accuracy 0.50" does not say that the line was drawn at 0.70 rather than at 0.50 or at 0.90. The same prediction, with a different line, can score 0.75 or 0.25. The isolated 0.50 hides the cut.

## Core

The prediction is fixed at all 1s. The label is `1{r > τ}`, with τ equal to 0.50, 0.70, and 0.90. Accuracy is the share of steps on which the prediction equals the label.

| threshold | returns above the threshold | labels | constant-up accuracy |
|---:|---|---|---:|
| 0.50 | 0.8571, 0.5897, 2.2258 | 1 1 1 0 | 0.75 |
| 0.70 | 0.8571, 2.2258 | 1 0 1 0 | 0.50 |
| 0.90 | 2.2258 | 0 0 1 0 | 0.25 |

The return 0.5897 satisfies `0.50 < 0.5897 < 0.70`, so it is a 1 only in the first row. The return 0.8571 satisfies `0.70 < 0.8571 < 0.90`, so it is a 1 in the first two rows and a 0 in the third. The return 2.2258 is greater than 0.90, so it is a 1 in all three rows. The return −0.4800 is less than 0.50, so it is a 0 in all three rows.

Two differences are the scale of the table:

```text
0.90 − 0.50 = 0.40
0.75 − 0.25 = 0.50
```

The threshold rises by 0.40, and the constant-up accuracy falls by 0.50. This is not an estimated regression slope. It is the difference of the endpoints on a table that has already been computed. The middle row, 0.70, corresponds to 0.50, so the change passes through the middle cut: each step up in the threshold turns one positive return from 1 to 0, and the accuracy falls by 0.25, because changing one class out of four steps is 1/4.

A report therefore carries τ. An accuracy of 0.75 written without the threshold 0.50 sits on top of the always-up accuracy on the sign labels. On this row the digits do match that 0.75, and the match holds when the cut is 0.50 and 0.5897 is still above the cut. An accuracy of 0.25 written without 0.90 looks like a change in the rule. The rule is unchanged. It is still four 1s. What changed is what counts as up.

## Further out

The sensitivity here is the sensitivity of the label definition. The prediction has no parameter to estimate. The four 1s are a constant written down in advance. The object that moves is the truncation point inside the target. Move that point from 0.50 to 0.70 and then to 0.90, and the number of positive labels goes from three to two and then to one. The hit rate goes from 0.75 to 0.50 and then to 0.25.

The table stops a single number from being carried off alone. The accuracy 0.50 holds only on the row τ = 0.70. Lift it out and make it a title, and the title has lost the row that produced it. A later label built at another threshold, compared with this 0.50, compares two definitions. The prediction is the same on all three rows.

Which side of each cut the four returns occupy decides the shape of the table. Accuracy falls as the threshold rises because always-up calls every row a 1, and a higher threshold turns some of those 1s off. The steps that turn off go from hits to misses. If the prediction were not all 1s, a row changing from 1 to 0 could add a hit. Today the prediction stays fixed, so the direction of the three rows is plain: a higher cut, fewer positive labels, fewer hits for the all-1s rule. The fall of 0.50 is the endpoint gap of this one experiment, and a citation of it includes the rise of 0.40.

Handing in one accuracy is taking one of the three rows and erasing the threshold. After the erasure, 0.75, 0.50, and 0.25 cannot be told apart. The cut has to remain beside the result.

Of the four returns, the ones that change side across these three cuts are 0.5897 and 0.8571. The return 2.2258 is above 0.90, and −0.4800 is below 0.50, so those two steps keep their class on all three rows. The accuracy move from 0.75 to 0.50 is 0.5897 leaving the positive class. The move from 0.50 to 0.25 is 0.8571 leaving it. Each step down has one return that can be named. The four steps do not change sign together. Write the list of returns next to the threshold and the accuracy, and 0.75, 0.50, and 0.25 each correspond to one stated cut.

Three rows, one prediction vector, three accuracies 0.75/0.50/0.25. Endpoints differ by 0.50 while τ moves 0.40—that is discrete class counts changing, not a tuned model. Never publish 0.50 without naming the τ=0.70 row it came from.

2.2258 stays positive on all three rows; −0.4800 stays negative. Sensitivity is entirely from 0.5897 and 0.8571 crossing cut lines as τ rises.
Endpoint spread 0.75 vs 0.25 with τ spread 0.40 is about class counts under a fixed always-up prediction—not a learned slope.
The three τ rows are enumerated upfront, not tuned to maximize accuracy. Document all three when citing any single row's accuracy.
## What the run showed

```bash
python days/13-threshold-sensitivity/sensitivity.py
```

The script prints the constant-up accuracies 0.75, 0.50, and 0.25 at the thresholds 0.50, 0.70, and 0.90. The implementation is [`sensitivity.py`](../../days/13-threshold-sensitivity/sensitivity.py).

The three accuracies come from one constant prediction and one series of returns. The threshold rises from 0.50 to 0.90, a rise of 0.40, and the accuracy falls from 0.75 to 0.25, a fall of 0.50. A single accuracy hides the cut it used.

