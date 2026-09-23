<p align="center"><a href="day-17.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 17 · A check on stated confidence

[Phase I · Models](../../README.en.md) · runs

The stated probability of an up move is 0.9634. The realized frequency is 0.75. The gap is 0.2134. Of the steps called about ninety-six percent, three quarters actually rose. Confidence and frequency sit side by side. Neither replaces the other.

```bash
python days/17-confidence-check/confidence.py
```

```text
stated P(up) = 0.9634
realized up frequency = 0.75
gap = 0.2134
```

Next the input is no longer a single price. Return and volume decide the label together.
