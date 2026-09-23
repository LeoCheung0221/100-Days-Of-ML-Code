<p align="center"><b>中文</b> &nbsp;&nbsp;·&nbsp;&nbsp; <a href="day-35.en.md">English</a></p>

# 第 35 天 · 停牌后的间隔

[第一阶段 · 模型](README.md) · 可运行

行号 35 和 36 相邻。日期是 2024-02-20 和 2024-02-22。交易日间隔是 2，中间缺了一个交易日。行号差 1 不能写成时间差 1。

```bash
python days/35-halt-gap/halt_gap.py
```

```text
row numbers 35 36
dates 2024-02-20 2024-02-22
business-day gap = 2
adjacent rows are not adjacent sessions
```

下一步把未复权收益和复权收益放在同一天。
