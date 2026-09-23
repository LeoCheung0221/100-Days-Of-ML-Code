<p align="center"><b>中文</b> &nbsp;&nbsp;·&nbsp;&nbsp; <a href="day-47.en.md">English</a></p>

# 第 47 天 · 线性外推

[第一阶段 · 模型](README.md) · 可运行

查询 t = 118，比样本最后一个横坐标远 40。直线给出 13.3936。样本里复权收盘最小 9.8971，最大 12.1679。13.3936 在这个区间外面。仿射类在支撑外仍有定义，定义不等于答案还在已见价格里。

```bash
python days/47-extrapolate/extrapolate.py
```

```text
query t = 118
line value = 13.3936
observed adj close min = 9.8971
observed adj close max = 12.1679
outside the observed range = true
```

下一步同一查询交给树。树只能重复一片叶子。
