<p align="center"><a href="day-23.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 23 · Three days the same way

[Phase I · Models](../../README.en.md) · runs

The rule is in the program before the count: after three adjusted moves of the same sign, predict that the fourth matches. There are 11 events, 6 hits, accuracy 0.5455. The condition was not rewritten after the result.

```bash
python days/23-three-day-run/three_day_run.py
```

```text
rule = after three equal signs, predict the fourth matches
events = 11
hits = 6
accuracy = 0.5455
the rule is fixed before the count
```

Next the same rule is scored only on the later stretch. The early accuracy is not the score.
