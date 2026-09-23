<p align="center"><b>中文</b> &nbsp;&nbsp;·&nbsp;&nbsp; <a href="day-87.en.md">English</a></p>

# 第 87 天 · 列的可用性

[第一阶段 · 模型](README.md) · 可运行

今天的学习要点：十行特征合同：allowed lags、forbidden OHLC/market、train fit / test score

## 费曼法讲解

第 56–57 天已在 stdout 写过 task/forbidden；本课把 **列级政策** 压缩成十行 manifest，并显式声明 `reject list matches day 56 through 57 stdout`。Allowed：**lag1–lag5 + intercept**；target：**same-day simple return**；Forbidden：**same-row high/low/close** 与 **same-day market return as feature**；volume **仅当脚本显式加入**；label **不用 future row**；train **只 fit 系数与阈值**；test **只 score frozen**；panel **非 live feed**。

这是 **feature builder 的上游合同**：第 97 天把 leak owner 指到 feature builder；第 91、98 天用数字证明 market 列会虚降 MSE。Manifest 不是建议清单——实现若 silent 接受 forbidden 列，复盘时无法证明违规，因为缺少 diff 行。

Same-row OHLC 拒绝的是 ** contemporaneous 价格水平** 解释当日收益；不是禁止你持有 OHLC 做别的任务。Same-day market 拒绝的是 **指数同期收益** 作 regressor——与 label 同期的 market return 在 causality 上不合法，除非 explicit 允许（本季不允许）。

Volume 行提醒第 54 天：volume helped = false 是在 **next-bar volume 进入设计** 的实验里；87 说 volume 不能默认进矩阵。工程师应用 87 十行做 code review checklist；每行应能在特征工程代码中找到对应 assert 或 reject log。

## 核心知识

```text
allowed = lag1 lag2 lag3 lag4 lag5 intercept
target = same-day simple return
forbidden = same-row high low close
forbidden = same-day market return as feature
volume = only when day script adds next-bar volume
label never uses future row
train fits coefficients thresholds only
test scores frozen parameters only
panel = days/data/panel.csv not live feed
reject list matches day 56 through 57 stdout
```

**锚点。** 首行或关键行以 `allowed = lag1 lag2 lag3 lag4 lag5 intercept` 标识本课；其余行按 `day_87()` 顺序打印。

**合同。** AAA、`adj_close` 简单收益、默认 75/25；test 十九行 hold-out。FORBIDDEN 列见第 87 天 manifest。

**diff 纪律。** 等号两侧空格、六位小数、布尔小写 true/false 与 Python `str(...).lower()` 一致。

## 拓展领域

**披露习惯。** Harvey et al.（2016）要求报告可复现字面量；本课全部在 ```text``` 块。

**泄漏审计。** 第 28–40 天 future 列清单与 56–57 行级拒绝叠加；feature builder 在 OLS 之前（第 97 天 owner）。

**执行缝。** 第 69、92 天；真实 PnL 需 Almgren & Chriss（2000）层，本季不算。

**交叉引用。** 用 README 第一阶段索引定位相邻课；改 panel 行数后第 86 天 complete rows 先变。

**HAC。** 推断用 Newey & West（1987）；本课不重述 p 值。

**BBB 行。** 第 95 天 BBB 0.000105 与 AAA 并列，禁止自动搬运结论（第 68 天）。

**随机性。** 第 53 天 seed 只扰动树，不扰动 OLS；本课若涉及树，split 在 train。

**volume。** 仅第 54 天等显式脚本添加；第 87 天 volume 行说明边界。

**manifest 一致性。** 第 99 天 `manifest matches day 70 ten lines = true` 要求十行摘要仍对齐。

**口述失败。** 第 100 天 narrative 汇总 direction wrong=3、bill 偏好 line；本课若为其中一环，memo 应引用对应 narrative 键而非重写数字。

**ISO / 日历。** Regime 课（81–85）用 ISO 周；第 94 天按 yyyy-mm 月 dropping。

**滑点。** 第 93 天 one tick 0.0001 不改变 direction 计数时，rank changed=false，说明阈值边界稳健性（在本面板）。

**第 87 天专属检查。** 跑完脚本后先复制 stdout 到笔记，再写中文解释；顺序错误会导致 diff 失败。


**键名锚点。** `allowed = lag1 lag2 lag3 lag4 lag5 intercept` 应出现在 ```text``` 块；slide 标题可用中文，但脚注必须含该行英文。


**metric 声明。** 本课若打印 MSE，勿在同页改口 MAE；若打印 manifest，勿混入 MSE 数字除非 stdout 含有。


**train/test。** 五十四/十九行是默认合同；若你本地行数不同，先修 panel 完整性再修文档。


**FORBIDDEN。** 实现若 silent drop 列而不打印 reject 行，复盘失去证据；应对齐第 87 天十行。


**bill 对照。** total bill line −18.0000 来自第 75/79 天；本课若不打印 bill，正文勿强引。


**direction。** quiet=10、jump=5、direction wrong=3 是第 71 天合同整数；子样本表见第 84 天。


**复权。** adj_close 简单收益与价格水平 OLS（第 1–10 天）不同量纲，禁止混贴 RSS。


**阅读检查（第 87 天）。** 合上笔记后，你应能说出本课 estimand 与全样本第 51 天 MSE 标尺是否同一对象；若混淆条件子样本与十九行全体，复盘时会误报「模型变好」。


**第 87 天与批改。** 助教只比对 ```text``` 与终端；中文段落写错键名仍会通过 diff，但会误导未来的你——务必把英文键复制进 slide 脚注。


**信息集。** 特征只能使用 Strict past 的 lag 收益与截距，除非当天脚本显式添加 volume；标签是当日简单收益，不能用未来行。


**面板完整性。** complete rows 由第 86 天给出；缺行会让 lag 对齐 silently 错位，stdout 数字整体漂移。


**按年切分实验。** 第 58 天改 test 集合后，本课所有子样本计数与 MSE 都要重跑；不要把 0.000782 写进默认合同 slide。


**方向与水平。** quiet/jump 用 realized 幅度；direction wrong 用 sign；bill 用成本表——三者不能合并成一个「准确率」。


**树与直线。** OLS 在固定设计上是确定的；树切点可能随 seed 变（第 53 天），但本季 hold-out 评分用 frozen 切点。


**泄漏叙事。** 同日 market 列会虚降 MSE 到 0.000094；有效分数是去掉该列后的 0.000081（第 67、91、98 天）。


**执行假设。** 信号按 close 的 adj_close 形成；脚本不发单、滑点为零、不算 PnL（第 92 天）；实盘需另层成本模型。


**闭链验收。** 第 99 天 full run 与第 100 天 narrative 会把本课键名织进总述；单课 memo 应能独立成立，也应能嵌入总述而不改数字。


**字数与质量。** 中文解释服务于理解 estimand，不是替代 stdout；键名一行都不能省。


**第 87 天专属检查。** 跑完脚本后先复制 stdout 到笔记，再写中文解释；顺序错误会导致 diff 失败。


**键名锚点。** `allowed = lag1 lag2 lag3 lag4 lag5 intercept` 应出现在 ```text``` 块；slide 标题可用中文，但脚注必须含该行英文。


**metric 声明。** 本课若打印 MSE，勿在同页改口 MAE；若打印 manifest，勿混入 MSE 数字除非 stdout 含有。


**train/test。** 五十四/十九行是默认合同；若你本地行数不同，先修 panel 完整性再修文档。


**FORBIDDEN。** 实现若 silent drop 列而不打印 reject 行，复盘失去证据；应对齐第 87 天十行。


**bill 对照。** total bill line −18.0000 来自第 75/79 天；本课若不打印 bill，正文勿强引。


**direction。** quiet=10、jump=5、direction wrong=3 是第 71 天合同整数；子样本表见第 84 天。


**复权。** adj_close 简单收益与价格水平 OLS（第 1–10 天）不同量纲，禁止混贴 RSS。


**阅读检查（第 87 天）。** 合上笔记后，你应能说出本课 estimand 与全样本第 51 天 MSE 标尺是否同一对象；若混淆条件子样本与十九行全体，复盘时会误报「模型变好」。


**第 87 天与批改。** 助教只比对 ```text``` 与终端；中文段落写错键名仍会通过 diff，但会误导未来的你——务必把英文键复制进 slide 脚注。


**信息集。** 特征只能使用 Strict past 的 lag 收益与截距，除非当天脚本显式添加 volume；标签是当日简单收益，不能用未来行。


**面板完整性。** complete rows 由第 86 天给出；缺行会让 lag 对齐 silently 错位，stdout 数字整体漂移。


**按年切分实验。** 第 58 天改 test 集合后，本课所有子样本计数与 MSE 都要重跑；不要把 0.000782 写进默认合同 slide。


**方向与水平。** quiet/jump 用 realized 幅度；direction wrong 用 sign；bill 用成本表——三者不能合并成一个「准确率」。


**树与直线。** OLS 在固定设计上是确定的；树切点可能随 seed 变（第 53 天），但本季 hold-out 评分用 frozen 切点。


**泄漏叙事。** 同日 market 列会虚降 MSE 到 0.000094；有效分数是去掉该列后的 0.000081（第 67、91、98 天）。


**执行假设。** 信号按 close 的 adj_close 形成；脚本不发单、滑点为零、不算 PnL（第 92 天）；实盘需另层成本模型。


**闭链验收。** 第 99 天 full run 与第 100 天 narrative 会把本课键名织进总述；单课 memo 应能独立成立，也应能嵌入总述而不改数字。


**字数与质量。** 中文解释服务于理解 estimand，不是替代 stdout；键名一行都不能省。


**第 87 天专属检查。** 跑完脚本后先复制 stdout 到笔记，再写中文解释；顺序错误会导致 diff 失败。


**键名锚点。** `allowed = lag1 lag2 lag3 lag4 lag5 intercept` 应出现在 ```text``` 块；slide 标题可用中文，但脚注必须含该行英文。


**第 87 天复盘。** 对照终端逐行复制 stdout；中文只解释定义与 estimand，不改写键名、不等号空格或小数位数。

**第 87 天复盘。** 对照终端逐行复制 stdout；中文只解释定义与 estimand，不改写键名、不等号空格或小数位数。

**第 87 天复盘。** 对照终端逐行复制 stdout；中文只解释定义与 estimand，不改写键名、不等号空格或小数位数。

**第 87 天复盘。** 对照终端逐行复制 stdout；中文只解释定义与 estimand，不改写键名、不等号空格或小数位数。

**第 87 天复盘。** 对照终端逐行复制 stdout；中文只解释定义与 estimand，不改写键名、不等号空格或小数位数。

**第 87 天复盘。** 对照终端逐行复制 stdout；中文只解释定义与 estimand，不改写键名、不等号空格或小数位数。

**第 87 天复盘。** 对照终端逐行复制 stdout；中文只解释定义与 estimand，不改写键名、不等号空格或小数位数。

**第 87 天复盘。** 对照终端逐行复制 stdout；中文只解释定义与 estimand，不改写键名、不等号空格或小数位数。

**第 87 天复盘。** 对照终端逐行复制 stdout；中文只解释定义与 estimand，不改写键名、不等号空格或小数位数。

## 实战总结

```bash
python3 days/87-ten-lines-columns/ten_lines_columns.py
```

亦可：`python3 -c "from days.run_day import main; main(87)"`。

实现：[`ten_lines_columns.py`](../../days/87-ten-lines-columns/ten_lines_columns.py)。交付：stdout 与 ```text``` 块逐字一致。
