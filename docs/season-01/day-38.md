<p align="center"><b>中文</b> &nbsp;&nbsp;·&nbsp;&nbsp; <a href="day-38.en.md">English</a></p>

# 第 38 天 · 信号滞后一日

[第一阶段 · 模型](README.md) · 可运行

当日市场涨跌与当日复权涨跌同号的比例是 0.6795。市场滞后一日之后，比例是 0.4026。消失的 0.2769 是同时信息。留下的 0.4026 低于 0.5，不能写成还能用的预测。

```bash
python days/38-lag-signal/lag_signal.py
```

```text
same-day market sign accuracy = 0.6795
lagged-one-day market sign accuracy = 0.4026
what disappeared was simultaneous
```

下一步从策略收益里扣一个最小来回成本。
