<p align="center"><a href="day-41.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 41 · A line on a longer sample

[Phase I · Models](../../README.en.md) · runs

What you learn today: after the blank row is dropped, AAA adjusted close has 79 sessions. The adjusted return on 2024-02-28 is 0.1349. Delete that session and refit. The slope stays 0.029901 to six decimals. The intercept moves from 9.8654 to 9.8528, and the fitted value at the jump moves from 11.0315 to 11.0189, a shift of 0.0126.

## Plain-language account

Lay the 79 adjusted closes on the session index. A line is a slope times that index, plus an intercept. The largest absolute adjusted return in the sample falls on 2024-02-28 and equals 0.1349. The check is the same operation as day 5: remove that session from the estimation sample, solve least squares again, and read the two fits side by side.

Before the deletion the slope prints as 0.029901 to six decimals. After the deletion it still prints as 0.029901. The intercept falls from 9.8654 to 9.8528. At the jump abscissa the fitted value falls from 11.0315 to 11.0189. Both gaps are 0.0126. With the printed slope unchanged, that gap in the fitted value is the intercept gap read at the jump index.

Day 5 had five points. Removing `(4, 20)` moved the slope from 3.2700 to 2.0971, a change of 1.1729, and the fitted-value displacement grew along the axis, reaching −4.6914 at session 5. That was one extreme label pulling the slope on a short sample. Today's sample has 79 sessions. The same kind of deletion — drop the session with the largest absolute return — leaves the slope at 0.029901. The printed movement is in the intercept and in the fitted value on that date, and its size is 0.0126. The long index spreads the curvature that the slope sits on, so one session's share is small. The slope movement visible on five points does not show up as a six-decimal change on these 79 points.

The claim covers this one comparison. The slope stays 0.029901. The intercept and the fitted value at the jump each move by 0.0126. The 1.1729 belongs to the five-point sample.

## Core

The series is AAA adjusted close. A row is kept only when close and adjusted close are both finite. After the blank row is dropped, the length is 79. The script's abscissa runs from 0 through the last kept session. An adjusted return is the relative change between adjacent adjusted closes, so the return series is one step shorter than the price series. The jump is the largest absolute return, shifted back onto the price row. The date is 2024-02-28.

```text
adjusted return that day        = 0.1349
slope with the jump             = 0.029901
slope without the jump          = 0.029901
intercept with the jump         = 9.8654
intercept without the jump      = 9.8528
fitted at the jump, with        = 11.0315
fitted at the jump, without     = 11.0189
```

To six decimals the slope gap is 0. The printed intercept gap is 9.8654 − 9.8528 = 0.0126, the same as the printed fitted gap 11.0315 − 11.0189. The two locations stay separate on the page. The intercept is the reading at abscissa 0. 11.0315 is the reading at the jump index. Those gaps coincide when the printed slope does not move. Report the printed columns.

Day 5's comparison is a slope change of 1.1729 on five points. There is no table of displacements growing in t today, because the slope does not leave 0.029901. Copying the short-sample slope change onto these 79 sessions does not match the printout.

11.0315 and 11.0189 are values of two estimated lines at that index. The session was removed in order to watch its influence, and the removal already used how large the return is. The result is a displacement of the coefficient and of the fitted value. The size is 0.0126. It is not an out-of-sample score for that date. A holdout that is declared before the fit is a different information set.

## Further out

The size of a one-day return and that day's leverage on the slope are different sentences. 0.1349 is how far adjacent adjusted closes moved relative to each other. Whether the slope moves depends on how far that row sits from the others in the design, and on its share of Σ(t − t̄)². Seventy-nine session indices spread that curvature, so one session's share is small. On five points, session 4 can be heavy in the sum of squares and can move the slope by 1.1729. Those sentences belong to days 3 and 5. Today's sample supports this sentence: after the session with adjusted return 0.1349 is removed, the slope is still 0.029901 and the intercept has moved by 0.0126.

A deletion diagnostic in a book of returns splits the same way. The first sentence is the return, here 0.1349. The second is the coefficient move: the slope is unchanged at six decimals, and the intercept moves by 0.0126. The third, only if the day was set aside before the fit, is a holdout error. Today has no third sentence. Seeing the jump and then deleting it produces influence.

A longer sample is not a theorem. A different abscissa, or many large moves packed into a short run of indices, can still move a slope. Those experiments are not run today. The printout belongs to this one deletion: the slope stays at 0.029901, and the movement that remains is in the intercept.

## What the run showed

```bash
python days/41-longer-line/longer_line.py
```

The script should print the jump date `2024-02-28`, the adjusted return `0.1349`, both slopes as `0.029901`, intercepts `9.8654` and `9.8528`, and fitted values `11.0315` and `11.0189`. The implementation is [`longer_line.py`](../../days/41-longer-line/longer_line.py).

Hand in the deletion comparison on 79 sessions. Day 42 keeps this adjusted-close stretch and penalizes the slope alone, leaving the intercept free. The penalty is 20000.
