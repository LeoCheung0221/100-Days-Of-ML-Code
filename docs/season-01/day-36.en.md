<p align="center"><a href="day-36.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 36 · Adjusted and unadjusted

[Phase I · Models](../../README.en.md) · runs

What you learn today: on 2024-03-11 the unadjusted return is −0.4938 and the adjusted return is 0.0124. Both numbers are due. Each belongs to its own price series. Reading −0.4938 as a crash reads the corporate action, not the move in the adjusted series.

## Plain-language account

On the same AAA history, compute simple returns from the unadjusted close, then from the adjusted close. Take the day where the absolute difference between the two return series is largest. The end date of that pair is 2024-03-11. The unadjusted return that day is −0.4938. The adjusted return is 0.0124.

−0.4938 is the simple return on the unadjusted close. 0.0124 is the simple return on the adjusted close over the same pair of sessions, and it is a small positive number. Both numbers are computed on their own series. The script prints both and states that both are due. When a corporate action hits the unadjusted series, the price level jumps with the split, the stock dividend, or a similar adjustment, and that jump is inside −0.4938. After the adjusted series removes that adjustment from the path, the same day leaves 0.0124. Calling −0.4938 a crash on this day reads the corporate action. The move in the adjusted series on this day is 0.0124. −0.4938 is not treated as a real crash.

## Core

```text
date = 2024-03-11
unadjusted return = -0.4938
adjusted return = 0.0124
both numbers are due
```

A return is the simple return of the later close on the earlier close. The comparison is between the two return series. The date is the end date of the pair whose absolute difference is largest.

−0.4938 is due on the unadjusted close. 0.0124 is due on the adjusted close. A study that wants the price change after the corporate-action adjustment uses the adjusted return as the label, and this day's label is 0.0124. A study that wants to audit the raw close itself uses −0.4938, the change in that raw close. The two series answer two questions. Putting −0.4938 into a model whose label is "how much did this day fall" puts the corporate action into the label. The fit then explains a price adjustment, not the 0.0124 on the adjusted path.

The print does not name the form of the corporate action. What can be said is that a move of this size in the unadjusted return is the corporate action showing up in the raw close, and the adjusted return is 0.0124. Both numbers are due.

## Further out

Adjustment can be anchored at the front or at the back. The price levels differ, and the returns should line up when the adjustment is done correctly. Today does not compare the two anchors. It compares the unadjusted close and the adjusted close in this repository on 2024-03-11. If an adjustment factor is written back onto earlier dates only after the corporate action, using a factor that had not yet been published adjusts history with a number known later. That is a separate leak. Today's two numbers are already enough: the raw return and the adjusted return can stand at −0.4938 against 0.0124, and both prints are due.

Volatility, a training label, and an excess return each need a declared close. Estimating volatility on the unadjusted series gives 2024-03-11 a contribution of −0.4938, and that one day dominates the sample variance. On the adjusted series the same day's contribution is on the scale of 0.0124. The absolute gap between the two returns is widest on this day. It is wide because the unadjusted close counts the corporate action as a price change, and the adjusted close, with that adjustment removed from the path, leaves 0.0124.

If the unadjusted return is the label in "predict the next day's direction," this day is recorded as a large decline. The adjusted label on the same day is 0.0124, and the sign is positive. Both labels are correctly computed on their own series. They describe different events. A model comparison fixes the series first. Otherwise −0.4938 enters the loss as an extreme sample, and the extreme comes from the corporate action. Next, AAA and BBB go into one split, the feature is the same-day market return, and the question is whether a random split can put the same date on both the training side and the test side.

2024-03-11: unadjusted return −0.4938 and adjusted 0.0124; both numbers are due. Do not call −0.4938 a crash without the unadjusted qualifier.

Pick adjusted or unadjusted returns before comparing models; corporate-action day is when the two series diverge most on this panel.

**Two return series.** Unadjusted −0.4938 and adjusted 0.0124 are both due on 2024-03-11—declare which price chain is the label.

## What the run showed

```bash
python days/36-adjusted-close/adjusted.py
```

The script should print the date 2024-03-11, the unadjusted return −0.4938, and the adjusted return 0.0124. The implementation is [`adjusted.py`](../../days/36-adjusted-close/adjusted.py).

Hand in the two returns on the same day. Both are due. −0.4938 is the corporate action as read on the unadjusted series. The move on the adjusted series is 0.0124.
