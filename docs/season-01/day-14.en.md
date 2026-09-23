<p align="center"><a href="day-14.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 14 · A constant baseline

[Phase I · Models](../../README.en.md) · runs

On the sign labels, always guessing down scores 0.25 and always guessing up scores 0.75. The baseline reads no price. Without the 0.25 beside it, 0.75 has no control.

```bash
python days/14-constant-baseline/baseline.py
```

```text
always-down accuracy = 0.25
always-up accuracy = 0.75
the baseline looks at no price
```

Next the two mistakes are counted apart, instead of being folded into one accuracy.
