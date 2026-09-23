<p align="center"><b>中文</b> &nbsp;&nbsp;·&nbsp;&nbsp; <a href="day-23.en.md">English</a></p>

# 第 23 天 · 连续三日同向

[第一阶段 · 模型](README.md) · 可运行

规则事先写在程序里：连续三个复权涨跌同号，就预测第四个同号。事件 11 次，命中 6 次，准确率 0.5455。条件没有在看见结果之后改过。

```bash
python days/23-three-day-run/three_day_run.py
```

```text
rule = after three equal signs, predict the fourth matches
events = 11
hits = 6
accuracy = 0.5455
the rule is fixed before the count
```

下一步同一条规则只在后半段上计分，前半段的准确率不作成绩。
