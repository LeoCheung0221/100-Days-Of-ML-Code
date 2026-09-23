<p align="center"><a href="day-27.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 27 · A split by time

[Phase I · Models](../../README.en.md) · runs

The time split scores 0.5417. The random split on the same series scores 0.4583. Both are printed. This time the time split is higher. A random split of one name did not inflate the score. Putting a second name in, so that one date can sit on both sides, is day 37.

```bash
python days/27-time-split/time_split.py
```

```text
time-split test accuracy = 0.5417
random-split test accuracy = 0.4583
the test of the time split sits entirely after the train
```

Next today's high explains today's close, and that column is marked forbidden.
