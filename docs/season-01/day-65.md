<p align="center"><b>中文</b> &nbsp;&nbsp;·&nbsp;&nbsp; <a href="day-65.en.md">English</a></p>

# 第 65 天 · 第二只股票

[第一阶段 · 模型](README.md) · 可运行

今天的学习要点：AAA MSE 0.000081；BBB 0.000105；勿自动搬结论

## 费曼法讲解

同一管道、同一 lag 规则，换 name=BBB 得 test MSE 0.000105，高于 AAA 的 0.000081。

结论不能从 AAA 自动搬到 BBB；每只股票应独立估计系数与分数。

BBB 波动结构与 AAA 不同，五 lag 线性可解释力也会变。

数据来自 days/data/panel.csv 的 AAA 行：简单收益由复权收盘相邻两日比值减一。有效样本从第五个收益之后才开始，因此比原始行数少五行。默认切分是这些有效行按日期排序后的前百分之七十五训练、其余测试（本段多数课为 train=54、test=19）。同一交易日的 high、low、close 不能解释当日收益；同日 market 收益也不能当作合法标签或特征，除非当天脚本明确允许。

第 65 天第二只股票：AAA test MSE = 0.000081，BBB test MSE = 0.000105。并列打印，禁止把 AAA 数字自动搬到 BBB 结论。

读核心块时请把英文键名当作 diff 基准：等号两侧空格、负号、六位小数与 FORBIDDEN 句都不可本地化改写。中文解释可以展开，但不要把 false 写成「否」、不要把 not a result 删掉。批改时优先逐行 diff stdout，再看叙述是否误导。

与第 51 天 frozen 直线对照：凡是 test MSE 课，0.000081 来自同一系数与十九行 hold-out；诊断课改读 MAE、方向或 bill，但不得回写修改 0.000081。第 58 天 0.000782 与 BBB 0.000105 只在指定天出现，禁止自动搬运结论。

交阶段作业：中文叙述可以长，但附录必须贴 stdout 核心块；没有附录，叙述里的数字无法被同伴独立验证。

与第 7 天留出思想一致：分数行必须在训练信息集之后。第 58 天按年切分会得到 0.000782，那是切分实验，不能覆盖默认 0.000081。改切分必重跑全链脚本，禁止手改合同字面量。

frozen 系数课意味着 test 行只代入 ŷ=Xβ̂，不在 test 上 refit。direction、quiet、jump 课（第 71 天起）改读分类与账单，但直线 MSE 锚点仍指向第 51 天估计。

写组会材料时分两栏：左栏 stdout 英文键名，右栏中文解释。任何只出现中文数字、不出现英文键名的 slide 都无法通过批改 diff。

树桩与 straight line 的对比应写在 hold-out 上：train MSE 更低常见于见过标签的切点，不能自动推广到 test。

报告里写「改进」一词时，请标明 baseline 是零预测、朴素均值还是第 51 天 line；不同 baseline 的 improvement 数字不可互换。

## 核心知识

```text
name = AAA test MSE = 0.000081
name = BBB test MSE = 0.000105
```

return 上的 test MSE 与早期「时间对价格水平」的 SSE 不是一列数；第 51 天及以后不要把第 45、46 天的树 SSE 贴进 return 表。hold-out 行是唯一评分集合；系数与阈值只在训练段估计。

| 概念 | 本课是否变动 | 备注 |
|---|---|---|
| 五 lag 直线系数 | 多数课 frozen | 来自第 51 天 train |
| test MSE 0.000081 | 仅 MSE 课重印 | 诊断课改读 MAE/方向/账单 |
| forbidden OHLC/market | 合同不变 | 见第 56–57、67 天 |
| train/test 行数 | 默认 54/19 | 第 58 天按年切分例外 |

第 65 天 stdout 核心块共 2 行。下面逐行说明读法纪律（不是改写成口语数字）：

- `name = AAA test MSE = 0.000081`：键名、等号两侧空格、负号与小数位须与终端一致。中文解释可以写长，但这行英文与数字是 diff 基准；不要把 false 写成中文「否」、不要把 FORBIDDEN 行删掉、不要把 bill −18 写成 18。若该行含 test MSE，默认指 hold-out 平均平方误差；若含 FORBIDDEN，表示该列不得进入合法特征。批改时对此行做逐字 diff，而不是只看摘要段。
- `name = BBB test MSE = 0.000105`：键名、等号两侧空格、负号与小数位须与终端一致。中文解释可以写长，但这行英文与数字是 diff 基准；不要把 false 写成中文「否」、不要把 FORBIDDEN 行删掉、不要把 bill −18 写成 18。若该行含 test MSE，默认指 hold-out 平均平方误差；若含 FORBIDDEN，表示该列不得进入合法特征。批改时对此行做逐字 diff，而不是只看摘要段。

lag-5 阶段常用锚点：line test MSE 0.000081（第 51、56、57、69 等课）、volume helped on the test stretch = false（第 54 天）、total bill line = -18.0000（第 75、79 天）。若本课核心块不含某锚点，正文中也不要为了「看起来完整」而提前写入；若本课含某锚点，不得四舍五入或去掉负号。第 58 天按年切分时的 0.000782 是切分实验，不能覆盖 0.000081 标尺。第 65、68 天 BBB 的 0.000105 与 AAA 并列，禁止自动搬运结论。

## 拓展领域

第 68 天用 pipeline(name) 统一入口，仍打印两行 MSE。

多股票面板里，泄漏规则与切分按 name 分组进行，不能混行训练。

AAA test MSE 0.000081，BBB 0.000105。同一管道不同 name，结论不能自动搬运。请在表格里分两行写 name 与 MSE，不要用「我们模型 0.000081」概括全面板。第 68 天 pipeline(name) 会复印这两行；本日是直接调用。多股票训练时禁止混行 fit；每个 name 独立 lag 向量。若 BBB 权重与 AAA 并排，记得 hold-out 行数可能不同——以脚本为准。

给工程师的阅读顺序：先跑本日脚本对照 stdout，再读正文；不要跳过第 51 天直接读诊断课，否则不知道直线系数从哪来。写单元测试时，对 frozen 系数在 hold-out 上断言 MSE 或账单与打印一致；失败常见原因是混用 train 行或把 BBB 行掺进 AAA。文档截图应至少露出核心块英文键名与六位小数，便于他人 diff。复现环境建议 python3 与仓库 pinned numpy；末位浮点差不改变本课结论，但不应改合同整数如 quiet=10、jump=5、direction wrong=3。

工程师复现顺序：先跑本日脚本抄终端，再读正文；跳过第 51 天会导致不知道系数从哪来。单元测试应对 hold-out 断言与打印一致；常见失败是混 train 行、混 BBB、或把价格 SSE 当 return MSE。

交作业时除核心块外，用一段话说明本课「改的是评分/合同/标签中的哪一项」，并引用至少一个 stdout 数字锚点。截图应露出 bash 命令与英文键名，便于同伴复现。

研究面板时，lag1 是上一交易日收益，不是上一行 CSV 收益；排序必须是 date 升序，否则 lag 特征与标签同时被破坏。

第 54 天 volume helped=false 表示在该 test stretch 上扩展特征未降 MSE；不代表 volume 在训练段无解释力，也不代表永远无效。

hold-out 十九行是唯一报告 test MSE 的集合；训练 RSS 或 train MSE 只能作诊断，不能替代 0.000081 标尺。写论文 Results 段时应写明 split 语汇与 name=AAA，Methods 段应写明 forbidden 与 lag 构造，否则读者无法复现 stdout。

第 56–57 天会把任务句与 FORBIDDEN 行写进 stdout；本课仍默认五列滞后收益加截距，同日 high/low/close 不得进特征。第 67 天 market lag 泄漏实验会打印 not a result——那是非法列，不是本课分数。

手算核对时先在纸上列 train fifty-four 与 test nineteen，再对照核心块。若用 sklearn 复现，请固定 train 掩码；失败常见原因是把 BBB 行掺进 AAA 或把价格残差 SSE 当 return MSE。

文档截图应露出英文键名与六位小数；中文段落可以长，但 diff 基准是终端 stdout。不要把 false 写成中文「否」，不要把 bill −18 写成 18。

第 9 天行序不变性适用于同一设计矩阵的行置换；panel 上 shuffle 后再 shift lag 会破坏对齐，不能引用行序不变性当挡箭牌。

return 标签是相邻 adj_close 简单收益；与第 1–10 天价格对时间 OLS 不同列量纲。混贴 3.2700 斜率或 96.339 RSS 表示标签合同读错。

第 40 天泄漏清单讲的是列语义；第 56–57 天讲的是同行 OHLC 与 market 的拒绝规则。两清单叠加，不是互相替代。

quiet=10、jump=5、direction wrong=3 是第 71 天打印的合同整数；诊断课引用时不要改成约数或百分比，除非脚本另给分母定义。

若你在 notebook 里 merge panel 与 market 列，请先核对 merge key 是 date+name 而非行号；行号 merge 等价于拆配对。

第 26 天随机切分与第 58 天日历切分都会改 test 行集合；改集合后所有 MSE/MAE/bill 都要重跑，不能手改单个数字。

FORBIDDEN 行不是装饰：它告诉特征工程代码应 reject 哪些列。实现若 silently drop 列而不打印 false/true，复盘时会失去证据。

## 实战总结

```bash
python3 days/65-second-name/second_name.py
```

脚本应打印与核心块一致的 stdout 行。实现是 [`second_name.py`](../../days/65-second-name/second_name.py).

自检清单：训练/测试行数是否与脚本一致；核心块英文键名、符号、六位小数是否与终端逐字相同；FORBIDDEN 与 not a result 句是否原样保留；不要把 line 与 tree 的 MSE 或 bill 列对调；AAA 的 0.000081 与 volume helped=false 与 bill −18 等 lag-5 锚点未被改写。