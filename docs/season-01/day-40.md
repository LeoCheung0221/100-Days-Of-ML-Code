<p align="center"><b>中文</b> &nbsp;&nbsp;·&nbsp;&nbsp; <a href="day-40.en.md">English</a></p>

# 第 40 天 · 泄漏清单

[第一阶段 · 模型](README.md) · 可运行

清单有六行，每一行的 future 都是 yes：第 28 天的当日最高价，第 29 天用以后的开盘做缩放，第 33 天的全样本缩放，第 34 天用后一日填空，第 37 天跨股票共享同一天，第 38 天的当日市场收益。这些行上的分数不记成结果。

```bash
python days/40-leakage-list/leakage_list.py
```

```text
leakage list
day 28  today's high explains today's close  future=yes
day 29  scale uses later opens  future=yes
day 33  scale uses the test stretch  future=yes
day 34  fill from the next close  future=yes
day 37  random split shares a date across names  future=yes
day 38  same-day market return  future=yes
a higher score on any of these lines is not a result
```

下一步在更长的复权序列上重做直线，看一个跳空还搬不搬得动斜率。
