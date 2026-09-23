<p align="center"><b>中文</b> &nbsp;&nbsp;·&nbsp;&nbsp; <a href="day-58.en.md">English</a></p>

# 第 58 天 · 按年切分

[第一阶段 · 模型](README.md) · 可运行

今天的学习要点：切点 2024-02-28，train=33，test=40，test MSE=0.000782，差于 75% 切分 0.000081

## 费曼法讲解

同一五 lag 直线，换切分就换分数。切点 2024-02-28 后，train 只剩 33 行、test 有 40 行，test MSE 升到 0.000782。

这不是模型公式变了，而是信息集与 hold-out 集合变了：更短的训练段估计更噪的系数，更长的测试段包含更多 regime。

与第 27 天时间切分思想一致，但这里用固定日历日而不是比例。不要把 0.000782 与 0.000081 直接比「模型好坏」而不提切分。

写实验记录时必须并列 cut date 与行数；只抄 MSE 会在组会里被问「你到底 hold-out 哪段」。

数据来自 days/data/panel.csv 的 AAA 行：简单收益由复权收盘相邻两日比值减一。有效样本从第五个收益之后才开始，因此比原始行数少五行。默认切分是这些有效行按日期排序后的前百分之七十五训练、其余测试（本段多数课为 train=54、test=19）。同一交易日的 high、low、close 不能解释当日收益；同日 market 收益也不能当作合法标签或特征，除非当天脚本明确允许。

## 核心知识

```text
cut date = 2024-02-28
train rows = 33 test rows = 40
test MSE = 0.000782
```


return 上的 test MSE 与早期「时间对价格水平」的 SSE 不是一列数；第 51 天及以后不要把第 45、46 天的树 SSE 贴进 return 表。hold-out 行是唯一评分集合；系数与阈值只在训练段估计。

| 概念 | 本课是否变动 | 备注 |
|---|---|---|
| 五 lag 直线系数 | 多数课 frozen | 来自第 51 天 train |
| test MSE 0.000081 | 仅 MSE 课重印 | 诊断课改读 MAE/方向/账单 |
| forbidden OHLC/market | 合同不变 | 见第 56–57、67 天 |
| train/test 行数 | 默认 54/19 | 第 58 天按年切分例外 |

## 核心块逐行读法

第 58 天 stdout 核心块共 3 行。下面逐行说明读法纪律（不是改写成口语数字）：

- `cut date = 2024-02-28`：键名、等号两侧空格、负号与小数位须与终端一致。中文解释可以写长，但这行英文与数字是 diff 基准；不要把 false 写成中文「否」、不要把 FORBIDDEN 行删掉、不要把 bill −18 写成 18。若该行含 test MSE，默认指 hold-out 平均平方误差；若含 FORBIDDEN，表示该列不得进入合法特征。批改时对此行做逐字 diff，而不是只看摘要段。
- `train rows = 33 test rows = 40`：键名、等号两侧空格、负号与小数位须与终端一致。中文解释可以写长，但这行英文与数字是 diff 基准；不要把 false 写成中文「否」、不要把 FORBIDDEN 行删掉、不要把 bill −18 写成 18。若该行含 test MSE，默认指 hold-out 平均平方误差；若含 FORBIDDEN，表示该列不得进入合法特征。批改时对此行做逐字 diff，而不是只看摘要段。
- `test MSE = 0.000782`：键名、等号两侧空格、负号与小数位须与终端一致。中文解释可以写长，但这行英文与数字是 diff 基准；不要把 false 写成中文「否」、不要把 FORBIDDEN 行删掉、不要把 bill −18 写成 18。若该行含 test MSE，默认指 hold-out 平均平方误差；若含 FORBIDDEN，表示该列不得进入合法特征。批改时对此行做逐字 diff，而不是只看摘要段。

lag-5 阶段常用锚点：line test MSE 0.000081（第 51、56、57、69 等课）、volume helped on the test stretch = false（第 54 天）、total bill line = -18.0000（第 75、79 天）。若本课核心块不含某锚点，正文中也不要为了「看起来完整」而提前写入；若本课含某锚点，不得四舍五入或去掉负号。第 58 天按年切分时的 0.000782 是切分实验，不能覆盖 0.000081 标尺。第 65、68 天 BBB 的 0.000105 与 AAA 并列，禁止自动搬运结论。

## 拓展领域

第 59 天回到 nineteen 行 test 的 seventy-five percent 切分，与 0.000081 标尺一致。

面板研究里「walk-forward 切分」比单次 random 更常见；本课是教学对比。

## 与前后课的关系

切点 2024-02-28 把 train 压到 33 行、test 扩到 40 行，test MSE=0.000782。与 0.000081 对比时，必须同时对比行数。这不是「模型坏了」，而是估计样本与评分样本都变了。请在笔记里画两个时间轴：75% 切分 vs 按年切分。第 59 天回到 seventy-five percent，恢复 0.000081 标尺；不要把 0.000782 写进 lag-5 锚点。walk-forward 回测常用这种日历切；本课只跑一次，强调「split 是分数的一部分」。若你手算系数，请只在 train=33 上算，再去 40 行 test 评分；混行会假造更漂亮的 MSE。

给工程师的阅读顺序：先跑本日脚本对照 stdout，再读正文；不要跳过第 51 天直接读诊断课，否则不知道直线系数从哪来。写单元测试时，对 frozen 系数在 hold-out 上断言 MSE 或账单与打印一致；失败常见原因是混用 train 行或把 BBB 行掺进 AAA。文档截图应至少露出核心块英文键名与六位小数，便于他人 diff。复现环境建议 python3 与仓库 pinned numpy；末位浮点差不改变本课结论，但不应改合同整数如 quiet=10、jump=5、direction wrong=3。

## 实战总结

```bash
python3 days/58-year-split/year_split.py
```

脚本应打印与核心块一致的 stdout 行。实现是 [`year_split.py`](../../days/58-year-split/year_split.py).



自检清单：训练/测试行数是否与脚本一致；核心块英文键名、符号、六位小数是否与终端逐字相同；FORBIDDEN 与 not a result 句是否原样保留；不要把 line 与 tree 的 MSE 或 bill 列对调；AAA 的 0.000081 与 volume helped=false 与 bill −18 等 lag-5 锚点未被改写。


第 58 天补记：lag-5 合同锚点包括 line test MSE 0.000081、volume helped=false（第 54 天）、total bill line=−18.0000（第 75 天）。改切分或 name 会改分数，但未重跑脚本时不得手改上述字面量。