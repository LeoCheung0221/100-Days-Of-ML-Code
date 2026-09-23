<p align="center"><b>中文</b> &nbsp;&nbsp;·&nbsp;&nbsp; <a href="day-25.en.md">English</a></p>

# 第 25 天 · 方向与价格并报

[第一阶段 · 模型](README.md) · 可运行

用昨日收益预测今日收益。方向准确率 0.4675，平均绝对收益误差 0.0167。有 9 天价格误差不超过中位数，符号却是错的。做符号决定时，信准确率，不信 0.0167。

```bash
python days/25-two-scores/two_scores.py
```

```text
lag-1 return forecast
direction accuracy = 0.4675
mean absolute return error = 0.0167
days with a small price error and the wrong sign = 9
for a sign decision, trust the direction accuracy
```

下一步把行随机切成训练和测试，这个数只作对照。
