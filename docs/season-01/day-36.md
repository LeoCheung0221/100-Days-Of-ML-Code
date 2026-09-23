<p align="center"><b>中文</b> &nbsp;&nbsp;·&nbsp;&nbsp; <a href="day-36.en.md">English</a></p>

# 第 36 天 · 复权与未复权

[第一阶段 · 模型](README.md) · 可运行

2024-03-11 的未复权收益是 −0.4938，复权收益是 0.0124。把 −0.4938 读成下跌，读到的是价格除权，不是复权序列里的涨跌。两个数都要交。

```bash
python days/36-adjusted-close/adjusted.py
```

```text
date = 2024-03-11
unadjusted return = -0.4938
adjusted return = 0.0124
both numbers are due
```

下一步把 AAA 和 BBB 混在一起切。随机切可以让同一天出现在两侧。
