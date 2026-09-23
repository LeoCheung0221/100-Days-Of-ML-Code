<p align="center"><a href="day-41.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 41 · The line on a longer sample

[Phase I · Models](../../README.en.md) · runs

The adjusted return on 2024-02-28 is 0.1349. Delete that session and the slope is still 0.029901 to six decimals. The intercept falls from 9.8654 to 9.8528. The fitted value that day falls from 11.0315 to 11.0189, a shift of 0.0126. On day 5, with five points, deleting session 4 lowered the slope by 1.1729. On the longer sample the same kind of jump barely moves anything but the intercept.

```bash
python days/41-longer-line/longer_line.py
```

```text
jump date = 2024-02-28
adjusted return that day = 0.1349
slope with the jump = 0.029901
slope without the jump = 0.029901
intercept with the jump = 9.8654
intercept without the jump = 9.8528
fitted at the jump, with = 11.0315
fitted at the jump, without = 11.0189
```

Next the slope is penalized. The tilt is no longer allowed to stay at 0.0299.
