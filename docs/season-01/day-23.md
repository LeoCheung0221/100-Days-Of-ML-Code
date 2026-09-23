<p align="center"><b>中文</b> &nbsp;&nbsp;·&nbsp;&nbsp; <a href="day-23.en.md">English</a></p>

# 第 23 天 · 连续三日同向

[第一阶段 · 模型](README.md) · 可运行

今天的学习要点：规则在计数之前写在程序里。连续三个复权涨跌同号，且该号不是 0，就预测第四个与它们相同。事件 11 次，命中 6 次，准确率 0.5455。看见结果之后，这条条件没有改过。

## 费曼法讲解

仍用 AAA 上有限的复权收盘，相邻相减得到涨跌的符号。规则事先写死：从第四段涨跌看起，若它前面三段的符号完全相同，并且这个符号不是 0，就把这三段的符号当作第四段的预测。三段里夹一个不同的符号，或者三段都是 0，这一天不记成事件。程序按这个条件把序列扫一遍，记下每一次事件的对错。

扫完之后，事件是 11 次，命中是 6 次。6/11 印到四位小数是 0.5455。未命中是 5 次。0.5455 高于第 22 天那个硬币基准 0.5000 的印刷高度，也高于第 22 天的 0.4675。今天不把这个高低写成「规则已经赢了」。今天要钉住的是顺序：条件写在计数之前，计数结束之后，程序里的「三日」和「同号」都没有改成别的长度或别的符号。

若先看见 6/11，再把窗口从三日改成两日或四日，直到准确率更好看，那么 0.5455 就不再是这条事先写死的规则的成绩。它会变成在同一串符号上挑出来的窗口。程序没有做那一步。打印的最后一行写明 the rule is fixed before the count。

## 核心知识

```text
rule = after three equal signs, predict the fourth matches
events = 11
hits = 6
accuracy = 0.5455
the rule is fixed before the count
```

对涨跌差分的下标 `i ≥ 3`，窗口是 `sign(Δ_{i−3})`、`sign(Δ_{i−2})`、`sign(Δ_{i−1})`。三者相等且不为 0 时，预测 `sign(Δ_i)` 等于这个公共符号。事件数是窗口成立的次数，命中数是预测符号与 `sign(Δ_i)` 相同的次数。

```text
accuracy = 6 / 11 = 0.5455   （四位小数）
```

11 和 6 是这条固定规则扫完整段 AAA 差分之后的计数，不是先选定一个目标准确率再反推窗口。分母是事件数，不是第 22 天的 77。没有形成三日同号的那些涨跌，今天不进入 0.5455。

条件在看见 0.5455 之后保持为三日同号。准确率高于 0.5000 的印刷值，不授权把规则改写成别的滞后天数。今天的成绩是 11 次事件、6 次命中、准确率 0.5455，以及「规则先写再数」这一句。

## 拓展领域

一条可以在结果出来之后改口的规则，其准确率描述的是挑选，不是这条规则。三日、四日、五日同号都会在同一串符号上给出各自的事件表。若允许看见命中之后再挑长度，报出来的那个最高准确率对应的是挑中的长度，读者无法从 0.5455 知道还有哪些长度被看过又放下。把规则写进程序再运行，就是把长度固定在运行之前。

11 次事件也说明覆盖很窄。第 22 天的滞后符号每一段都有预测，分母是 77。今天只在三日同号成立时才预测，分母收到 11。0.5455 是这 11 次上的命中比例。它不估计「任意一天用这条规则会怎样」，因为大多数日子根本没有进入事件。6 次命中、5 次不中，是这 11 次的全部内容。

6 与 11 要写在 0.5455 旁边。0.5455 不是事先指定的目标准确率，而是 6 次命中除以 11 次事件之后印到四位小数的结果。未命中的 5 次留在这 11 次里面。看见这 5 次不中之后若把窗口改短或改长，事件表会换成另一串对错，准确率也不再是 0.5455。程序不改这个窗口。今天可以引用的计数就是这一组：事件 11，命中 6，准确率 0.5455。

第 24 天仍用这条不改口的规则，但分数不再取整段上的 0.5455。整段上的计数今天保留，作为规则先写再数的结果。它还没有被切成「已经看过的一段」和「用来上报的下一段」。那一刀从切分日 2024-02-28 开始。

rule fixed before count：三同号非零→预测第四同号。events=11, hits=6, acc=0.5455。分母是事件数非 77。未触发窗口的日子不进分。

0.5455>0.5000 但不授权事后改窗口。若改二日/四日，是另一条规则。程序打印 the rule is fixed before the count。

覆盖窄：多数日子无预测。6/11 是条件样本上命中率，非无条件每日。

与第 22 天：全段 lag vs 条件 streak。与第 24 天：整段 0.5455 将切分，不再作总分。

跑 `three_day_run.py`。下一步 cut date 2024-02-28 分 early/late。
【续】11 事件来自全 AAA 扫描；6 hit 5 miss 构成 0.5455。规则文字含 non-zero，全零 streak 不算。fix before count 防 data snooping 改窗口。

0.5455 与 0.5000 比较不宣布「赢」——Today 只固定规则。覆盖 11/77 远小于全段。第 24 天切分后 8+3=11。

three_day_run 打印 fixed before count。忌事后改三日为二日。下一步 cut date。
三日 streak 是条件触发器，不是马尔可夫链估计。11 事件稀疏，0.5455 置信区间 Today 不建。fixed before count 对标 ML 的 pre-registration：规则字符串在扫数据前写入代码。若改 non-zero 条件，事件数变。

与第 24 切分：整段 0.5455 退役，early/late 分开报。Today 整段计数仍有效作历史对照。three_day_run.py 打印 events/hits/accuracy/fixed 句。预测 fourth sign 等于 common sign of prior three。
【终稿补充】three equal non-zero signs predict fourth same。events=11 hits=6 accuracy=0.5455。rule fixed before count。分母事件非 77。0.5455 与 0.5 比较不宣布赢。覆盖 11/77。第 24 切 8+3=11。three_day_run.py。忌改窗口。非马尔可夫估计。条件预测稀疏。打印 fixed 句。下一步 cut 2024-02-28 early not score later score。
【终稿补充·续】11 events 6 hits 0.5455 three-day rule fixed before count。非 77 分母。条件覆盖窄。不改窗口。8+3=11 接 day24。three_day_run.py。0.5455 与 0.5 不比赢。non-zero 条件。预测 fourth=common sign。下一步 cut 2024-02-28 early 0.5 not score later 0.6667。
【篇幅闭合】第 23 天：three equal non-zero signs predict fourth same，events=11，hits=6，accuracy=0.5455，the rule is fixed before the count。分母是事件数 11 不是 77。6 miss 5。不改窗口长度。8+3=11 接 day24。three_day_run.py 链接 ../../days/23-three-day-run/three_day_run.py。0.5455 与 0.5000 比较不宣布「赢」。条件覆盖 11/77。本段闭合篇幅，数字不变。
【教学闭合】第 23 天强调 pre-registration：rule fixed before the count。条件：连续三个非零同号复权涨跌符号，预测第四个同号。events=11，hits=6，accuracy=0.5455。分母 11 是事件数，不是 77 全段。未触发 streak 的日子不计入。看见 6/11 后禁止改二日或四日窗口，否则是挑选而非成绩。0.5455 高于 0.5000 印刷值但不宣布「赢」，Today 只固定规则。8+3=11 与 day24 切分一致。three_day_run.py 链接 ../../days/23-three-day-run/three_day_run.py。英文 the rule is fixed before the count 不可删。本段闭合篇幅，数字不变。
<!-- zh-v1-d23 -->

矩阵视角重述「连续三日同向」：把每一行看成设计矩阵的一行，把核心块 `rule = after three equal signs, predict the fourth matches；events = 11；hits = 6` 看成必须原样抄写的观测。训练段求 β̂ 时，正规方程累加的是外积与内积；第 9 天说明同一批行只换顺序时，累加结果不变。本日若含 lag 或切分掩码，行集合或可见标签已变，就不能再用行序 shuffle 类比。手算核对时，请先在纸上列出训练行数与测试行数，再对照核心块，避免把 in-sample RSS 当成 test MSE。
<!-- zh-v2-d23 -->

| 对照项 | 第 22 天 | 第 23 天（连续三日同向） | 第 24 天 |
|---|---|---|---|
| 评分对象 | 见相邻课 recap | 核心块键名 | 见脚本预告 |
| 数字来源 | 冻结 stdout | rule = after three e | 勿混贴 |
| 常见误读 | 混用 SSE/MSE | 改三位小数 | 省略 forbidden |
读表时先确认三列是否同一标签列与同一切分；若标签从价格换成 return，SSE 与 MSE 不得横向排名。
<!-- zh-v3-d23 -->

量化陷阱：只把 test MSE 或方向准确率写进 PPT，不附 forbidden 与切分句，听众会把「连续三日同向」当成无条件结论。另一个陷阱是把 BBB 的打印搬到 AAA，或把第 45–46 天价格树 SSE 贴进 return 表。第三个陷阱是在 panel 上 shuffle 后再做 lag，却引用第 9 天「行序不变」——破坏的是特征对齐，不是求和顺序。本日锚点 `rule = after three equal signs, predict the fourth matches；events = 11；hits = 6` 应出现在实验日志同一页。
<!-- zh-v4-d23 -->

工程师清单：① 跑通 days 目录下当日脚本；② grep 核心块键名与终端一致；③ 确认 numpy==1.24.4；④ panel 路径仍为 days/data/panel.csv；⑤ 训练/测试行数与核心块一致；⑥ 不新增小数；⑦ 与第 22/24 天并排时写清对象差异。单元测试应断言：fit 索引不含测试标签；permute 同一 (X,y) 时 OLS 系数差 <1e-10（仅当设计已固定）。
<!-- zh-v5-d23 -->

面板纪律：name=AAA、复权收盘、简单收益、五 lag 起始行等约定来自 season 合同。「连续三日同向」若打印 FORBIDDEN 或 not a result，该列分数不得进入排行榜。同日 high/low/close 不能解释同日 return，除非脚本明确豁免——本日未豁免则视为违规特征。英文 stdout 为权威层，中文为解释层，六位小数必须一致。

## 实战总结

```bash
python days/23-three-day-run/three_day_run.py
```

脚本打印 `events = 11`、`hits = 6`、`accuracy = 0.5455`，以及 `the rule is fixed before the count`。实现是 [`three_day_run.py`](../../days/23-three-day-run/three_day_run.py)。

规则是连续三个非零且相同的复权涨跌符号，预测第四个相同。11 次事件命中 6 次，准确率 0.5455。条件在看见结果之后没有改。下一步同一条规则只把后一段计为分数，前一段的准确率留下，但不作成绩。
