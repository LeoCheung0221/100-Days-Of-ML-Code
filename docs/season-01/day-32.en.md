<p align="center"><a href="day-32.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 32 · A sixty-day window

[Phase I · Models](../../README.en.md) · runs

On the same last session the sixty-day slope is 0.0353 and the absolute miss is 0.4426. The three-day slope is −0.1195 and the absolute miss is 0.0867. The long window is still sitting on the older slope, and on this day it is farther from the close.

```bash
python days/32-sixty-day-window/sixty_day.py
```

```text
sixty-day slope = 0.0353
three-day slope = -0.1195
sixty-day absolute miss = 0.4426
three-day absolute miss = 0.0867
```

Next the mean and variance may be estimated on the training stretch only.
