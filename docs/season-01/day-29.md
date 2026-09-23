<p align="center"><b>中文</b> &nbsp;&nbsp;·&nbsp;&nbsp; <a href="day-29.en.md">English</a></p>

# 第 29 天 · 用未来开盘标准化

[第一阶段 · 模型](README.md) · 可运行

用全部开盘的均值和标准差缩放收盘，包括该收盘之后的开盘，收益回归的 RSS 是 0.2642。只用过去收盘缩放，RSS 是 0.2650。差是 0.0008。泄漏的识别不靠分数变得更好，靠缩放的自变量里有以后的开盘。

```bash
python days/29-future-open/future_open.py
```

```text
leaky scale uses every open, including later ones
RSS of return on leaky close = 0.2642
RSS of return on past-only close = 0.2650
the leaky scale is a function of later opens
```

下一步每天只许看过去一个固定窗口，不能再拿整段历史一起拟合。
