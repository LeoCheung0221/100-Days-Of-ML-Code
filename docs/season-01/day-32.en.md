<p align="center"><a href="day-32.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 32 · A sixty-day window

[Phase I · Models](../../README.en.md) · runs

What you learn today: the same last session. The sixty-day slope is 0.0353 and the absolute miss is 0.4426. The three-day slope is still −0.1195 and the absolute miss is still 0.0867. The long window still sits on the older slope and is farther from the close on this day.

## Plain-language account

The endpoint is the same as yesterday. The last adjusted close is still used only as the answer. The three-day line is still the three sessions before the endpoint: slope −0.1195, absolute miss 0.0867. The sixty-day line uses the sixty sessions before the endpoint. The slope is 0.0353, positive, and opposite the three-day slope. Placed at the last time index, that line misses the close by 0.4426.

0.4426 is larger than 0.0867. On this one close the long window sits farther away. It has not followed the last three sessions down to a slope of −0.1195. The extrapolation stays on the older positive slope, 0.0353, and the distance to the latest close is pulled out to 0.4426. This day's distance says the long window is still sitting on the old slope. It does not hand window length a general accuracy rank. The sixty-day window is farther on this day, and the three-day window is closer on this day. Both sentences cover this one time index.

## Core

The sixty-day slice is the sixty time indices before the endpoint. The three-day slice is still the three time indices before the endpoint. The endpoint's adjusted close stays out of the slope.

```text
sixty-day slope = 0.0353
three-day slope = -0.1195
sixty-day absolute miss = 0.4426
three-day absolute miss = 0.0867
```

Read this beside yesterday. The twenty-day slope was 0.0251 and the absolute miss was 0.1506. The sixty-day slope is 0.0353 and the absolute miss is 0.4426. Lengthening the window from twenty sessions to sixty leaves the slope positive, and this day's absolute miss rises from 0.1506 to 0.4426. The added rows are earlier sessions. They hold the line on the old direction. The three-day slope −0.1195 is the direction of the last three points themselves. The three rows answer three different questions: the local direction, the slope already formed over twenty sessions, and the older slope the sixty-day window is still using. Each miss belongs to that information set at this one time index.

## Further out

Stretching the window from twenty sessions to sixty changes the rows in the design, not the last close. With more rows, the early prices still contribute to the normal equations, and the last three points do not flip the slope. Those three sessions already have slope −0.1195. The sixty-day slope is still 0.0353. The extrapolation keeps walking along the old upward direction and lands 0.4426 from a close that has turned. The three-day window has none of those earlier rows, so its slope is the end's own −0.1195 and the distance comes in to 0.0867.

0.4426 is how far the old slope sits on this day. Reading it as a permanent defect of long windows uses the same single residual that yesterday's 0.0867 would use if it were called an accuracy win for three days. A comparison of the lengths 3, 20, and 60 writes the scoring sessions down first, reports the miss for every length on that same stretch, and does not change the length after seeing the misses. This script has no such stretch. It puts sixty days and three days on one endpoint so the old slope's position is a distance that can be checked.

The sign gap between 0.0353 and −0.1195 says more about the information set than the gap between 0.4426 and 0.0867. Earlier prices among the sixty sessions are still in the equations, and the turn in the last three sessions does not pull the slope from positive to negative. Both distances describe this one close. Calling 0.4426 the typical error of a sixty-day window, or 0.0867 the typical error of a three-day window, goes past this one print.

The sixty-day slope 0.0353 and the three-day slope −0.1195 use the same endpoint and the same adjusted close. The difference is how long the slice is. 0.4426 is how far the sixty-session extrapolation sits from this close. 0.0867 is how far the three-session extrapolation sits from the same close. The two misses already have their own lines. That the long window is farther on this day stays on the 0.4426 line. That the short window is chasing a local direction stays on the −0.1195 line. Yesterday's twenty-day slope 0.0251 and absolute miss 0.1506 stay on their own print and are not folded into a ranking today. Next the question leaves window length and asks whether the mean and standard deviation used for scaling come from the training stretch, or whether they have also seen the test stretch.

## What the run showed

```bash
python days/32-sixty-day-window/sixty_day.py
```

The script should print the sixty-day slope 0.0353, the three-day slope −0.1195, the sixty-day absolute miss 0.4426, and the three-day absolute miss 0.0867. The implementation is [`sixty_day.py`](../../days/32-sixty-day-window/sixty_day.py).

Hand in the two lines at the same endpoint. The long window is still on the older positive slope 0.0353. On this day it sits 0.4426 from the close, farther than the three-day miss of 0.0867. That is this day's position, not a general ranking of window lengths.
