<p align="center"><a href="day-13.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 13 · Threshold sensitivity

[Phase I · Models](../../README.en.md) · runs

The constant-up accuracy is 0.75, 0.50, and 0.25 at thresholds 0.50, 0.70, and 0.90. Raising the threshold by 0.40 lowers the accuracy by 0.50. One of those accuracies, alone, does not say which cut it depends on.

```bash
python days/13-threshold-sensitivity/sensitivity.py
```

```text
threshold  accuracy
0.50  0.75
0.70  0.50
0.90  0.25
```

Next comes a baseline that looks at nothing: always guess down.
