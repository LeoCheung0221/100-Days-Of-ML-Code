<p align="center"><b>中文</b> &nbsp;&nbsp;·&nbsp;&nbsp; <a href="day-11.en.md">English</a></p>

# 第 11 天 · 涨跌标签

[第一阶段 · 模型](README.md) · 可运行

成绩从价格距离改成方向命中。四步里命中 3/4。第四日的绝对残差仍是 8.21，但这个距离不再是分数。拟合斜率恒为正，所以这 3/4 与「每一步都猜涨」是同一条规则。

```bash
python days/11-direction-labels/labels.py
```

```text
score = direction hits 3/4
day 4 absolute price residual = 8.21
that residual is not the score
```

下一步要把收益按一个自己选定的阈值切开，不能再把符号本身当成现成的标签。
