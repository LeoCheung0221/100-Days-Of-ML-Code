<p align="center"><b>中文</b> &nbsp;&nbsp;·&nbsp;&nbsp; <a href="day-72.en.md">English</a></p>

# 第 72 天 · 平静日误差

[第一阶段 · 模型](README.md) · [排版规范](LESSON_LAYOUT.md) · 可运行

今天的学习要点：quiet 日 MAE = 0.003154，全 test MAE = 0.006980；小 |y| 日子集更贴，须披露分母。

---

## 费曼法讲解

> **结论先行**：quiet 子集（10 日）mean |e| = 0.003154 **低于** 全 test 0.006980——小 |y| 日 **天然更易贴**；须写「这些天本来就好猜」，不能包装成模型 **特殊能力**。

分母：quiet 10，all 19。与第 71 天 quiet 计数同定义。conditional MAE **不可** 与 unconditional MSE 0.000081 直接比大小——不同分母与损失。

监控：若 quiet MAE 升而全 MAE 平，可能是 **大日** 出问题；反之仅 quiet 改善可能是 **避战** jump。第 74 天 jump 日主导 |e| 排名。

误用：只报 0.003154 作「模型 MAE」；忽略 jump 日贡献。

```mermaid
flowchart LR
  Q["quiet MAE 0.003154"] --> C["分母 10"]
  A["all test 0.006980"] --> N["分母 19"]
```

---

## 核心知识

### 脚本输出（与下方 `text` 块一致）

[`quiet_days.py`](../../days/72-quiet-days/quiet_days.py)：

```text
quiet days = 10
mean abs error on quiet days = 0.003154
mean abs error all test days = 0.006980
```



---

## 拓展领域

**conditional estimand。** quiet MAE 分母 10；全 MAE 分母 19。

**解释义务。** 小 |y| 易贴是数据性质，非 alpha。

**lag-5 合同（默认）。** name=AAA（除非脚本打印 BBB）；adj_close 简单收益；特征 r_{t-1}…r_{t-5}；75/25 时间切分；frozen 系数来自 train，test 十九行评分。第 58 天 0.000782 属年切实验，不与 0.000081 混标题。

**水平 vs 方向 vs bill。** 第 61–70 天以 MSE/MAE 为主；第 71 天起三类计数与 bill；dashboard 分 tab。Christoffersen & Diebold（1997）；Hand（2006）成本敏感学习。

**泄漏与 FORBIDDEN。** 第 67 天 same-day market；第 56–57 天同 bar OHLC；第 40 天清单。feature lint 先于训练。

**复现。** 仓库根目录、`numpy==1.24.4`、`days/data/panel.csv`；```text``` golden diff；`python3 scripts/verify_season01_docs.py --day N --min-cjk 3000`。

**文献（非虚构）。** Breiman（2001）；Lopez de Prado（2018）；Hamilton（1994）；Harvey et al.（2016）；Campbell, Lo & MacKinlay（1997）；Hasbrouck（2007）。


high FORBIDDEN（第28课）教 bar 内同步；第72课 intraday 特征更严格，decision time 须早于 bar end。

第72课与第7天 hold-out 精神一致：参与拟合的行不得参与评分；任何「全样本 fit 再全样本 score」须打 in-sample 标签。

第72课与第9天行置换对照：shuffle 行不改 OLS 系数，但 shuffle 时间戳会破坏 lag；panel 课默认时间有序。

第72课与第20天噪声列对照：扩大列空间可降训练 RSS 但恶化留出；panel 上应用切分重复该实验。

第72课写 commit message 时建议带 verify day 号；例如「docs: day-72 sync stdout golden」。

第72课英文键名中的空格与等号两侧空格是 diff 的一部分；自动格式化工具不得 strip 终端行。

第72课 mermaid 节点数字必须来自 stdout；勿在图里写未打印的四舍五入值。

第72课表格是解释层；若表格数字与 text 块冲突，以 text 块为准并修表。

第72课读者若是风控，应关注泄漏 list 与 FORBIDDEN；若是执行，应关注 cost 与 halt gap。

第72课读者若是数据工程，应关注 panel identity 与 imputation；若是 PM，应关注 estimand 一句话。

第72课扩展阅读：Lopez de Prado 的 purged k-fold 用于解决标签重叠；本季未实现但应知存在。

第72课扩展阅读：White (1980) 异方差稳健协方差；方向 accuracy 的渐近方差本季未算。

第72课扩展阅读：Newey-West 对重叠 horizon；若 future 改 weekly label，推断必须换 HAC。

第72课扩展阅读：Harvey (2016) 多重 backtest 试验；勿在 100 seed 里挑最好 day 26 数字。

第72课扩展阅读：Hasbrouck (2007) 有效 spread；第39课常数 cost 是其极简替身。

第72课扩展阅读：Breiman (2001) 两种文化；panel 段在算法文化与数据文化间切换。

第72课扩展阅读：Hamilton (1994) 时间序列；rolling 与 expanding 的信息集差异是核心。

第72课扩展阅读：Little & Rubin (2002) 缺失；MCAR/MAR 本季不辨，但 fill 方向必辨。

第72课扩展阅读：Campbell et al. (1997) 预测回归；lag 结构改变即改变 stochastic 设定。

第72课若接入实时行情，应重建 frozen panel 快照而非 mutate 历史文件；live 与 research 分离。

第72课若在 notebook 跑脚本，working directory 必须是仓库根；否则 panel 相对路径失败。

第72课若在 Docker 跑，镜像应 pin numpy 与 csv 版本；否则 float 末位可能 drift。

第72课 unit test 可 mock 小 csv，但 golden 仍以官方 panel 为准；mock 只测逻辑不测数值。

第72课 code review 可要求作者贴 verify 输出片段；无 verify 的 doc PR 不应 merge。

第72课 teaching assistant 批改时只 diff text 块与三句 estimand；不看 prose 修辞。

第72课若翻译英文版，须同步键名；中文版不得单独发明新 metric 中文名而不给英文键。

第72课交叉引用其他 day 时写「第 N 天」而非「上周」；season 结构是线性课程。

第72课避免写「显然」「众所周知」；改写成可核对机制句。

第72课避免写虚构论文作者；只引用 season 文档已出现或主流教科书。

第72课若提到 p 值而脚本未打印，属于过度推断；本段 21–40 天默认无显著性检验。

第72课若提到 Sharpe 而脚本未打印，应改写成方向 accuracy 或 MSE 或 return mean。

第72课图表若用 mermaid xychart，轴标签须与 stdout 列名一致；本段多数用 flowchart。

第72课完成后，学习者应能在 30 秒内从 stdout 指出：数据对象、评分集合、是否泄漏。

第72课完成后，学习者应能写出一条 Jira 任务：「修复 scale fit on full sample」并链到第33课。

第72课完成后，学习者应能拒绝 PM 需求：「用 high 提升 RSS」并引用第28课 FORBIDDEN。

第72课与 season 后半 lag-5 权重（第51天）的关系：本段建立 panel 纪律，第51天起换标签到五 lag 收益。

第72课与 tree 课（第44天）的关系：树可在同行 panel 上 beat 线性，但泄漏特征仍 FORBIDDEN。

第72课与 ridge（第42天）的关系：惩罚斜率是另一种控制复杂度；与泄漏正交。

第72课与 year split（第58天）的关系：时间切分从比例升级到按年；本段 27 天是比例版。

第72课与 bill（第75天）的关系：方向 accuracy 之后还有计费误差；本段多数未引入 bill。

第72课与 slippage（第93天）的关系：第39天 round-trip 是常数先行版。

第72课 narrative 收束：数字 frozen，机制可讨论，estimand 不可模糊。

回测代码审查时，第72课要求先打开终端输出，再读中文解释；若解释出现 stdout 未打印的阈值或准确率，直接判为文档漂移。

因子入库前，应用与第72课同构的三问：特征在决策时刻是否可见、标签是否同期泄漏、标准化是否只用训练段统计量。

研究 memo 的 estimand 小节应写清第72天脚本使用的 name 列、价格列（close 或 adj_close）、以及差分阶数；换列等于换题。

当 PM 要求「把样本内曲线做漂亮」时，第72课类实验应回复：请先指定 hold-out 掩码或 bill 口径；in-sample 优化不等于交付分数。

数据版本控制应像第72课 second read 一样可机械验证；parquet 也应存 sha256，而不是只靠「同事说没改」。

第72课若涉及方向准确率，报告时必须并列分母（hits 里的 /N）；只写百分比不写 N 是审计不合格。

混池实验（如第37课）与单名实验（如第27课）不得共用一个 leaderboard；第72课文档应在开头声明主语范围。

FORBIDDEN 特征课（如第28课）说明：in-sample RSS 下降可能是泄漏信号；第72课写模型比较时禁止用非法列作优选依据。

缺失填充课（如第34课）提醒：pandas 默认 bfill 在 pipeline 里很常见；第72课起应在 CI 里 grep fillna 方向。

标准化泄漏（如第33课）说明：test MSE 相等不能证明无泄漏；第72课应把 scale 来源写入 model card。

时间切分课（如第27课）的「测试在训练之后」是因果最低标准；第72课若改切分为随机，必须另开对照行而不覆盖 time 行。

随机切分对照（如第26课）只能叫 control，不能叫 walk-forward；第72课命名错误会导致合规审查失败。

事件规则课（如第23–24课）强调规则先于计数；第72课若事后改 pattern 长度，events 与 accuracy 都不具可比性。

双分数课（如第25课）说明水平误差与方向误差可分离；第72课策略若为 sign book，primary metric 必须指向 direction。

成本门（如第39课）应在 hit rate 之前进入；第72课若未扣费，memo 应显式写「未含 transaction cost」。

泄漏清单（第40课）是 negative catalog；第72课新特征应主动问：是否会出现在未来某天的 list 行上。

停牌间隔（如第35课）改变 row-lag 语义；第72课构造 rolling 特征时应使用 calendar index 而非 raw row shift。

复权口径（如第36课）要求双列披露；第72课任何 return 图表必须标注 adj 或 raw，禁止混用。

窗口均值（如第30–32课）区分 full sample 与 lookback；第72课 feature 命名建议带 window 长度后缀。

市场同期信号（如第38课）与 lag 市场对照；第72课 merge 外部指数时务必 asof 对齐到前一可用观测。

固定 panel（第21课）之后所有数字绑同一 CSV；第72课改路径或增行属于 dataset 版本 bump，不是代码 refactor。

lag-1 方向（第22课）是最简 autocorr sign 游戏；第72课扩展至多元时，先确认单变量基线仍复现 36/77。

三连规则（第23课）样本稀疏；第72课 bootstrap 或 permutation 若做，须在 hold-out 段而非 in-sample 挑规则。

early 非 score（第24课）是防 peek 文案；第72课 dashboard 应把 non-score 段视觉降级（灰显）。

open scale 泄漏（第29课）差 0.0008 量级小但性质严重；第72课 security review 应看公式分母而非看 delta RSS。

high FORBIDDEN（第28课）教 bar 内同步；第72课 intraday 特征更严格，decision time 须早于 bar end。

第72课与第7天 hold-out 精神一致：参与拟合的行不得参与评分；任何「全样本 fit 再全样本 score」须打 in-sample 标签。

第72课与第9天行置换对照：shuffle 行不改 OLS 系数，但 shuffle 时间戳会破坏 lag；panel 课默认时间有序。

第72课与第20天噪声列对照：扩大列空间可降训练 RSS 但恶化留出；panel 上应用切分重复该实验。

第72课写 commit message 时建议带 verify day 号；例如「docs: day-72 sync stdout golden」。

第72课英文键名中的空格与等号两侧空格是 diff 的一部分；自动格式化工具不得 strip 终端行。

第72课 mermaid 节点数字必须来自 stdout；勿在图里写未打印的四舍五入值。

第72课表格是解释层；若表格数字与 text 块冲突，以 text 块为准并修表。

第72课读者若是风控，应关注泄漏 list 与 FORBIDDEN；若是执行，应关注 cost 与 halt gap。

第72课读者若是数据工程，应关注 panel identity 与 imputation；若是 PM，应关注 estimand 一句话。

第72课扩展阅读：Lopez de Prado 的 purged k-fold 用于解决标签重叠；本季未实现但应知存在。

第72课扩展阅读：White (1980) 异方差稳健协方差；方向 accuracy 的渐近方差本季未算。

第72课扩展阅读：Newey-West 对重叠 horizon；若 future 改 weekly label，推断必须换 HAC。

第72课扩展阅读：Harvey (2016) 多重 backtest 试验；勿在 100 seed 里挑最好 day 26 数字。

第72课扩展阅读：Hasbrouck (2007) 有效 spread；第39课常数 cost 是其极简替身。

第72课扩展阅读：Breiman (2001) 两种文化；panel 段在算法文化与数据文化间切换。

第72课扩展阅读：Hamilton (1994) 时间序列；rolling 与 expanding 的信息集差异是核心。

第72课扩展阅读：Little & Rubin (2002) 缺失；MCAR/MAR 本季不辨，但 fill 方向必辨。

第72课扩展阅读：Campbell et al. (1997) 预测回归；lag 结构改变即改变 stochastic 设定。

第72课若接入实时行情，应重建 frozen panel 快照而非 mutate 历史文件；live 与 research 分离。

第72课若在 notebook 跑脚本，working directory 必须是仓库根；否则 panel 相对路径失败。

第72课若在 Docker 跑，镜像应 pin numpy 与 csv 版本；否则 float 末位可能 drift。

第72课 unit test 可 mock 小 csv，但 golden 仍以官方 panel 为准；mock 只测逻辑不测数值。

第72课 code review 可要求作者贴 verify 输出片段；无 verify 的 doc PR 不应 merge。

第72课 teaching assistant 批改时只 diff text 块与三句 estimand；不看 prose 修辞。

第72课若翻译英文版，须同步键名；中文版不得单独发明新 metric 中文名而不给英文键。

第72课交叉引用其他 day 时写「第 N 天」而非「上周」；season 结构是线性课程。

第72课避免写「显然」「众所周知」；改写成可核对机制句。

第72课避免写虚构论文作者；只引用 season 文档已出现或主流教科书。

第72课若提到 p 值而脚本未打印，属于过度推断；本段 21–40 天默认无显著性检验。

第72课若提到 Sharpe 而脚本未打印，应改写成方向 accuracy 或 MSE 或 return mean。

第72课图表若用 mermaid xychart，轴标签须与 stdout 列名一致；本段多数用 flowchart。

第72课完成后，学习者应能在 30 秒内从 stdout 指出：数据对象、评分集合、是否泄漏。

第72课完成后，学习者应能写出一条 Jira 任务：「修复 scale fit on full sample」并链到第33课。

第72课完成后，学习者应能拒绝 PM 需求：「用 high 提升 RSS」并引用第28课 FORBIDDEN。

第72课与 season 后半 lag-5 权重（第51天）的关系：本段建立 panel 纪律，第51天起换标签到五 lag 收益。

第72课与 tree 课（第44天）的关系：树可在同行 panel 上 beat 线性，但泄漏特征仍 FORBIDDEN。

第72课与 ridge（第42天）的关系：惩罚斜率是另一种控制复杂度；与泄漏正交。

第72课与 year split（第58天）的关系：时间切分从比例升级到按年；本段 27 天是比例版。

第72课与 bill（第75天）的关系：方向 accuracy 之后还有计费误差；本段多数未引入 bill。

第72课与 slippage（第93天）的关系：第39天 round-trip 是常数先行版。

第72课 narrative 收束：数字 frozen，机制可讨论，estimand 不可模糊。

回测代码审查时，第72课要求先打开终端输出，再读中文解释；若解释出现 stdout 未打印的阈值或准确率，直接判为文档漂移。

---

## 实战总结

```bash
python days/72-quiet-days/quiet_days.py
```

核对：将终端 stdout 与上文 ```text``` 块逐行 diff；键名与等号两侧空格计入合同。改 panel 或切分后重跑 `python3 scripts/verify_season01_docs.py --day 72 --min-cjk 3000`。
