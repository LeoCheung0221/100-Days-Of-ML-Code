<p align="center"><b>中文</b> &nbsp;&nbsp;·&nbsp;&nbsp; <a href="day-33.en.md">English</a></p>

# 第 33 天 · 训练集标准化

[第一阶段 · 模型](README.md) · 可运行

训练段收益的均值和标准差是 0.003241 和 0.022132。把测试段也放进缩放，是 0.002470 和 0.019265。两种缩放下的测试 MSE 在小数点后六位都是 0.000109。分数没有动。全样本缩放仍然看见了测试段。看见和变好不是一回事。

```bash
python days/33-train-scale/train_scale.py
```

```text
train mean/std = 0.003241 0.022132
whole-sample mean/std = 0.002470 0.019265
test MSE, scale from the training stretch = 0.000109
test MSE, scale from the whole sample = 0.000109
the whole-sample scale sees the test stretch
```

下一步把空着的收盘分别用前一日和后一日填上，后一种要标成偷看。
