<p align="center"><a href="day-49.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 49 · The same jump day

[Phase I · Models](../../README.en.md) · runs

What you learn today: the adjusted close on 2024-02-28 is 12.0142. The full-sample line has slope 0.0299 and ridge has slope 0.0201, with λ = 20000 on the slope only and the intercept free. The two lines cross at the jump index, so both fitted values are 11.0315 and both residuals are 0.9827. Ten sessions later the line is 11.3305 and ridge is 11.2326. The tree at the jump is 11.7285, residual 0.2857, and it is still 11.7285 ten sessions later.

## Plain-language account

Return to 2024-02-28. The adjusted close that day is 12.0142. The adjusted return 0.1349 was already read on day 41. Today the day is not deleted. All three fits are estimated on the full 79 adjusted closes, then read at the jump index and at the session ten steps later.

The line slope is 0.0299 and the ridge slope is 0.0201. The penalty is still 20000, added to the slope entry of the full-sample Gram matrix. It is not 50, and it is not the penalty that was applied only to the first 59 rows. The slopes differ, and each intercept adjusts. At the jump index both fitted values print as 11.0315. The lines meet there. Both residuals are 12.0142 − 11.0315 = 0.9827. On the day they meet, ridge and ordinary least squares do not separate in level.

They separate ten sessions later. The line's fitted value is 11.3305 and ridge's is 11.2326. The steeper slope rises more. The gap between 0.0299 and 0.0201 becomes a gap in level only after the index leaves the crossing. At the crossing itself both rows are 11.0315 and 0.9827.

The tree is depth 2, fit on the same 79 points. The leaf value on the jump date is 11.7285, and the residual is 12.0142 − 11.7285 = 0.2857. Ten sessions later the fitted value is still 11.7285. The leaf is constant on this stretch of the index. No slope carries the level forward. 11.7285 is higher than the 11.0315 shared by the two lines on the jump date, so the leaf sits above both lines at that index. The tree put the stretch in that higher leaf. The level is the leaf mean. It is not 0.0299 or 0.0201 multiplied forward.

## Core

```text
jump date = 2024-02-28
adj close = 12.0142
line slope = 0.0299
ridge slope = 0.0201
lambda = 20000, slope only, full sample
line  at jump = 11.0315   residual = 0.9827   ten later = 11.3305
ridge at jump = 11.0315   residual = 0.9827   ten later = 11.2326
tree  at jump = 11.7285   residual = 0.2857   ten later = 11.7285
```

At the jump index the gap between the line and ridge is 11.0315 − 11.0315 = 0. The gap in residuals is 0 as well. Ten sessions later, 11.3305 and 11.2326 are no longer the same number. A sentence about how far the two lines sit apart on the jump date uses that day's 11.0315. A sentence about the penalty's effect on the level uses the two numbers ten sessions later.

The tree residual 0.2857 is smaller than the line residual 0.9827 because 11.7285 is closer to 12.0142 than 11.0315 is. That is the distance in the jump-date cell. It is not a later-stretch SSE, and it is not the extrapolation at t = 118. The rightmost leaf read on day 48 at t = 118 is 11.9608, a different constant from this 11.7285. The jump date and the session ten steps later share 11.7285, so those two indices fall in the same leaf.

Day 41 deleted this session and the slope stayed 0.029901. Today the session stays, the line slope prints as 0.0299 to four decimals, and ridge pulls it to 0.0201. Deletion barely moves the slope. The penalty moves the slope. The moved slope does not yet show up as two different fitted values on the crossing date.

## Further out

Two lines with different slopes cross at most once. Which index holds the crossing depends on both intercepts and both slopes. Today's printout places the crossing on the jump index: both sides are 11.0315. This date therefore cannot display "ridge sits closer to the jump price than the line does." Both are the same distance away, residual 0.9827. The level effect of the penalty is read away from the crossing. Ten sessions later the line is 11.3305 and ridge is 11.2326, and the slope gap has been written into the price.

The tree holding 11.7285 across ten adjacent sessions is the shape of a piecewise constant. The jump price 12.0142 sits 0.2857 above the leaf, and that 0.2857 does not turn into a slope along the leaf. Reading the smaller tree residual as "the tree tilted along with the jump" does not match a fitted value that is still 11.7285 ten sessions later. What moves are the two lines that have slopes: from 11.0315 to 11.3305, and from 11.0315 to 11.2326.

λ on the full sample is still 20000. Day 46's training SSE 16.3596 belongs to the first 59 rows and does not replace today's 0.0201. Today does not print a sum of squares. It prints levels on the jump date and ten sessions later.

## What the run showed

```bash
python days/49-one-jump/one_jump.py
```

The script should print the jump date `2024-02-28`, adjusted close `12.0142`, slopes `0.0299` and `0.0201`, and both the line and ridge at the jump as `11.0315` with residual `0.9827`, then ten sessions later `11.3305` and `11.2326`. The tree is `11.7285` with residual `0.2857`, and ten sessions later it is still `11.7285`. The implementation is [`one_jump.py`](../../days/49-one-jump/one_jump.py).

Hand in the shared fitted value at the crossing, and the constant leaf. Day 50 votes on one-step direction along the later stretch, and records what a majority produces when all three models are wrong.
