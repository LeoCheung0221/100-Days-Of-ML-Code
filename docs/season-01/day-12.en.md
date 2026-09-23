<p align="center"><a href="day-12.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 12 · A threshold on the return

[Phase I · Models](../../README.en.md) · runs

What you learn today: the four returns 0.8571, 0.5897, 2.2258, and −0.4800, cut at the threshold 0.70, give the labels 1 0 1 0. The same always-up rule scores 0.50. On day 11 that same rule against the sign labels scored 0.75. The cut is part of the definition.

## Plain-language account

Write the four returns in time order: 0.8571, 0.5897, 2.2258, −0.4800. Draw a horizontal line at height 0.70. The value 0.8571 sits above the line, 0.5897 sits below it, 2.2258 sits above it, and −0.4800 sits below it. Above the line write 1. Below the line write 0. The four labels are 1 0 1 0.

Always-up does not read these four numbers. It hands in 1 on every step. Against 1 0 1 0 it hits the first step, misses the second, hits the third, and misses the fourth. Two of four steps hit. The accuracy is 0.50.

Take the same always-up rule to the sign labels of day 11. A sign asks only whether the return is positive. The returns 0.8571, 0.5897, and 2.2258 are positive, and −0.4800 is negative, so the sign labels are 1 1 1 0. Always-up against those four signs hits three steps. The accuracy is 0.75. The prediction used both times is identical: 1 1 1 1. What changes is the label. The step that changes is the second one. The return 0.5897 is greater than 0, so the sign records it as up. The return 0.5897 is less than 0.70, so the threshold 0.70 records it as 0. The prediction does not change its call. That step goes from a hit to a miss, and the accuracy goes from 0.75 to 0.50.

The value 0.70 therefore sits inside the target, not in a note attached after the score. It decides which class receives 0.5897. Drop the threshold from the definition and report only "up accuracy 0.50," and the second step cannot be rebuilt as up or as not up. The definition of the label has to carry this cut.

## Core

A simple return is the difference of neighboring closes divided by the earlier close. The four numbers are given, and the threshold is given:

```text
r = 0.8571, 0.5897, 2.2258, −0.4800
τ = 0.70
label = 1{r > 0.70}
```

| step | return | return > 0 | return > 0.70 |
|---:|---:|---:|---:|
| 1 | 0.8571 | 1 | 1 |
| 2 | 0.5897 | 1 | 0 |
| 3 | 2.2258 | 1 | 1 |
| 4 | −0.4800 | 0 | 0 |

The right column is today's label: 1 0 1 0. The middle column is the sign label of day 11: 1 1 1 0. The columns differ only in the second row, because only 0.5897 falls between 0 and 0.70. The numerator of the accuracy 0.50 is the two 1s in the right column, the returns 0.8571 and 2.2258. The denominator is four steps, and 2/4 written to two decimals is 0.50. The day-11 accuracy 0.75 is 3/4. The extra step is exactly the 0.5897 that 0.70 excludes. The numerators differ by one step because the definition gained a threshold, not because the prediction gained a different sign.

The always-up prediction is a vector of four 1s. Against the right column the hits are row 1 and row 3, and the accuracy is 0.50. Against the middle column the hits are the first three rows, and the accuracy is 0.75. One prediction, two label sets, two accuracies. When 0.50 is reported, 0.70 and the comparison "strictly greater" are reported with it. Replacing the comparison with greater-or-equal, or replacing 0.70 with another number, replaces the target. Today uses strictly greater than 0.70.

The day-11 accuracy 0.75 came from a positive slope, and a positive slope's direction rule is exactly always-up. Today does not estimate a slope. The prediction is fixed at the constant 1, so that the label definition is exposed: move the cut, and the accuracy moves. The value 0.50 is this constant's hit rate on the threshold labels. It is not the slope of a new line, and it is not the day-4 residual 8.21.

## Further out

A classification target is often described as "up or down," as if the sign were a column already sitting in the data. A return is a real number. Between the real number and the pair {0, 1} there is one truncation. Once the truncation point is written into the definition, it belongs to the target in the same way the return does. Two records can use the same closes and the same always-up rule, one with the sign and one with 0.70, and obtain 0.75 and 0.50. The difference is which side of the cut receives the second-step return 0.5897.

When a note says the rule is right on half the steps, the half is the two 1s inside 1 0 1 0. Those two 1s are 0.8571 and 2.2258. The step 0.5897 is also a rise in price, and it does not clear 0.70. Under today's definition it is 0, and always-up is wrong on that step. If the rise that should be caught includes 0.5897, today's label is a different target, and 0.50 does not describe that target. The cut is part of the definition.

The threshold can still move. The value 0.70 is one cut. Raise it or lower it and the number of 1s changes, and the always-up accuracy changes with it. The next table records that movement: one constant rule, three thresholds, three accuracies. Today fixes one fact first: the number 0.50 contains 0.70 inside its definition.

## What the run showed

```bash
python days/12-threshold/threshold.py
```

The script prints the threshold 0.70, the four returns 0.8571, 0.5897, 2.2258, and −0.4800, the labels 1 0 1 0, and `constant-up accuracy = 0.50`. The implementation is [`threshold.py`](../../days/12-threshold/threshold.py).

The prediction is still up on every step. On day 11 this same rule against the sign labels scored 0.75. Today, against the labels cut at 0.70, it scores 0.50. What changes is the class of the step whose return is 0.5897. A citation of 0.50 writes 0.70 in the same definition.
