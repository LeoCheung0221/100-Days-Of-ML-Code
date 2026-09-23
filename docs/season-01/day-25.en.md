<p align="center"><a href="day-25.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 25 · Direction and price together

[Phase I · Models](../../README.en.md) · runs

What you learn today: yesterday's return is the forecast of today's return. Direction accuracy is 0.4675. Mean absolute return error is 0.0167. On 9 days the absolute error is at most the median and the sign is wrong. For a sign decision, trust the direction accuracy, not 0.0167.

## Plain-language account

The rows are still the AAA rows whose close and adjusted close are both finite. Adjusted close is turned into a simple return: today's close minus yesterday's close, divided by yesterday's close. The forecast adds no slope and no intercept. Yesterday's simple return is used as it stands as the forecast of today's simple return. The print name is lag-1 return forecast.

The sign column compares the sign of the forecast with the sign of the realized return. The accuracy is 0.4675, the same four-decimal print as the lagged-sign accuracy on day 22. Day 22 compared signs of adjusted-close differences. Today compares signs of simple returns. When the previous adjusted close is positive, those two signs agree, so on the sign the two rules are the same object. The 0.4675 is not a new direction score. It is yesterday's sign reported again.

The price column is the average of absolute return errors. Each day subtracts yesterday's return from today's return, takes the absolute value, and averages over the comparable days. The average is 0.0167. That number is a distance in return units. It does not say whether the sign was right. The program then marks a day as small when the absolute error is at most the median of those absolute errors, and it counts how many of those days have the wrong sign. The count is 9. On those 9 days the price error sits at or below the median, and the direction is wrong. The average distance 0.0167 can be small while the signs on those 9 days are still reversed.

A sign decision trusts the direction accuracy 0.4675. The number 0.0167 answers how far the return sat from yesterday's return. It does not answer whether the up or down call was right. Day 22 already placed 0.4675 under the coin-flip baseline 0.5000. Handing in an extra 0.0167 does not turn that direction rule into a pass.

## Core

```text
lag-1 return forecast
direction accuracy = 0.4675
mean absolute return error = 0.0167
days with a small price error and the wrong sign = 9
for a sign decision, trust the direction accuracy
```

Write the simple return as `r_t = (P_t − P_{t−1}) / P_{t−1}`, with `P` the adjusted close. The forecast is `r̂_t = r_{t−1}`, with no estimated coefficient. A direction hit is `sign(r_t) = sign(r_{t−1})`. The direction accuracy prints as 0.4675.

The mean absolute return error is the average of `|r_t − r_{t−1}|`, printed as 0.0167. A small error is defined in the program: the absolute error is less than or equal to the median of all the absolute errors. Under that definition, the number of days with the wrong sign is 9. The median itself is not printed as a separate number today. The 9 is a count, 0.0167 is an average, and 0.4675 is a sign hit rate. The three columns answer three questions.

A sign decision uses the direction accuracy. The print says to trust the direction accuracy for a sign decision. The 0.0167 stays in the return-distance column. Using 0.0167 to underwrite 0.4675 uses an average distance to underwrite a sign count. Those 9 days say the underwriting fails: the error is already at or below the median, and the sign can still be wrong.

## Further out

A regression often hands in a price distance. A trading decision often hands in a sign. The two functionals can be read in opposite ways on the same days. Today fits no new line. The forecast is yesterday's return itself, so the distance and the sign both come from the same identity rule, and the conflict still shows up: the mean absolute return error is 0.0167, 9 days combine a small error with the wrong sign, and the direction accuracy sits at 0.4675.

The unit of 0.0167 is the return, not the price level. It is smaller than the absolute residuals of day 10, which were in price units, because a simple return is a ratio. A small numeral is not a correct sign. Reading 0.0167 as "the forecast is close," and then letting that reading cover 0.4675, copies the answer of the distance question into the sign question. The coin-flip baseline 0.5000 from day 22 is still above 0.4675. The distance 0.0167 did not enter that comparison.

When a direction accuracy and a mean absolute error arrive together, the first question is whether the decision is a sign or a distance. When the decision is a sign, the score column takes the accuracy and sets it beside a baseline. The mean absolute error stays, as a statement of how far the return numbers sat, and as a check of how many days have a modest distance and the wrong sign. The check today is 9 days. Those 9 days are the concrete count that 0.0167 does not stand in for 0.4675.

Direction accuracy 0.4675 pairs with mean absolute return error 0.0167; nine days can be small-error yet wrong-sign. For sign decisions, trust direction accuracy, not the MAE column—same separation as level vs direction on day 10.
Trust direction accuracy for sign calls; MAE 0.0167 and the nine wrong-sign small-error days prove the columns diverge.
Nine wrong-sign days despite small absolute return error justify trusting direction accuracy for sign decisions, not MAE alone.
## What the run showed

```bash
python days/25-two-scores/two_scores.py
```

The script prints `direction accuracy = 0.4675`, `mean absolute return error = 0.0167`, and `days with a small price error and the wrong sign = 9`, and it states that a sign decision trusts the direction accuracy. The implementation is [`two_scores.py`](../../days/25-two-scores/two_scores.py).

The lag-1 return forecast hands in two columns: direction 0.4675, and mean absolute return error 0.0167. On 9 days the absolute error is at most the median and the sign is wrong. The score for a sign decision is 0.4675. Next the rows are split at random into train and test, and that test accuracy is only a control.
