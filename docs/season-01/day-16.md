<p align="center"><b>中文</b> &nbsp;&nbsp;·&nbsp;&nbsp; <a href="day-16.en.md">English</a></p>

# 第 16 天 · 上涨程度

[第一阶段 · 模型](README.md) · 可运行

斜率 3.27 送进 sigmoid，得到 0.9634。四步都是这一个数。仿射拟合的一步差分是常数，所以这个程度不能把四步排成不同的把握。

```bash
python days/16-up-score/up_score.py
```

```text
slope = 3.27
P(up) = sigmoid(slope) = 0.9634
the same score is attached to every step
```

下一步核对这个 0.9634 和实际上涨的频率是不是一回事。
