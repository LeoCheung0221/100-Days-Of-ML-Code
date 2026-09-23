<p align="center"><a href="day-43.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 43 · A local mean

[Phase I · Models](../../README.en.md) · runs

What you learn today: the query date is 2024-03-20. The five time-neighbors run from 2024-03-18 through 2024-03-22 and do not include the jump date 2024-02-28. The local mean is 11.6932. Ordinary least squares on the full sample reads 11.4800 at the same query. The jump date stays inside the normal equations and stays outside the neighbor set.

## Plain-language account

Stand on 2024-03-20 and keep only the five adjusted closes whose session indices are nearest the query. The nearest row is the query itself, at distance 0. The other four are 2024-03-19, 2024-03-21, 2024-03-18, and 2024-03-22. The script prints them by increasing distance, and on a tie the earlier date comes first, so the printed order is 2024-03-20, 2024-03-19, 2024-03-21, 2024-03-18, 2024-03-22. Those five dates cover 18 March through 22 March. 28 February is not among them.

The arithmetic mean of those five adjusted closes is 11.6932. There is no slope and no normal equation. The query's own label is one of the five numbers. 11.6932 is a local mean that includes the query. It is not a score with the query held out.

On the same date, the full-sample line from day 41 reads 11.4800. That line has slope 0.029901 and intercept 9.8654, estimated on all 79 adjusted closes. 2024-02-28 is still inside XᵀX and Xᵀy. The local mean left that day outside the neighbor set. The two readings sit side by side: neighbor average 11.6932, line 11.4800, gap 0.2132. The gap is an information-set gap. One side uses five sessions. The other uses the whole stretch, and the jump is still in that stretch.

The claim is this. The neighbor set behind 11.6932 does not contain 2024-02-28. The ordinary least-squares reading 11.4800 is produced by normal equations that still contain that day.

## Core

```text
query date = 2024-03-20
neighbor dates = 2024-03-20 2024-03-19 2024-03-21 2024-03-18 2024-03-22
jump date in the neighbors = false
local mean = 11.6932
ols at the query = 11.4800
```

The series is still the 79 AAA adjusted closes. Neighbors are the five rows with smallest |t − t_query|. The sort is stable, so equal distances keep their original order: the query, then the previous session, then the next, then two sessions back, then two sessions forward.

11.6932 − 11.4800 = 0.2132 is the gap between the two printed readings. The local mean has no coefficient. The line's value at the query is slope times the query index plus intercept, and those coefficients come from all 79 rows. Membership of the jump date is a set test. The print is false.

The five neighbors are neighbors in time, not in price. Which adjusted close sits nearer some level does not decide the five dates. The only rule is distance on the index. 2024-02-28 is farther from 2024-03-20 than those five sessions, so it cannot enter the average. It can still enter the full-sample Xᵀy.

The query is inside the five. Subtracting the query's own adjusted close from 11.6932 would build a residual that already used its own label. That residual is not today's score. Today's comparison is two readings at the query abscissa: the local mean, and the full-sample line.

## Further out

A local mean is a hard kernel: the bandwidth keeps five nearest indices, weights inside the kernel are equal, and everything else is 0. A narrow bandwidth takes the vote away from distant sessions. The adjusted return on 2024-02-28 is 0.1349, and day 41 already showed that deleting it barely moves the full-sample slope. Today takes a different route. The point stays in the sample, and the query simply refuses distant neighbors. The evidence is the neighbor list, and `jump date in the neighbors = false`.

The full-sample line cannot refuse that row. The normal equations sum over every row. The jump's adjusted close, times its index, enters Xᵀy. As long as that row is one of the 79, it participates in 11.4800. The local mean's average does not contain that row. The two estimators can read 11.6932 and 11.4800 on the same query date because they read different samples.

The five neighbors include the query, so this is not the holdout of day 7. A holdout removes the query from the estimate and only then talks about error. Today's local mean counts the query inside 11.6932. Treating that number as an out-of-sample score uses the wrong information set. An out-of-sample cut arrives with the first 59 training sessions on day 44.

Local mean 11.6932 vs OLS 11.4800 at 2024-03-20; jump date not in five neighbors.

Local mean includes the query day in the five neighbors; it is not a holdout score like day 7.

**Local vs global.** Five-day local mean 11.6932 vs OLS 11.4800 at 2024-03-20; jump not in neighbors.

## What the run showed

```bash
python days/43-local-mean/local_mean.py
```

The script should print the query `2024-03-20`, the five neighbor dates above, `jump date in the neighbors = false`, `local mean = 11.6932`, and `ols at the query = 11.4800`. The implementation is [`local_mean.py`](../../days/43-local-mean/local_mean.py).

Hand in the two information sets: the five neighbors omit the jump date, and the full-sample line still contains it. Day 44 cuts the first 75 percent into 59 training sessions and replaces the slope with a tree that splits once.
