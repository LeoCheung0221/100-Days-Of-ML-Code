<p align="center"><a href="day-20.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 20 · A noise column

[Phase I · Models](../../README.en.md) · runs

What you learn today: the noise uses seed 0, fixed in advance. The fit is on t = 1..4 and the score is on t = 5. In-sample RSS goes from 42.0500 without noise to 26.7061 with noise. Holdout absolute error goes from 11.6500 without noise to 18.1513 with noise. The in-sample drop is not an improvement.

## Plain-language account

The five sessions are still the closes 2.1, 3.9, 6.2, 20.0, and 10.4. Today the estimate and the score are split. The times t = 1, 2, 3, 4 are used to fit, with closes 2.1, 3.9, 6.2, and 20.0. The time t = 5 does not enter the coefficients. It is used only to score, and its close is 10.4.

First use time alone. Fit a line with an intercept on the first four points, square the gaps between the four fitted values and the four closes, and add them. The in-sample residual sum of squares is 42.0500. Then look at t = 5: the absolute distance between this line's prediction on day 5 and the close 10.4 is 11.6500. Those are the two numbers without a noise column. The in-sample number describes how tight the first four days are. The holdout number is the error on day 5.

Then add a noise column. The noise is fixed before the fit: the random seed is 0, each of the five sessions has a number drawn in advance, and the draw is not repeated after the day-5 error has been seen. The first four noise numbers enter the least squares on t = 1..4 together with time and an intercept. The column space is larger, and the residual sum of squares on the first four days falls to 26.7061. The fifth noise number is used only when day 5 is scored. The holdout absolute error rises to 18.1513.

The training sum of squares goes from 42.0500 down to 26.7061. The day-5 absolute error goes from 11.6500 up to 18.1513. The score that is handed in is the holdout error, and it got worse. The drop inside the sample is not an improvement.

## Core

```text
noise seed = 0, fixed in advance
fit on t = 1..4
score on t = 5
```

|  | without noise | with noise |
|---|---:|---:|
| in-sample RSS | 42.0500 | 26.7061 |
| holdout absolute error | 11.6500 | 18.1513 |

The fit without noise is time plus an intercept, and the coefficients use only the first four closes. The fit with noise adds the column drawn at seed 0, and the coefficients still use only the first four sessions. The day-5 close 10.4 enters neither least-squares problem. The day-5 noise value is used only after the coefficients are already estimated: it is multiplied by its own coefficient, added into the prediction, and then the absolute difference with 10.4 is taken.

A larger column space may lower the training sum of squares. The value 42.0500 reached by time plus an intercept is still attainable in the larger space: set the noise coefficient to 0 and the original fit is back. Least squares can also use the noise column, so the sum of squares can go lower. Today it does go lower, to 26.7061. That drop is what a larger column space permits. It is not evidence that day 5 became easier to predict. The day-5 numbers are 18.1513 against 11.6500, and the side with noise is larger.

The value 26.7061 is also not 0. On four training points, with time, noise, and an intercept, three columns, the sum of squares fell, and it did not fall far enough to put the four points exactly on the fit. Even so, the holdout error still rose. A smaller in-sample sum is not a smaller holdout error. The holdout side today has one point, t = 5. Its absolute error is the number that counts as the score, and that number went from 11.6500 to 18.1513.

The seed is fixed in advance so that this noise column was not chosen by looking at day 5. The holdout error was not used to pick the seed. Even so, the column that was drawn still made the holdout error larger. A larger column space may lower the training sum of squares. Today that sentence is the move from 42.0500 to 26.7061. The score that counts is the holdout error, and it got worse. The in-sample drop is not an improvement.

## Further out

Adding a column is a direct way to make the training error smaller. If the new column supplies a new direction on the four training points, least squares will use it whenever it reduces the sum of squares on the first four days. The noise column is a series of numbers fixed by seed 0. The reduction happened, from 42.0500 to 26.7061. After that direction is used, the absolute error at t = 5 rises from 11.6500 to 18.1513.

A model comparison that calls the fit with the smaller training residual sum of squares the better fit would select the fit that includes noise. That selection disagrees with the holdout score. On the holdout score, 11.6500 is smaller than 18.1513, so the side without noise has the smaller error. Both orderings are facts in this table. Which ordering is called the score is written down in advance. Today the score is the holdout absolute error.

This also bounds the practice of fitting and then scoring on the same points. Fitting on a set of points and then measuring residuals on those same points is the same kind of object as today's training sum of squares: those points already entered the coefficients. Once day 5 is kept out of the coefficients, a drop in the training sum of squares is no longer treated as the result. The result looks at 18.1513 and 11.6500. The noise column made the training error smaller and the holdout error larger. The in-sample drop is not an improvement.

Fixing the seed does not turn this one run into a claim that every noise series hurts the holdout point. What it guarantees is that the column was fixed before the holdout result was seen, so the worsening reported today was not produced by shopping for a seed. For this one column, already fixed, the holdout absolute error got larger. The conclusion stops at this run. This one result is enough to show that a training sum of squares can fall from 42.0500 to 26.7061 at the same time as the holdout error rises from 11.6500 to 18.1513.

Training RSS falls 42.0500→26.7061 when noise joins fit on t=1..4, but holdout absolute error rises 11.6500→18.1513 on t=5 with seed 0 fixed upfront. The scored metric is holdout, not the in-sample drop.
Holdout 18.1513 vs 11.6500 is the scored comparison; training RSS 26.7061 is not the win metric.
Seed 0 fixes the noise draw before scoring session 5; lower train RSS with worse holdout abs error is the intended pairing.
## What the run showed

```bash
python days/20-noise-column/noise.py
```

The script states that the fit is on t = 1..4 and the score is on t = 5. It prints the in-sample residual sums of squares 42.0500 without noise and 26.7061 with noise, and the holdout absolute errors 11.6500 and 18.1513, and it states that the in-sample drop is not an improvement. The noise seed is 0, fixed in advance. The implementation is [`noise.py`](../../days/20-noise-column/noise.py).

After the column space grows, the training sum of squares can fall. The score that counts is the holdout absolute error. It went from 11.6500 to 18.1513, and it got worse. The value 26.7061 is not a better result.
