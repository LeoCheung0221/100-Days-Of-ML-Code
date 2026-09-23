<p align="center"><b>中文</b> &nbsp;&nbsp;·&nbsp;&nbsp; <a href="day-83.en.md">English</a></p>

# 第 83 天 · 低波动周的树

[第一阶段 · 模型](README.md) · 可运行

今天的学习要点：低波动周 7 日：line MSE 0.000059，stump 0.000221，depth-2 0.000219；deeper worse than stump = false

## 费曼法讲解

```mermaid
flowchart LR
  L["line MSE"] --> Cmp["vs stump / depth2"]
```

第 81 天把 test 按 ISO 周波动分成高/低两桶；本课固定 **低波动周** 七行，在 **同一 hold-out 子样本** 上并排比较三种 frozen 预测器的 test MSE。五 lag OLS 直线（系数来自五十四行 train）在低波动周 MSE **0.000059**，低于全 test 标尺 **0.000081**——说明「平静周」上水平预测相对更准，但 **n=7** 极短，不能外推为 unconditional 改进。

树部分沿用第 52–55 天合同：训练段上 `_best_stump` 选 lag 列与阈值，depth-2 在 stump 最优列上 `tree_depth2` 拟合；test 只代入 frozen 切点与叶均值。低波动周上 stump MSE **0.000221**、depth-2 **0.000219**，二者都远高于 line；`deeper tree worse than stump on low vol = false` 表示 **平方误差意义下** depth-2 略优于 stump，但 **仍远劣于 line**。读数时不要把它说成「深树赢了直线」——决策格应看 line 是否最小。

本课 estimand 是 **regime 条件 MSE**，不是全局 re-fit。若在低波动七行上重新估计 OLS，会另开实验；脚本禁止 test refit。MSE 对 tail 敏感；第 82 天已说明高波动 jump 上 MAE 很大，而本课低波动段 jump 仅 1 日（见第 84 天表），故 line 在低波动 MSE 低并不矛盾。

与第 85 天对照：85 在 **高波动周** 用 MSE 在 line 与 stump 间择一（`model kept = line`）；本课在 **低波动周** 展示树族无法逼近 line MSE。Poon & Granger（2003）提醒别混淆「波动预测」与「收益水平预测」——此处全是 \(r_t\) 水平 MSE。

工程师 diff 时认六行英文键；尤其 `deeper tree worse than stump on low vol = false` 的布尔字面量须小写 **false**，与 `day_83()` 一致。改第 58 天切分或 BBB 行须重跑，禁止手改 0.000059 等小数。

## 核心知识

```text
regime = low volatility ISO weeks on test stretch
low vol week days = 7
line test MSE low vol weeks = 0.000059
stump test MSE low vol weeks = 0.000221
depth-2 tree test MSE low vol weeks = 0.000219
deeper tree worse than stump on low vol = false
```

**实现。** 对 `_lag5_xy()` 得 train/test 设计矩阵；`_week_vol_high_low` 在低波动索引上切片 `test_y` 与三种 `hat`；MSE 为均值平方误差。depth-2 列由 train 上 stump 最优 lag 决定。

| 模型 | 低波动周 test MSE | 读法 |
|---|---|---|
| line | 0.000059 | frozen OLS，子样本最优 |
| stump | 0.000221 | 单 lag 阶跃 |
| depth-2 | 0.000219 | 略优于 stump，仍劣于 line |

**合同。** 树在 train 估 split；test 只评分。FORBIDDEN 列规则同第 56–57 天。全 test line MSE 仍为 0.000081，本课 0.000059 是 **条件** 统计量。

## 拓展领域

**样本量。** 七行 MSE 方差极大；Bailey & Lopez de Prado（2014）会要求报告 trial 结构——此处模型族 prespec 为 line/stump/depth-2，但子样本 n 仍小。

**与 MAE 课分工。** 81–82 用 MAE 看水平；本课用 MSE 对齐第 51–55 天树比较传统。memo 并列时应标注 metric。

**深度 vs 宽度。** depth-2 只在单列上扩展，不是随机森林；`false` 只比较 deep 与 stump 的 MSE 次序，不授予「非线性普遍更好」。

**复现链。** 先跑第 51、52 天确认 line 与 stump 全样本数字，再跑本课；`main(83)` 与目录脚本等价。

**HAC / infer。** Newey & West（1987）适用于系数推断；此处仅点估计 MSE，不做「显著优于」措辞。

**第 85 天预告。** 高波动周 MSE 择模；本课说明低波动周树族仍败于 line，支持 85 保留 line 的叙事。

**泄漏。** 同周划分只用 test 日期与收益；不得加入 same-day market（第 67、91 天）。

**训练过拟合。** stump train MSE 常低于 test；本课只报 test 子样本 MSE，不印 train。

**工程师清单。** 六行 stdout 全进 ```text```；布尔行小写；确认 low vol days = 7 与第 81 天一致。

**手算。** 在低波动七行任挑一日，用第 51 天系数算 ŷ，核对 (y−ŷ)² 量级；七行均值应接近 0.000059 量级（MSE 非 MAE）。

**报告脚注。** Slide 上须写「低波动周 n=7、MSE、frozen train 估计」三词，缺一则 estimand 不明。

**与 bill 无关。** 本课不算 direction/jump bill；第 79 天 line bill 仍独立存在。

**阅读检查（第 83 天）。** 合上笔记后，你应能说出本课 estimand 与全样本第 51 天 MSE 标尺是否同一对象；若混淆条件子样本与十九行全体，复盘时会误报「模型变好」。

**第 83 天与批改。** 助教只比对 ```text``` 与终端；中文段落写错键名仍会通过 diff，但会误导未来的你——务必把英文键复制进 slide 脚注。

**信息集。** 特征只能使用 Strict past 的 lag 收益与截距，除非当天脚本显式添加 volume；标签是当日简单收益，不能用未来行。

**面板完整性。** complete rows 由第 86 天给出；缺行会让 lag 对齐 silently 错位，stdout 数字整体漂移。

**按年切分实验。** 第 58 天改 test 集合后，本课所有子样本计数与 MSE 都要重跑；不要把 0.000782 写进默认合同 slide。

**方向与水平。** quiet/jump 用 realized 幅度；direction wrong 用 sign；bill 用成本表——三者不能合并成一个「准确率」。

**树与直线。** OLS 在固定设计上是确定的；树切点可能随 seed 变（第 53 天），但本季 hold-out 评分用 frozen 切点。

**泄漏叙事。** 同日 market 列会虚降 MSE 到 0.000094；有效分数是去掉该列后的 0.000081（第 67、91、98 天）。

**执行假设。** 信号按 close 的 adj_close 形成；脚本不发单、滑点为零、不算 PnL（第 92 天）；实盘需另层成本模型。

**闭链验收。** 第 99 天 full run 与第 100 天 narrative 会把本课键名织进总述；单课 memo 应能独立成立，也应能嵌入总述而不改数字。

**字数与质量。** 中文解释服务于理解 estimand，不是替代 stdout；键名一行都不能省。

**手算。** 在低波动七行任挑一日，用第 51 天系数算 ŷ，核对 (y−ŷ)² 量级；七行均值应接近 0.000059 量级（MSE 非 MAE）。

**报告脚注。** Slide 上须写「低波动周 n=7、MSE、frozen train 估计」三词，缺一则 estimand 不明。

**与 bill 无关。** 本课不算 direction/jump bill；第 79 天 line bill 仍独立存在。

**阅读检查（第 83 天）。** 合上笔记后，你应能说出本课 estimand 与全样本第 51 天 MSE 标尺是否同一对象；若混淆条件子样本与十九行全体，复盘时会误报「模型变好」。

**第 83 天与批改。** 助教只比对 ```text``` 与终端；中文段落写错键名仍会通过 diff，但会误导未来的你——务必把英文键复制进 slide 脚注。

**信息集。** 特征只能使用 Strict past 的 lag 收益与截距，除非当天脚本显式添加 volume；标签是当日简单收益，不能用未来行。

**面板完整性。** complete rows 由第 86 天给出；缺行会让 lag 对齐 silently 错位，stdout 数字整体漂移。

**按年切分实验。** 第 58 天改 test 集合后，本课所有子样本计数与 MSE 都要重跑；不要把 0.000782 写进默认合同 slide。

**方向与水平。** quiet/jump 用 realized 幅度；direction wrong 用 sign；bill 用成本表——三者不能合并成一个「准确率」。

**树与直线。** OLS 在固定设计上是确定的；树切点可能随 seed 变（第 53 天），但本季 hold-out 评分用 frozen 切点。

**泄漏叙事。** 同日 market 列会虚降 MSE 到 0.000094；有效分数是去掉该列后的 0.000081（第 67、91、98 天）。

**执行假设。** 信号按 close 的 adj_close 形成；脚本不发单、滑点为零、不算 PnL（第 92 天）；实盘需另层成本模型。

**闭链验收。** 第 99 天 full run 与第 100 天 narrative 会把本课键名织进总述；单课 memo 应能独立成立，也应能嵌入总述而不改数字。

**字数与质量。** 中文解释服务于理解 estimand，不是替代 stdout；键名一行都不能省。

**手算。** 在低波动七行任挑一日，用第 51 天系数算 ŷ，核对 (y−ŷ)² 量级；七行均值应接近 0.000059 量级（MSE 非 MAE）。

**报告脚注。** Slide 上须写「低波动周 n=7、MSE、frozen train 估计」三词，缺一则 estimand 不明。

**与 bill 无关。** 本课不算 direction/jump bill；第 79 天 line bill 仍独立存在。

**阅读检查（第 83 天）。** 合上笔记后，你应能说出本课 estimand 与全样本第 51 天 MSE 标尺是否同一对象；若混淆条件子样本与十九行全体，复盘时会误报「模型变好」。

**第 83 天与批改。** 助教只比对 ```text``` 与终端；中文段落写错键名仍会通过 diff，但会误导未来的你——务必把英文键复制进 slide 脚注。

**信息集。** 特征只能使用 Strict past 的 lag 收益与截距，除非当天脚本显式添加 volume；标签是当日简单收益，不能用未来行。

**面板完整性。** complete rows 由第 86 天给出；缺行会让 lag 对齐 silently 错位，stdout 数字整体漂移。

**按年切分实验。** 第 58 天改 test 集合后，本课所有子样本计数与 MSE 都要重跑；不要把 0.000782 写进默认合同 slide。

**方向与水平。** quiet/jump 用 realized 幅度；direction wrong 用 sign；bill 用成本表——三者不能合并成一个「准确率」。

**树与直线。** OLS 在固定设计上是确定的；树切点可能随 seed 变（第 53 天），但本季 hold-out 评分用 frozen 切点。

**泄漏叙事。** 同日 market 列会虚降 MSE 到 0.000094；有效分数是去掉该列后的 0.000081（第 67、91、98 天）。

**执行假设。** 信号按 close 的 adj_close 形成；脚本不发单、滑点为零、不算 PnL（第 92 天）；实盘需另层成本模型。

**闭链验收。** 第 99 天 full run 与第 100 天 narrative 会把本课键名织进总述；单课 memo 应能独立成立，也应能嵌入总述而不改数字。

**字数与质量。** 中文解释服务于理解 estimand，不是替代 stdout；键名一行都不能省。

## 实战总结

```bash
python3 days/83-tree-low-vol/tree_low_vol.py
```

亦可：`python3 -c "from days.run_day import main; main(83)"`。

实现：[`tree_low_vol.py`](../../days/83-tree-low-vol/tree_low_vol.py)。交付：stdout 与 ```text``` 块逐字一致。
