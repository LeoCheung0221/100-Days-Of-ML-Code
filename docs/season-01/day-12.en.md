<p align="center"><a href="day-12.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 12 · A threshold

[Phase I · Models](../../README.en.md) · runs

The four returns are 0.8571, 0.5897, 2.2258, and −0.4800. At a threshold of 0.70 the labels are 1 0 1 0, and the constant-up rule scores 0.50. Against the sign labels on day 11, the same rule scored 0.75. Where the cut sits is part of the definition.

```bash
python days/12-threshold/threshold.py
```

```text
threshold = 0.70
returns = 0.8571 0.5897 2.2258 -0.4800
label up = 1 0 1 0
constant-up accuracy = 0.50
```

Next the threshold moves, and the change in accuracy has to be reported with it.
