<p align="center"><a href="day-42.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 42 · Ridge

[Phase I · Models](../../README.en.md) · runs

What you learn today: on the same AAA adjusted-close stretch, the penalty sits on the slope only, λ = 20000, and the intercept is free. The ordinary least-squares slope is 0.0299. The ridge slope is 0.0201. The line is required to tilt 0.0098 less.

## Plain-language account

Day 41's line lies on the 79 adjusted closes. Its slope is 0.029901 to six decimals, which prints as 0.0299 to four. Today nothing is deleted. A positive number is added to the slope entry of the normal equations, so tilt has a cost, and the new slope is read off.

The design has two columns: the session index t, and a column of ones. Ordinary least squares solves XᵀX β = Xᵀy. This ridge changes only the top-left entry. That entry is Σt², and λ is added to it. The intercept entry is untouched. The intercept still adjusts to the pulled slope. It has no penalty of its own. The λ in the script is 20000.

The slope moves from 0.0299 to 0.0201. The gap is 0.0098. Same adjusted closes, same axis: the line must rise 0.0098 price units less per session. 0.0201 is still positive. The piece removed from the tilt is 0.0098.

The scale of λ is read against Σt². The sum of squares of 79 session indices is already large. Replacing 20000 with 50 adds a number that is negligible beside that sum, and the slope stays next to the least-squares value. 50 is not today's penalty, and it is not day 49's penalty. Both days use 20000, on the slope only.

## Core

The estimation sample is the 79 adjusted closes from day 41, blank row already dropped. There is no train cut. The penalty is written into the Gram matrix:

```text
(XᵀX)₁₁  ←  Σt² + 20000
(XᵀX)₂₂  ←  n          (intercept, unpenalized)
```

The linear system is then solved. The intercept is a free parameter. Its equation contains no λ.

```text
lambda = 20000, penalty on the slope only
ols slope   = 0.0299
ridge slope = 0.0201
tilt reduction = 0.0299 − 0.0201 = 0.0098
```

0.0299 is day 41's slope 0.029901 printed to four decimals. Same ordinary least-squares fit, coarser print. The ridge value 0.0201 is a new estimate. The reduction 0.0098 is the difference of those two printed slopes. Report it with both operands.

The penalty raises curvature in the slope direction, so the slope is pulled toward 0 in absolute value. The intercept is outside the penalty. 0.0201 is not "the intercept was multiplied by a shrinkage factor." The script does not print the intercept. Today's numbers are the two slopes.

The in-sample sum of squares rises when the slope is pulled off the least-squares value. That is what a penalty does. The number waits until day 46, in one table with the line and the tree. It is not a score today.

## Further out

A slope of price on a session index has units of price per session. On these 79 indices, Σt² is already large. A two-digit λ added to that entry leaves the curvature almost where it was. That is why 50 does not act as a penalty on this index: it is too small to bargain with Σt². 20000 is large enough to move the slope from 0.0299 to 0.0201, a reduction of 0.0098. On a shorter index the same 20000 would press harder. λ has no standard value that detaches from the scale of the axis.

Penalizing the slope and leaving the intercept free matches a setting where the level may sit anywhere and the tilt must pay. The overall level of the adjusted price is still chosen by the data. Adding λ to both diagonal entries of the identity would also pull the intercept toward 0, and the fit would be a different line. That is not this script. This script adds 20000 only to the slope entry of the Gram matrix.

Shrinkage is not deletion. Day 41 removed 2024-02-28 and the slope stayed 0.029901. Today no point is removed, and the penalty brings the slope to 0.0201. The two days answer two questions. One jump on the long sample barely changes the slope. An explicit slope penalty does change the slope, once λ is large relative to Σt².

The penalty changes the slope, and the intercept refits around that new slope, but the script does not print the intercept. Today's reported numbers are 0.0299 and 0.0201, not a ridge equation with an intercept attached. The 0.0098 is a gap in the slope. The levels separate after the lines leave their crossing. That reading is day 49: at the jump index both the line and ridge are 11.0315, and ten sessions later they are 11.3305 and 11.2326. Today the penalty stays on the slope entry, and λ stays at 20000.

## What the run showed

```bash
python days/42-ridge/ridge.py
```

The script should print `lambda = 20000, penalty on the slope only`, then `ols slope = 0.0299` and `ridge slope = 0.0201`. The implementation is [`ridge.py`](../../days/42-ridge/ridge.py).

Hand in the 0.0098 reduction in tilt. The penalty is on the slope, and the intercept is free. Day 43 changes the local picture: average the five sessions nearest the query, and leave 2024-02-28 outside that neighbor set.
