<p align="center"><b>中文</b> &nbsp;&nbsp;·&nbsp;&nbsp; <a href="day-43.en.md">English</a></p>

# 第 43 天 · 局部平均

[第一阶段 · 模型](README.md) · 可运行

查询日是 2024-03-20。五个时间近邻是 2024-03-18 到 2024-03-22，不含 2024-02-28。局部均值是 11.6932。OLS 在该点是 11.4800，二月二十八日仍在它的正规方程里。局部平均把那一天留在了邻居集合外面。

```bash
python days/43-local-mean/local_mean.py
```

```text
query date = 2024-03-20
neighbor dates = 2024-03-20 2024-03-19 2024-03-21 2024-03-18 2024-03-22
jump date in the neighbors = false
local mean = 11.6932
ols at the query = 11.4800
```

下一步用一棵只有一次分裂的树。它可以把后半段切成一个常数。
