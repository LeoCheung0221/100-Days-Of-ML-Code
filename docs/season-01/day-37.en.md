<p align="center"><a href="day-37.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 37 · Several names, mixed split

[Phase I · Models](../../README.en.md) · runs

AAA and BBB are stacked, and the sign of the same-day market return predicts each name. Random-split test accuracy is 0.7234. The time split scores 0.6170. The extra accuracy can come from one date sitting on both sides: one name in the train, the other in the test, sharing that day's market.

```bash
python days/37-mixed-names/mixed_names.py
```

```text
pooled AAA and BBB
random-split test accuracy = 0.7234
time-split test accuracy = 0.6170
the random split can train and test on the same date
```

Next the market signal is lagged by one day. The simultaneous part should disappear.
