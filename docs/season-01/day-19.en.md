<p align="center"><a href="day-19.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 19 · Unscaled volume

[Phase I · Models](../../README.en.md) · runs

What you learn today: the raw beta on time is 1.482253 and the raw beta on volume is 1.731932e-06, while the mean absolute contributions are 4.4468 and 4.3645. After standardization the beta on time is 2.7049 and the beta on volume is 4.7815. The tiny raw volume coefficient is a units illusion, in shares, not evidence that volume can be dropped.

## Plain-language account

Two columns now sit on the five sessions. Time is 1, 2, 3, 4, 5. Volume is 1.0e6, 1.2e6, 0.9e6, 8.0e6, and 1.5e6, in shares. The two columns together fit the five closes 2.1, 3.9, 6.2, 20.0, and 10.4. The fit returns two raw coefficients: time 1.482253, volume 1.731932e-06.

Set those two coefficients side by side and volume looks as if it can be ignored: 1.731932e-06 is several orders of magnitude smaller than 1.482253. That comparison is a comparison of two units. The coefficient 1.482253 is the price coefficient on the time column. The coefficient 1.731932e-06 is the price coefficient per share. A day and a share are not the same scale. The volume numbers themselves sit near a million shares. A per-share coefficient multiplied by a volume counted in shares comes back to the scale of price. The coefficient is small because the column it multiplies is large.

The mean absolute contribution forms that product and then averages the absolute value. The mean absolute contribution of the time column is 4.4468. The mean absolute contribution of the volume column is 4.3645. Both numbers are on the scale of price, and they sit close to each other. On that scale the volume column has not disappeared from the fit just because its coefficient was printed in scientific notation.

Subtract each column's own mean, divide by its own standard deviation, and fit again. The standardized coefficient on time is 2.7049, and the standardized coefficient on volume is 4.7815. Both columns are now in units of one standard deviation, and the coefficients can be compared in size. The volume coefficient 4.7815 is larger than the time coefficient 2.7049. The suggestion, coming from the raw 1.731932e-06, that volume is almost irrelevant, does not hold once the units are aligned. The tiny raw coefficient is an illusion produced by the share unit. It is not evidence that volume can be dropped from the columns.

## Core

The two raw coefficients:

```text
raw beta time   = 1.482253
raw beta volume = 1.731932e-06
```

The contribution of column j on a session is the coefficient times that column's raw value. Average the absolute contribution over the five sessions:

```text
mean |time contribution|   = 4.4468
mean |volume contribution| = 4.3645
```

The values 4.4468 and 4.3645 can be compared, because each has been multiplied back by its own column and both are in price units. The values 1.482253 and 1.731932e-06 cannot decide what to keep by asking which is closer to 0, because their units are price per unit of time and price per share.

Standardization is applied to the columns: subtract the mean of the five values in the column, divide by the standard deviation of the column, and run least squares again. The new coefficients are

```text
standardized beta time   = 2.7049
standardized beta volume = 4.7815
```

In these units the volume coefficient is larger than the time coefficient. The direction is the opposite of the visual impression of the raw coefficients. The raw impression comes from writing 1.731932e-06. The standardized result comes from comparing 4.7815 with 2.7049. Before the units are aligned, the smaller coefficient can be nothing more than the larger unit of measurement.

The time coefficient 1.482253 is also not the slope 3.27 of the earlier one-variable line. The slope 3.27 belongs to `ŷ = 3.27x − 1.29`, whose columns are time and an intercept. Today's raw fit places time and unscaled volume in one least-squares problem, and the coefficients are reallocated. Reading 1.482253 as if it were 3.27, or reading today's volume coefficient through 3.27, treats two different column spaces as one coefficient. The comparison that belongs to today stays inside one fit: one pair of raw coefficients, one pair of mean absolute contributions, one pair of standardized coefficients.

An argument for dropping volume that cites only 1.731932e-06 does not say where the mean absolute contribution 4.3645 sits on the price scale. The value 4.3645 and the time value 4.4468 are two numbers on the same contribution table. Dropping this column drops an input whose mean absolute contribution is comparable to the time column. The standardized coefficient 4.7815 adds that, once the columns are aligned by their standard deviations, this column's coefficient is larger than time's 2.7049. That is a fact about the fit on these five points. What it rules out is the sentence produced by the units: the coefficient is small, so the column can be deleted.

## Further out

When time and volume are placed together, the units of the columns often differ by several orders of magnitude. A price-on-time coefficient and a price-on-shares coefficient, printed on the same line, let the position of the decimal point imitate importance. If importance means the contribution to the fitted value, the object to look at is the size of the coefficient times the column. Today's summary of that size is 4.4468 and 4.3645. The two summaries are close. The raw coefficients are 1.482253 and 1.731932e-06. The illusion sits in that pair of comparisons.

The standardized coefficients are another summary, with the unit changed to each column's own variation. Across the five days, volume runs from 0.9e6 to 8.0e6, and time runs only from 1 to 5. Volume's raw numbers are large, so its raw coefficient is compressed. Time's raw numbers are small, so its raw coefficient looks large. Dividing by the standard deviation moves that scale out of the coefficient. After it is moved, comparing 2.7049 with 4.7815 asks which coefficient is larger when each column moves by one standard deviation. The volume coefficient is larger. That answer does not delete time from the columns, and it does not extend the conclusion into a claim that volume is useful on every other sample. What it forbids is a deletion decision made from 1.731932e-06 alone.

A coefficient printed in scientific notation is followed by its unit, and then by the mean absolute contribution or the standardized coefficient. With all three lines present, a small coefficient can be told apart as a unit of measurement or as a contribution that really is near 0. Today's contribution is not near 0: 4.3645 sits beside time's 4.4468. Volume stays on this table.

Compare mean absolute contributions 4.4468 vs 4.3645, not raw betas 1.482253 vs 1.731932e-06. Standardized volume beta 4.7815 exceeds time 2.7049— opposite of the raw coefficient eyeball. Conclusions stay within these five rows.
Lead with contribution means 4.4468 vs 4.3645 when arguing column importance on these five rows.
On five rows, small raw volume beta with sizable mean contribution is a units lesson, not a delete-column lesson.
## What the run showed

```bash
python days/19-unscaled-volume/unscaled.py
```

The script prints the raw time coefficient 1.482253, the raw volume coefficient 1.731932e-06, the mean absolute contributions 4.4468 and 4.3645, and the standardized coefficients 2.7049 and 4.7815. The implementation is [`unscaled.py`](../../days/19-unscaled-volume/unscaled.py).

The coefficient 1.731932e-06 is a price coefficient per share. After it multiplies a volume counted in shares, the mean absolute contribution is 4.3645, on the same price scale as time's 4.4468. After standardization the volume coefficient 4.7815 is larger than the time coefficient 2.7049. The small raw coefficient is a units illusion, not evidence that volume can be dropped.
