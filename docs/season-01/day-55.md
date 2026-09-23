<p align="center"><b>中文</b> &nbsp;&nbsp;·&nbsp;&nbsp; <a href="day-55.en.md">English</a></p>

# 第 55 天 · 三种失手

[第一阶段 · 模型](README.md) · 可运行

今天的学习要点：line MSE 0.000081，ridge 0.000098，tree 0.000174；三句 miss mode 英文同脚本

## 费曼法讲解

第 55 天的数字来自脚本 stdout，不是手算补值。岭 λ=20000 惩罚五 lag，截距自由。line 最小 MSE。三句失手描述形状，不是命中率。

面板文件是 days/data/panel.csv，名称列 AAA，收益由复权收盘相邻两日比值减一得到。特征行从第五个收益之后才开始，因此有效样本比原始行数少五。除非当天脚本改写切分，训练集是这些有效行按日期排序后的前百分之七十五；剩余行只做测试，不参与重估系数或阈值。同一交易日上的 high、low、close 不能作为解释当日收益的输入；同日 market 收益也不能当作合法结果。

读数时先把训练与测试分开：参数只在训练段估计，MSE 只在 hold-out 行上算平均平方误差。line MSE 0.000081，ridge 0.000098，tree 0.000174；三句 miss mode 英文同脚本

MSE 在 hold-out 行上是预测减标签的平方的平均，脚本用六位小数打印。return 上的 MSE 与早期「时间对价格水平」的 SSE 不是一列数；读第 51 天及以后的表时，不要把第 45、46 天的树 SSE 贴进来。

结论只服务本次打印。换切分、换股票代码或加列，会得到另一套六位小数；另一套不在本页。

三模型共用同一 test 十九行：line 0.000081<ridge 0.000098<tree 0.000174。失手句是英文机制句，与 MSE 并列存档：line 平滑混合 lag，ridge 再向零收缩，tree 只留单 lag 阈值台阶。不要用 tree 的最小 train SSE 论证 test 更好。

## 核心知识

面板文件是 days/data/panel.csv，名称列 AAA，收益由复权收盘相邻两日比值减一得到。特征行从第五个收益之后才开始，因此有效样本比原始行数少五。除非当天脚本改写切分，训练集是这些有效行按日期排序后的前百分之七十五；剩余行只做测试，不参与重估系数或阈值。同一交易日上的 high、low、close 不能作为解释当日收益的输入；同日 market 收益也不能当作合法结果。

```text
test MSE line = 0.000081
test MSE ridge = 0.000098
test MSE tree = 0.000174
line miss mode = smooth blend of lags misses sharp jumps
ridge miss mode = same blend pulled toward zero misses jumps and size
tree miss mode = one lag threshold leaves a constant on each side
```

MSE 在 hold-out 行上是预测减标签的平方的平均，脚本用六位小数打印。return 上的 MSE 与早期「时间对价格水平」的 SSE 不是一列数；读第 51 天及以后的表时，不要把第 45、46 天的树 SSE 贴进来。

三行 miss mode 英文应原样入笔记，不与 MSE 行合并。ridge 0.000098 介于 line 与 tree 之间，说明收缩并不保证 beat OLS on this stretch。

量化课程从价格水平转向 return 后，MSE 均在收益标签上计算。hold-out 行是唯一评分集合；训练行只用于参数估计。写实验记录时，把 forbidden 规则、切分方式与 test MSE 同页保存。英文 stdout 是权威来源，中文正文是解释层，两者数字必须一致。若本地复跑六位小数不一致，先核对 panel 路径、name 列与切分行数，再改笔记。

## 拓展领域

把当天 stdout 与正文交叉核对：核心块中的英文键名、符号和小数位应与终端一致。岭 λ=20000 惩罚五 lag，截距自由。line 最小 MSE。三句失手描述形状，不是命中率。

研究日志里，禁止项与 MSE 要同页保存，避免日后只抄分数、不抄规则。下一课若改切分或目标，应新开一行记录，而不是覆盖本日数字。

写笔记时，英文 stdout 键名与数值应原样抄写，不要把 line 与 tree 的 MSE 列对调。比较模型时，先确认标签列、特征列与切分行数一致，再读 improvement 或失手句。若脚本声明 FORBIDDEN 或 not a result，该列分数不进入结果表，即使六位小数更小。阶段一固定在 panel.csv 的 AAA 行上；BBB 只在指定天出现，不能把 AAA 的 0.000081 自动搬到 BBB。十行清单与单日脚本的关系是汇总与分项：汇总不替代分项复跑，分项也不省略汇总中的禁止项。

## 实战总结

```bash
python days/55-three-miss-modes/three_miss_modes.py
```

脚本应打印三行 `test MSE line/ridge/tree` 与三行 `line/ridge/tree miss mode` 英文句（与核心块一致）。实现是 [`three_miss_modes.py`](../../days/55-three-miss-modes/three_miss_modes.py)。

今天交出去的是第 55 天打印表上的数与规则句。请保留脚本路径便于复跑。


核对清单：训练行数、测试行数、核心块英文键名、MSE 小数位、FORBIDDEN 句是否与终端一致。