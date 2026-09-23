<p align="center"><a href="day-11.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 11 · Direction labels

[Phase I · Models](../../README.en.md) · runs

The score is now a direction hit, not a price distance. Three of the four steps hit. The absolute residual on session 4 is still 8.21, and that distance is no longer the score. The fitted slope is positive on every step, so 3/4 is the same rule as calling every step an up move.

```bash
python days/11-direction-labels/labels.py
```

```text
score = direction hits 3/4
day 4 absolute price residual = 8.21
that residual is not the score
```

Next the return is cut by a threshold you choose. The sign itself is no longer the label.
