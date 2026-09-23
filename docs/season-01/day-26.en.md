<p align="center"><a href="day-26.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 26 · A random split

[Phase I · Models](../../README.en.md) · runs

What you learn today: the seed is 1 and the train fraction is 0.70. Least squares of today's return on yesterday's return is fit on the training rows. The test direction accuracy is 0.4583. This number is the control. Today only marks it as the control.

## Plain-language account

The sample is still the simple returns of the finite adjusted closes on AAA. Yesterday's return is the input and today's return is the target, and one lag is one row. Day 25 used yesterday's return as the forecast unchanged, with no estimated slope or intercept. Today estimates a line on some of the rows and then reads the sign on the rest.

Which rows enter the train is decided by the random generator with seed 1. The train fraction is fixed at 0.70, drawn without replacement. The rows that are not drawn are the test. The line is ordinary least squares on the training rows only: today's return on yesterday's return, one slope and one intercept. The test rows use that line, and the sign of the fitted return is compared with the sign of the realized return. The test direction accuracy prints as 0.4583.

The last printed line says this number is the control. The identity of 0.4583 today is the control. It is not yet placed next to a test accuracy from a split by time. The program's sentence for it is only that this number is the control. The seed, the fraction, and this accuracy are the whole of what today hands in.

Day 25's 0.4675 is the full-sample sign hit rate of the forecast that equals yesterday's return. Today's 0.4583 is a different object: the slope is estimated on the training rows, and the signs are counted only on the test rows. The two four-decimal numbers sit near each other and are not the same count. Today does not merge 0.4583 with day 25's 0.4675 into one conclusion, and it does not put 0.4583 in the same sentence as the time split, which has not been computed yet.

## Core

```text
split = random, seed 1, train fraction 0.70
test direction accuracy = 0.4583
this number is the control
```

A row is `(x_t, y_t) = (r_{t−1}, r_t)`. The training mask is drawn without replacement from seed 1, at a fraction 0.70. On the training rows,

```text
ŷ = β̂₀ + β̂₁ x
```

The coefficients come only from least squares on those rows. The test direction accuracy is the fraction of test rows with `sign(y) = sign(ŷ)`, printed as 0.4583.

Three things in the definition of 0.4583 are already fixed: seed 1, train fraction 0.70, and a score that counts signs only on the test rows. A different seed would draw a different training set, and the accuracy could print as another four-decimal number. Today does not change the seed. The control that gets printed is this one number, 0.4583.

The number is not set beside a time split today. That pairing is the next day's work. Today's sentence stops at the line the program already prints: this number is the control.

## Further out

A random split shuffles which rows estimate the coefficients. A test row can sit earlier in time than a training row, or later. On a return series laid out by date, the shuffle answers one question: under this draw, what test sign accuracy gets printed. It does not answer what the accuracy is when every training row sits before every test row. That question is left to the next day. Writing the two numbers down together today would stop the control from being a control. It would already be one side of a comparison. The program does not make that comparison.

The number 0.4583 is also not day 22's lagged sign, which estimated no parameter. That rule was already "yesterday's sign" before the count, and the denominator was every comparable step. Today's signs come from a line that has seen only the training rows. The test labels did not enter `β̂`. That is why the number can be called a test accuracy. It is called the control because today's note gives it only that identity.

The seed is written into the program so that another run draws the same rows. The fraction 0.70 is fixed the same way. Neither one is a knob turned after 0.4583 has been seen. The control can therefore be read again: the same file, the same seed, and the same fraction still give the test direction accuracy 0.4583. Today does not give 0.4583 a second identity.


<!-- uniq-exp-en-27-50 -->

Keep 0.4583 as the control until day 27 prints the time split beside it. Random row masks can place test rows before train rows in calendar order; that protocol is what 0.4583 counts. Do not merge it with day 25's 0.4675 full-sample lag sign rule. Report seed 1 and train fraction 0.70 whenever you cite the number.

## What the run showed

```bash
python days/26-random-split/random_split.py
```

The script prints `split = random, seed 1, train fraction 0.70`, `test direction accuracy = 0.4583`, and `this number is the control`. The implementation is [`random_split.py`](../../days/26-random-split/random_split.py).

The test direction accuracy 0.4583 is the control. The seed is 1, the train fraction is 0.70, and the coefficients come from least squares on the training rows. Today does not place this number next to a time split. Next the cut is by time, the test sits entirely after the train, and both accuracies are printed.
