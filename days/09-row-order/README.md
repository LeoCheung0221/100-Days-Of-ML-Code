<p align="center"><a href="../../docs/season-01/day-09.md">中文讲解</a> · <a href="../../docs/season-01/day-09.en.md">English</a></p>

# 第 9 天 · 打乱日期

行序换为 `[2, 4, 3, 0, 1]`，配对不拆。批量 OLS 仍是 `ŷ = 3.2700x − 1.2900`，`RSS = 96.3390`。斜率差在 `1e-15`，平方和之差在 `1e-14`。

不变的是行序。日历坐标 `x_t = t` 仍在设计矩阵里。

论证写在 [中文讲解](../../docs/season-01/day-09.md) 与 [English](../../docs/season-01/day-09.en.md)。

```bash
python days/09-row-order/row_order.py
```
