<p align="center"><b>中文</b> &nbsp;&nbsp;·&nbsp;&nbsp; <a href="day-52.en.md">English</a></p>

# 第 52 天 · 五日收益上的树

[第一阶段 · 模型](README.md) · 可运行

今天的学习要点：lag4 阈值 −0.020177，左 0.0319，右 −0.0014，train MSE 0.000378，test MSE 0.000174，大于直线 0.000081

## 费曼法讲解

树桩在训练段上只切 lag4 一刀：lag4≤−0.020177 预测左叶均值 0.0319，否则预测 −0.0014。这是台阶函数，不是五个连续系数；左右均值差约 0.0333，远大于单个 lag 权重。

train MSE 0.000378 在训练行上往往更乐观，因为切点与叶均值都见过这些行。test MSE 0.000174 仍高于直线 0.000081，说明「训练上最好的单 lag 阈值」不自动带来更小 hold-out MSE。

读数时 train 与 test 共用同一阈值与左右常数，差别只在行集合。不要把 train 0.000378 写成泛化证据。

数据来自 days/data/panel.csv 的 AAA 行：简单收益由复权收盘相邻两日比值减一。有效样本从第五个收益之后才开始，因此比原始行数少五行。默认切分是这些有效行按日期排序后的前百分之七十五训练、其余测试（本段多数课为 train=54、test=19）。同一交易日的 high、low、close 不能解释当日收益；同日 market 收益也不能当作合法标签或特征，除非当天脚本明确允许。

## 核心知识

```text
split column = lag 4
threshold = -0.020177
left mean = 0.0319  right mean = -0.0014
train MSE = 0.000378
test MSE = 0.000174
```


return 上的 test MSE 与早期「时间对价格水平」的 SSE 不是一列数；第 51 天及以后不要把第 45、46 天的树 SSE 贴进 return 表。hold-out 行是唯一评分集合；系数与阈值只在训练段估计。

| 概念 | 本课是否变动 | 备注 |
|---|---|---|
| 五 lag 直线系数 | 多数课 frozen | 来自第 51 天 train |
| test MSE 0.000081 | 仅 MSE 课重印 | 诊断课改读 MAE/方向/账单 |
| forbidden OHLC/market | 合同不变 | 见第 56–57、67 天 |
| train/test 行数 | 默认 54/19 | 第 58 天按年切分例外 |

## 核心块逐行读法

第 52 天 stdout 核心块共 5 行。下面逐行说明读法纪律（不是改写成口语数字）：

- `split column = lag 4`：键名、等号两侧空格、负号与小数位须与终端一致。中文解释可以写长，但这行英文与数字是 diff 基准；不要把 false 写成中文「否」、不要把 FORBIDDEN 行删掉、不要把 bill −18 写成 18。若该行含 test MSE，默认指 hold-out 平均平方误差；若含 FORBIDDEN，表示该列不得进入合法特征。批改时对此行做逐字 diff，而不是只看摘要段。
- `threshold = -0.020177`：键名、等号两侧空格、负号与小数位须与终端一致。中文解释可以写长，但这行英文与数字是 diff 基准；不要把 false 写成中文「否」、不要把 FORBIDDEN 行删掉、不要把 bill −18 写成 18。若该行含 test MSE，默认指 hold-out 平均平方误差；若含 FORBIDDEN，表示该列不得进入合法特征。批改时对此行做逐字 diff，而不是只看摘要段。
- `left mean = 0.0319  right mean = -0.0014`：键名、等号两侧空格、负号与小数位须与终端一致。中文解释可以写长，但这行英文与数字是 diff 基准；不要把 false 写成中文「否」、不要把 FORBIDDEN 行删掉、不要把 bill −18 写成 18。若该行含 test MSE，默认指 hold-out 平均平方误差；若含 FORBIDDEN，表示该列不得进入合法特征。批改时对此行做逐字 diff，而不是只看摘要段。
- `train MSE = 0.000378`：键名、等号两侧空格、负号与小数位须与终端一致。中文解释可以写长，但这行英文与数字是 diff 基准；不要把 false 写成中文「否」、不要把 FORBIDDEN 行删掉、不要把 bill −18 写成 18。若该行含 test MSE，默认指 hold-out 平均平方误差；若含 FORBIDDEN，表示该列不得进入合法特征。批改时对此行做逐字 diff，而不是只看摘要段。
- `test MSE = 0.000174`：键名、等号两侧空格、负号与小数位须与终端一致。中文解释可以写长，但这行英文与数字是 diff 基准；不要把 false 写成中文「否」、不要把 FORBIDDEN 行删掉、不要把 bill −18 写成 18。若该行含 test MSE，默认指 hold-out 平均平方误差；若含 FORBIDDEN，表示该列不得进入合法特征。批改时对此行做逐字 diff，而不是只看摘要段。

lag-5 阶段常用锚点：line test MSE 0.000081（第 51、56、57、69 等课）、volume helped on the test stretch = false（第 54 天）、total bill line = -18.0000（第 75、79 天）。若本课核心块不含某锚点，正文中也不要为了「看起来完整」而提前写入；若本课含某锚点，不得四舍五入或去掉负号。第 58 天按年切分时的 0.000782 是切分实验，不能覆盖 0.000081 标尺。第 65、68 天 BBB 的 0.000105 与 AAA 并列，禁止自动搬运结论。

## 拓展领域

与第 44–48 天价格水平树对比：那里的标签是收盘，这里是 return；SSE 数字不可横向粘贴。下一课换随机种子看树切点是否变，直线权重应不变。

若报告写「树更灵活所以 test 更好」，本日 stdout 直接否定：0.000174>0.000081。

## 与前后课的关系

第 51 天的直线是平滑加权；本日树桩把 lag4 切成两档常数预测。train MSE 0.000378 往往诱惑人宣布「非线性更好」，但 test 0.000174 对 0.000081 给出否定答案。请在报告里并排画「台阶」与「斜率」示意图，标注阈值 −0.020177。第 53 天会换 seed 看树切点漂移，直线权重应不动。复习第 44–48 天时，只借直觉，不借 SSE 数字。若你在 sklearn 里用 DecisionTreeRegressor(max_depth=1)，请确认 split 特征与阈值与 stdout 一致，而不是默认 gini 分类树。交作业除核心块外，用一句话说明：为什么 train MSE 不能替代 test MSE 当泛化论据。

给工程师的阅读顺序：先跑本日脚本对照 stdout，再读正文；不要跳过第 51 天直接读诊断课，否则不知道直线系数从哪来。写单元测试时，对 frozen 系数在 hold-out 上断言 MSE 或账单与打印一致；失败常见原因是混用 train 行或把 BBB 行掺进 AAA。文档截图应至少露出核心块英文键名与六位小数，便于他人 diff。复现环境建议 python3 与仓库 pinned numpy；末位浮点差不改变本课结论，但不应改合同整数如 quiet=10、jump=5、direction wrong=3。

## 实战总结

```bash
python3 days/52-five-lag-tree/five_lag_tree.py
```

脚本应打印与核心块一致的 stdout 行。实现是 [`five_lag_tree.py`](../../days/52-five-lag-tree/five_lag_tree.py).

今天交出去的是 lag4 切点、左右均值与 train/test MSE 四行。下一课固定直线、扰动树种子。

自检清单：训练/测试行数是否与脚本一致；核心块英文键名、符号、六位小数是否与终端逐字相同；FORBIDDEN 与 not a result 句是否原样保留；不要把 line 与 tree 的 MSE 或 bill 列对调；AAA 的 0.000081 与 volume helped=false 与 bill −18 等 lag-5 锚点未被改写。


第 52 天补记：lag-5 合同锚点包括 line test MSE 0.000081、volume helped=false（第 54 天）、total bill line=−18.0000（第 75 天）。改切分或 name 会改分数，但未重跑脚本时不得手改上述字面量。