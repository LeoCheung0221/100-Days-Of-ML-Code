<p align="center"><a href="day-27.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 27 · A time split

[Phase I · Models](../../README.en.md) · runs

What you learn today: the time-split test direction accuracy is 0.5417. On the same series, the random split with seed 1 and train fraction 0.70 is 0.4583. Both are printed. On this one name the random split did not lift the accuracy above the time split. The time-split test sits entirely after the train. Mixing in a second name, so the same date can appear on both sides, is day 37.

## Plain-language account

The rows are still AAA's lagged returns: yesterday's return predicts today's return, the coefficients come from least squares on the training rows, and the score is the sign accuracy on the test rows. Day 26 shuffled the rows with seed 1 and got the control 0.4583, and that day did not set it beside another split. Today both splits are printed.

Under the time split, the train is the opening stretch of the series, with length still taken at the fraction 0.70. The test is the remaining later stretch. Every row in that later stretch is dated after the training rows. The test direction accuracy is 0.5417. The random split still uses seed 1 and the same train fraction 0.70, and its test direction accuracy is 0.4583, the same print as the control on day 26. The two numbers appear together: time split 0.5417, random split 0.4583.

On this one name, the random split's 0.4583 is below the time split's 0.5417. The random split did not lift the test accuracy above the time split. That the time split is higher is a fact of this print. It does not rewrite the sentence from day 26, where 0.4583 was only the control. Today is the day the two numbers are placed side by side.

The same date on both the train side and the test side cannot happen on a single-name series: one date is one row. Putting the same date on both sides requires a second name's same day inside the same split. That is left to day 37. Today's sample is AAA only. The time-split test lies entirely after the train, and the print says so.

## Core

```text
time-split test accuracy = 0.5417
random-split test accuracy = 0.4583
the test of the time split sits entirely after the train
```

Both splits estimate the same kind of line, `ŷ = β̂₀ + β̂₁ x`, with `x` yesterday's return and `y` today's return. The difference is the training mask.

| Split | Training mask | Test direction accuracy |
|---|---|---:|
| Time | opening stretch, fraction 0.70 | 0.5417 |
| Random | seed 1, without replacement, fraction 0.70 | 0.4583 |

Every test index in the time split is greater than every training index. The random split does not guarantee that order. Both accuracies are printed. The higher number, 0.5417, is not kept alone. 0.5417 is the time-split test score. 0.4583 is the random-split test score of the same forecast, the same seed, and the same fraction.

The comparison on this one name is that the random split did not inflate the score. 0.4583 is below 0.5417. The single-name random split is not the higher number in this print. Day 37 is when a second name is added, so that one date can land in train and test at once. Today's print does not report that split.

## Further out

A time split matches a use in which the coefficients are estimated only on rows that are already past, and the sign is then read on later rows. 0.5417 is the test direction accuracy under that order. A random split scrambles where the rows sit in time, and 0.4583 is the test direction accuracy under that draw. Printing both lets the reader see which one is higher this time. Printing only 0.5417 would hide the random split's 0.4583.

On a single-name panel, a random shuffle cannot put the same date on both sides of the split, because that date has only AAA's one row. So today's 0.4583 cannot be described as the result of the same day leaking into both sides. Relative to the time split, this random split is the lower number. The higher number is the time split's 0.5417, and the time-split test lies entirely after the train, so the same day cannot sit on both sides.

Day 26 marked 0.4583 as the control on its own, so that the number would have an identity that did not depend on a comparison. Today's comparison uses it, and writes down the time split's 0.5417. The sentence of the comparison is: on this one name, the random split did not lift the accuracy above the time split. A second name, and the cross-side date that would come with it, is not in today's print.


<!-- uniq-exp-en-27-50 -->

Print both 0.5417 and 0.4583. On single-name AAA the random split does not beat the time split. The line about the test sitting entirely after the train defines the time-split information set. Day 37's pooled 0.7234 vs 0.6170 is a different design; do not replace today's pair.

## What the run showed

```bash
python days/27-time-split/time_split.py
```

The script prints `time-split test accuracy = 0.5417`, `random-split test accuracy = 0.4583`, and `the test of the time split sits entirely after the train`. The implementation is [`time_split.py`](../../days/27-time-split/time_split.py).

Both test direction accuracies are handed in: time split 0.5417, random split 0.4583. On this one name the random split did not inflate the score. Next, today's high is used to explain today's close, and that column is marked forbidden.
