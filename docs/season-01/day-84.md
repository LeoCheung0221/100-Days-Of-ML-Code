<p align="center"><b>中文</b> &nbsp;&nbsp;·&nbsp;&nbsp; <a href="day-84.en.md">English</a></p>

# 第 84 天 · 残差计数表

[第一阶段 · 模型](README.md) · 可运行

今天的学习要点：quiet/jump/direction 与高/低波动并表：高波动 direction wrong 0、低波动 3

## 费曼法讲解

本课把 **两条 regime 轴** 与 **三条诊断轴** 做成八行计数表。Vol 轴来自第 81 天 ISO 周 std 中位数切分；quiet/jump 来自 test 上 |r| 相对中位数与 p75；direction wrong 来自 sign(y) 与 sign(ŷ) 不等。直线仍 frozen 自第 51 天 train，表内只 **计数** 与 **子样本 MAE**，不重估系数。

高波动段（十二 test 行）：quiet 6、jump 4、direction wrong **0**、MAE **0.007341**（与第 81 天高波动全体 MAE 一致，因 MAE 对该十二行平均）。低波动段（七行）：quiet 4、jump 1、direction wrong **3**、MAE **0.006362**。关键读法是 **方向错误集中在低波动周**，而 jump 主要集中在高波动周——合并成一个「错误率」会掩盖结构。Christoffersen & Diebold（2006）主张水平与方向分轨；本表是 regime 条件分轨。

Jump 与 quiet 在 test 十九行上互斥划分（median / p75 规则与第 71 天一致）；direction wrong 可与 quiet 或 jump 共存。高波动段 jump 4 与第 82 天交集 n 一致；低波动 jump 1 日可能仍 direction wrong，表不展开日期，第 90 天给 top 失败日。

表内 MAE 行是 **子样本 |r−ŷ| 均值**，不是 MSE 0.000081。工程师 diff 八行 `table high vol ...` / `table low vol ...` 键；空格与六位小数须与 `day_84()` 一致。改切分或 ticker 须重跑全表，禁止手改 6/4/0 等整数。

Campbell、Lo、MacKinlay（1997）强调评估协议可 diff；本 stdout 是 **二维 regime × 三维 mistake 标签** 的最小充分统计。Harvey et al.（2016）提醒小样本格子不要作显著性声明；十九行拆成 12+7 后每格更 sparse。

第 85 天将在高波动周用 MSE 在 line 与 stump 间决策；本表说明高波动段方向全对但水平 MAE 仍可达 0.007341，决策不应只看 direction 计数。

## 核心知识

```text
table high vol quiet days = 6
table high vol jump days = 4
table high vol direction wrong days = 0
table high vol mean abs error = 0.007341
table low vol quiet days = 4
table low vol jump days = 1
table low vol direction wrong days = 3
table low vol mean abs error = 0.006362
```

**实现。** 对 `_lag5_line_test()` 得 test_y、test_hat、dates；`_week_vol_high_low` 得 high/low 索引；quiet/jump/wrong 为布尔掩码；循环打印四行×两 regime。

| 高波动 | quiet | jump | dir wrong | MAE |
|---|---|---|---|---|
| 计数 | 6 | 4 | 0 | 0.007341 |
| 低波动 | 4 | 1 | 3 | 0.006362 |

**合同。** 计数整数须与 stdout 一致；MAE 六位小数。FORBIDDEN 列不变。

## 拓展领域

**稀疏格。** 低波动 direction wrong 3 占七行多数「符号错误」；高波动 jump 4 驱动第 82 天 MAE 叙事。写 memo 时用表而非 prose 重复数字。

**与 bill。** 第 75 天 bill 用 jump cost 3；本表 jump 计数可对照 bill 分母，但不自动相等（bill 还有 direction cost）。

**泄漏与标签。** quiet/jump 用 realized |r|；属于 ex post 诊断，不是 prespec 交易信号。Same-day market 仍 forbidden（第 67 天）。

**复现。** `main(84)`；八行顺序固定：每个 regime 先 quiet 后 jump 后 direction 后 MAE。

**HAC。** 格子计数无 infer；若比较 proportion 需新实验设计。

**ISO 周。** Vol 轴与 81 相同；跨年/短周在 live 数据更常见。

**第 90 天。** 失败日排序用 |r−ŷ|；两 jump horizontal miss 可能落在高波动 jump 四日集合。

**工程师清单。** Slide 用英文键名列；中文只解释定义，不替换键名。

**Andersen et al.（2001）。** Realized vol 分区与水平误差并列报告是常见 desk 习惯；本表是教学极简版。

**Poon & Granger（2003）。** 别把 MAE 差说成 vol 模型 beat 收益模型。

**手算。** 任取高波动 quiet 日，验证 sign(y)=sign(ŷ) 且 |r| 低于 median 阈值。

**切分敏感。** 第 58 天改 test 集合后八行全变；experiment id 须更新。

**脚注模板。** 表前写 vol 定义（ISO 周 std 中位数）、quiet/jump 分位、direction 定义、frozen β 来源。


**与 82 课链接。** 高波动 jump 4 与本课 jump 列一致；MAE 0.007341 等于 81 高波动 MAE。


**合规语言。** 避免「低波动周模型失效」；应写「低波动七行 direction wrong 计数为 3」。


**阅读检查（第 84 天）。** 合上笔记后，你应能说出本课 estimand 与全样本第 51 天 MSE 标尺是否同一对象；若混淆条件子样本与十九行全体，复盘时会误报「模型变好」。


**第 84 天与批改。** 助教只比对 ```text``` 与终端；中文段落写错键名仍会通过 diff，但会误导未来的你——务必把英文键复制进 slide 脚注。


**信息集。** 特征只能使用 Strict past 的 lag 收益与截距，除非当天脚本显式添加 volume；标签是当日简单收益，不能用未来行。


**面板完整性。** complete rows 由第 86 天给出；缺行会让 lag 对齐 silently 错位，stdout 数字整体漂移。


**按年切分实验。** 第 58 天改 test 集合后，本课所有子样本计数与 MSE 都要重跑；不要把 0.000782 写进默认合同 slide。


**方向与水平。** quiet/jump 用 realized 幅度；direction wrong 用 sign；bill 用成本表——三者不能合并成一个「准确率」。


**树与直线。** OLS 在固定设计上是确定的；树切点可能随 seed 变（第 53 天），但本季 hold-out 评分用 frozen 切点。


**泄漏叙事。** 同日 market 列会虚降 MSE 到 0.000094；有效分数是去掉该列后的 0.000081（第 67、91、98 天）。


**执行假设。** 信号按 close 的 adj_close 形成；脚本不发单、滑点为零、不算 PnL（第 92 天）；实盘需另层成本模型。


**闭链验收。** 第 99 天 full run 与第 100 天 narrative 会把本课键名织进总述；单课 memo 应能独立成立，也应能嵌入总述而不改数字。


**字数与质量。** 中文解释服务于理解 estimand，不是替代 stdout；键名一行都不能省。


**脚注模板。** 表前写 vol 定义（ISO 周 std 中位数）、quiet/jump 分位、direction 定义、frozen β 来源。


**与 82 课链接。** 高波动 jump 4 与本课 jump 列一致；MAE 0.007341 等于 81 高波动 MAE。


**合规语言。** 避免「低波动周模型失效」；应写「低波动七行 direction wrong 计数为 3」。


**阅读检查（第 84 天）。** 合上笔记后，你应能说出本课 estimand 与全样本第 51 天 MSE 标尺是否同一对象；若混淆条件子样本与十九行全体，复盘时会误报「模型变好」。


**第 84 天与批改。** 助教只比对 ```text``` 与终端；中文段落写错键名仍会通过 diff，但会误导未来的你——务必把英文键复制进 slide 脚注。


**信息集。** 特征只能使用 Strict past 的 lag 收益与截距，除非当天脚本显式添加 volume；标签是当日简单收益，不能用未来行。


**面板完整性。** complete rows 由第 86 天给出；缺行会让 lag 对齐 silently 错位，stdout 数字整体漂移。


**按年切分实验。** 第 58 天改 test 集合后，本课所有子样本计数与 MSE 都要重跑；不要把 0.000782 写进默认合同 slide。


**方向与水平。** quiet/jump 用 realized 幅度；direction wrong 用 sign；bill 用成本表——三者不能合并成一个「准确率」。


**树与直线。** OLS 在固定设计上是确定的；树切点可能随 seed 变（第 53 天），但本季 hold-out 评分用 frozen 切点。


**泄漏叙事。** 同日 market 列会虚降 MSE 到 0.000094；有效分数是去掉该列后的 0.000081（第 67、91、98 天）。


**执行假设。** 信号按 close 的 adj_close 形成；脚本不发单、滑点为零、不算 PnL（第 92 天）；实盘需另层成本模型。


**闭链验收。** 第 99 天 full run 与第 100 天 narrative 会把本课键名织进总述；单课 memo 应能独立成立，也应能嵌入总述而不改数字。


**字数与质量。** 中文解释服务于理解 estimand，不是替代 stdout；键名一行都不能省。


**脚注模板。** 表前写 vol 定义（ISO 周 std 中位数）、quiet/jump 分位、direction 定义、frozen β 来源。


**与 82 课链接。** 高波动 jump 4 与本课 jump 列一致；MAE 0.007341 等于 81 高波动 MAE。


**合规语言。** 避免「低波动周模型失效」；应写「低波动七行 direction wrong 计数为 3」。


**阅读检查（第 84 天）。** 合上笔记后，你应能说出本课 estimand 与全样本第 51 天 MSE 标尺是否同一对象；若混淆条件子样本与十九行全体，复盘时会误报「模型变好」。


**第 84 天与批改。** 助教只比对 ```text``` 与终端；中文段落写错键名仍会通过 diff，但会误导未来的你——务必把英文键复制进 slide 脚注。


**信息集。** 特征只能使用 Strict past 的 lag 收益与截距，除非当天脚本显式添加 volume；标签是当日简单收益，不能用未来行。


**面板完整性。** complete rows 由第 86 天给出；缺行会让 lag 对齐 silently 错位，stdout 数字整体漂移。


**按年切分实验。** 第 58 天改 test 集合后，本课所有子样本计数与 MSE 都要重跑；不要把 0.000782 写进默认合同 slide。


**方向与水平。** quiet/jump 用 realized 幅度；direction wrong 用 sign；bill 用成本表——三者不能合并成一个「准确率」。


**树与直线。** OLS 在固定设计上是确定的；树切点可能随 seed 变（第 53 天），但本季 hold-out 评分用 frozen 切点。


**泄漏叙事。** 同日 market 列会虚降 MSE 到 0.000094；有效分数是去掉该列后的 0.000081（第 67、91、98 天）。


**执行假设。** 信号按 close 的 adj_close 形成；脚本不发单、滑点为零、不算 PnL（第 92 天）；实盘需另层成本模型。


**闭链验收。** 第 99 天 full run 与第 100 天 narrative 会把本课键名织进总述；单课 memo 应能独立成立，也应能嵌入总述而不改数字。


**字数与质量。** 中文解释服务于理解 estimand，不是替代 stdout；键名一行都不能省。


**脚注模板。** 表前写 vol 定义（ISO 周 std 中位数）、quiet/jump 分位、direction 定义、frozen β 来源。


## 实战总结

```bash
python3 days/84-regime-table/regime_table.py
```

亦可：`python3 -c "from days.run_day import main; main(84)"`。

实现：[`regime_table.py`](../../days/84-regime-table/regime_table.py)。交付：stdout 与 ```text``` 块逐字一致。
