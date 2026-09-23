<p align="center"><b>中文</b> &nbsp;&nbsp;·&nbsp;&nbsp; <a href="day-21.en.md">English</a></p>

# 第 21 天 · 固定收盘表

[第一阶段 · 模型](README.md) · 可运行

表在 days/data/panel.csv。160 行，AAA 与 BBB 各 80 个交易日，从 2024-01-02 到 2024-04-23。AAA 有 1 个收盘为空。连读两次，文件文本一致。这张表不是第 1 天手写的五个收盘，也不是运行时重新抽样。

```bash
python days/21-fixed-table/fixed_table.py
```

```text
path = days/data/panel.csv
rows = 160
second read matches = true
AAA dates 2024-01-02 .. 2024-04-23
AAA blank closes = 1
the table is not resampled
```

下一步用昨日复权涨跌的符号猜今日，并和硬币的 0.5 并排。
