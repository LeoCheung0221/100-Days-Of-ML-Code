<p align="center"><a href="../../docs/season-01/day-08.md">中文讲解</a> · <a href="../../docs/season-01/day-08.en.md">English</a></p>

# 第 8 天 · 三日窗口

窗口 `{1, 2, 3}` 的斜率为 **2.0500**，`RSS = 0.0417`。向前滑到 `{2, 3, 4}` 之后，斜率为 **8.0500**，`RSS = 22.0417`。斜率增加 **6.0000**。第一日离开信息集，第四日进入。

两个 `RSS` 的求和集合不同，不能跨窗口排名。

论证写在 [中文讲解](../../docs/season-01/day-08.md) 与 [English](../../docs/season-01/day-08.en.md)。

```bash
python days/08-three-day-window/three_day_window.py
```
