<p align="center"><a href="../../docs/season-01/day-06.md">中文讲解</a> · <a href="../../docs/season-01/day-06.en.md">English</a></p>

# 第 6 天 · 训练支撑外的查询

查询 `x = 6`，支撑是 `[1, 5]`。样本里没有 `y_6`，残差无定义。

最近邻复制第五日的 **10.4**。OLS 外推得 **18.33**。两者相差 **7.93**，这是估计之差，不是失手。

论证写在 [中文讲解](../../docs/season-01/day-06.md) 与 [English](../../docs/season-01/day-06.en.md)。

```bash
python days/06-off-support/off_support.py
```
