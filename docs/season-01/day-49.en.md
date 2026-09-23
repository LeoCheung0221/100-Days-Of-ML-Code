<p align="center"><a href="day-49.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 49 · One jump, three models

[Phase I · Models](../../README.en.md) · runs

The adjusted close on 2024-02-28 is 12.0142. The line's slope is 0.0299 and the ridge slope is 0.0201. The two lines cross on that day, so both fitted values are 11.0315 and both residuals are 0.9827. Ten sessions later the line is 11.3305 and ridge is 11.2326. The penalty separates them in level only away from the crossing. The tree fits 11.7285 that day, residual 0.2857, and it is still 11.7285 ten sessions later. It put the stretch in a higher leaf. It was not carried there by a slope.

```bash
python days/49-one-jump/one_jump.py
```

```text
jump date = 2024-02-28
adj close = 12.0142
line slope = 0.0299 ridge slope = 0.0201
line at jump = 11.0315  residual = 0.9827  ten later = 11.3305
ridge at jump = 11.0315  residual = 0.9827  ten later = 11.2326
tree at jump = 11.7285  residual = 0.2857  ten later = 11.7285
```

Next the three models vote on the one-step direction in the later stretch. Find a day when all three are wrong and the vote is wrong too.
