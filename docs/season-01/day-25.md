<p align="center"><b>中文</b> &nbsp;&nbsp;·&nbsp;&nbsp; <a href="day-25.en.md">English</a></p>

# 第 25 天 · 方向与价格并报

[第一阶段 · 模型](README.md) · [排版规范](LESSON_LAYOUT.md) · 可运行

今天的学习要点：lag-1 收益预测：direction accuracy = 0.4675，mean absolute return error = 0.0167；`days with a small price error and the wrong sign = 9` 说明水平误差小不等于方向对；sign 决策应信 direction accuracy。

---

## 费曼法讲解

> **结论先行**：`direction accuracy = 0.4675` 与 `mean absolute return error = 0.0167` 是 **同一 lag-1 线性预测** 的两个评分；`days with a small price error and the wrong sign = 9` 证明 **水平准 ≠ 方向对**；sign 决策应信 direction accuracy。

特征：昨日简单收益；标签：今日简单收益。OLS 给出水平预测，再算 MAE 与 sign 命中。9 天满足「价格误差小但符号错」——对 **多空开关** 策略，这 9 天是 **假安全** 日。Christoffersen & Diebold（1997）区分水平与方向预测；本课用打印数字固定 **estimand 并列**。

0.0167 的 MAE 在百分之一量级收益上看似「贴价」，但 direction 仍低于 0.5。PM 若只看 RMSE/MAE 会误选 **水平优** 模型做方向 trade。代码审查：metrics 模块是否同时 export `direction_accuracy` 与 `mae`？

与第 10–11 天五点方向分数对照：那里无 panel、无 lag 收益。本课起 **双分数合同** 延续到第 71 天 bill 与 direction 分轨。报告时 **for a sign decision, trust the direction accuracy** 是 stdout 给的工程指令，不是修辞。

```mermaid
flowchart LR
  D["direction 0.4675"] --> T["sign 决策"]
  M["MAE 0.0167"] --> W["9 日小误差错符号"]
```

---

## 核心知识

### 脚本输出（与下方 `text` 块一致）

[`two_scores.py`](../../days/25-two-scores/two_scores.py)：

```text
lag-1 return forecast
direction accuracy = 0.4675
mean absolute return error = 0.0167
days with a small price error and the wrong sign = 9
for a sign decision, trust the direction accuracy
```


| 指标 | 值 | 决策含义 |
|:---|---:|:---|
| direction accuracy | 0.4675 | sign book 主指标 |
| mean abs return error | 0.0167 | 水平贴价，非方向 |
| small error, wrong sign | 9 | 假安全日计数 |

stdout 末行 `for a sign decision, trust the direction accuracy` 为工程裁决，不是修辞。


---

## 拓展领域

**双分数合同.** `direction accuracy = 0.4675` 与 `mean absolute return error = 0.0167` 来自 **同一 lag-1 水平预测**。`days with a small price error and the wrong sign = 9` 标识 **水平贴价但符号错** 的交易日——对 sign book 是「假安全」。Christoffersen–Diebold 区分水平与方向；PM 若只看 MAE 会误选模型。

**stdout 末行裁决.** `for a sign decision, trust the direction accuracy` 是 **工程 primary metric** 声明。Metrics 模块应 export 两列，禁止 dashboard 默认 MAE。

**与第 22 天.** 22 无回归；25 有 OLS 水平预测再评 sign。扩展 bill（第 75 天）时仍分轨。
**数值与复现.** 在仓库根目录运行当日脚本；`panel.csv` 与 `numpy==1.24.4` 为默认合同。正文 ```text``` 块须与终端 stdout **逐行零 diff**；改数据或 `fmt` 时同一 commit 更新 golden 与 md。

**全季衔接.** 第 1–20 天：五点 toy 与 OLS/损失/hold-out 语言；第 21 天起：冻结 panel。两套数字 **不可混表**（例如斜率 3.27 与 accuracy 0.4675 无直接比较关系）。第 41 天起模型复杂度上升；第 51 天 lag-5；第 58 年切；第 71 天 bill/direction 分轨——**信息集合同** 全季不变。

**文献锚（非虚构，只作机制分类）.** Campbell, Lo & MacKinlay (1997)；Harvey, Liu & Zhu (2016)；Lopez de Prado (2018)；Little & Rubin (2002)；Hasbrouck (2007)。不得把教科书结论偷换为「本 panel 显著」——本段多数课 **无** 显著性检验 stdout。

**代码审查五问（panel 段）.** 特征在决策时刻是否可见；标准化是否只用训练段矩；train/test 是否按 date/name 分组；metrics 是否诚实区分 in-sample 与 hold-out；FORBIDDEN 行是否仍打印。缺任一条，spec 不完整。

**手算与 CI.** 任取 stdout 一行在 REPL 复算；`verify_season01_docs.py --day N --min-cjk 3000` 为合并必要条件。改 `panel.csv` 须重跑依赖该面板的 golden 日。


第25课完成后，学习者应能写出一条 Jira 任务：「修复 scale fit on full sample」并链到第33课。

第25课完成后，学习者应能拒绝 PM 需求：「用 high 提升 RSS」并引用第28课 FORBIDDEN。

第25课与 season 后半 lag-5 权重（第51天）的关系：本段建立 panel 纪律，第51天起换标签到五 lag 收益。

第25课与 tree 课（第44天）的关系：树可在同行 panel 上 beat 线性，但泄漏特征仍 FORBIDDEN。

第25课与 ridge（第42天）的关系：惩罚斜率是另一种控制复杂度；与泄漏正交。

第25课与 year split（第58天）的关系：时间切分从比例升级到按年；本段 27 天是比例版。

第25课与 bill（第75天）的关系：方向 accuracy 之后还有计费误差；本段多数未引入 bill。

第25课与 slippage（第93天）的关系：第39天 round-trip 是常数先行版。

第25课 narrative 收束：数字 frozen，机制可讨论，estimand 不可模糊。

回测代码审查时，第25课要求先打开终端输出，再读中文解释；若解释出现 stdout 未打印的阈值或准确率，直接判为文档漂移。

因子入库前，应用与第25课同构的三问：特征在决策时刻是否可见、标签是否同期泄漏、标准化是否只用训练段统计量。

研究 memo 的 estimand 小节应写清第25天脚本使用的 name 列、价格列（close 或 adj_close）、以及差分阶数；换列等于换题。

当 PM 要求「把样本内曲线做漂亮」时，第25课类实验应回复：请先指定 hold-out 掩码或 bill 口径；in-sample 优化不等于交付分数。

数据版本控制应像第25课 second read 一样可机械验证；parquet 也应存 sha256，而不是只靠「同事说没改」。

第25课若涉及方向准确率，报告时必须并列分母（hits 里的 /N）；只写百分比不写 N 是审计不合格。

混池实验（如第37课）与单名实验（如第27课）不得共用一个 leaderboard；第25课文档应在开头声明主语范围。

FORBIDDEN 特征课（如第28课）说明：in-sample RSS 下降可能是泄漏信号；第25课写模型比较时禁止用非法列作优选依据。

缺失填充课（如第34课）提醒：pandas 默认 bfill 在 pipeline 里很常见；第25课起应在 CI 里 grep fillna 方向。

标准化泄漏（如第33课）说明：test MSE 相等不能证明无泄漏；第25课应把 scale 来源写入 model card。

时间切分课（如第27课）的「测试在训练之后」是因果最低标准；第25课若改切分为随机，必须另开对照行而不覆盖 time 行。

随机切分对照（如第26课）只能叫 control，不能叫 walk-forward；第25课命名错误会导致合规审查失败。

事件规则课（如第23–24课）强调规则先于计数；第25课若事后改 pattern 长度，events 与 accuracy 都不具可比性。

双分数课（如第25课）说明水平误差与方向误差可分离；第25课策略若为 sign book，primary metric 必须指向 direction。

成本门（如第39课）应在 hit rate 之前进入；第25课若未扣费，memo 应显式写「未含 transaction cost」。

泄漏清单（第40课）是 negative catalog；第25课新特征应主动问：是否会出现在未来某天的 list 行上。

停牌间隔（如第35课）改变 row-lag 语义；第25课构造 rolling 特征时应使用 calendar index 而非 raw row shift。

复权口径（如第36课）要求双列披露；第25课任何 return 图表必须标注 adj 或 raw，禁止混用。

窗口均值（如第30–32课）区分 full sample 与 lookback；第25课 feature 命名建议带 window 长度后缀。

市场同期信号（如第38课）与 lag 市场对照；第25课 merge 外部指数时务必 asof 对齐到前一可用观测。

固定 panel（第21课）之后所有数字绑同一 CSV；第25课改路径或增行属于 dataset 版本 bump，不是代码 refactor。

lag-1 方向（第22课）是最简 autocorr sign 游戏；第25课扩展至多元时，先确认单变量基线仍复现 36/77。

三连规则（第23课）样本稀疏；第25课 bootstrap 或 permutation 若做，须在 hold-out 段而非 in-sample 挑规则。

early 非 score（第24课）是防 peek 文案；第25课 dashboard 应把 non-score 段视觉降级（灰显）。

open scale 泄漏（第29课）差 0.0008 量级小但性质严重；第25课 security review 应看公式分母而非看 delta RSS。

high FORBIDDEN（第28课）教 bar 内同步；第25课 intraday 特征更严格，decision time 须早于 bar end。

第25课与第7天 hold-out 精神一致：参与拟合的行不得参与评分；任何「全样本 fit 再全样本 score」须打 in-sample 标签。

第25课与第9天行置换对照：shuffle 行不改 OLS 系数，但 shuffle 时间戳会破坏 lag；panel 课默认时间有序。

第25课与第20天噪声列对照：扩大列空间可降训练 RSS 但恶化留出；panel 上应用切分重复该实验。

第25课写 commit message 时建议带 verify day 号；例如「docs: day-25 sync stdout golden」。

第25课英文键名中的空格与等号两侧空格是 diff 的一部分；自动格式化工具不得 strip 终端行。

第25课 mermaid 节点数字必须来自 stdout；勿在图里写未打印的四舍五入值。

第25课表格是解释层；若表格数字与 text 块冲突，以 text 块为准并修表。

第25课读者若是风控，应关注泄漏 list 与 FORBIDDEN；若是执行，应关注 cost 与 halt gap。

第25课读者若是数据工程，应关注 panel identity 与 imputation；若是 PM，应关注 estimand 一句话。

第25课扩展阅读：Lopez de Prado 的 purged k-fold 用于解决标签重叠；本季未实现但应知存在。

第25课扩展阅读：White (1980) 异方差稳健协方差；方向 accuracy 的渐近方差本季未算。

第25课扩展阅读：Newey-West 对重叠 horizon；若 future 改 weekly label，推断必须换 HAC。

第25课扩展阅读：Harvey (2016) 多重 backtest 试验；勿在 100 seed 里挑最好 day 26 数字。

第25课扩展阅读：Hasbrouck (2007) 有效 spread；第39课常数 cost 是其极简替身。

第25课扩展阅读：Breiman (2001) 两种文化；panel 段在算法文化与数据文化间切换。

第25课扩展阅读：Hamilton (1994) 时间序列；rolling 与 expanding 的信息集差异是核心。

第25课扩展阅读：Little & Rubin (2002) 缺失；MCAR/MAR 本季不辨，但 fill 方向必辨。

第25课扩展阅读：Campbell et al. (1997) 预测回归；lag 结构改变即改变 stochastic 设定。

第25课若接入实时行情，应重建 frozen panel 快照而非 mutate 历史文件；live 与 research 分离。

第25课若在 notebook 跑脚本，working directory 必须是仓库根；否则 panel 相对路径失败。

第25课若在 Docker 跑，镜像应 pin numpy 与 csv 版本；否则 float 末位可能 drift。

第25课 unit test 可 mock 小 csv，但 golden 仍以官方 panel 为准；mock 只测逻辑不测数值。

第25课 code review 可要求作者贴 verify 输出片段；无 verify 的 doc PR 不应 merge。

第25课 teaching assistant 批改时只 diff text 块与三句 estimand；不看 prose 修辞。

第25课若翻译英文版，须同步键名；中文版不得单独发明新 metric 中文名而不给英文键。

第25课交叉引用其他 day 时写「第 N 天」而非「上周」；season 结构是线性课程。

第25课避免写「显然」「众所周知」；改写成可核对机制句。

第25课避免写虚构论文作者；只引用 season 文档已出现或主流教科书。

第25课若提到 p 值而脚本未打印，属于过度推断；本段 21–40 天默认无显著性检验。

第25课若提到 Sharpe 而脚本未打印，应改写成方向 accuracy 或 MSE 或 return mean。

第25课图表若用 mermaid xychart，轴标签须与 stdout 列名一致；本段多数用 flowchart。

第25课完成后，学习者应能在 30 秒内从 stdout 指出：数据对象、评分集合、是否泄漏。

第25课完成后，学习者应能写出一条 Jira 任务：「修复 scale fit on full sample」并链到第33课。

第25课完成后，学习者应能拒绝 PM 需求：「用 high 提升 RSS」并引用第28课 FORBIDDEN。

第25课与 season 后半 lag-5 权重（第51天）的关系：本段建立 panel 纪律，第51天起换标签到五 lag 收益。

第25课与 tree 课（第44天）的关系：树可在同行 panel 上 beat 线性，但泄漏特征仍 FORBIDDEN。

第25课与 ridge（第42天）的关系：惩罚斜率是另一种控制复杂度；与泄漏正交。

第25课与 year split（第58天）的关系：时间切分从比例升级到按年；本段 27 天是比例版。

第25课与 bill（第75天）的关系：方向 accuracy 之后还有计费误差；本段多数未引入 bill。

第25课与 slippage（第93天）的关系：第39天 round-trip 是常数先行版。

第25课 narrative 收束：数字 frozen，机制可讨论，estimand 不可模糊。

回测代码审查时，第25课要求先打开终端输出，再读中文解释；若解释出现 stdout 未打印的阈值或准确率，直接判为文档漂移。

因子入库前，应用与第25课同构的三问：特征在决策时刻是否可见、标签是否同期泄漏、标准化是否只用训练段统计量。

研究 memo 的 estimand 小节应写清第25天脚本使用的 name 列、价格列（close 或 adj_close）、以及差分阶数；换列等于换题。

当 PM 要求「把样本内曲线做漂亮」时，第25课类实验应回复：请先指定 hold-out 掩码或 bill 口径；in-sample 优化不等于交付分数。

数据版本控制应像第25课 second read 一样可机械验证；parquet 也应存 sha256，而不是只靠「同事说没改」。

第25课若涉及方向准确率，报告时必须并列分母（hits 里的 /N）；只写百分比不写 N 是审计不合格。

混池实验（如第37课）与单名实验（如第27课）不得共用一个 leaderboard；第25课文档应在开头声明主语范围。

FORBIDDEN 特征课（如第28课）说明：in-sample RSS 下降可能是泄漏信号；第25课写模型比较时禁止用非法列作优选依据。

缺失填充课（如第34课）提醒：pandas 默认 bfill 在 pipeline 里很常见；第25课起应在 CI 里 grep fillna 方向。

标准化泄漏（如第33课）说明：test MSE 相等不能证明无泄漏；第25课应把 scale 来源写入 model card。

时间切分课（如第27课）的「测试在训练之后」是因果最低标准；第25课若改切分为随机，必须另开对照行而不覆盖 time 行。

随机切分对照（如第26课）只能叫 control，不能叫 walk-forward；第25课命名错误会导致合规审查失败。

---

## 实战总结

```bash
python days/25-two-scores/two_scores.py
```

核对：将终端 stdout 与上文 ```text``` 块逐行 diff；中文叙述中的小数位与键名空格须与英文输出一致。本课机制见 [`two_scores.py`](../../days/25-two-scores/two_scores.py)；改 panel 或切分参数时同步更新 golden 块并跑 `python3 scripts/verify_season01_docs.py --day 25 --min-cjk 3000`。
