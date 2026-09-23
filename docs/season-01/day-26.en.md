<p align="center"><a href="day-26.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 26 · A random split

[Phase I · Models](../../README.en.md) · runs

Seed 1, training fraction 0.70, and the sign of the lagged return predicts the next step. Test direction accuracy is 0.4583. This is the control. It is not yet set beside the time split.

```bash
python days/26-random-split/random_split.py
```

```text
split = random, seed 1, train fraction 0.70
test direction accuracy = 0.4583
this number is the control
```

Next the split is by time, the test sits entirely after the train, and both accuracies are printed.
