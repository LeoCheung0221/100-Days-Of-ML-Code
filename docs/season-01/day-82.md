<p align="center"><b>中文</b> &nbsp;&nbsp;·&nbsp;&nbsp; <a href="day-82.en.md">English</a></p>

# 第 82 天 · 高波动周的跳空

[第一阶段 · 模型](README.md) · 可运行

今天的学习要点：高波动 ISO 周内 jump 日 4 天；这些日子上 frozen 直线 MAE 0.015044

## 费曼法讲解

第 81 天用 ISO 周内的收益标准差把 test 十九行切成「高波动周」与「低波动周」，并报告子样本 MAE。本课在同一高波动周子集上再套第 71 天的 jump 规则：在全体 test 行上对 \(|r_t|\) 取第 75 分位，达到或超过阈值的日记为 jump。两轴相交后，高波动周里共有 **4** 个 jump 日；脚本只在这 4 天上算 frozen 五 lag 直线的平均绝对误差 **0.015044**。

读数时要把三个层次分开。第一层是全局 hold-out 上的直线 MSE 标尺（第 51 天 **0.000081**），本课不重印。第二层是第 81 天高波动周全体十二天的 MAE **0.007341**。第三层才是本课：高波动周 × jump 的交集，MAE 几乎翻倍到 **0.015044**——说明「波动 regime 更差」主要来自 regime 内 tail 日，而不是十二天均匀变差。直线系数仍来自五十四行训练段 OLS，**不在** jump 子样本上重估；否则 estimand 变成「在已知大波动日上再拟合」，与 prespec 的 frozen 预测相反。

Jump 与周波动是不同几何。Jump 看单日 \(|r|\) 在 test 横截面上的分位；周波动看同一 ISO 周内多日的离散度。一个 \(|r|\) 很大的日可以落在低波动周（若同周其余日极平），反之亦然。第 84 天会把 quiet/jump/direction 与高/低波动并表；本课 stdout 首行 `regime = high volatility ISO weeks on test stretch` 锁定子总体，避免读者误用全样本 jump 计数 **5**。

MAE 在这里是水平误差度量，与 direction wrong 计数无关。高波动 jump 日上 \(|r-\hat y|\) 大，既可能因为 \(\hat y\) 幅度偏小，也可能因为 realized 符号对但幅度极端。Christoffersen & Diebold（2006）强调方向与水平应分轨报告；本课只给水平 MAE，不推断「jump 日必 direction wrong」。样本只有 4 天，任何点估计都不支撑显著性声明；价值在于协议：在 prespec regime 内报告 tail 子样本误差，而不是事后挑最大残差日。

与 Andersen & Bollerslev（1998）的波动 clustering 叙事一致：高波动状态下水平预测更难，但本脚本用的是教学面板上极简的「周 std」代理，不是 GARCH 条件方差。工程师 diff 时只认三行英文键；`line mean abs error on those jump days = 0.015044` 必须与 `day_82()` 打印逐字一致，slide 不得四舍五入。

若交集为空，脚本会打印 `line mean abs error on those jump days = not defined`；本面板下高波动周与 jump 有四点交集，故为 0.015044。改切分或 ticker 后若出现 not defined，文档须同步改 ```text``` 块，不能留旧数。

Poon & Granger（2003）综述提醒：波动模型与收益模型可并行；本季先钉 lag 水平线，再在 regime×tail 上看 MAE 形状。不要把 0.015044 解释成「GARCH 残差更大」——这里没有估计条件方差。

与第 71 天 quiet/jump 分位一致之处：jump 阈值在 test 十九行上算 p75，属于评估协议的一部分；若把 train 行并入算分位，会泄漏 hold-out 形状信息。本课 jump 掩码与 71–80 诊断同源，保证 bill 与 MAE 子样本可交叉引用。

Campbell、Lo、MacKinlay（1997）把可预测性讨论绑定在信息集与 out-of-sample 协议上；本课 stdout 就是该协议的一格：给定 frozen \(\hat\beta\)，在高波动 jump 四日上报告 MAE。任何「改进」声称必须换 experiment id 并重跑 51–82 全链。

## 核心知识

```text
regime = high volatility ISO weeks on test stretch
jump days in high vol weeks = 4
line mean abs error on those jump days = 0.015044
```

**实现。** `_week_vol_high_low()` 复用第 81 天逻辑得到高波动周索引；jump 掩码来自 test 上 \(|y|\) 的 p75；交集 `jump_high` 长度为 4。MAE 为 `np.abs(test_y - test_hat)[jump_high].mean()`，\(\hat y\) 来自 `_lag5_line_test()`。

| 量 | 含义 |
|---|---|
| jump days in high vol weeks = 4 | 两轴交集行数，不是全 test jump 5 |
| 0.015044 | 交集上 MAE，高于第 81 天高波动周全体 0.007341 |
| regime 首行 | 声明子总体，防与低波动周 jump 混淆 |

**合同。** AAA、`adj_close` 简单收益、默认 75/25 时间切分；禁止 same-row OHLC 与 same-day market 作特征（第 56–57、87 天）。改第 58 天切分或换 BBB 须重跑，禁止手改 4 或 0.015044。

**与 MSE 标尺对照。** 第 51 天 test MSE 0.000081 是平方误差均值；MAE 0.015044 是 tail 子样本绝对误差均值，量纲同为收益但统计量不同。高 MSE 日未必在 jump∩高波动四日集合内——排序见第 90 天。

**代码入口。** `day_82()` 在 `days/run_day.py`；目录脚本 `jumps_high_vol.py` 应调用同一逻辑。批改时以 stdout diff 为准，不以 notebook 中间变量为准。

## 拓展领域

**子样本 estimand。** 在交集上报告 MAE 是描述性诊断，不是新估计问题。若要在 jump 日上重新 fit OLS，必须在新 experiment id 里 prespec，并承认 test 信息已进入特征选择。Bailey & Lopez de Prado（2014）提醒子样本挖掘与 multiple testing；本课交集由 81 与 71 的规则冻结定义，不是 ex post 挑日。

**与 bill 的关系。** 第 75、79 天用 jump 日 cost 3 计 bill；本课不算账，只报水平 MAE。Memo 里应写清：bill 针对 jump 分类，MAE 针对连续误差，二者不可互换。Almgren & Chriss（2000）说明执行与 tail 日交互；第 92 天声明 close fill、零滑点、不算 PnL——本季 scoring 停在误差与 bill 字面量。

**低波动周对照。** 第 84 天表显示低波动周 jump 仅 1 日且 direction wrong 3 日集中在低波动段；本课只覆盖高波动 jump 四日。写组会材料时应并排引用 84 的八行表，而不是只放大 0.015044。

**复现。** 工作目录为仓库根；先确认第 51 天直线可跑，再跑本脚本。`python3 -c "from days.run_day import main; main(82)"` 与目录脚本等价。

**HAC 与 i.i.d.** Newey & West（1987）说明滞后收益回归残差常序列相关；4 日 MAE 无 infer 意义，若比较 line 与 tree 子样本差应在新课里 prespec 并用 HAC，而非口头「显著更好」。

**ISO 周边界。** Test 仅 2024 春季若干 ISO 周；短 week 与跨年 week 在 live 面板更常见。`isocalendar()` 与 Python 3.8+ 一致即可 diff。

**手算 sanity。** 在 hold-out 上找一日同时属于高波动周且 \(|r|\) 达 p75：用第 51 天六个系数算 \(\hat y\)，核对 \(|r-\hat y|\) 是否接近该子样本均值量级；单日不能重现 0.015044，但可验证 frozen 管道未在 test refit。

**与第 83 天分工。** 83 在低波动周比较 line、stump、depth-2 的 MSE；本课不碰树，只读直线 MAE。若 memo 写「高波动段树更好」，应引用第 85 天 MSE 格（`model kept = line`），而不是本课 MAE。

**报告模板。** 建议四行：regime 定义、交集 n=4、MAE 指标、frozen 系数来源（第 51 天 train）。缺任何一行，外部读者无法复现 estimand。

**数据行合同。** 面板来自 `days/data/panel.csv` 的 AAA；简单收益为复权收盘相邻比值减一；有效样本从第五个收益起算，默认 train 五十四行、test 十九行。第 86 天 manifest 会重述日期端点；本课假设你已接受该切分。

**禁止泄漏复述。** 同行 high/low/close 与 same-day market 不得作特征；第 67、91、98 天说明 market 列会虚降 MSE。本课 jump 与 vol 划分只用 test 上的 \(r_t\) 与日期，不引入 forbidden 列。

**误差分母。** MAE 分母是 4 而非 19；与全样本 MAE 不可比。Slide 上并列时应标注 n，避免观众以为「整体 MAE 变成 0.015」。

**波动与 jump 的因果语言。** 只能说「在高波动 jump 子样本上误差更大」；不能说「波动导致 jump」——两者都是 realized 标签上的分类。预测任务仍是 \(r_t\) 水平，不是 jump 概率。

**第 90 天预告。** 90 按 \(|r-\hat y|\) 排序列三个 fail 日；其中两则 reason 为 jump day horizontal miss，与本课 tail 叙事一致，但排序是全 test 而非仅高波动交集。

**工程师 checklist。** 跑 `main(82)`；复制三行 stdout 到 ```text```；diff 与 slide 键名；确认 jump 全局计数仍为 71 天合同的 5，本课 4 是子集。

**教学意图。** 让你习惯「先 prespec regime，再在 regime 内看 tail」的报告顺序；实盘 research memo 常因省略 n 与定义而被合规挑战。本课三行 stdout 就是为 slide 脚注准备的最小充分统计量。

**与 direction 诊断对照。** 第 84 天高波动段 direction wrong 0 日、低波动段 3 日；本课 MAE 在 high-vol jump 上仍大。说明「方向对但幅度错」与「方向错」可同时存在于不同子样本——合并成一个 KPI 会误导风控读者。

**文档验收。** 本课中文解释须与 ```text``` 三行逐字对齐；复习时先跑 `main(82)` 再读费曼段，若数字不一致以终端为准并回改文档。

**子样本 n 的展示。** 高波动 jump 四日占 test 十九日约五分之一；MAE 0.015044 是条件均值，报告时应与全 test MAE 或 MSE 标尺分栏列出，避免听众以为整体误差等于 0.015。

**模型族不变。** 本课不引入 ridge 或 depth-2；若比较非线性应引用第 83、85 天在 regime 上的 MSE 格，而不是在本课 MAE 上改口「树更好」。

**审计链。** 自第 51 天冻结系数至本课，中间任何改 panel、切分或 ticker 的 PR 都应附带 `main(82)` 的新 stdout；旧文档数字若未重跑，视为过期而非「四舍五入误差」。

**教学收束。** 本课把 regime 与 tail 两层诊断叠在一起：先锁定高波动周，再看 jump 子集 MAE；读数顺序错误时，容易把全 test 的五个 jump 日误当成四个。复习请对照第 84 天八行表，确认 jump 与 direction 在不同 vol 桶中的分布。

## 实战总结

```bash
python3 days/82-jumps-high-vol/jumps_high_vol.py
```

亦可：`python3 -c "from days.run_day import main; main(82)"`。

实现：[`jumps_high_vol.py`](../../days/82-jumps-high-vol/jumps_high_vol.py)。交付：三行 stdout 与 ```text``` 块逐字一致。
