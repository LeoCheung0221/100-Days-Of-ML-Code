<p align="center"><b>中文</b> &nbsp;&nbsp;·&nbsp;&nbsp; <a href="day-74.en.md">English</a></p>

# 第 74 天 · 误差前五名

[第一阶段 · 模型](README.md) · 可运行

今天的学习要点：前五：2024-04-03 err=0.019717 jump 方向对；04-18 0.017449 jump 对；04-22 0.014328 mid 错；03-28 0.013401 jump 对；04-02 0.009609 jump 对

## 费曼法讲解

前五按绝对误差排序，不是按 MSE 贡献单独加权。四名 jump、一名 mid（04-22）。

04-22 方向错且为 mid，说明大误差日不一定 jump，方向失手也不一定 jump。

其余四名 jump 方向对，展示「幅度大但符号对」与「幅度中等却 sign 错」可并存。

抄表时保留 class= 与 direction= 英文值，便于与 stdout diff。

数据来自 days/data/panel.csv 的 AAA 行：简单收益由复权收盘相邻两日比值减一。有效样本从第五个收益之后才开始，因此比原始行数少五行。默认切分是这些有效行按日期排序后的前百分之七十五训练、其余测试（本段多数课为 train=54、test=19）。同一交易日的 high、low、close 不能解释当日收益；同日 market 收益也不能当作合法标签或特征，除非当天脚本明确允许。

第 74 天前五误差日：rank 1 2024-04-03 error 0.019717 class jump direction right 等五行。日期、误差、class、direction 四列都要 diff。

读核心块时请把英文键名当作 diff 基准：等号两侧空格、负号、六位小数与 FORBIDDEN 句都不可本地化改写。中文解释可以展开，但不要把 false 写成「否」、不要把 not a result 删掉。批改时优先逐行 diff stdout，再看叙述是否误导。

与第 51 天 frozen 直线对照：凡是 test MSE 课，0.000081 来自同一系数与十九行 hold-out；诊断课改读 MAE、方向或 bill，但不得回写修改 0.000081。第 58 天 0.000782 与 BBB 0.000105 只在指定天出现，禁止自动搬运结论。

文档截图应露出英文键名与六位小数；中文段落可以长，但 diff 基准是终端 stdout。不要把 false 写成中文「否」，不要把 bill −18 写成 18。

return 标签是相邻 adj_close 简单收益；与第 1–10 天价格对时间 OLS 不同列量纲。混贴 3.2700 斜率或 96.339 RSS 表示标签合同读错。

quiet=10、jump=5、direction wrong=3 是第 71 天打印的合同整数；诊断课引用时不要改成约数或百分比，除非脚本另给分母定义。

## 核心知识

```text
rank 1 date = 2024-04-03 error = 0.019717 class = jump direction = right
rank 2 date = 2024-04-18 error = 0.017449 class = jump direction = right
rank 3 date = 2024-04-22 error = 0.014328 class = mid direction = wrong
rank 4 date = 2024-03-28 error = 0.013401 class = jump direction = right
rank 5 date = 2024-04-02 error = 0.009609 class = jump direction = right
```

return 上的 test MSE 与早期「时间对价格水平」的 SSE 不是一列数；第 51 天及以后不要把第 45、46 天的树 SSE 贴进 return 表。hold-out 行是唯一评分集合；系数与阈值只在训练段估计。

第 71–80 天多数只诊断同一条五 lag 直线：系数 frozen 在第 51 天训练段，本课不再重印 test MSE 0.000081，但直线仍是 lag1=−0.1359、lag2=0.0829、lag3=0.1094、lag4=−0.1726、lag5=−0.0803、截距 0.0023 那一套。

| 概念 | 本课是否变动 | 备注 |
|---|---|---|
| 五 lag 直线系数 | 多数课 frozen | 来自第 51 天 train |
| test MSE 0.000081 | 仅 MSE 课重印 | 诊断课改读 MAE/方向/账单 |
| forbidden OHLC/market | 合同不变 | 见第 56–57、67 天 |
| train/test 行数 | 默认 54/19 | 第 58 天按年切分例外 |

第 74 天 stdout 核心块共 5 行。下面逐行说明读法纪律（不是改写成口语数字）：

- `rank 1 date = 2024-04-03 error = 0.019717 class = jump direction = right`：键名、等号两侧空格、负号与小数位须与终端一致。中文解释可以写长，但这行英文与数字是 diff 基准；不要把 false 写成中文「否」、不要把 FORBIDDEN 行删掉、不要把 bill −18 写成 18。若该行含 test MSE，默认指 hold-out 平均平方误差；若含 FORBIDDEN，表示该列不得进入合法特征。批改时对此行做逐字 diff，而不是只看摘要段。
- `rank 2 date = 2024-04-18 error = 0.017449 class = jump direction = right`：键名、等号两侧空格、负号与小数位须与终端一致。中文解释可以写长，但这行英文与数字是 diff 基准；不要把 false 写成中文「否」、不要把 FORBIDDEN 行删掉、不要把 bill −18 写成 18。若该行含 test MSE，默认指 hold-out 平均平方误差；若含 FORBIDDEN，表示该列不得进入合法特征。批改时对此行做逐字 diff，而不是只看摘要段。
- `rank 3 date = 2024-04-22 error = 0.014328 class = mid direction = wrong`：键名、等号两侧空格、负号与小数位须与终端一致。中文解释可以写长，但这行英文与数字是 diff 基准；不要把 false 写成中文「否」、不要把 FORBIDDEN 行删掉、不要把 bill −18 写成 18。若该行含 test MSE，默认指 hold-out 平均平方误差；若含 FORBIDDEN，表示该列不得进入合法特征。批改时对此行做逐字 diff，而不是只看摘要段。
- `rank 4 date = 2024-03-28 error = 0.013401 class = jump direction = right`：键名、等号两侧空格、负号与小数位须与终端一致。中文解释可以写长，但这行英文与数字是 diff 基准；不要把 false 写成中文「否」、不要把 FORBIDDEN 行删掉、不要把 bill −18 写成 18。若该行含 test MSE，默认指 hold-out 平均平方误差；若含 FORBIDDEN，表示该列不得进入合法特征。批改时对此行做逐字 diff，而不是只看摘要段。
- `rank 5 date = 2024-04-02 error = 0.009609 class = jump direction = right`：键名、等号两侧空格、负号与小数位须与终端一致。中文解释可以写长，但这行英文与数字是 diff 基准；不要把 false 写成中文「否」、不要把 FORBIDDEN 行删掉、不要把 bill −18 写成 18。若该行含 test MSE，默认指 hold-out 平均平方误差；若含 FORBIDDEN，表示该列不得进入合法特征。批改时对此行做逐字 diff，而不是只看摘要段。

lag-5 阶段常用锚点：line test MSE 0.000081（第 51、56、57、69 等课）、volume helped on the test stretch = false（第 54 天）、total bill line = -18.0000（第 75、79 天）。若本课核心块不含某锚点，正文中也不要为了「看起来完整」而提前写入；若本课含某锚点，不得四舍五入或去掉负号。第 58 天按年切分时的 0.000782 是切分实验，不能覆盖 0.000081 标尺。第 65、68 天 BBB 的 0.000105 与 AAA 并列，禁止自动搬运结论。

## 拓展领域

第 71–80 天多数只诊断同一条五 lag 直线：系数 frozen 在第 51 天训练段，本课不再重印 test MSE 0.000081，但直线仍是 lag1=−0.1359、lag2=0.0829、lag3=0.1094、lag4=−0.1726、lag5=−0.0803、截距 0.0023 那一套。

第 75 天引入账单：direction wrong −1，jump 日 −3，total −18。

前五误差带日期与 class/direction：04-22 为 mid 且 direction wrong，其余 jump 且 direction right。说明大误差不等于 jump 类，jump 也不保证方向错。抄表保留英文 class= 与 direction=。第 75 天 bill −18 用 jump 与 direction 扣分；本日是无账单排序。若你画误差条形图，请标注 04-22 为唯一 mid。

给工程师的阅读顺序：先跑本日脚本对照 stdout，再读正文；不要跳过第 51 天直接读诊断课，否则不知道直线系数从哪来。写单元测试时，对 frozen 系数在 hold-out 上断言 MSE 或账单与打印一致；失败常见原因是混用 train 行或把 BBB 行掺进 AAA。文档截图应至少露出核心块英文键名与六位小数，便于他人 diff。复现环境建议 python3 与仓库 pinned numpy；末位浮点差不改变本课结论，但不应改合同整数如 quiet=10、jump=5、direction wrong=3。

工程师复现顺序：先跑本日脚本抄终端，再读正文；跳过第 51 天会导致不知道系数从哪来。单元测试应对 hold-out 断言与打印一致；常见失败是混 train 行、混 BBB、或把价格 SSE 当 return MSE。

交作业时除核心块外，用一段话说明本课「改的是评分/合同/标签中的哪一项」，并引用至少一个 stdout 数字锚点。截图应露出 bash 命令与英文键名，便于同伴复现。

与第 7 天留出思想一致：分数行必须在训练信息集之后。第 58 天按年切分会得到 0.000782，那是切分实验，不能覆盖默认 0.000081。改切分必重跑全链脚本，禁止手改合同字面量。

手算核对时先在纸上列 train fifty-four 与 test nineteen，再对照核心块。若用 sklearn 复现，请固定 train 掩码；失败常见原因是把 BBB 行掺进 AAA 或把价格残差 SSE 当 return MSE。

frozen 系数课意味着 test 行只代入 ŷ=Xβ̂，不在 test 上 refit。direction、quiet、jump 课（第 71 天起）改读分类与账单，但直线 MSE 锚点仍指向第 51 天估计。

第 9 天行序不变性适用于同一设计矩阵的行置换；panel 上 shuffle 后再 shift lag 会破坏对齐，不能引用行序不变性当挡箭牌。

写组会材料时分两栏：左栏 stdout 英文键名，右栏中文解释。任何只出现中文数字、不出现英文键名的 slide 都无法通过批改 diff。

第 40 天泄漏清单讲的是列语义；第 56–57 天讲的是同行 OHLC 与 market 的拒绝规则。两清单叠加，不是互相替代。

树桩与 straight line 的对比应写在 hold-out 上：train MSE 更低常见于见过标签的切点，不能自动推广到 test。

## 实战总结

```bash
python3 days/74-top-five-errors/top_five_errors.py
```

脚本应打印与核心块一致的 stdout 行。实现是 [`top_five_errors.py`](../../days/74-top-five-errors/top_five_errors.py).

自检清单：训练/测试行数是否与脚本一致；核心块英文键名、符号、六位小数是否与终端逐字相同；FORBIDDEN 与 not a result 句是否原样保留；不要把 line 与 tree 的 MSE 或 bill 列对调；AAA 的 0.000081 与 volume helped=false 与 bill −18 等 lag-5 锚点未被改写。