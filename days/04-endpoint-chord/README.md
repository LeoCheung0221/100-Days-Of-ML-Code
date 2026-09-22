<p align="center"><a href="../../docs/season-01/day-04.md">中文讲解</a> · <a href="../../docs/season-01/day-04.en.md">English</a></p>

# 第 4 天 · 端点连线

弦过 `(1, 2.1)` 与 `(5, 10.4)`：`ŷ = 2.075x + 0.025`。它与 OLS 同属仿射类。

平方损失上弦更高：`L2` 为 **136.3837**，OLS 为 **96.3390**。绝对损失上弦更低：`L1` 为 **12.0000**，OLS 为 **16.6600**。两种损失的名次相反。

论证写在 [中文讲解](../../docs/season-01/day-04.md) 与 [English](../../docs/season-01/day-04.en.md)。

```bash
python days/04-endpoint-chord/endpoint_chord.py
```
