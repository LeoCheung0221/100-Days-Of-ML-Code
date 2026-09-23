<p align="center"><b>中文</b> &nbsp;&nbsp;·&nbsp;&nbsp; <a href="day-56.en.md">English</a></p>

# 第 56 天 · 下一日收益

[第一阶段 · 模型](README.md) · 可运行

今天的学习要点：task 行声明 lag1–5 预测 AAA 当日收益；train=54，test=19，test MSE=0.000081

## 费曼法讲解

第 56 天把「我们在做什么」写进 stdout 合同：target 是 same-day simple return，forbidden 是 same-row OHLC。这不是新模型，特征与第 51 天相同，因此 test MSE 仍是 0.000081。

train rows=54、test rows=19 与 seventy-five percent 切分一致；写报告时把行数与 MSE 并列，避免只抄分数。

合同行的价值是防止 silent leakage：若有人把 close 偷偷加进 X，forbidden 行与 feature build 应对不上。

数据来自 days/data/panel.csv 的 AAA 行：简单收益由复权收盘相邻两日比值减一。有效样本从第五个收益之后才开始，因此比原始行数少五行。默认切分是这些有效行按日期排序后的前百分之七十五训练、其余测试（本段多数课为 train=54、test=19）。同一交易日的 high、low、close 不能解释当日收益；同日 market 收益也不能当作合法标签或特征，除非当天脚本明确允许。

## 核心知识

```text
task = predict today's return from lags 1 through 5 on AAA adj_close
target = same-day simple return on adjusted close
forbidden = same-row high low close as features
train rows = 54 test rows = 19
test MSE = 0.000081
```


return 上的 test MSE 与早期「时间对价格水平」的 SSE 不是一列数；第 51 天及以后不要把第 45、46 天的树 SSE 贴进 return 表。hold-out 行是唯一评分集合；系数与阈值只在训练段估计。

| 概念 | 本课是否变动 | 备注 |
|---|---|---|
| 五 lag 直线系数 | 多数课 frozen | 来自第 51 天 train |
| test MSE 0.000081 | 仅 MSE 课重印 | 诊断课改读 MAE/方向/账单 |
| forbidden OHLC/market | 合同不变 | 见第 56–57、67 天 |
| train/test 行数 | 默认 54/19 | 第 58 天按年切分例外 |

## 核心块逐行读法

第 56 天 stdout 核心块共 5 行。下面逐行说明读法纪律（不是改写成口语数字）：

- `task = predict today's return from lags 1 through 5 on AAA adj_close`：键名、等号两侧空格、负号与小数位须与终端一致。中文解释可以写长，但这行英文与数字是 diff 基准；不要把 false 写成中文「否」、不要把 FORBIDDEN 行删掉、不要把 bill −18 写成 18。若该行含 test MSE，默认指 hold-out 平均平方误差；若含 FORBIDDEN，表示该列不得进入合法特征。批改时对此行做逐字 diff，而不是只看摘要段。
- `target = same-day simple return on adjusted close`：键名、等号两侧空格、负号与小数位须与终端一致。中文解释可以写长，但这行英文与数字是 diff 基准；不要把 false 写成中文「否」、不要把 FORBIDDEN 行删掉、不要把 bill −18 写成 18。若该行含 test MSE，默认指 hold-out 平均平方误差；若含 FORBIDDEN，表示该列不得进入合法特征。批改时对此行做逐字 diff，而不是只看摘要段。
- `forbidden = same-row high low close as features`：键名、等号两侧空格、负号与小数位须与终端一致。中文解释可以写长，但这行英文与数字是 diff 基准；不要把 false 写成中文「否」、不要把 FORBIDDEN 行删掉、不要把 bill −18 写成 18。若该行含 test MSE，默认指 hold-out 平均平方误差；若含 FORBIDDEN，表示该列不得进入合法特征。批改时对此行做逐字 diff，而不是只看摘要段。
- `train rows = 54 test rows = 19`：键名、等号两侧空格、负号与小数位须与终端一致。中文解释可以写长，但这行英文与数字是 diff 基准；不要把 false 写成中文「否」、不要把 FORBIDDEN 行删掉、不要把 bill −18 写成 18。若该行含 test MSE，默认指 hold-out 平均平方误差；若含 FORBIDDEN，表示该列不得进入合法特征。批改时对此行做逐字 diff，而不是只看摘要段。
- `test MSE = 0.000081`：键名、等号两侧空格、负号与小数位须与终端一致。中文解释可以写长，但这行英文与数字是 diff 基准；不要把 false 写成中文「否」、不要把 FORBIDDEN 行删掉、不要把 bill −18 写成 18。若该行含 test MSE，默认指 hold-out 平均平方误差；若含 FORBIDDEN，表示该列不得进入合法特征。批改时对此行做逐字 diff，而不是只看摘要段。

lag-5 阶段常用锚点：line test MSE 0.000081（第 51、56、57、69 等课）、volume helped on the test stretch = false（第 54 天）、total bill line = -18.0000（第 75、79 天）。若本课核心块不含某锚点，正文中也不要为了「看起来完整」而提前写入；若本课含某锚点，不得四舍五入或去掉负号。第 58 天按年切分时的 0.000782 是切分实验，不能覆盖 0.000081 标尺。第 65、68 天 BBB 的 0.000105 与 AAA 并列，禁止自动搬运结论。

## 拓展领域

与第 40 天泄漏清单衔接：列里含未来或 same-bar 价格仍是非法，只是今天用英文 task 行显式化。

下一课在 feature build 层拒绝 same-bar OHLC 并打印 FORBIDDEN 标记。

## 与前后课的关系

本日数字与第 51 天相同，价值在 task/forbidden/train/test 四行合同。把它当作 README 里的「可执行规格」。CI 可 snapshot 这五条与 test MSE 0.000081；若 MSE 变了而 task 行没变，说明数据或切分被改。第 57 天会在列级别打印 FORBIDDEN same-bar；本日 forbidden 行是语义层，下一天是构建器层。新人 onboarding：先背 task 行，再背 lag 权重；否则后面诊断课不知道预测什么。与第 40 天泄漏清单对照：same-row OHLC 仍非法，只是今天用英文写进 stdout。

给工程师的阅读顺序：先跑本日脚本对照 stdout，再读正文；不要跳过第 51 天直接读诊断课，否则不知道直线系数从哪来。写单元测试时，对 frozen 系数在 hold-out 上断言 MSE 或账单与打印一致；失败常见原因是混用 train 行或把 BBB 行掺进 AAA。文档截图应至少露出核心块英文键名与六位小数，便于他人 diff。复现环境建议 python3 与仓库 pinned numpy；末位浮点差不改变本课结论，但不应改合同整数如 quiet=10、jump=5、direction wrong=3。

## 实战总结

```bash
python3 days/56-next-day-task/next_day_task.py
```

脚本应打印与核心块一致的 stdout 行。实现是 [`next_day_task.py`](../../days/56-next-day-task/next_day_task.py).



自检清单：训练/测试行数是否与脚本一致；核心块英文键名、符号、六位小数是否与终端逐字相同；FORBIDDEN 与 not a result 句是否原样保留；不要把 line 与 tree 的 MSE 或 bill 列对调；AAA 的 0.000081 与 volume helped=false 与 bill −18 等 lag-5 锚点未被改写。


第 56 天补记：lag-5 合同锚点包括 line test MSE 0.000081、volume helped=false（第 54 天）、total bill line=−18.0000（第 75 天）。改切分或 name 会改分数，但未重跑脚本时不得手改上述字面量。