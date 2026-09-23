<p align="center"><b>中文</b> &nbsp;&nbsp;·&nbsp;&nbsp; <a href="day-31.en.md">English</a></p>

# 第 31 天 · 三日窗口的噪声

[第一阶段 · 模型](README.md) · 可运行

预测最后一个复权收盘时，三日斜率是 −0.1195，二十日斜率是 0.0251，符号相反。三日的绝对失手是 0.0867，二十日是 0.1506。短窗口在追局部方向。这一天它的绝对误差更小，不能据此说它更准。失手单独印出来。

```bash
python days/31-three-day-noise/three_day_noise.py
```

```text
three-day slope = -0.1195
twenty-day slope = 0.0251
three-day absolute miss = 0.0867
twenty-day absolute miss = 0.1506
```

下一步把窗口放到六十日，和这三日并排。
