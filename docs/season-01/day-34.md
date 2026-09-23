<p align="center"><b>中文</b> &nbsp;&nbsp;·&nbsp;&nbsp; <a href="day-34.en.md">English</a></p>

# 第 34 天 · 缺失的两种填法

[第一阶段 · 模型](README.md) · 可运行

AAA 在 2024-02-01 的收盘是空的。用前一日填，得到 10.1047。用后一日填，得到 9.8971。两个数都印。后一个看见了未来。

```bash
python days/34-two-fills/two_fills.py
```

```text
blank date = 2024-02-01
fill from the previous close = 10.1047
fill from the next close = 9.8971
the next close sees the future
```

下一步删掉间隔之后，检查行号相邻是不是交易日相邻。
