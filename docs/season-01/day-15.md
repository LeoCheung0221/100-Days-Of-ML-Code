<p align="center"><b>中文</b> &nbsp;&nbsp;·&nbsp;&nbsp; <a href="day-15.en.md">English</a></p>

# 第 15 天 · 两类误分

[第一阶段 · 模型](README.md) · 可运行

恒猜涨的四步里，把涨说成跌是 0 次，把跌说成涨是 1 次。准确率 0.75 把这两格加成了一个数。本日要求两格都在。

```bash
python days/15-two-mistakes/mistakes.py
```

```text
up called down = 0
down called up = 1
```

下一步不再只交 0 或 1，要交一个 0 到 1 的程度。
