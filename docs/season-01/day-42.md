<p align="center"><b>中文</b> &nbsp;&nbsp;·&nbsp;&nbsp; <a href="day-42.en.md">English</a></p>

# 第 42 天 · 岭回归

[第一阶段 · 模型](README.md) · 可运行

惩罚只加在斜率上，λ = 20000，截距自由。OLS 斜率是 0.0299，岭回归斜率是 0.0201。同一段复权收盘，线被要求少倾斜 0.0098。

```bash
python days/42-ridge/ridge.py
```

```text
lambda = 20000, penalty on the slope only
ols slope = 0.0299
ridge slope = 0.0201
```

下一步只平均查询附近的五日。远处的跳空进不了这五个近邻。
