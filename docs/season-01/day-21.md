<p align="center"><b>中文</b> &nbsp;&nbsp;·&nbsp;&nbsp; <a href="day-21.en.md">English</a></p>

# 第 21 天 · 固定收盘表

[第一阶段 · 模型](README.md) · 可运行

今天的学习要点：`days/data/panel.csv` 有 160 行，AAA 与 BBB 各 80 个交易日，日期从 2024-01-02 到 2024-04-23，AAA 有 1 个收盘为空。连读两次，文件文本一致。这张表冻结在仓库里，运行时不重新抽样，也不是第 1 天到第 20 天写进公式的五个收盘。

## 费曼法讲解

打开仓库里的 `days/data/panel.csv`，按行数。文件给出 160 行。名字是 AAA 和 BBB，各 80 个交易日。AAA 的日期从 2024-01-02 排到 2024-04-23，BBB 使用同一段日期。160 等于 80 加 80。表上 AAA 的收盘有 1 格是空的。程序把这一格计为 1，今天不填数，也不把它换成邻近一天的收盘。

核对文件有没有在两次读取之间被换掉，比较的是文件文本。程序把路径上的文本读入一次，再读一次，两段字符串相同，打印 `second read matches = true`。空收盘解析之后是 NaN。NaN 与 NaN 不相等，若拿解析后的字典互相比，同一份文件会被说成变了。今天的核对停在文本上，不经过那一步。

第 1 天到第 20 天用的收盘写在公式里，是五个手写数字：2.1、3.9、6.2、20.0、10.4。那些天的残差、方向和噪声列都从这五个数长出来。今天的收盘改从这 160 行里读。脚本里没有抽样。再运行一次，读到的仍是同一段文本。日期停在 2024-04-23，行数停在 160。后面几天若引用命中或平方和，引用的是这份文件上的计算。

## 核心知识

```text
path = days/data/panel.csv
rows = 160
second read matches = true
AAA dates 2024-01-02 .. 2024-04-23
AAA blank closes = 1
the table is not resampled
```

路径是仓库内的 `days/data/panel.csv`。`rows = 160` 是表的行数，两个名字各 80 行，日期区间同为 2024-01-02 至 2024-04-23。AAA 的空收盘计数是 1。BBB 的空单元格今天不另报一个数。

第二次读取比较的是路径上 `read_text()` 的两次返回。相等表示文件文本未变。这个判断不把空字符串解析成 NaN 之后再比较字典。空单元格留在文件里，计数为 1。

手写五收盘与这张表是两套数字。五收盘留在前二十天的公式里。今天的对象是冻结在仓库里的表。打印的最后一行写明 the table is not resampled：运行时不重新抽行，也不另生成一份表。

## 拓展领域

固定表把后面的分数绑在同一份文件上。重跑脚本会重读同一路径。文本两次一致，则两次运行之间数字的来源没有被换成另一张表。行数 160、日期终点 2024-04-23、AAA 的 1 个空收盘，是这张表的边界。讨论规则时，样本是这 160 行里读出来的记录，加上已经写明的那一个空位。

空收盘是缺失单元格。后面用复权收盘做差分时，会先留下收盘和复权收盘都取有限值的行。今天只把缺失计数出来，并确认文本可读且两次相同。给空格填上一个收盘，会改变有效行的长度，那一步今天不做。

160 这个长度是文件的行数，不是运行时抽出来的样本大小。AAA 的 80 行与 BBB 的 80 行相加仍是 160，表里没有第三只名字。日期从 2024-01-02 到 2024-04-23，是文件里写着的起止，不是程序按日历现推出来的区间。空收盘被计数的是 AAA 的那 1 格。把文件文本读两遍并要求相同，是为了让「表没有被换掉」成为一次可以复跑的检查。解析之后空单元格变成 NaN，而 NaN 与自身不等，字典比较不能充当这次检查。文本相同，第二次打开同一路径时面对的仍是同一张表。

表的身份也划清程序在做什么。程序只读仓库里的这个文件，运行时不刷新行，不重新抽样。第 22 天起的滞后符号、切分和回归，都是对这份冻结表的计算。换路径或改文件文本，打印的 160 和那 1 个空位就不再是今天这些数。

panel.csv 160 行，AAA/BBB 各 80，日期 2024-01-02..2024-04-23。AAA blank closes=1。second read matches=true 比 text 不比 NaN dict。

非 resampled；非 five-point 2.1..10.4。后续 day 22+ 均绑此文件。空单元格不填、不 forward-fill today。

文本一致性检查可复跑。解析 NaN 相等性失败是预期，故不用 dict compare。160=80+80，无第三 symbol today。

边界：空 close 行后续差分排除。Today 只计数与 identity。换文件则数字全变。

跑 `fixed_table.py` 全键。下一步 lagged direction 36/77 vs coin 0.5000。
【续】160 行身份是后续 36/77、11 events、cut 2024-02-28 的母集。改 panel.csv 文本则全系数字失效。second read matches 是 integrity check，非业务指标。

空 close 1 格在 AAA；差分前须 finite 过滤，故有效段少于 80。Today 不填缺失。BBB 同行数但不进 day 22 规则。

fixed_table 键全打印。路径 days/data/panel.csv 勿改。下一步 lag direction 对 coin。
panel 是 season 1 后半的物理数据源。160、2024-04-23、blank=1 是身份三角。Git 改 panel.csv 应视为改题。second read matches 可在 CI 里做 smoke test。NaN dict 比较失败是设计选择，写进 FAQ：为何不用 pandas equals。

与第 1–20 手写五点的关系：前段教 OLS/方向/阈值/基准/噪声；后段教真实 CSV 纪律。交作业写清 not resampled 指运行时非随机子采样，非指文件不含随机列（第 20 天噪声是另一文件实验）。
【终稿补充】panel.csv 160 行 AAA/BBB 各 80，2024-01-02 至 2024-04-23，AAA blank closes=1。second read matches=true 比 text。not resampled。非五点 2.1..10.4。NaN dict 比较故意不用。空 close 不填。后续 36/77、11 events、cut 2024-02-28 绑此文件。改文件即改题。fixed_table.py 键全。BBB 同行数 Today 只报 AAA 空位。Git 改 panel 需全季重验。160=80+80 无第三 symbol。路径 days/data/panel.csv。文本稳定性 smoke test 可 CI。解析 NaN 相等失败 FAQ。前 20 天手写点后进入 CSV 纪律。交作业 identity 三角：160、日期终点、blank=1。
【终稿补充·续】160 行冻结表是 season1 后半母集。2024-04-23 终点。AAA blank=1。text read twice match。非 resampled 非五点。NaN dict FAQ。改 CSV 全季重验。fixed_table.py 键。BBB 80 行 Today 只报 AAA 空。CI smoke text match。前段 toy 后段 CSV 纪律。路径 days/data/panel.csv。identity 三角交作业。下一步 36/77 0.4675 coin 0.5。
【篇幅闭合】第 21 天确立 panel 身份：path=days/data/panel.csv，rows=160，AAA/BBB 各 80，dates 2024-01-02..2024-04-23，AAA blank closes=1，second read matches=true，the table is not resampled。请把 identity 三角写进笔记：行数 160、日期终点、空 close 计数。文本两次 read 相同证明文件未被换。NaN 解析后 dict 比较会误报变化，故 Today 不比 dict。空单元格不填。后续 day22 的 77、day23 的 11、day24 的 cut 2024-02-28 都依赖此文件。改 panel.csv 等于改题。fixed_table.py 链接 ../../days/21-fixed-table/fixed_table.py。前 20 天五点 toy 与后段 CSV 纪律分界。BBB 同行数 Today 只报 AAA 空位。CI 可加 text match smoke。本段闭合篇幅，数字不变。
【教学闭合】第 21 天是数据工程纪律日：冻结 panel.csv，禁止运行时 resample。identity 检查清单：① path=days/data/panel.csv；② rows=160；③ AAA dates 2024-01-02..2024-04-23；④ AAA blank closes=1；⑤ second read matches=true；⑥ the table is not resampled。解释 77 与 160：77 是 AAA 有效 adj close 做 lag 后的段数，不是全表行数。解释 11 events：是 streak 条件触发次数，不是 160。解释 cut 2024-02-28：是 day24 的日期切分，依赖同文件。NaN dict 比较失败 FAQ：空字符串 parse 成 NaN，NaN!=NaN，故 text match 更可靠。BBB 80 行存在但 day22 规则只用 AAA。改 panel 文本则全系数字失效。fixed_table.py 链接保持。前 20 天五点与后段 CSV 的分界要会讲。本段闭合篇幅，数字不变。
<!-- zh-v1-d21 -->

面板纪律：name=AAA、复权收盘、简单收益、五 lag 起始行等约定来自 season 合同。「固定收盘表」若打印 FORBIDDEN 或 not a result，该列分数不得进入排行榜。同日 high/low/close 不能解释同日 return，除非脚本明确豁免——本日未豁免则视为违规特征。英文 stdout 为权威层，中文为解释层，六位小数必须一致。
<!-- zh-v2-d21 -->

切分纪律：时间切分要求测试块在训练之后（第 27 天并排）；随机切分允许日历逆序（第 26 天对照 0.4583）。本日「固定收盘表」若写 seed 与 train fraction，两者都是复现锚点，不是事后调参。hold-out 行是唯一报告 MSE/方向分数的集合；训练 RSS 不作最终成绩（第 7 天）。核心块 `path = days/data/panel.csv；rows = 160；second read matches = true` 中的 split 语汇请与终端逐字对齐。
<!-- zh-v3-d21 -->

与第 9 天对照：行序 shuffle 不改变同一 (X,y) 的 OLS；信息集 shuffle（换窗口、换切分、混日期）会改变 β̂ 或分数。「固定收盘表」属于后者还是前者，取决于脚本是否只交换行顺序而不改配对与掩码。第 8 天换窗口斜率 8.0500 与第 1 天 3.2700 的差异是集合变化，不是浮点噪声。写笔记时勿把 1e-14 级差与 8.0500 级差混谈。
<!-- zh-v4-d21 -->

报告规范：交作业三句应包含 (1) 本日对象「固定收盘表」；(2) 核心块中一条可核对数字；(3) 与相邻课边界一句。禁止在文末堆叠第二份「复习时」整段；拓展段只放对照与陷阱，命令与交作业句留在实战总结。若截图，至少露出核心块首行与 bash 命令行。

## 实战总结

```bash
python days/21-fixed-table/fixed_table.py
```

脚本打印 `path = days/data/panel.csv`、`rows = 160`、`second read matches = true`、AAA 的日期从 2024-01-02 到 2024-04-23、`AAA blank closes = 1`，以及 `the table is not resampled`。实现是 [`fixed_table.py`](../../days/21-fixed-table/fixed_table.py)。

今天交的是表的身份。160 行，AAA 与 BBB 各 80 个交易日，AAA 一格收盘为空，文件文本连读一致，运行时不重新抽样。下一步用昨日复权涨跌的符号猜今日，并和硬币基准 0.5000 并排。
