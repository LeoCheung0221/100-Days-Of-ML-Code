<p align="center"><a href="day-28.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 28 · Today's high

[Phase I · Models](../../README.en.md) · runs

What you learn today: the column `high` is marked FORBIDDEN. The in-sample RSS of close on today's high is 31.8715. The in-sample RSS of close on yesterday's close is 35.5233. The fall of 3.6518 is same-bar information, not a forecast. A lower RSS here is not a result.

## Plain-language account

The rows are still AAA rows with a finite close. The target is today's close. Two in-sample lines sit side by side, on the same observations from the second row onward, so that yesterday's close exists. The first line uses today's high as the input. The high and the close are written on the same row, the same day. The second line uses yesterday's close. Yesterday's close is written on the previous row.

The residual sum of squares of the first line is 31.8715. The second is 35.5233. Subtracting 31.8715 from 35.5233 leaves 3.6518. The sum of squares fell by 3.6518. The column that produced the fall is today's high. The script marks that column FORBIDDEN. The high and the close come from the same bar: the high of the day already contains information about where the price went that day, and the close is another price from that same day. Fitting the close with it can look tighter in sample. The tightness comes from the same bar. It is not a forecast that could have been submitted before the close was formed.

Yesterday's close is a number already written on the previous session. Its RSS is higher, 35.5233. Being higher does not make it the forbidden column, and being lower does not make 31.8715 the result. A result has to answer how good a forecast is when the forecast uses information from the past. 31.8715 answers how close two prices from the same day are. Treating the fall of 3.6518 as an improvement treats same-bar closeness as a forecast.

## Core

```text
column high = FORBIDDEN
in-sample RSS close~high = 31.8715
in-sample RSS close~lagged close = 35.5233
```

Both fits are ordinary least squares in sample, both with an intercept:

`high_t` and `close_t` share a row. `close_{t−1}` comes from the previous row. The residual sums of squares are

The 3.6518 is a fall in the in-sample sum of squares on the same rows. It is not an error on a held-out day, and it is not a direction hit. The column `high` is marked FORBIDDEN because it is being used to explain the close of the same session. The lower number, 31.8715, is not the result. The in-sample sum of squares that remains as the reference is 35.5233, from yesterday's close. Even that 35.5233 is an in-sample sum of squares, and today does not promote it by itself into a forecast score. What today fixes in place is that the fall of 3.6518 comes from the same bar.

## Further out

Price fields on the same row share that day's traded range. The high is the top of the range. The close is a point inside the range. The top often sits near the close, so the in-sample sum of squares of `close ~ high` can fall below that of `close ~ lagged close`. 31.8715 is below 35.5233, by 3.6518, and that gap is the same-day geometry showing up in the sum of squares. Being closer in that geometry does not produce a forecast that could be submitted before the open.

A forbidden column is decided by the date of the information, not by the size of the sum of squares. If columns were chosen by RSS alone, 31.8715 would be kept as the better fit and the FORBIDDEN mark would come off. The program marks the column forbidden first and then prints both sums of squares. That order says 31.8715 cannot lift the ban. The fall of 3.6518 is shown so that the sum-of-squares advantage of same-day information is visible, and so that it is not written into the score.

The difference 3.6518 has to be read together with the dates of the two columns. The high inside 31.8715 is from the same day as the close. The close inside 35.5233 is from the previous day. On the fit with the smaller sum of squares, the information is not earlier. It is written on the same row as the close being explained. The fall is therefore not a forecast that got better. The FORBIDDEN mark on `high` takes that column off the list of inputs that may be used as a forecast. After it is taken off, 31.8715 may still be printed, to show how far same-day prices push the in-sample sum of squares down. Printing is not scoring. An input that is scored has to be fixed before the close is written. Yesterday's close meets that. Today's high does not.

Day 29 switches to a quieter leak. There the two residual sums of squares sit almost on top of each other. Today's two differ by 3.6518, and the gap is plain to see. The identification still does not run through "which one is smaller." It runs through the high and the close sharing a row. Which one is smaller is only a consequence of same-day information. The consequence can be large, as with today's 3.6518, or small. In either case the identifying fact is whether the input contains a price that was not yet available.

**FORBIDDEN before RSS.** Lower in-sample RSS on same-bar high does not overturn the ban. 31.8715 vs 35.5233 differ by 3.6518 on the same rows—geometry, not forecast skill.

## What the run showed

```bash
python days/28-todays-high/todays_high.py
```

The script prints `column high = FORBIDDEN`, `in-sample RSS close~high = 31.8715`, and `in-sample RSS close~lagged close = 35.5233`. The implementation is [`todays_high.py`](../../days/28-todays-high/todays_high.py).

The in-sample sum of squares falls from 35.5233 to 31.8715, a fall of 3.6518. The fall uses today's high, on the same row as the close. The lower RSS is not the result. Next, later opens are written into a scale. A leak need not show up as a sum of squares that gets clearly better.
