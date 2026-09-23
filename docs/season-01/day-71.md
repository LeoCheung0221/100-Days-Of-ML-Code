<p align="center"><b>中文</b> &nbsp;&nbsp;·&nbsp;&nbsp; <a href="day-71.en.md">English</a></p>

# 第 71 天 · 三类交易日

[第一阶段 · 模型](README.md) · 可运行

今天的学习要点：在 AAA 五 lag 直线 hold-out 上，按真实 |收益| 分 quiet=10、jump=5；方向错共 3 天。

## 费曼法讲解

第 71 天仍用第 51 天 frozen 的五 lag 直线，只在后十九行测试段上读标签与预测。分类看的是真实当日简单收益的绝对值，不是 |ŷ|。

quiet 的定义是 |y| 不超过测试段 |y| 的中位数。jump 的定义是 |y| 不低于测试段 |y| 的第七十五百分位。介于两者之间的日子脚本里叫 mid，本日只打印 quiet 与 jump 的个数。quiet=10 说明一半左右的测试日波动落在「不超过中位数」一侧；jump=5 说明最猛的五分之一左右落在高波动档。

方向失手单独计数：sign(y) 与 sign(ŷ) 不同记一天，共 3 天。方向与 quiet/jump 是正交维度——大 jump 日可以方向对，quiet 日也可以方向错。不要把 direction wrong=3 理解成 quiet 或 jump 的子集计数；脚本没有要求三者相加等于十九。

今天的结论停在这三个整数。它们描述的是同一条 lag-5 return 直线在同一 seventy-five percent 切分下的测试段形状，不是新拟合的模型。

## 核心知识

面板文件是 days/data/panel.csv，名称列 AAA，收益由复权收盘相邻两日比值减一得到。特征行从第五个收益之后才开始，因此有效样本比原始行数少五。除非当天脚本改写切分，训练集是这些有效行按日期排序后的前百分之七十五；剩余行只做测试，不参与重估系数或阈值。同一交易日上的 high、low、close 不能作为解释当日收益的输入；同日 market 收益也不能当作合法结果。

```text
quiet days = 10
jump days = 5
direction wrong days = 3
```

本课在 hold-out 十九行上读绝对误差、方向或账单，不再重印 return MSE 0.000081；直线仍是第 51 天同一套五 lag OLS，系数 frozen 在训练段。return 上的分数与早期「时间对价格水平」的 SSE 不是一列数；不要把第 45、46 天的树 SSE 贴进来。

## 拓展领域

交叉核对：quiet 与 jump 按 |y| 划分，中位数与 p75 都在测试段 nineteen 行上算，不能拿训练段分位数代替。

下一课在第 72 天只盯 quiet 子集的 MAE，并与全测试 MAE 0.006980 对照。不要把 jump=5 写成「方向错的 jump 有五天」——方向错仍是 3。

写笔记时，英文 stdout 键名与数值应原样抄写，不要把 line 与 tree 的账单对调。比较模型时，先确认标签列、特征列与切分行数一致，再读 direction wrong 或 total bill。若脚本声明 FORBIDDEN 或 not a result，该列分数不进入结果表，即使六位小数更小。阶段一固定在 panel.csv 的 AAA 行上；BBB 只在指定天出现，不能把 AAA 的系数自动搬到 BBB。账单 −18 与 jump=5、direction wrong=3 的关系是 3×1+5×3 的扣分，不是十九天各扣一次。quiet 与 jump 按真实 |y| 划分；|ŷ| 阈值课只影响 speaking 计数，不改变 quiet 定义。

写笔记时，英文 stdout 键名与数值应原样抄写，不要把 line 与 tree 的账单对调。比较模型时，先确认标签列、特征列与切分行数一致，再读 direction wrong 或 total bill。若脚本声明 FORBIDDEN 或 not a result，该列分数不进入结果表，即使六位小数更小。阶段一固定在 panel.csv 的 AAA 行上；BBB 只在指定天出现，不能把 AAA 的系数自动搬到 BBB。账单 −18 与 jump=5、direction wrong=3 的关系是 3×1+5×3 的扣分，不是十九天各扣一次。quiet 与 jump 按真实 |y| 划分；|ŷ| 阈值课只影响 speaking 计数，不改变 quiet 定义。

写笔记时，英文 stdout 键名与数值应原样抄写，不要把 line 与 tree 的账单对调。比较模型时，先确认标签列、特征列与切分行数一致，再读 direction wrong 或 total bill。若脚本声明 FORBIDDEN 或 not a result，该列分数不进入结果表，即使六位小数更小。阶段一固定在 panel.csv 的 AAA 行上；BBB 只在指定天出现，不能把 AAA 的系数自动搬到 BBB。账单 −18 与 jump=5、direction wrong=3 的关系是 3×1+5×3 的扣分，不是十九天各扣一次。quiet 与 jump 按真实 |y| 划分；|ŷ| 阈值课只影响 speaking 计数，不改变 quiet 定义。

写笔记时，英文 stdout 键名与数值应原样抄写，不要把 line 与 tree 的账单对调。比较模型时，先确认标签列、特征列与切分行数一致，再读 direction wrong 或 total bill。若脚本声明 FORBIDDEN 或 not a result，该列分数不进入结果表，即使六位小数更小。阶段一固定在 panel.csv 的 AAA 行上；BBB 只在指定天出现，不能把 AAA 的系数自动搬到 BBB。账单 −18 与 jump=5、direction wrong=3 的关系是 3×1+5×3 的扣分，不是十九天各扣一次。quiet 与 jump 按真实 |y| 划分；|ŷ| 阈值课只影响 speaking 计数，不改变 quiet 定义。

## 实战总结

```bash
python days/71-three-classes/three_classes.py
```

脚本应打印`quiet days = 10`、`jump days = 5`、`direction wrong days = 3`。实现是 [`three_classes.py`](../../days/71-three-classes/three_classes.py).

今天交出去的是 quiet、jump 与方向错三个计数。下一课比较 quiet 上的平均绝对误差。
