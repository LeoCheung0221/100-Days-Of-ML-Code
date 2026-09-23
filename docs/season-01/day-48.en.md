<p align="center"><a href="day-48.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 48 · A tree does not extrapolate

[Phase I · Models](../../README.en.md) · runs

The same query is t = 118. The tree returns 11.9608, inside the minimum and maximum of the training labels. The line is still 13.3936, outside that range. Off the support the tree has no slope. It repeats the mean of the rightmost leaf.

```bash
python days/48-tree-leaf/tree_leaf.py
```

```text
query t = 118
tree value = 11.9608
line value = 13.3936
tree stays inside the training range = true
```

Next the line, ridge, and the tree are placed on the same jump day.
