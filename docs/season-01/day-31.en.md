<p align="center"><a href="day-31.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 31 · Noise in a three-day window

[Phase I · Models](../../README.en.md) · runs

What you learn today: forecasting the last adjusted close, the three-day slope is −0.1195 and the twenty-day slope is 0.0251. The signs disagree. The three-day absolute miss is 0.0867 and the twenty-day absolute miss is 0.1506. The short window is chasing a local direction. Its smaller miss on this one day is not a claim that it is more accurate. The miss is printed on its own.

## Plain-language account

The last adjusted close stays outside the fit and is used only as the answer. The three sessions before it, with their time index, give a least-squares slope of −0.1195, so the line falls. The twenty sessions before it give a slope of 0.0251, so the line is still rising. One close, two directions.

Each line is evaluated at the last time index and compared with that adjusted close in absolute distance. The three-day line is 0.0867 away. The twenty-day line is 0.1506 away. The two misses each get their own line. 0.0867 is smaller than 0.1506, which says that on this day the short window sits closer to this one close. Three points follow a local direction. The twenty-day slope still carries the positive sign of the longer stretch. The short window is chasing a local direction. One smaller absolute miss, on a sample of this single day, does not rank window lengths by accuracy.

## Core

The slopes come from rows before the endpoint. The three-day slice is the three time indices before the end. The twenty-day slice is the twenty time indices before the end. The endpoint's adjusted close enters the absolute miss and stays out of `lstsq`.

```text
three-day slope = -0.1195
twenty-day slope = 0.0251
three-day absolute miss = 0.0867
twenty-day absolute miss = 0.1506
```

−0.1195 and 0.0251 are the signs on the slopes. 0.0867 and 0.1506 are the two miss lines. Read a window by listing the sessions inside the information set, then by reading that day's distance. A smaller distance is this print. Which window is more accurate is a comparison on a scoring stretch chosen in advance, and that stretch is not reused to pick the window again. Today does not publish that ranking.

An absolute miss on the price level and a statement about direction are separate. The signs already place the last day on opposite sides of flat. The short window can be closer in price and still be the direction that three points are able to flip.

## Further out

Window length is the boundary of the information set. Once the rows are chosen, the normal equations see only those rows. The three-day design has the three time indices before the endpoint, so a turn at the end can pull the slope through zero to −0.1195. The twenty-day window keeps the earlier sessions inside `XᵀX` and `Xᵀy`, and the slope stays at 0.0251. The two lines therefore extrapolate to the same time index from opposite directions, at absolute distances 0.0867 and 0.1506.

The short window asks how far the recent direction lands on this last close. The long window asks how far the slope already formed over its own stretch lands on the same close. Each question has its own distance. Writing the smaller distance up as a model-selection result awards the window length for one day's residual. A comparison of lengths states the lengths first and then reports absolute error, or a direction hit, on a held-out run of sessions, without looking at the misses and then changing the length. This script has no such run. The order of 0.0867 and 0.1506 stays on this one endpoint.

The miss and the slope are stored apart. −0.1195 is the slope on the three-day slice. 0.0251 is the slope on the twenty-day slice. 0.0867 and 0.1506 record how close each line came. They leave the disagreement in direction in place. If a later endpoint named in advance shows a larger three-day miss, that print stays on its own line and does not go back and rewrite today's 0.0867 as an accuracy advantage. A comparison of window lengths accumulates many endpoints. This pair of numbers covers this one endpoint. Next the window is sixty sessions, set beside these three.


<!-- uniq-exp-en-27-50 -->

Slopes −0.1195 vs 0.0251; misses 0.0867 vs 0.1506 at one endpoint. Smaller miss is not a window championship without a pre-specified holdout set.


<!-- uniq-exp-en2 -->

Hand in all four printed numbers and state that endpoint miss does not rank window length. Re-run the script before narrating.

## What the run showed

```bash
python days/31-three-day-noise/three_day_noise.py
```

The script should print the three-day slope −0.1195, the twenty-day slope 0.0251, the three-day absolute miss 0.0867, and the twenty-day absolute miss 0.1506. The implementation is [`three_day_noise.py`](../../days/31-three-day-noise/three_day_noise.py).

Hand in the two slopes and the two misses for this day. The short window is chasing a local direction. The smaller miss stays on its own line and is not rewritten as three days being more accurate.
