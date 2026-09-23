<p align="center"><a href="day-44.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 44 · A shallow tree

[Phase I · Models](../../README.en.md) · runs

The train uses the first 59 adjusted closes. One split sends t > 38.50 to the right. The left mean is 10.2690 and the right mean is 11.7467. Train SSE is 2.6315, against 10.1623 for the line. The tree replaces the slope with a step.

```bash
python days/44-shallow-tree/shallow_tree.py
```

```text
train sessions = 59
split when t > 38.50
left mean = 10.2690 right mean = 11.7467
train SSE stump = 2.6315
train SSE line = 10.1623
```

Next the tree is one level deeper. Train SSE falls. The later stretch need not fall with it.
