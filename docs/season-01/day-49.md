<p align="center"><b>中文</b> &nbsp;&nbsp;·&nbsp;&nbsp; <a href="day-49.en.md">English</a></p>

# 第 49 天 · 同一跳空日

[第一阶段 · 模型](README.md) · 可运行

2024-02-28 的复权收盘是 12.0142。直线斜率 0.0299，岭回归斜率 0.0201。两条线在这一天交叉，所以当日拟合值都是 11.0315，残差都是 0.9827。十日之后，直线是 11.3305，岭回归是 11.2326，惩罚才在水平上分开。树当日拟合 11.7285，残差 0.2857，十日之后仍是 11.7285。它把这一段放进了更高的叶子，而不是被斜率搬走。

```bash
python days/49-one-jump/one_jump.py
```

```text
jump date = 2024-02-28
adj close = 12.0142
line slope = 0.0299 ridge slope = 0.0201
line at jump = 11.0315  residual = 0.9827  ten later = 11.3305
ridge at jump = 11.0315  residual = 0.9827  ten later = 11.2326
tree at jump = 11.7285  residual = 0.2857  ten later = 11.7285
```

下一步三个模型对后一段的一步方向投票，找出三个都错、投票也错的日子。
