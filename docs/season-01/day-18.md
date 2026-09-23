<p align="center"><b>中文</b> &nbsp;&nbsp;·&nbsp;&nbsp; <a href="day-18.en.md">English</a></p>

# 第 18 天 · 涨幅与成交量

[第一阶段 · 模型](README.md) · 可运行

只看收益是否为正，四步里有 3 步上涨。再加上成交量高于五个成交量的中位数 1200000，只留下第 4 日。标签变了，是因为输入多了一列，不是因为价格被重估了。

```bash
python days/18-return-volume/volume_split.py
```

```text
median volume = 1200000
up on return alone = 3
up on return and volume = 1
sessions kept = 4
```

下一步把成交量不缩放就放进回归，看单位如何改写系数。
