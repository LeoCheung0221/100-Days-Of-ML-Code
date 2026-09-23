<p align="center"><b>中文</b> &nbsp;&nbsp;·&nbsp;&nbsp; <a href="day-41.en.md">English</a></p>

# 第 41 天 · 更长样本上的直线

[第一阶段 · 模型](README.md) · 可运行

2024-02-28 的复权收益是 0.1349。删掉这一天，斜率在六位小数上仍是 0.029901。截距从 9.8654 降到 9.8528。当日拟合值从 11.0315 降到 11.0189，只挪了 0.0126。第 5 天在五个点上，删掉第四日让斜率下降 1.1729。样本变长之后，同一种跳空几乎只挪截距。

```bash
python days/41-longer-line/longer_line.py
```

```text
jump date = 2024-02-28
adjusted return that day = 0.1349
slope with the jump = 0.029901
slope without the jump = 0.029901
intercept with the jump = 9.8654
intercept without the jump = 9.8528
fitted at the jump, with = 11.0315
fitted at the jump, without = 11.0189
```

下一步对斜率加惩罚。倾斜不许再保持 0.0299。
