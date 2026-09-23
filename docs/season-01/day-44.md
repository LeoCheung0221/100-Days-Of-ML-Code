<p align="center"><b>中文</b> &nbsp;&nbsp;·&nbsp;&nbsp; <a href="day-44.en.md">English</a></p>

# 第 44 天 · 浅层树

[第一阶段 · 模型](README.md) · 可运行

训练用前 59 个复权收盘。一次分裂把 t > 38.50 分到右边，左侧均值 10.2690，右侧均值 11.7467。训练 SSE 是 2.6315，直线是 10.1623。树用一个阶梯代替了斜率。

```bash
python days/44-shallow-tree/shallow_tree.py
```

```text
train sessions = 59
split when t > 38.50
left mean = 10.2690 right mean = 11.7467
train SSE stump = 2.6315
train SSE line = 10.1623
```

下一步树再深一层。训练 SSE 会下降，后一段不一定跟着下降。
