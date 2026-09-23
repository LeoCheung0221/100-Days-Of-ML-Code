<p align="center"><b>中文</b> &nbsp;&nbsp;·&nbsp;&nbsp; <a href="day-45.en.md">English</a></p>

# 第 45 天 · 更深的树

[第一阶段 · 模型](README.md) · 可运行

深度 1 的训练 SSE 是 2.6315，后一段是 0.5669。深度 2 的训练 SSE 是 1.3953，后一段是 2.1488。训练下降了 1.2362，后一段上升了 1.5819。训练更好的那一层，换一段更差。

```bash
python days/45-deeper-tree/deeper_tree.py
```

```text
train SSE depth1 = 2.6315
later SSE depth1 = 0.5669
train SSE depth2 = 1.3953
later SSE depth2 = 2.1488
```

下一步直线、岭回归和这棵树同时报到后一段，看谁还在。
