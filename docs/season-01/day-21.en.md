<p align="center"><a href="day-21.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 21 · A fixed close table

[Phase I · Models](../../README.en.md) · runs

The table is days/data/panel.csv. It has 160 rows, AAA and BBB, 80 sessions each, from 2024-01-02 through 2024-04-23. AAA has 1 blank close. Two reads of the file match. This is not the five handwritten closes of day 1, and it is not redrawn at runtime.

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

Next yesterday's adjusted sign predicts today, beside a coin-flip 0.5.
