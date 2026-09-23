<p align="center"><b>中文</b> &nbsp;&nbsp;·&nbsp;&nbsp; <a href="day-78.en.md">English</a></p>

# 第 78 天 · 低门槛发言

[第一阶段 · 模型](README.md) · 可运行

今天的学习要点：threshold=0.0010；speaking=17；speaking MAE=0.007663。

## 费曼法讲解

第 78 天的数字来自脚本 stdout，不是手算补值。τ=0.001 时十七日 |ŷ| 够大，speaking MAE 0.007663 接近全测试 0.006980。仅 2 日静音，说明多数预测幅度超过 0.001。

与第 77 天对照：门槛从 0.01 降到 0.001，发言从 0 到 17，说明 |ŷ| 分布集中在 0.001–0.01 之间。

面板文件是 days/data/panel.csv，名称列 AAA，收益由复权收盘相邻两日比值减一得到。特征行从第五个收益之后才开始，因此有效样本比原始行数少五。除非当天脚本改写切分，训练集是这些有效行按日期排序后的前百分之七十五；剩余行只做测试，不参与重估系数或阈值。同一交易日上的 high、low、close 不能作为解释当日收益的输入；同日 market 收益也不能当作合法结果。

读数时先把训练与测试分开：五 lag 直线只在训练段估计系数，本课所有计数与均值只在 hold-out 十九行上算。threshold=0.0010；speaking=17；speaking MAE=0.007663。

本课在 hold-out 十九行上读绝对误差、方向或账单，不再重印 return MSE 0.000081；直线仍是第 51 天同一套五 lag OLS，系数 frozen 在训练段。return 上的分数与早期「时间对价格水平」的 SSE 不是一列数；不要把第 45、46 天的树 SSE 贴进来。

结论只服务本次打印。换切分、换股票代码或加列，会得到另一套小数；另一套不在本页。

## 核心知识

面板文件是 days/data/panel.csv，名称列 AAA，收益由复权收盘相邻两日比值减一得到。特征行从第五个收益之后才开始，因此有效样本比原始行数少五。除非当天脚本改写切分，训练集是这些有效行按日期排序后的前百分之七十五；剩余行只做测试，不参与重估系数或阈值。同一交易日上的 high、low、close 不能作为解释当日收益的输入；同日 market 收益也不能当作合法结果。

```text
threshold = 0.0010
days speaking = 17
mean abs error when speaking = 0.007663
```

本课在 hold-out 十九行上读绝对误差、方向或账单，不再重印 return MSE 0.000081；直线仍是第 51 天同一套五 lag OLS，系数 frozen 在训练段。return 上的分数与早期「时间对价格水平」的 SSE 不是一列数；不要把第 45、46 天的树 SSE 贴进来。

## 拓展领域

把当天 stdout 与正文交叉核对：核心块中的英文键名、符号和小数位应与终端一致。τ=0.001 时十七日 |ŷ| 够大，speaking MAE 0.007663 接近全测试 0.006980。仅 2 日静音，说明多数预测幅度超过 0.001。

与第 77 天对照：门槛从 0.01 降到 0.001，发言从 0 到 17，说明 |ŷ| 分布集中在 0.001–0.01 之间。

研究日志里，账单规则与方向定义要同页保存，避免日后只抄 total bill、不抄 jump 单价。下一课若改切分或目标，应新开一行记录，而不是覆盖本日数字。

写笔记时，英文 stdout 键名与数值应原样抄写，不要把 line 与 tree 的账单对调。比较模型时，先确认标签列、特征列与切分行数一致，再读 direction wrong 或 total bill。若脚本声明 FORBIDDEN 或 not a result，该列分数不进入结果表，即使六位小数更小。阶段一固定在 panel.csv 的 AAA 行上；BBB 只在指定天出现，不能把 AAA 的系数自动搬到 BBB。账单 −18 与 jump=5、direction wrong=3 的关系是 3×1+5×3 的扣分，不是十九天各扣一次。quiet 与 jump 按真实 |y| 划分；|ŷ| 阈值课只影响 speaking 计数，不改变 quiet 定义。

写笔记时，英文 stdout 键名与数值应原样抄写，不要把 line 与 tree 的账单对调。比较模型时，先确认标签列、特征列与切分行数一致，再读 direction wrong 或 total bill。若脚本声明 FORBIDDEN 或 not a result，该列分数不进入结果表，即使六位小数更小。阶段一固定在 panel.csv 的 AAA 行上；BBB 只在指定天出现，不能把 AAA 的系数自动搬到 BBB。账单 −18 与 jump=5、direction wrong=3 的关系是 3×1+5×3 的扣分，不是十九天各扣一次。quiet 与 jump 按真实 |y| 划分；|ŷ| 阈值课只影响 speaking 计数，不改变 quiet 定义。

写笔记时，英文 stdout 键名与数值应原样抄写，不要把 line 与 tree 的账单对调。比较模型时，先确认标签列、特征列与切分行数一致，再读 direction wrong 或 total bill。若脚本声明 FORBIDDEN 或 not a result，该列分数不进入结果表，即使六位小数更小。阶段一固定在 panel.csv 的 AAA 行上；BBB 只在指定天出现，不能把 AAA 的系数自动搬到 BBB。账单 −18 与 jump=5、direction wrong=3 的关系是 3×1+5×3 的扣分，不是十九天各扣一次。quiet 与 jump 按真实 |y| 划分；|ŷ| 阈值课只影响 speaking 计数，不改变 quiet 定义。

## 实战总结

```bash
python days/78-low-threshold/low_threshold.py
```

脚本应打印与核心块一致的 stdout 行。实现是 [`low_threshold.py`](../../days/78-low-threshold/low_threshold.py).

今天交出去的是第 78 天打印表上的数与规则句。请保留脚本路径便于复跑。
