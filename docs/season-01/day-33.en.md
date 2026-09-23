<p align="center"><a href="day-33.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 33 · Scale from the training stretch

[Phase I · Models](../../README.en.md) · runs

What you learn today: the training-stretch mean and standard deviation of the return are 0.003241 and 0.022132. The whole-sample pair is 0.002470 and 0.019265. Test MSE under both scales is 0.000109 to six decimals. The score did not move. The whole-sample scale still saw the test stretch. Seeing is not the same as improving.

## Plain-language account

The feature is the previous adjusted simple return. The label is the next adjusted simple return. The training stretch keeps only the early pairs and computes the mean and standard deviation on that stretch of the feature: 0.003241 and 0.022132. The whole sample puts the later stretch of the feature into the same two moments. The mean falls to 0.002470 and the standard deviation falls to 0.019265. The two pairs differ, so the test stretch did enter the location and the scale of the whole sample.

Each pair then scales the feature. Least squares with an intercept is fit on the training stretch, and mean squared error is computed on the test stretch. Test MSE with the training scale is 0.000109. Test MSE with the whole-sample scale is also 0.000109. To six decimals the score did not move. The leak sits in the moments: the whole-sample 0.002470 and 0.019265 use the test stretch. It does not sit in an improved score, because the score did not improve. Seeing the test stretch and making the test error smaller are two checks. The leaky scale did not improve test MSE.

## Core

With one feature and an intercept, changing the mean and the standard deviation is an affine map of the feature. `(x − μ) / σ` together with an intercept spans the same column space as `x`. Fitted values on the training stretch, as a function of the raw return, do not depend on which pair `(μ, σ)` is chosen. The test stretch is scaled with that same pair, so the predictions do not depend on it either. Test MSE can therefore sit still. The print stops at six decimals, and both sides are 0.000109. What can be said today is that the score did not move at those six decimals. Digits past the print are not a new gap.

```text
train mean/std = 0.003241 0.022132
whole-sample mean/std = 0.002470 0.019265
test MSE, scale from the training stretch = 0.000109
test MSE, scale from the whole sample = 0.000109
the whole-sample scale sees the test stretch
```

The difference in the moments is real. The mean goes from 0.003241 to 0.002470, and the standard deviation goes from 0.022132 to 0.019265. That is the evidence that the whole sample saw the test stretch. The difference in the score is zero at the printed precision. The leak is decided by whether the test stretch entered the sample used for scaling, not by whether mean squared error got smaller. The test stretch was seen, and the score is still 0.000109.

## Further out

A scale at each stretch may use only observations already allowed at that time. The training moments are fixed before the test stretch begins, and they may be applied to the test stretch as they stand. Putting the test stretch into the mean and the standard deviation makes the scaling function depend on later returns. The dependence is in place the moment the moments are computed. A later mean squared error, whether it moves or not, does not undo that. Today it did not move. The print is still 0.000109, and the question sits on 0.002470 and 0.019265.

With several features, a distance, a tree split, or a correlation matrix, the same leak can change the estimate, and the score can move. Today is one line plus an intercept. The column space absorbs location and scale, which is the easiest case to misread: the moments changed, and the printed test MSE did not. The misreading turns "the score did not move" into "the whole-sample scale is harmless." The decision is already on the two pairs of moments.

The training standard deviation 0.022132 is larger than the whole-sample 0.019265, and the training mean 0.003241 is higher than the whole-sample 0.002470. The test stretch pulls the location down and compresses the scale. That is how it enters the moments. After it enters, the line with an intercept absorbs location and scale again, and test MSE still prints as 0.000109. Absorption holds the score still. It does not take the test stretch back out of the whole sample. Saving only the mean squared error, and dropping the mean and the standard deviation, hides the leak on this print. The script prints all four numbers together so that 0.003241, 0.022132, 0.002470, 0.019265, and the two copies of 0.000109 are on the page at once. Next is a blank close, and the question is whether filling from the previous close and filling from the next close are the same number.

## What the run showed

```bash
python days/33-train-scale/train_scale.py
```

The script should print the training mean and standard deviation 0.003241 and 0.022132, the whole-sample pair 0.002470 and 0.019265, and a test MSE of 0.000109 on both scales. The implementation is [`train_scale.py`](../../days/33-train-scale/train_scale.py).

Hand in two pairs of moments and a score that did not move. The whole-sample scale saw the test stretch. Seeing is not improving. The leaky scale did not improve test MSE.
