<p align="center"><a href="day-45.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 45 · A deeper tree

[Phase I · Models](../../README.en.md) · runs

Depth 1 has train SSE 2.6315 and later SSE 0.5669. Depth 2 has train SSE 1.3953 and later SSE 2.1488. Training fell by 1.2362 and the later stretch rose by 1.5819. The deeper fit is better on the train and worse on the next stretch.

```bash
python days/45-deeper-tree/deeper_tree.py
```

```text
train SSE depth1 = 2.6315
later SSE depth1 = 0.5669
train SSE depth2 = 1.3953
later SSE depth2 = 2.1488
```

Next the line, the ridge fit, and this tree are all scored on the later stretch.
