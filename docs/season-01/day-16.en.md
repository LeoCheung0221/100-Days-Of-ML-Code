<p align="center"><a href="day-16.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 16 · Degree of being up

[Phase I · Models](../../README.en.md) · runs

The slope 3.27, passed through a sigmoid, is 0.9634. Every step receives that same number. The one-step change of an affine fit is constant, so this degree cannot rank the four steps.

```bash
python days/16-up-score/up_score.py
```

```text
slope = 3.27
P(up) = sigmoid(slope) = 0.9634
the same score is attached to every step
```

Next that 0.9634 is checked against how often the steps actually rise.
