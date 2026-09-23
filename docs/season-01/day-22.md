<p align="center"><b>中文</b> &nbsp;&nbsp;·&nbsp;&nbsp; <a href="day-22.en.md">English</a></p>

# 第 22 天 · 滞后一日的方向

[第一阶段 · 模型](README.md) · 可运行

用昨日复权涨跌的符号猜今日，命中 36/77，准确率 0.4675。硬币基准是 0.5000。这条规则没有赢过不看价格的基准。

```bash
python days/22-lagged-direction/lagged_direction.py
```

```text
predict today's adj move with yesterday's sign
hits = 36/77
accuracy = 0.4675
coin-flip baseline = 0.5000
```

下一步把「连续三日同号则第四日同号」写成死规则，先写再数。
