<p align="center"><a href="day-43.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 43 · A local average

[Phase I · Models](../../README.en.md) · runs

The query date is 2024-03-20. The five time-neighbors run from 2024-03-18 through 2024-03-22 and do not include 2024-02-28. The local mean is 11.6932. OLS at the query is 11.4800, and 28 February is still inside its normal equations. The local average left that day outside the neighbor set.

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

Next a tree with one split. It can cut the later sessions into one constant.
