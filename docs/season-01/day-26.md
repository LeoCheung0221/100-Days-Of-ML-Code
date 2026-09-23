<p align="center"><b>中文</b> &nbsp;&nbsp;·&nbsp;&nbsp; <a href="day-26.en.md">English</a></p>

# 第 26 天 · 随机切分

[第一阶段 · 模型](README.md) · 可运行

种子 1，训练占 0.70，用滞后收益的符号预测下一步。测试方向准确率是 0.4583。这是对照。它还没有和按时间切的数放在一起。

```bash
python days/26-random-split/random_split.py
```

```text
split = random, seed 1, train fraction 0.70
test direction accuracy = 0.4583
this number is the control
```

下一步改成按时间切，测试全部落在训练之后，两个准确率都要印。
