<p align="center"><b>中文</b> &nbsp;&nbsp;·&nbsp;&nbsp; <a href="day-48.en.md">English</a></p>

# 第 48 天 · 树不外推

[第一阶段 · 模型](README.md) · 可运行

同一查询 t = 118。树给出 11.9608，落在训练标签的最小值和最大值之间。直线仍是 13.3936，在区间外。树在支撑外没有斜率，它重复的是最右侧叶子的均值。

```bash
python days/48-tree-leaf/tree_leaf.py
```

```text
query t = 118
tree value = 11.9608
line value = 13.3936
tree stays inside the training range = true
```

下一步把直线、岭回归和树放在同一个跳空日上。
