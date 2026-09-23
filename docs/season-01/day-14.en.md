<p align="center"><a href="day-14.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 14 · Constant baselines

[Phase I · Models](../../README.en.md) · runs

What you learn today: on the sign labels, always-down accuracy is 0.25 and always-up accuracy is 0.75. The baseline looks at no price. A 0.75 with no 0.25 beside it has no control.

## Plain-language account

The four returns are still 0.8571, 0.5897, 2.2258, and −0.4800. Today's labels look only at the sign: a positive number is up, a negative number is down. The first three are positive and the last is negative. The labels are 1 1 1 0.

Always-up writes 1 on all four steps. Against the labels, the first three steps agree and the fourth disagrees. The accuracy is 0.75. Always-down writes 0 on all four steps. Against the labels, the first three steps disagree and the fourth agrees. The accuracy is 0.25.

Both rules have an empty input. They do not read the closes 2.1, 3.9, 6.2, 20.0, and 10.4. They do not read the slope 3.27. They do not read the line `ŷ = 3.27x − 1.29`. Once the labels are written as 1 1 1 0, both accuracies are already fixed. The price column can be replaced by another column of numbers, and as long as the four signs remain three positive and one negative, 0.75 and 0.25 remain. The baseline looks at no price.

The direction hit on day 11 was also 3/4. Because the slope was positive, that rule and always-up were the same rule. Today supplies the other number that belongs beside that sentence. Always-up scores 0.75, and always-down scores 0.25 at the same time. Taken alone, 0.75 looks like a model score that used the price. With 0.25 beside it, the table shows that on sign labels with three ups and one down, two constants that look at no price already occupy 0.75 and 0.25. A 0.75 with no 0.25 beside it has no control.

## Core

The sign labels:

```text
y = 1{r > 0} = 1, 1, 1, 0
```

A constant prediction depends on no row's price:

```text
always up   = 1, 1, 1, 1     accuracy = 0.75
always down = 0, 0, 0, 0     accuracy = 0.25
```

| rule | columns it reads | steps it hits | accuracy |
|---|---|---|---:|
| always up | none | the three positive returns | 0.75 |
| always down | none | the one negative return | 0.25 |

Three of the four steps are positive, so the all-1s hit rate is 0.75. One of the four steps is negative, so the all-0s hit rate is 0.25. The two predictions disagree on every step, so exactly one of them is right on each step, and the two rates sum to 1. That addition is the arithmetic of complementary constants on a binary label. It is not extra information from the sample.

The control is used side by side. Citing only 0.75 states the class frequency as the rule's result and leaves 0.25 off the table. The 0.25 says what the opposite constant scores on the same labels. With it present, 0.75 is read as the hit rate of the up-constant that looks at no price, on a sample with three positive steps.

The positive-slope rule of day 11 collapses, on direction, to the first row of this table. Its 3/4 and today's 0.75 are the same number, and they are read together with 0.25. The slope 3.27 supplies no further direction distinction beyond the sign: the one-day difference is constantly 3.27, and the sign is constantly positive. Price entered the estimate of the slope. The predicted sign still does not change from step to step. A rule that looked at price, and whose predicted sign is nevertheless the same every day, has direction accuracy 0.75 on these four steps. This chapter writes down that the baseline looks at no price.

The threshold labels of days 12 and 13 are a different definition. There, always-up can score 0.50 or 0.25, because 1 no longer means "the return is positive." Today's 0.75 and 0.25 belong only to the sign labels. Ranking a number from the threshold table against a number from this table compares different targets as if they were different models.

## Further out

A constant baseline is a control. The control answers how high a fixed guess can score on this label when the price column is not used at all. Today's answer is two numbers, 0.75 and 0.25, for two fixed guesses. The class counts are written in those two numbers. Three steps up and one step down: the up-constant receives 0.75, and the down-constant receives 0.25.

Any later direction rule that reports 0.75 on these four sign labels is checked first for a prediction that is positive on all four steps. If it is, the rule coincides with always-up. The baseline has already produced the same 0.75, and the price column has left no extra hit in the direction score. If a 0 appears in the prediction, the accuracy can leave these two constants. After it leaves, 0.75 and 0.25 stay at the side of the table, so the new accuracy has a reference.

The two constants are a complementary pair on one label table. Dropping 0.25 drops the statement of how much of the hit rate comes from the positive class occupying three steps. The baseline looks at no price. That sentence is complete when both accuracies are present: one rule that looks at no price scores 0.75, another rule that looks at no price scores 0.25, and the results come from the counts of 1 and 0 in the labels.

Always-down 0.25 and always-up 0.75 sum to 1 on the same symbol labels—a complementary pair that ignores prices. Any rule that prints up every day cannot beat 0.75 on these labels without changing predictions; slope 3.27's direction score coincides with that benchmark.

Do not mix threshold-label accuracies from days 12–13 into this table. Day 22's coin 0.5000 is yet another baseline on 77 AAA segments.
Pair 0.75 with 0.25 and the sentence that the baseline ignores prices. Do not mix in threshold-label accuracies from days 12–13.
Seventy-five percent on symbol labels with always-up is a label-frequency fact, not evidence that prices were used in the baseline table.
## What the run showed

```bash
python days/14-constant-baseline/baseline.py
```

On the sign labels the script prints `always-down accuracy = 0.25` and `always-up accuracy = 0.75`, and it states that the baseline looks at no price. The implementation is [`baseline.py`](../../days/14-constant-baseline/baseline.py).

The two numbers are cited together. The 0.75 is the three positive signs hit by all 1s. The 0.25 is the one negative sign hit by all 0s. A 0.75 with no 0.25 beside it has no control.

