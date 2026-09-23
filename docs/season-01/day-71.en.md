<p align="center"><a href="day-71.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 71 · Three day classes

[Phase I · Models](../../README.en.md) · runs

What you learn today: On the AAA five-lag line hold-out, label quiet=10 and jump=5 by actual |return|; direction wrong on 3 days.

## Plain-language account

Day 71 keeps the frozen five-lag line from day 51 and reads labels and predictions on nineteen hold-out rows. Classes use the actual same-day simple return magnitude, not |ŷ|.

quiet means |y| at or below the test median of |y|. jump means |y| at or above the test seventy-fifth percentile. Rows between are mid in code; this print gives quiet and jump counts only. quiet=10 places about half the test days at or below the median move; jump=5 marks the top volatility slice.

Direction wrong counts sign(y) ≠ sign(ŷ), total 3. Direction is orthogonal to quiet/jump—a jump day can be direction-right and a quiet day direction-wrong. direction wrong=3 is not a partition of quiet or jump.

The claim stops at these three integers on the same lag-5 line and seventy-five percent split.

## Core

```text
quiet days = 10
jump days = 5
direction wrong days = 3
```

## Further out

Cross-check: quiet and jump use |y| with median and p75 on the nineteen test rows only, not train quantiles.

Next lesson: MAE on quiet only versus all-test MAE 0.006980. jump=5 is not «five direction-wrong jumps»; direction wrong stays 3.

## What the run showed

```bash
python days/71-three-classes/three_classes.py
```

The script should print `quiet days = 10`, `jump days = 5`, `direction wrong days = 3`. The implementation is [`three_classes.py`](../../days/71-three-classes/three_classes.py).

Hand in quiet, jump, and direction-wrong counts. Next: mean absolute error on quiet days.
