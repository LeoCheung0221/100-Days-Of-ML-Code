<p align="center"><b>中文</b> &nbsp;&nbsp;·&nbsp;&nbsp; <a href="day-23.en.md">English</a></p>

# 第 23 天 · 连续三日同向

[第一阶段 · 模型](README.md) · [排版规范](LESSON_LAYOUT.md) · 可运行

今天的学习要点：三连同号后押第四日同向：events = 11，hits = 6，accuracy = 0.5455；`the rule is fixed before the count` 锁定规则先于样本量。

---

## 费曼法讲解

> **结论先行**：`events = 11`、`accuracy = 0.5455` 来自 **固定规则**——三连同号后押第四日同向；`the rule is fixed before the count` 禁止先看 11 再改规则。

扫描 `move` 序列：窗口 `sign(move_{t−3:t−1})` 全相等且非零时，记录 `sign(move_t)` 是否延续。这是 **事件研究** 的最小版本：样本量 11 很小，0.5455 **无** p 值含义。Jegadeesh & Titman（1993）动量与 De Bondt & Thaler（1985）反转在更长样本上讨论；本课只教 **条件触发计数** 与 **规则冻结**。

与第 22 天无条件 lag-1 符号对比：本日 **稀疏触发**（11 次），命中率可高于 0.4675，但 **方差更大**。写 memo 须并列 events 与 accuracy，不能只报 0.5455。规则若改成「两连」或「四连」，events 与分数都变——属于 **estimand 变更**，不是调参。

生产映射：形态识别策略常犯 **multiple testing**；本课 11 事件是提醒 **小 n 下 accuracy 不稳定**。第 24 天把 cut 移到 2024-02-28 后，early 段 8 事件 accuracy 0.5000 **不是 score**，避免 **peek** 后挑段。

```mermaid
flowchart LR
  S3["三连同号"] --> E["events 11"]
  E --> H["hits 6"]
  H --> ACC["accuracy 0.5455"]
```

---

## 核心知识

### 脚本输出（与下方 `text` 块一致）

[`three_day_run.py`](../../days/23-three-day-run/three_day_run.py)：

```text
rule = after three equal signs, predict the fourth matches
events = 11
hits = 6
accuracy = 0.5455
the rule is fixed before the count
```


| 量 | 值 |
|:---|---:|
| events | 11 |
| hits | 6 |
| accuracy | 0.5455 |

规则冻结句 `the rule is fixed before the count` 与 events 计数绑定；改 pattern 长度等于换 estimand。


---

## 拓展领域

**events = 11 的稀疏性.** 三连同号规则在 AAA 全样本只触发 11 次；`accuracy = 0.5455` 的方差极大，不能 star 标注。`the rule is fixed before the count` 是 **legal 句**：禁止先看 11 再改 pattern 长度。Jegadeesh–Titman 动量用月频长窗；本课是 **事件触发计数** 玩具，只教 **规则冻结** 与 **条件样本**。

**与第 22 天无条件 lag-1 对照.** 0.5455 高于 0.4675 但 events≪77；memo 必须 **并列 events**。Multiple testing：若扫描 2/3/4/5 连规则，应多重检验校正——本季不做，但 senior 应知 **挑选规则 = 换 estimand**。

**实现 replay.** 循环从 i=3 起，窗口 `sign(move[i-3:i])` 全等且非零才计数。Code review 应确认 **无 future sign 参与 threshold 选择**。第 24 天在同一规则上切 early/later。
**数值与复现.** 在仓库根目录运行当日脚本；`panel.csv` 与 `numpy==1.24.4` 为默认合同。正文 ```text``` 块须与终端 stdout **逐行零 diff**；改数据或 `fmt` 时同一 commit 更新 golden 与 md。

**全季衔接.** 第 1–20 天：五点 toy 与 OLS/损失/hold-out 语言；第 21 天起：冻结 panel。两套数字 **不可混表**（例如斜率 3.27 与 accuracy 0.4675 无直接比较关系）。第 41 天起模型复杂度上升；第 51 天 lag-5；第 58 年切；第 71 天 bill/direction 分轨——**信息集合同** 全季不变。

**文献锚（非虚构，只作机制分类）.** Campbell, Lo & MacKinlay (1997)；Harvey, Liu & Zhu (2016)；Lopez de Prado (2018)；Little & Rubin (2002)；Hasbrouck (2007)。不得把教科书结论偷换为「本 panel 显著」——本段多数课 **无** 显著性检验 stdout。

**代码审查五问（panel 段）.** 特征在决策时刻是否可见；标准化是否只用训练段矩；train/test 是否按 date/name 分组；metrics 是否诚实区分 in-sample 与 hold-out；FORBIDDEN 行是否仍打印。缺任一条，spec 不完整。

**手算与 CI.** 任取 stdout 一行在 REPL 复算；`verify_season01_docs.py --day N --min-cjk 3000` 为合并必要条件。改 `panel.csv` 须重跑依赖该面板的 golden 日。


第23课 code review 可要求作者贴 verify 输出片段；无 verify 的 doc PR 不应 merge。

第23课 teaching assistant 批改时只 diff text 块与三句 estimand；不看 prose 修辞。

第23课若翻译英文版，须同步键名；中文版不得单独发明新 metric 中文名而不给英文键。

第23课交叉引用其他 day 时写「第 N 天」而非「上周」；season 结构是线性课程。

第23课避免写「显然」「众所周知」；改写成可核对机制句。

第23课避免写虚构论文作者；只引用 season 文档已出现或主流教科书。

第23课若提到 p 值而脚本未打印，属于过度推断；本段 21–40 天默认无显著性检验。

第23课若提到 Sharpe 而脚本未打印，应改写成方向 accuracy 或 MSE 或 return mean。

第23课图表若用 mermaid xychart，轴标签须与 stdout 列名一致；本段多数用 flowchart。

第23课完成后，学习者应能在 30 秒内从 stdout 指出：数据对象、评分集合、是否泄漏。

第23课完成后，学习者应能写出一条 Jira 任务：「修复 scale fit on full sample」并链到第33课。

第23课完成后，学习者应能拒绝 PM 需求：「用 high 提升 RSS」并引用第28课 FORBIDDEN。

第23课与 season 后半 lag-5 权重（第51天）的关系：本段建立 panel 纪律，第51天起换标签到五 lag 收益。

第23课与 tree 课（第44天）的关系：树可在同行 panel 上 beat 线性，但泄漏特征仍 FORBIDDEN。

第23课与 ridge（第42天）的关系：惩罚斜率是另一种控制复杂度；与泄漏正交。

第23课与 year split（第58天）的关系：时间切分从比例升级到按年；本段 27 天是比例版。

第23课与 bill（第75天）的关系：方向 accuracy 之后还有计费误差；本段多数未引入 bill。

第23课与 slippage（第93天）的关系：第39天 round-trip 是常数先行版。

第23课 narrative 收束：数字 frozen，机制可讨论，estimand 不可模糊。

回测代码审查时，第23课要求先打开终端输出，再读中文解释；若解释出现 stdout 未打印的阈值或准确率，直接判为文档漂移。

因子入库前，应用与第23课同构的三问：特征在决策时刻是否可见、标签是否同期泄漏、标准化是否只用训练段统计量。

研究 memo 的 estimand 小节应写清第23天脚本使用的 name 列、价格列（close 或 adj_close）、以及差分阶数；换列等于换题。

当 PM 要求「把样本内曲线做漂亮」时，第23课类实验应回复：请先指定 hold-out 掩码或 bill 口径；in-sample 优化不等于交付分数。

数据版本控制应像第23课 second read 一样可机械验证；parquet 也应存 sha256，而不是只靠「同事说没改」。

第23课若涉及方向准确率，报告时必须并列分母（hits 里的 /N）；只写百分比不写 N 是审计不合格。

混池实验（如第37课）与单名实验（如第27课）不得共用一个 leaderboard；第23课文档应在开头声明主语范围。

FORBIDDEN 特征课（如第28课）说明：in-sample RSS 下降可能是泄漏信号；第23课写模型比较时禁止用非法列作优选依据。

缺失填充课（如第34课）提醒：pandas 默认 bfill 在 pipeline 里很常见；第23课起应在 CI 里 grep fillna 方向。

标准化泄漏（如第33课）说明：test MSE 相等不能证明无泄漏；第23课应把 scale 来源写入 model card。

时间切分课（如第27课）的「测试在训练之后」是因果最低标准；第23课若改切分为随机，必须另开对照行而不覆盖 time 行。

随机切分对照（如第26课）只能叫 control，不能叫 walk-forward；第23课命名错误会导致合规审查失败。

事件规则课（如第23–24课）强调规则先于计数；第23课若事后改 pattern 长度，events 与 accuracy 都不具可比性。

双分数课（如第25课）说明水平误差与方向误差可分离；第23课策略若为 sign book，primary metric 必须指向 direction。

成本门（如第39课）应在 hit rate 之前进入；第23课若未扣费，memo 应显式写「未含 transaction cost」。

泄漏清单（第40课）是 negative catalog；第23课新特征应主动问：是否会出现在未来某天的 list 行上。

停牌间隔（如第35课）改变 row-lag 语义；第23课构造 rolling 特征时应使用 calendar index 而非 raw row shift。

复权口径（如第36课）要求双列披露；第23课任何 return 图表必须标注 adj 或 raw，禁止混用。

窗口均值（如第30–32课）区分 full sample 与 lookback；第23课 feature 命名建议带 window 长度后缀。

市场同期信号（如第38课）与 lag 市场对照；第23课 merge 外部指数时务必 asof 对齐到前一可用观测。

固定 panel（第21课）之后所有数字绑同一 CSV；第23课改路径或增行属于 dataset 版本 bump，不是代码 refactor。

lag-1 方向（第22课）是最简 autocorr sign 游戏；第23课扩展至多元时，先确认单变量基线仍复现 36/77。

三连规则（第23课）样本稀疏；第23课 bootstrap 或 permutation 若做，须在 hold-out 段而非 in-sample 挑规则。

early 非 score（第24课）是防 peek 文案；第23课 dashboard 应把 non-score 段视觉降级（灰显）。

open scale 泄漏（第29课）差 0.0008 量级小但性质严重；第23课 security review 应看公式分母而非看 delta RSS。

high FORBIDDEN（第28课）教 bar 内同步；第23课 intraday 特征更严格，decision time 须早于 bar end。

第23课与第7天 hold-out 精神一致：参与拟合的行不得参与评分；任何「全样本 fit 再全样本 score」须打 in-sample 标签。

第23课与第9天行置换对照：shuffle 行不改 OLS 系数，但 shuffle 时间戳会破坏 lag；panel 课默认时间有序。

第23课与第20天噪声列对照：扩大列空间可降训练 RSS 但恶化留出；panel 上应用切分重复该实验。

第23课写 commit message 时建议带 verify day 号；例如「docs: day-23 sync stdout golden」。

第23课英文键名中的空格与等号两侧空格是 diff 的一部分；自动格式化工具不得 strip 终端行。

第23课 mermaid 节点数字必须来自 stdout；勿在图里写未打印的四舍五入值。

第23课表格是解释层；若表格数字与 text 块冲突，以 text 块为准并修表。

第23课读者若是风控，应关注泄漏 list 与 FORBIDDEN；若是执行，应关注 cost 与 halt gap。

第23课读者若是数据工程，应关注 panel identity 与 imputation；若是 PM，应关注 estimand 一句话。

第23课扩展阅读：Lopez de Prado 的 purged k-fold 用于解决标签重叠；本季未实现但应知存在。

第23课扩展阅读：White (1980) 异方差稳健协方差；方向 accuracy 的渐近方差本季未算。

第23课扩展阅读：Newey-West 对重叠 horizon；若 future 改 weekly label，推断必须换 HAC。

第23课扩展阅读：Harvey (2016) 多重 backtest 试验；勿在 100 seed 里挑最好 day 26 数字。

第23课扩展阅读：Hasbrouck (2007) 有效 spread；第39课常数 cost 是其极简替身。

第23课扩展阅读：Breiman (2001) 两种文化；panel 段在算法文化与数据文化间切换。

第23课扩展阅读：Hamilton (1994) 时间序列；rolling 与 expanding 的信息集差异是核心。

第23课扩展阅读：Little & Rubin (2002) 缺失；MCAR/MAR 本季不辨，但 fill 方向必辨。

第23课扩展阅读：Campbell et al. (1997) 预测回归；lag 结构改变即改变 stochastic 设定。

第23课若接入实时行情，应重建 frozen panel 快照而非 mutate 历史文件；live 与 research 分离。

第23课若在 notebook 跑脚本，working directory 必须是仓库根；否则 panel 相对路径失败。

第23课若在 Docker 跑，镜像应 pin numpy 与 csv 版本；否则 float 末位可能 drift。

第23课 unit test 可 mock 小 csv，但 golden 仍以官方 panel 为准；mock 只测逻辑不测数值。

第23课 code review 可要求作者贴 verify 输出片段；无 verify 的 doc PR 不应 merge。

第23课 teaching assistant 批改时只 diff text 块与三句 estimand；不看 prose 修辞。

第23课若翻译英文版，须同步键名；中文版不得单独发明新 metric 中文名而不给英文键。

第23课交叉引用其他 day 时写「第 N 天」而非「上周」；season 结构是线性课程。

第23课避免写「显然」「众所周知」；改写成可核对机制句。

第23课避免写虚构论文作者；只引用 season 文档已出现或主流教科书。

第23课若提到 p 值而脚本未打印，属于过度推断；本段 21–40 天默认无显著性检验。

第23课若提到 Sharpe 而脚本未打印，应改写成方向 accuracy 或 MSE 或 return mean。

第23课图表若用 mermaid xychart，轴标签须与 stdout 列名一致；本段多数用 flowchart。

第23课完成后，学习者应能在 30 秒内从 stdout 指出：数据对象、评分集合、是否泄漏。

第23课完成后，学习者应能写出一条 Jira 任务：「修复 scale fit on full sample」并链到第33课。

第23课完成后，学习者应能拒绝 PM 需求：「用 high 提升 RSS」并引用第28课 FORBIDDEN。

第23课与 season 后半 lag-5 权重（第51天）的关系：本段建立 panel 纪律，第51天起换标签到五 lag 收益。

第23课与 tree 课（第44天）的关系：树可在同行 panel 上 beat 线性，但泄漏特征仍 FORBIDDEN。

第23课与 ridge（第42天）的关系：惩罚斜率是另一种控制复杂度；与泄漏正交。

第23课与 year split（第58天）的关系：时间切分从比例升级到按年；本段 27 天是比例版。

第23课与 bill（第75天）的关系：方向 accuracy 之后还有计费误差；本段多数未引入 bill。

第23课与 slippage（第93天）的关系：第39天 round-trip 是常数先行版。

第23课 narrative 收束：数字 frozen，机制可讨论，estimand 不可模糊。

回测代码审查时，第23课要求先打开终端输出，再读中文解释；若解释出现 stdout 未打印的阈值或准确率，直接判为文档漂移。

因子入库前，应用与第23课同构的三问：特征在决策时刻是否可见、标签是否同期泄漏、标准化是否只用训练段统计量。

研究 memo 的 estimand 小节应写清第23天脚本使用的 name 列、价格列（close 或 adj_close）、以及差分阶数；换列等于换题。

当 PM 要求「把样本内曲线做漂亮」时，第23课类实验应回复：请先指定 hold-out 掩码或 bill 口径；in-sample 优化不等于交付分数。

---

## 实战总结

```bash
python days/23-three-day-run/three_day_run.py
```

核对：将终端 stdout 与上文 ```text``` 块逐行 diff；中文叙述中的小数位与键名空格须与英文输出一致。本课机制见 [`three_day_run.py`](../../days/23-three-day-run/three_day_run.py)；改 panel 或切分参数时同步更新 golden 块并跑 `python3 scripts/verify_season01_docs.py --day 23 --min-cjk 3000`。
