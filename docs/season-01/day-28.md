<p align="center"><b>中文</b> &nbsp;&nbsp;·&nbsp;&nbsp; <a href="day-28.en.md">English</a></p>

# 第 28 天 · 当日最高价

[第一阶段 · 模型](README.md) · 可运行

最高价与当日收盘写在同一行，脚本把它标成 FORBIDDEN。close 对 high 的样本内 RSS 是 31.8715，对昨日收盘是 35.5233。RSS 下降了 3.6518。下降来自同一根 K 线，不是来自一个可以提前知道的列。

```bash
python days/28-todays-high/todays_high.py
```

```text
column high = FORBIDDEN
in-sample RSS close~high = 31.8715
in-sample RSS close~lagged close = 35.5233
```

下一步把以后的开盘写进缩放。泄漏可以不表现为大幅变好。
