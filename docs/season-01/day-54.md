<p align="center"><b>中文</b> &nbsp;&nbsp;·&nbsp;&nbsp; <a href="day-54.en.md">English</a></p>

# 第 54 天 · 去掉成交量

[第一阶段 · 模型](README.md) · 可运行

今天的学习要点：五 lag test MSE 0.000081；加 volume 0.000121；MSE rise −0.000040；volume helped=false

## 费曼法讲解

对照实验：先拟合五 lag 直线得 test 0.000081，再在同样切分上多加一列 volume 得 0.000121。MSE rise when volume removed = −0.000040 的定义是 mse5−mse6；负号表示去掉 volume 后五 lag 模型更好。

volume helped=false 应读成「加 volume hurt test MSE」，不是「volume 列缺失」或「volume 无信息」。

第 19 天曾用未缩放 volume 做价格实验；这里的 volume 进入 return 设计，仍要在 hold-out 上判优劣，不能只看 train。

数据来自 days/data/panel.csv 的 AAA 行：简单收益由复权收盘相邻两日比值减一。有效样本从第五个收益之后才开始，因此比原始行数少五行。默认切分是这些有效行按日期排序后的前百分之七十五训练、其余测试（本段多数课为 train=54、test=19）。同一交易日的 high、low、close 不能解释当日收益；同日 market 收益也不能当作合法标签或特征，除非当天脚本明确允许。

五 lag  alone 时 test MSE 0.000081；加入 volume 后 0.000121。MSE rise when volume removed = −0.000040 的符号与大小要按 stdout 读：本 stretch 上 volume 没有帮助 test MSE，故 volume helped = false。

volume 是同日信息，与 forbidden OHLC 同类风险：除非课脚本允许，否则不能把「加列后 MSE 变化」当成合法改进。本课允许做 ablation 对比，但结论句是 false，不是「volume 无用于一切样本」。

解释 0.000121>0.000081 时，写「hold-out 上多一列同期 volume 增大误差」，不要写「模型讨厌成交量」。frozen 直线系数仍来自第 51 天 train，volume 列只进扩展特征实验。

quiet=10、jump=5、direction wrong=3 是第 71 天打印的合同整数；诊断课引用时不要改成约数或百分比，除非脚本另给分母定义。

第 26 天随机切分与第 58 天日历切分都会改 test 行集合；改集合后所有 MSE/MAE/bill 都要重跑，不能手改单个数字。

第 70 天十行摘要适合 onboarding，但不替代分项脚本；新人仍应至少重跑第 51、56、67 三天验证环境。

研究面板时，lag1 是上一交易日收益，不是上一行 CSV 收益；排序必须是 date 升序，否则 lag 特征与标签同时被破坏。

hold-out 十九行是唯一报告 test MSE 的集合；训练 RSS 或 train MSE 只能作诊断，不能替代 0.000081 标尺。写论文 Results 段时应写明 split 语汇与 name=AAA，Methods 段应写明 forbidden 与 lag 构造，否则读者无法复现 stdout。

## 核心知识

```text
test MSE five lags only = 0.000081
test MSE five lags and volume = 0.000121
MSE rise when volume removed = -0.000040
volume helped on the test stretch = false
```

return 上的 test MSE 与早期「时间对价格水平」的 SSE 不是一列数；第 51 天及以后不要把第 45、46 天的树 SSE 贴进 return 表。hold-out 行是唯一评分集合；系数与阈值只在训练段估计。

| 概念 | 本课是否变动 | 备注 |
|---|---|---|
| 五 lag 直线系数 | 多数课 frozen | 来自第 51 天 train |
| test MSE 0.000081 | 仅 MSE 课重印 | 诊断课改读 MAE/方向/账单 |
| forbidden OHLC/market | 合同不变 | 见第 56–57、67 天 |
| train/test 行数 | 默认 54/19 | 第 58 天按年切分例外 |

第 54 天 stdout 核心块共 4 行。下面逐行说明读法纪律（不是改写成口语数字）：

- `test MSE five lags only = 0.000081`：键名、等号两侧空格、负号与小数位须与终端一致。中文解释可以写长，但这行英文与数字是 diff 基准；不要把 false 写成中文「否」、不要把 FORBIDDEN 行删掉、不要把 bill −18 写成 18。若该行含 test MSE，默认指 hold-out 平均平方误差；若含 FORBIDDEN，表示该列不得进入合法特征。批改时对此行做逐字 diff，而不是只看摘要段。
- `test MSE five lags and volume = 0.000121`：键名、等号两侧空格、负号与小数位须与终端一致。中文解释可以写长，但这行英文与数字是 diff 基准；不要把 false 写成中文「否」、不要把 FORBIDDEN 行删掉、不要把 bill −18 写成 18。若该行含 test MSE，默认指 hold-out 平均平方误差；若含 FORBIDDEN，表示该列不得进入合法特征。批改时对此行做逐字 diff，而不是只看摘要段。
- `MSE rise when volume removed = -0.000040`：键名、等号两侧空格、负号与小数位须与终端一致。中文解释可以写长，但这行英文与数字是 diff 基准；不要把 false 写成中文「否」、不要把 FORBIDDEN 行删掉、不要把 bill −18 写成 18。若该行含 test MSE，默认指 hold-out 平均平方误差；若含 FORBIDDEN，表示该列不得进入合法特征。批改时对此行做逐字 diff，而不是只看摘要段。
- `volume helped on the test stretch = false`：键名、等号两侧空格、负号与小数位须与终端一致。中文解释可以写长，但这行英文与数字是 diff 基准；不要把 false 写成中文「否」、不要把 FORBIDDEN 行删掉、不要把 bill −18 写成 18。若该行含 test MSE，默认指 hold-out 平均平方误差；若含 FORBIDDEN，表示该列不得进入合法特征。批改时对此行做逐字 diff，而不是只看摘要段。

lag-5 阶段常用锚点：line test MSE 0.000081（第 51、56、57、69 等课）、volume helped on the test stretch = false（第 54 天）、total bill line = -18.0000（第 75、79 天）。若本课核心块不含某锚点，正文中也不要为了「看起来完整」而提前写入；若本课含某锚点，不得四舍五入或去掉负号。第 58 天按年切分时的 0.000782 是切分实验，不能覆盖 0.000081 标尺。第 65、68 天 BBB 的 0.000105 与 AAA 并列，禁止自动搬运结论。

## 拓展领域

写论文式 ablation 时，列名应写 five lags only 与 five lags and volume，不要合并成「加特征更好」。第 70 天十行清单会再次提到 volume did not help；与今日 false 一致。

下一课比较 line、ridge、tree 三模型 MSE 与失手句式。

对照实验的写法应是：基线 five lags only=0.000081，处理组加 volume=0.000121。MSE rise −0.000040 与 volume helped=false 必须同页出现，否则读者会以为 volume 列缺失。第 19 天曾在价格水平玩 volume；今天是 return 标签上的 ablation，结论可以相反，不要自动搬运。第 70 天十行 recap 会写 volume did not help；与本日 false 一致，提交阶段一总结时请交叉引用。若你在特征工程里做 log(volume)，仍须 hold-out 判优劣；train 上 R² 上升不是交付理由。

给工程师的阅读顺序：先跑本日脚本对照 stdout，再读正文；不要跳过第 51 天直接读诊断课，否则不知道直线系数从哪来。写单元测试时，对 frozen 系数在 hold-out 上断言 MSE 或账单与打印一致；失败常见原因是混用 train 行或把 BBB 行掺进 AAA。文档截图应至少露出核心块英文键名与六位小数，便于他人 diff。复现环境建议 python3 与仓库 pinned numpy；末位浮点差不改变本课结论，但不应改合同整数如 quiet=10、jump=5、direction wrong=3。

第 55 天会把 line/ridge/tree 的 miss mode 并排；本日只建立 volume 无效锚点。研究日志里把 false 与切分、name=AAA 同页保存。

复现：对照两次 test MSE 与 rise 行；禁止四舍五入到三位小数。

写组会材料时分两栏：左栏 stdout 英文键名，右栏中文解释。任何只出现中文数字、不出现英文键名的 slide 都无法通过批改 diff。

第 40 天泄漏清单讲的是列语义；第 56–57 天讲的是同行 OHLC 与 market 的拒绝规则。两清单叠加，不是互相替代。

树桩与 straight line 的对比应写在 hold-out 上：train MSE 更低常见于见过标签的切点，不能自动推广到 test。

若你在 notebook 里 merge panel 与 market 列，请先核对 merge key 是 date+name 而非行号；行号 merge 等价于拆配对。

报告里写「改进」一词时，请标明 baseline 是零预测、朴素均值还是第 51 天 line；不同 baseline 的 improvement 数字不可互换。

FORBIDDEN 行不是装饰：它告诉特征工程代码应 reject 哪些列。实现若 silently drop 列而不打印 false/true，复盘时会失去证据。

方向类分数用 sign(ŷ) 与 sign(y) 比较；水平类分数用 (y−ŷ)² 或 |y−ŷ|。混读两类分数会把 jump 日方向对但水平差大的日子判成「全错」。

bill 表里的 cost 整数来自脚本合同，不是货币单位；读 total bill line = −18.0000 时，把它当作加权失误计数，不是美元。

第 54 天 volume helped=false 表示在该 test stretch 上扩展特征未降 MSE；不代表 volume 在训练段无解释力，也不代表永远无效。

交阶段作业：中文叙述可以长，但附录必须贴 stdout 核心块；没有附录，叙述里的数字无法被同伴独立验证。

第 56–57 天会把任务句与 FORBIDDEN 行写进 stdout；本课仍默认五列滞后收益加截距，同日 high/low/close 不得进特征。第 67 天 market lag 泄漏实验会打印 not a result——那是非法列，不是本课分数。

## 实战总结

```bash
python3 days/54-drop-volume/drop_volume.py
```

脚本应打印与核心块一致的 stdout 行。实现是 [`drop_volume.py`](../../days/54-drop-volume/drop_volume.py).

自检清单：训练/测试行数是否与脚本一致；核心块英文键名、符号、六位小数是否与终端逐字相同；FORBIDDEN 与 not a result 句是否原样保留；不要把 line 与 tree 的 MSE 或 bill 列对调；AAA 的 0.000081 与 volume helped=false 与 bill −18 等 lag-5 锚点未被改写。