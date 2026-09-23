<p align="center"><a href="day-30.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 30 · A fixed lookback

[Phase I · Models](../../README.en.md) · runs

What you learn today: the lookback is 20. At the last time index, the value fit on every finite adjusted close is 12.1976, the value fit on those 20 days is 12.0095, and the difference is 0.1881. The information set is those 20 days, not the whole table.

## Plain-language account

The rows are still the AAA rows whose close and adjusted close are both finite. Adjusted close is regressed on the time index by ordinary least squares, with an intercept. The index runs from the start of this series to the end. The full-sample fit uses every such adjusted close. The window fit uses only the last 20. Both lines are evaluated at the last index. That last index belongs to the 20 days, and it also belongs to the full sample. Both numbers are therefore fitted values inside the window, or inside the full sample. They are not a forecast made after holding the last day out.

The full-sample fitted value on the last day is 12.1976. The 20-day window's fitted value on that same day is 12.0095. Subtracting 12.0095 from 12.1976 leaves 0.1881. On the same day and the same index, the two lines differ by 0.1881. The difference comes from which rows entered the least squares. The full sample includes the sessions before the window. The window includes only those 20 days.

The number 0.1881 is not a trading profit, and it is not the last day's close. The program does not print the realized close beside these two fitted values. It prints the fitted level under two information sets. If the information set is the whole stretch of the table that the fit uses, the fitted value is 12.1976. If the information set is only the last 20 days, the fitted value is 12.0095. Today treats the second number as the window's value, because the rows allowed into the estimate are those 20. The earlier rows that the rest of the table would add are not in this information set.

## Core

```text
lookback = 20
full-sample value at last t = 12.1976
window value at last t = 12.0095
the full sample is not the information set
```

Let the time index be `t = 0, 1, …` and the adjusted close be `P_t`. The full-sample line and the window line are both

```text
P̂_t = α + β t
```

The full-sample `α, β` are estimated on every finite adjusted close. The window's `α, β` are estimated on only the last 20 pairs `(t, P_t)`. The query is the last index `t*`, and it lies inside those 20 indexes.

```text
P̂^{full}(t*) = 12.1976
P̂^{20}(t*) = 12.0095
12.1976 − 12.0095 = 0.1881
```

The 0.1881 is the difference of two fitted values. The two fitted values use the same query day and different rows. The information set of the window value 12.0095 is those 20 days. The information set of the full-sample value 12.1976 is the whole stretch of finite adjusted closes. The print says the full sample is not the information set: when the declared history has length 20, the rows that enter the estimate are not the whole table.

The last index lies inside the window, so 12.0095 is the fitted level of the 20-day line at the end of the window. It does not answer how the previous 20 days would predict a day outside the window. Today does not print a holdout error for that question. What it prints is that, after the information set is changed, the fitted value on the same day moves by 0.1881.

## Further out

A fixed lookback writes the number of rows used in the estimate as a length given in advance. The length is 20. It is not "use every day from the first row of the table through the query." If the query day used the full sample, earlier sessions would enter the slope and the intercept, even if the declaration was that only the latest 20 days were in view. The gap between 12.1976 and 12.0095, which is 0.1881, is how far the fitted level at the end moves when those earlier rows are still inside the estimate. The direction and size of the move are fixed by the adjusted closes on this frozen table. Today only reports the difference that has already been computed.

The point at the end of the window takes part in the window's own least squares. So 12.0095 absorbs the last day's adjusted close. It is a fitted value, not an extrapolation made after hiding that day. Reading 12.0095 or 12.1976 as a prediction of an unseen close would call an in-sample fitted level a holdout score. Their difference, 0.1881, likewise only compares two in-sample fits. It measures how far the level at the end changes once the information set shrinks from the whole stretch to 20 days.

Day 28 forbade the high on the same row. Day 29 showed a scale that had read in later opens. Today restricts the length of the past: rows earlier than these 20 days, although they have already happened, do not enter this window line. Having already happened and being allowed into the information set are two different things. The earlier rows are already written in the file. The window regression does not read them. The information set is those 20 days, the fitted value is 12.0095, and it differs from the full-sample fitted value 12.1976 by 0.1881.

## What the run showed

```bash
python days/30-fixed-lookback/lookback.py
```

The script prints `lookback = 20`, `full-sample value at last t = 12.1976`, `window value at last t = 12.0095`, and `the full sample is not the information set`. The implementation is [`lookback.py`](../../days/30-fixed-lookback/lookback.py).

The lookback is 20 days. At the last index the full-sample fitted value is 12.1976, the window fitted value is 12.0095, and the difference is 0.1881. The information set is those 20 days. Next the window shrinks to three days, and the local slope can change sign with the moves inside those three days.
