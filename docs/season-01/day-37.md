<p align="center"><b>中文</b> &nbsp;&nbsp;·&nbsp;&nbsp; <a href="day-37.en.md">English</a></p>

# 第 37 天 · 多标的混切

[第一阶段 · 模型](README.md) · 可运行

AAA 与 BBB 叠在一起，用当日市场收益的符号预测各自行情。随机切分的测试准确率是 0.7234，按时间切是 0.6170。高出的部分可以来自同一天：一只股票在训练里，另一只在测试里，它们共享这一天的市场。

```bash
python days/37-mixed-names/mixed_names.py
```

```text
pooled AAA and BBB
random-split test accuracy = 0.7234
time-split test accuracy = 0.6170
the random split can train and test on the same date
```

下一步把市场信号整体滞后一天，同时信息应当消失。
