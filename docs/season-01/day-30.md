<p align="center"><b>中文</b> &nbsp;&nbsp;·&nbsp;&nbsp; <a href="day-30.en.md">English</a></p>

# 第 30 天 · 固定历史窗口

[第一阶段 · 模型](README.md) · 可运行

最后一天，用全部复权收盘拟合的值是 12.1976。只用过去 20 日拟合的值是 12.0095。差是 0.1881。信息集是这 20 日，不是整张表。

```bash
python days/30-fixed-lookback/lookback.py
```

```text
lookback = 20
full-sample value at last t = 12.1976
window value at last t = 12.0095
the full sample is not the information set
```

下一步把窗口收成三日，斜率可以跟着局部噪声改号。
