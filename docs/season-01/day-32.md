<p align="center"><b>中文</b> &nbsp;&nbsp;·&nbsp;&nbsp; <a href="day-32.en.md">English</a></p>

# 第 32 天 · 六十日窗口

[第一阶段 · 模型](README.md) · 可运行

同一个最后交易日，六十日斜率是 0.0353，绝对失手是 0.4426。三日斜率是 −0.1195，绝对失手是 0.0867。长窗口还停在更早的斜率上，这一天离收盘更远。

```bash
python days/32-sixty-day-window/sixty_day.py
```

```text
sixty-day slope = 0.0353
three-day slope = -0.1195
sixty-day absolute miss = 0.4426
three-day absolute miss = 0.0867
```

下一步均值和方差只许用训练段估计。
