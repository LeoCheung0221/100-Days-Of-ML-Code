<p align="center"><a href="../../docs/season-01/day-33.md">中文讲解</a> · <a href="../../docs/season-01/day-33.en.md">English</a></p>

# 第 33 天 · 训练集标准化

训练段收益的均值和标准差是 0.003241 和 0.022132。把测试段也放进缩放，是 0.002470 和 0.019265。两种缩放下的测试 MSE 在小数点后六位都是 0.000109。分数没有动。全样本缩放仍然看见了测试段。看见和变好不是一回事。

```bash
python days/33-train-scale/train_scale.py
```
