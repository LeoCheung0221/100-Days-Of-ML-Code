<p align="center"><a href="day-37.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 37 · Pooled names

[Phase I · Models](../../README.en.md) · runs

What you learn today: AAA and BBB are pooled in one split, and the feature is the same-day market return. Random-split test accuracy is 0.7234. The time split is 0.6170. The random split can train and test on the same date across names. This is the case where a random split can look better. That statement is not about the single-name split on days 26 and 27.

## Plain-language account

Each name's adjusted return is the label. The same-day market return is the feature. Rows are stacked with AAA first and BBB after. The random split uses the constants day 26 printed: seed 1, training fraction 0.70. Test direction accuracy is 0.7234. The time split sorts by date and puts the earlier stretch into training. Test direction accuracy is 0.6170. 0.7234 is higher than 0.6170.

On this run the reason can sit on the date. The random draw samples rows. AAA's row on a given day can land in training while BBB's row on the same day lands in the test. The two rows share that day's market return. A test row can therefore be the other name on a date the training side has already seen. 0.7234 is the print on which a random split can look higher because of that shared date. It is the print for this pooled split. On day 26 the single-name random split scores 0.4583. On day 27 the time split of that same series scores 0.5417, and the time split is the higher one. Today's sentence is not taken back to rewrite that pair.

## Core

Direction accuracy is the fraction of test rows on which the label's sign matches the fitted value's sign. The fit is least squares with an intercept. The feature is the same-day market return, written on the same day as the label.

```text
pooled AAA and BBB
random-split test accuracy = 0.7234
time-split test accuracy = 0.6170
the random split can train and test on the same date
```

Days 26 and 27 are one name, and the feature is the lagged own return. There the random split is 0.4583 and the time split is 0.5417. A single name has one row per day, so a random draw of rows cannot pick "the other name on the same day." After BBB is pooled in, a day has two rows, and a random split can put that day on both sides. "A random split can look better" refers to today's split, the one that can share a date across names.

0.7234 still carries the same-day market return. The market and the name are known at the same time, and the next day separates that with a lag. Today the split is the object: on the run where 0.7234 is above 0.6170, training and test can share a date. The subject of that sentence is the AAA and BBB pool.

## Further out

A panel row is a name crossed with a date. If the split unit is the row, a random sample shuffles rows. A test that is meant to be about later dates splits on the date: every name on a date is in training, or every name on that date is in the test. Splitting by name is a different question. It asks about a name that was never seen. Today's time split sorts by date and takes the earlier stretch. Its printed accuracy is 0.6170. The random split targets rows, so a date can be shared across names. How many dates are shared is not given its own printed line. What can be checked is the line the script does print: the random split can place the same date in training and in the test.

A shared date plus a same-day market feature lets a test row see a market return that a training row has already used. Direction accuracy then has a channel that is simultaneous and cross-sectional. 0.7234 is a higher print along that channel. The higher print stays inside the design "random split, AAA and BBB, same-day market." It is not extended into "a random split is usually higher." The single-name prints on days 26 and 27 are 0.4583 and 0.5417, and the random split is the lower one there. With one row per day, drawing rows does not put the same day on both sides.

Next stays with AAA, lines up the sign of the market return with the sign of the adjusted return, and then lags the market sign by one day, so the part of the accuracy that was simultaneous can be seen to drop. The gap between 0.7234 and 0.6170 has today's explanation only when the two names are drawn in one sample.


<!-- uniq-exp-en-27-50 -->

Pooled names: random test 0.7234, time 0.6170; random split can share a date across names. Single-name day 26–27 ordering does not generalize.


<!-- uniq-exp-en2 -->

When names are pooled, random splits can leak calendar information across symbols; time split 0.6170 uses a different protocol than single-name day 27.

## What the run showed

```bash
python days/37-mixed-names/mixed_names.py
```

The script should print random-split test accuracy 0.7234 and time-split test accuracy 0.6170. The implementation is [`mixed_names.py`](../../days/37-mixed-names/mixed_names.py).

Hand in the two accuracies of the pooled split. The random split can share one date across names. On this run it is 0.7234 and the time split is 0.6170. That sentence is not used for the single-name split on days 26 and 27.
