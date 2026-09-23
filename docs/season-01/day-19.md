<p align="center"><b>中文</b> &nbsp;&nbsp;·&nbsp;&nbsp; <a href="day-19.en.md">English</a></p>

# 第 19 天 · 未缩放的成交量

[第一阶段 · 模型](README.md) · 可运行

成交量的原始系数是 1.731932e-06，日期的原始系数是 1.482253。只看系数，成交量像是可以丢掉。平均绝对贡献分别是 4.3645 和 4.4468，同一量级。标准化之后，成交量的系数是 4.7815，日期是 2.7049。小系数是股数这个单位写出来的。

```bash
python days/19-unscaled-volume/unscaled.py
```

```text
raw beta time = 1.482253
raw beta volume = 1.731932e-06
mean |time contribution| = 4.4468
mean |volume contribution| = 4.3645
standardized beta time = 2.7049
standardized beta volume = 4.7815
```

下一步加一列固定种子的噪声。样本内变好不算改善。
