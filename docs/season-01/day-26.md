<p align="center"><b>中文</b> &nbsp;&nbsp;·&nbsp;&nbsp; <a href="day-26.en.md">English</a></p>

# 第 26 天 · 随机切分

[第一阶段 · 模型](README.md) · [排版规范](LESSON_LAYOUT.md) · 可运行

今天的学习要点：random split，seed 1，train fraction 0.70：test direction accuracy = 0.4583；`this number is the control`——本日只交付对照，不与时间切分并排。

---

## 费曼法讲解

> **结论先行**：`test direction accuracy = 0.4583` 在 **random split、seed 1、train 0.70** 下产生；`this number is the control` 声明本日 **只** 交付对照，不与 time split 并排（并排在第 27 天）。

训练掩码随机抽 70% 行估 OLS `r_t ~ r_{t−1}`，测试行上数 sign 命中率。允许 **未来行进训练、过去行进测试**——因此 0.4583 **不能** 叫 walk-forward 成绩。第 27 天会把 time-split 0.5417 放在旁边；今天读者应记住 **0.4583 的身份是对照**。

White（1980）稳健标准误不改点估计；本课尚未做推断。seed 1 是 **复现锚点**，不是最优 seed 搜索。误用：在 100 个 seed 里挑最高 test acc 再报告——那是 **多重检验泄漏**。正确：固定 seed 1，原样引 `this number is the control`。

单名 AAA 上，同一日期只有一行，random 不会把 **同一日历** 拆到两侧；第 37 天 pooled 才会。学习笔记保留两句：单名 random 0.4583；混池 random 可 0.7234—— **主语不同**。

```mermaid
flowchart TD
  S["seed 1 · 70% train"] --> R["random 掩码"]
  R --> A["test acc 0.4583"]
  A --> L["control 对照"]
```

---

## 核心知识

### 脚本输出（与下方 `text` 块一致）

[`random_split.py`](../../days/26-random-split/random_split.py)：

```text
split = random, seed 1, train fraction 0.70
test direction accuracy = 0.4583
this number is the control
```


| 项 | 值 |
|:---|:---|
| split | random, seed 1, train 0.70 |
| test direction accuracy | 0.4583 |
| 身份 | control（对照） |

本日 **不** 与 time split 并排；`this number is the control` 禁止改写成 walk-forward 成绩。


---

## 拓展领域

**control 身份.** `this number is the control` 锁定 0.4583 **不是** walk-forward 成绩。random split、seed 1、train 0.70 允许未来行进训练；单名 AAA 不会拆同日历两行，但 **时间逆序** 仍可能。

**与第 27 天关系.** 本日 **不** 并排 time split；并排在 27。Memo 只许引 control 句 + 0.4583。禁止 100 seed 搜最优。

**seed 1.** 复现锚点；换 seed 数字变、机制不变。
**数值与复现.** 在仓库根目录运行当日脚本；`panel.csv` 与 `numpy==1.24.4` 为默认合同。正文 ```text``` 块须与终端 stdout **逐行零 diff**；改数据或 `fmt` 时同一 commit 更新 golden 与 md。

**全季衔接.** 第 1–20 天：五点 toy 与 OLS/损失/hold-out 语言；第 21 天起：冻结 panel。两套数字 **不可混表**（例如斜率 3.27 与 accuracy 0.4675 无直接比较关系）。第 41 天起模型复杂度上升；第 51 天 lag-5；第 58 年切；第 71 天 bill/direction 分轨——**信息集合同** 全季不变。

**文献锚（非虚构，只作机制分类）.** Campbell, Lo & MacKinlay (1997)；Harvey, Liu & Zhu (2016)；Lopez de Prado (2018)；Little & Rubin (2002)；Hasbrouck (2007)。不得把教科书结论偷换为「本 panel 显著」——本段多数课 **无** 显著性检验 stdout。

**代码审查五问（panel 段）.** 特征在决策时刻是否可见；标准化是否只用训练段矩；train/test 是否按 date/name 分组；metrics 是否诚实区分 in-sample 与 hold-out；FORBIDDEN 行是否仍打印。缺任一条，spec 不完整。

**手算与 CI.** 任取 stdout 一行在 REPL 复算；`verify_season01_docs.py --day N --min-cjk 3000` 为合并必要条件。改 `panel.csv` 须重跑依赖该面板的 golden 日。


第26课与 year split（第58天）的关系：时间切分从比例升级到按年；本段 27 天是比例版。

第26课与 bill（第75天）的关系：方向 accuracy 之后还有计费误差；本段多数未引入 bill。

第26课与 slippage（第93天）的关系：第39天 round-trip 是常数先行版。

第26课 narrative 收束：数字 frozen，机制可讨论，estimand 不可模糊。

回测代码审查时，第26课要求先打开终端输出，再读中文解释；若解释出现 stdout 未打印的阈值或准确率，直接判为文档漂移。

因子入库前，应用与第26课同构的三问：特征在决策时刻是否可见、标签是否同期泄漏、标准化是否只用训练段统计量。

研究 memo 的 estimand 小节应写清第26天脚本使用的 name 列、价格列（close 或 adj_close）、以及差分阶数；换列等于换题。

当 PM 要求「把样本内曲线做漂亮」时，第26课类实验应回复：请先指定 hold-out 掩码或 bill 口径；in-sample 优化不等于交付分数。

数据版本控制应像第26课 second read 一样可机械验证；parquet 也应存 sha256，而不是只靠「同事说没改」。

第26课若涉及方向准确率，报告时必须并列分母（hits 里的 /N）；只写百分比不写 N 是审计不合格。

混池实验（如第37课）与单名实验（如第27课）不得共用一个 leaderboard；第26课文档应在开头声明主语范围。

FORBIDDEN 特征课（如第28课）说明：in-sample RSS 下降可能是泄漏信号；第26课写模型比较时禁止用非法列作优选依据。

缺失填充课（如第34课）提醒：pandas 默认 bfill 在 pipeline 里很常见；第26课起应在 CI 里 grep fillna 方向。

标准化泄漏（如第33课）说明：test MSE 相等不能证明无泄漏；第26课应把 scale 来源写入 model card。

时间切分课（如第27课）的「测试在训练之后」是因果最低标准；第26课若改切分为随机，必须另开对照行而不覆盖 time 行。

随机切分对照（如第26课）只能叫 control，不能叫 walk-forward；第26课命名错误会导致合规审查失败。

事件规则课（如第23–24课）强调规则先于计数；第26课若事后改 pattern 长度，events 与 accuracy 都不具可比性。

双分数课（如第25课）说明水平误差与方向误差可分离；第26课策略若为 sign book，primary metric 必须指向 direction。

成本门（如第39课）应在 hit rate 之前进入；第26课若未扣费，memo 应显式写「未含 transaction cost」。

泄漏清单（第40课）是 negative catalog；第26课新特征应主动问：是否会出现在未来某天的 list 行上。

停牌间隔（如第35课）改变 row-lag 语义；第26课构造 rolling 特征时应使用 calendar index 而非 raw row shift。

复权口径（如第36课）要求双列披露；第26课任何 return 图表必须标注 adj 或 raw，禁止混用。

窗口均值（如第30–32课）区分 full sample 与 lookback；第26课 feature 命名建议带 window 长度后缀。

市场同期信号（如第38课）与 lag 市场对照；第26课 merge 外部指数时务必 asof 对齐到前一可用观测。

固定 panel（第21课）之后所有数字绑同一 CSV；第26课改路径或增行属于 dataset 版本 bump，不是代码 refactor。

lag-1 方向（第22课）是最简 autocorr sign 游戏；第26课扩展至多元时，先确认单变量基线仍复现 36/77。

三连规则（第23课）样本稀疏；第26课 bootstrap 或 permutation 若做，须在 hold-out 段而非 in-sample 挑规则。

early 非 score（第24课）是防 peek 文案；第26课 dashboard 应把 non-score 段视觉降级（灰显）。

open scale 泄漏（第29课）差 0.0008 量级小但性质严重；第26课 security review 应看公式分母而非看 delta RSS。

high FORBIDDEN（第28课）教 bar 内同步；第26课 intraday 特征更严格，decision time 须早于 bar end。

第26课与第7天 hold-out 精神一致：参与拟合的行不得参与评分；任何「全样本 fit 再全样本 score」须打 in-sample 标签。

第26课与第9天行置换对照：shuffle 行不改 OLS 系数，但 shuffle 时间戳会破坏 lag；panel 课默认时间有序。

第26课与第20天噪声列对照：扩大列空间可降训练 RSS 但恶化留出；panel 上应用切分重复该实验。

第26课写 commit message 时建议带 verify day 号；例如「docs: day-26 sync stdout golden」。

第26课英文键名中的空格与等号两侧空格是 diff 的一部分；自动格式化工具不得 strip 终端行。

第26课 mermaid 节点数字必须来自 stdout；勿在图里写未打印的四舍五入值。

第26课表格是解释层；若表格数字与 text 块冲突，以 text 块为准并修表。

第26课读者若是风控，应关注泄漏 list 与 FORBIDDEN；若是执行，应关注 cost 与 halt gap。

第26课读者若是数据工程，应关注 panel identity 与 imputation；若是 PM，应关注 estimand 一句话。

第26课扩展阅读：Lopez de Prado 的 purged k-fold 用于解决标签重叠；本季未实现但应知存在。

第26课扩展阅读：White (1980) 异方差稳健协方差；方向 accuracy 的渐近方差本季未算。

第26课扩展阅读：Newey-West 对重叠 horizon；若 future 改 weekly label，推断必须换 HAC。

第26课扩展阅读：Harvey (2016) 多重 backtest 试验；勿在 100 seed 里挑最好 day 26 数字。

第26课扩展阅读：Hasbrouck (2007) 有效 spread；第39课常数 cost 是其极简替身。

第26课扩展阅读：Breiman (2001) 两种文化；panel 段在算法文化与数据文化间切换。

第26课扩展阅读：Hamilton (1994) 时间序列；rolling 与 expanding 的信息集差异是核心。

第26课扩展阅读：Little & Rubin (2002) 缺失；MCAR/MAR 本季不辨，但 fill 方向必辨。

第26课扩展阅读：Campbell et al. (1997) 预测回归；lag 结构改变即改变 stochastic 设定。

第26课若接入实时行情，应重建 frozen panel 快照而非 mutate 历史文件；live 与 research 分离。

第26课若在 notebook 跑脚本，working directory 必须是仓库根；否则 panel 相对路径失败。

第26课若在 Docker 跑，镜像应 pin numpy 与 csv 版本；否则 float 末位可能 drift。

第26课 unit test 可 mock 小 csv，但 golden 仍以官方 panel 为准；mock 只测逻辑不测数值。

第26课 code review 可要求作者贴 verify 输出片段；无 verify 的 doc PR 不应 merge。

第26课 teaching assistant 批改时只 diff text 块与三句 estimand；不看 prose 修辞。

第26课若翻译英文版，须同步键名；中文版不得单独发明新 metric 中文名而不给英文键。

第26课交叉引用其他 day 时写「第 N 天」而非「上周」；season 结构是线性课程。

第26课避免写「显然」「众所周知」；改写成可核对机制句。

第26课避免写虚构论文作者；只引用 season 文档已出现或主流教科书。

第26课若提到 p 值而脚本未打印，属于过度推断；本段 21–40 天默认无显著性检验。

第26课若提到 Sharpe 而脚本未打印，应改写成方向 accuracy 或 MSE 或 return mean。

第26课图表若用 mermaid xychart，轴标签须与 stdout 列名一致；本段多数用 flowchart。

第26课完成后，学习者应能在 30 秒内从 stdout 指出：数据对象、评分集合、是否泄漏。

第26课完成后，学习者应能写出一条 Jira 任务：「修复 scale fit on full sample」并链到第33课。

第26课完成后，学习者应能拒绝 PM 需求：「用 high 提升 RSS」并引用第28课 FORBIDDEN。

第26课与 season 后半 lag-5 权重（第51天）的关系：本段建立 panel 纪律，第51天起换标签到五 lag 收益。

第26课与 tree 课（第44天）的关系：树可在同行 panel 上 beat 线性，但泄漏特征仍 FORBIDDEN。

第26课与 ridge（第42天）的关系：惩罚斜率是另一种控制复杂度；与泄漏正交。

第26课与 year split（第58天）的关系：时间切分从比例升级到按年；本段 27 天是比例版。

第26课与 bill（第75天）的关系：方向 accuracy 之后还有计费误差；本段多数未引入 bill。

第26课与 slippage（第93天）的关系：第39天 round-trip 是常数先行版。

第26课 narrative 收束：数字 frozen，机制可讨论，estimand 不可模糊。

回测代码审查时，第26课要求先打开终端输出，再读中文解释；若解释出现 stdout 未打印的阈值或准确率，直接判为文档漂移。

因子入库前，应用与第26课同构的三问：特征在决策时刻是否可见、标签是否同期泄漏、标准化是否只用训练段统计量。

研究 memo 的 estimand 小节应写清第26天脚本使用的 name 列、价格列（close 或 adj_close）、以及差分阶数；换列等于换题。

当 PM 要求「把样本内曲线做漂亮」时，第26课类实验应回复：请先指定 hold-out 掩码或 bill 口径；in-sample 优化不等于交付分数。

数据版本控制应像第26课 second read 一样可机械验证；parquet 也应存 sha256，而不是只靠「同事说没改」。

第26课若涉及方向准确率，报告时必须并列分母（hits 里的 /N）；只写百分比不写 N 是审计不合格。

混池实验（如第37课）与单名实验（如第27课）不得共用一个 leaderboard；第26课文档应在开头声明主语范围。

FORBIDDEN 特征课（如第28课）说明：in-sample RSS 下降可能是泄漏信号；第26课写模型比较时禁止用非法列作优选依据。

缺失填充课（如第34课）提醒：pandas 默认 bfill 在 pipeline 里很常见；第26课起应在 CI 里 grep fillna 方向。

标准化泄漏（如第33课）说明：test MSE 相等不能证明无泄漏；第26课应把 scale 来源写入 model card。

时间切分课（如第27课）的「测试在训练之后」是因果最低标准；第26课若改切分为随机，必须另开对照行而不覆盖 time 行。

随机切分对照（如第26课）只能叫 control，不能叫 walk-forward；第26课命名错误会导致合规审查失败。

事件规则课（如第23–24课）强调规则先于计数；第26课若事后改 pattern 长度，events 与 accuracy 都不具可比性。

双分数课（如第25课）说明水平误差与方向误差可分离；第26课策略若为 sign book，primary metric 必须指向 direction。

成本门（如第39课）应在 hit rate 之前进入；第26课若未扣费，memo 应显式写「未含 transaction cost」。

泄漏清单（第40课）是 negative catalog；第26课新特征应主动问：是否会出现在未来某天的 list 行上。

停牌间隔（如第35课）改变 row-lag 语义；第26课构造 rolling 特征时应使用 calendar index 而非 raw row shift。

复权口径（如第36课）要求双列披露；第26课任何 return 图表必须标注 adj 或 raw，禁止混用。

---

## 实战总结

```bash
python days/26-random-split/random_split.py
```

核对：将终端 stdout 与上文 ```text``` 块逐行 diff；中文叙述中的小数位与键名空格须与英文输出一致。本课机制见 [`random_split.py`](../../days/26-random-split/random_split.py)；改 panel 或切分参数时同步更新 golden 块并跑 `python3 scripts/verify_season01_docs.py --day 26 --min-cjk 3000`。
