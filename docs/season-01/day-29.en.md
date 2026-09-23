<p align="center"><a href="day-29.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 29 · A scale that uses later opens

[Phase I · Models](../../README.en.md) · runs

What you learn today: the leaky scale uses every open, including later ones. The RSS of the return on the leaky close is 0.2642. The RSS of the return on the close scaled with past closes only is 0.2650. The difference is 0.0008. Both RSS values use the same finite mask. Leakage is identified because later opens are arguments of the scale, not because the score got better.

## Plain-language account

The series is still AAA's finite closes and opens. The leaky scale subtracts the mean of every open from each close, then divides by the standard deviation of every open. Every open includes opens that come after that row. The scaled value on an earlier day is therefore a function of later opens. An open that has not happened yet has already entered that day's feature.

The comparison scale uses only the past. From index 5 onward, the scale on a day uses the mean and standard deviation of the closes before that row. It does not use the current close, and it does not use later opens. Rows that do not yet have a long enough past are left undefined. The target is the simple return. Two in-sample lines fit that return, one on the leaky close and one on the past-only close.

The two residual sums of squares use one mask: the rows on which the past-only scale is already defined. The leaky scale is defined on those rows as well, because it used every open on every row. On that shared mask, the RSS of the return on the leaky close is 0.2642, and the RSS of the return on the past-only scaled close is 0.2650. The two differ by 0.0008.

The gap 0.0008 is small. It is not evidence that the leaky fit is better, and today does not write 0.2642 down as a score that beats 0.2650. On day 28, today's high pulled the sum of squares down by 3.6518, and the gap was obvious. Today's gap sits in the fourth decimal. If leakage had to be identified by a clear drop in the sum of squares, 0.0008 would be let through. The identification is written in the definition of the scale: the mean and standard deviation of the leaky scale take later opens as arguments. The last printed line says the leaky scale is a function of later opens.

## Core

```text
leaky scale uses every open, including later ones
RSS of return on leaky close = 0.2642
RSS of return on past-only close = 0.2650
the leaky scale is a function of later opens
```

Let `open` be the open on every row. The leaky feature is

`mean(open)` and `std(open)` use every open in the series, including opens after `t`. The past feature is defined from index 5 onward:

The window is the closes before that row. The return `r` is fit by in-sample least squares with an intercept, once on `z` and once on `z^{past}`. The mask is the rows, among those used in the regression, on which `z^{past}` is finite. Both RSS values share it.

The difference is 0.0008. The two sums of squares sit next to each other. Whether the scale leaks depends on whether later opens are among the arguments of `z_t`. They are, so this is a leaky scale. The ordering of 0.2642 and 0.2650 does not enter that judgment, and it does not promote the lower one into a better score. The shared mask keeps the two sums of squares from becoming incomparable through a different row count. Once they are comparable, the identification still comes from the definition, not from 0.0008.

## Further out

A standardization looks like nothing more than subtracting a mean and dividing by a standard deviation. If the mean and the standard deviation are computed on the whole sample, observations that lie later in time enter the feature of an earlier day. An open is a price. Once a later open enters today's scale, today's feature contains a later price level. Fitting a return with that feature uses a column that is not clean on the calendar.

The sum of squares can barely move. 0.2642 and 0.2650 differ by 0.0008. A reading that watches only for a clear fall in RSS would treat the two columns as similar fits. In definition they are not the same: one is a function of every open, and the other is a function of past closes. Similar sums of squares do not cancel that difference. Day 28 used a large fall, 3.6518, to show same-day information. Today uses a small difference, 0.0008, to show a second sentence: leakage can be identified while the sum of squares barely changes.

The mask has to be the same, or else 0.0008 itself would mix in a difference of row counts. The past-only scale is undefined at the start of the series. The leaky scale is defined everywhere. If the leaky scale were allowed to use those opening rows and the past-only scale were not, the two RSS values would no longer be sums over the same returns. The program takes the mask on which the past-only scale is finite, and both regressions sit on that mask. So 0.2642 and 0.2650 are two sums of squares on the same rows. Their difference does not announce which fit is better. What announces the leak is that the scale read in later opens.

**Quiet leakage.** RSS 0.2642 vs 0.2650 differs by 0.0008 yet future=yes. Audit the information source, not the gain magnitude.

## What the run showed

```bash
python days/29-future-open/future_open.py
```

The script prints that the leaky scale uses every open, including later ones, `RSS of return on leaky close = 0.2642`, `RSS of return on past-only close = 0.2650`, and `the leaky scale is a function of later opens`. The implementation is [`future_open.py`](../../days/29-future-open/future_open.py).

The two RSS values are 0.2642 and 0.2650, a difference of 0.0008, on the same mask. The fact that identifies the leak is that later opens are arguments of the scale. Next, each day may use only a fixed window of the past. The information set is no longer the whole table.
