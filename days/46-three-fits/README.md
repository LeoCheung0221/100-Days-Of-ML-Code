<p align="center"><a href="../../docs/season-01/day-46.md">中文讲解</a> · <a href="../../docs/season-01/day-46.en.md">English</a></p>

# 第 46 天 · 三种拟合换样本

训练 SSE：直线 10.1623，岭回归 16.3596，树 1.3953。后一段 SSE：直线 2.9263，岭回归 3.2545，树 2.1488。后一段还在的是树。三者的训练误差并不接近。后一段的名次仍然要单独写，不能用训练 SSE 最小代替。

```bash
python days/46-three-fits/three_fits.py
```
