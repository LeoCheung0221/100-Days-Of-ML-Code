<p align="center"><b>中文</b> &nbsp;&nbsp;·&nbsp;&nbsp; <a href="day-20.en.md">English</a></p>

# 第 20 天 · 噪声列

[第一阶段 · 模型](README.md) · 可运行

噪声列用种子 0，事先写死。前四日的样本内 RSS 从 42.0500 降到 26.7061。第五日的绝对误差从 11.6500 升到 18.1513。列空间变大，训练平方和下降是允许发生的。允许当作成绩的是留出误差，它变差了。

```bash
python days/20-noise-column/noise.py
```

```text
fit on t=1..4, score on t=5
in-sample RSS without noise = 42.0500
in-sample RSS with noise = 26.7061
holdout absolute error without noise = 11.6500
holdout absolute error with noise = 18.1513
the in-sample drop is not an improvement
```

下一步换一张冻结在仓库里的收盘表，数字不再写在公式里。
