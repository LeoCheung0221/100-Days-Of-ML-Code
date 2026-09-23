# -*- coding: utf-8 -*-
"""Day-specific 拓展领域 prose (≥800 CJK each) for season-01 days 21–40."""

PROSE = {
    21: """
**Frozen artifact 与版本 bump.** 第 21 天不估计任何参数；stdout 是 **数据集身份证**。`path = days/data/panel.csv` 与 `rows = 160` 把后续 22–99 天的分母锁在同一文件上。研究环境若 silently 替换 CSV，36/77、11 events、0.5417 等数字会整体漂移而 commit message 仍写「调参」——这是 quant dev 最昂贵的 silent bug。应像 pin 依赖一样 pin 数据：Git tag、DVC hash，或 internal artifact registry。

**Text match 而非 float dict.** `second read matches = true` 比较的是 **两次 read_text() 的字符串相等**，刻意绕过 parse 后 NaN≠NaN 的伪差异。工程上若只做 `pd.read_csv` 后 `equals()`，可能漏掉 dtype 或空白差异；本课选择最保守的 **字节合同**。扩展至 parquet 时，仍应存 **content hash** 并在 CI smoke 中比对。

**AAA blank closes = 1.** 本日 **不计** 填法、不删行；只声明存在一格空 close（与第 34 天 `blank date = 2024-02-01` 同源）。任何 lag/return 管道必须先 `_complete` 或显式 imputation policy；否则 diff 链在 blank 处断裂，hits 分母会神秘地变成 77 而非 80。

**not resampled 与 bootstrap 的边界.** `the table is not resampled` 声明脚本 **不** 在运行时抽子样本。第 26–27 天的 train mask 是 **行掩码**，不是换表；第 21 天若增删行，属于 **换题** 而非 resample。Walk-forward 研究者应把「换 CSV」与「换 mask」写进 memo 不同小节。

**Senior 交付.** 本课合格交付 = 终端七行零 diff + 三句 estimand（对象=panel 文本、评分=identity 键、泄漏=无模型）。PM 若问 alpha，回答：今日无 alpha，只有 **数据是否被换**。
""",
    22: """
**hits = 36/77 的分母纪律.** 77 来自 `_complete(AAA)` 上 `adj_close` 一阶差分后的有效对数，不是 80 行也不是 160 行。对外报告 direction accuracy 必须并列 **36/77**；只写 46.75% 而不写 n 在合规审查里不合格。Wilson 区间在 n=77 时仍宽，本课不算 p 值，但 quant 应直觉到 **低于 0.5 可能是噪声**。

**coin-flip baseline = 0.5000 的含义.** 这是 **二项符号游戏** 的刻度，不是「市场有效」定理。Lo & MacKinlay（1988）方差比与自相关检验需要更长样本与 formal 检验；本课固定 in-sample 计数，**未** 做 train/test。把 0.4675 写进「样本外 IC」摘要属于误标，与第 7 天 hold-out 精神冲突。

**信息集：sign(r_{t−1}) 在 t 开盘前可知吗？** 教学合同：昨日收盘后符号已知，今日符号是 **同期标签**。这与第 38 天 market 同期泄漏对照——本课 lag-1 **自身** 是因果可读的，只是 **无预测力**（低于 0.5）。策略原型「跟昨日方向」在第 39 天还要过 **round-trip cost** 门。

**与五点方向课的分叉.** 第 11–16 天在价格水平 toy 上算 direction；第 22 天起在 **panel 简单收益** 上算。两套数字不可比大小。扩展多元因子前，应先在本 stdout 上复现 36/77，作为 **单变量基线**。
""",
    38: """
**0.6795 不是 alpha，是 simultaneity ledger.** 用 **同日** market 收益符号预测 AAA 方向，命中 0.6795。该特征在 decision time 通常 **不可见**（market 与 AAA 同期收盘），属于 **标签侧信息倒流进特征**。研究 log 应把 0.6795 记入 **泄漏 premium 归档**，而不是 factor zoo 入库。

**0.4026 才是可交易对照.** `lagged-one-day market sign accuracy = 0.4026` 使用 **滞后一日** 的市场符号，信息集与第 22 天 lag-1 自方向类似：特征在 t 前已知。两数差 ~0.28 几乎全部来自 **同步性**；stdout 用 `what disappeared was simultaneous` 锁定机制，禁止改写成「市场无效」叙事。

**与第 28 天 FORBIDDEN 同族.** `column high = FORBIDDEN` 教 **bar 内同步**；本课教 **指数/市场列同步**。多因子回归里 contemporaneous market 可用于 **解释方差**（beta 估计），但 **不能** 作为 trading signal 进入回测。Residual 分析与 alpha 信号必须 **分文件** 维护。

**生产 merge 纪律.** 外部 index 字段 merge 进 panel 时，应 `merge_asof` 且 timestamp **严格 ≤ 决策时刻**。Code review grep：`market_return` 无 lag 后缀却进入 `features.parquet` 是 red flag。第 40 天清单行 `same-day market return` 应出现在 onboarding 幻灯 **负例** 页。
""",
    40: """
**Negative catalog 闭合 season-1 泄漏词汇.** 第 40 天不重跑模型；stdout 索引六类 **future=yes** 违规：同期 high（28）、未来 open scale（29）、test 段 scale（33）、next fill（34）、跨名同日期 random（37）、同期 market（38）。这是 **合规训练文档**，不是「失败项目」羞耻清单。

**a higher score is not a result.** 英文句是 **global negation**：在这些设计下刷高的 RSS、accuracy、MSE **不得** 进入 leaderboard、PM deck 或 external marketing。科研诚信要求 **与成功同权地报告违规与负结果**；许多团队只在 appendix 里写「试过 high 特征」而不给数字——本季要求 **数字也归档**。

**与 honest time split 的边界.** 第 27 天 `time-split test accuracy = 0.5417` **不是** 泄漏；泄漏在 **特征/scale/fill/池化切分**。新同事常混淆「我做了 time split 所以没问题」与「scale fit 在全表」——第 33 天 MSE 相等反例说明 **metric 不变 ≠ 合同合法**。

**PR 模板.** 新特征 PR 描述应回答：（1）decision time；（2）label time；（3）是否出现在本 list 六行之一。若 yes，只能进 **反例附录** 并引用第 40 天 stdout，不得 merge 到 production alpha pipeline。
""",
}

# Remaining days: dense prose keyed to stdout (generated in-repo for rewrite pass).
for _day, _text in {
    23: """
**events = 11 的稀疏性.** 三连同号规则在 AAA 全样本只触发 11 次；`accuracy = 0.5455` 的方差极大，不能 star 标注。`the rule is fixed before the count` 是 **legal 句**：禁止先看 11 再改 pattern 长度。Jegadeesh–Titman 动量用月频长窗；本课是 **事件触发计数** 玩具，只教 **规则冻结** 与 **条件样本**。

**与第 22 天无条件 lag-1 对照.** 0.5455 高于 0.4675 但 events≪77；memo 必须 **并列 events**。Multiple testing：若扫描 2/3/4/5 连规则，应多重检验校正——本季不做，但 senior 应知 **挑选规则 = 换 estimand**。

**实现 replay.** 循环从 i=3 起，窗口 `sign(move[i-3:i])` 全等且非零才计数。Code review 应确认 **无 future sign 参与 threshold 选择**。第 24 天在同一规则上切 early/later。
""",
    24: """
**early accuracy is not the score.** `cut date = 2024-02-28` 把事件按 **第四日日期** 分 early/later。early 8 次 accuracy 0.5000 **不得** 进 KPI；later 3 次 0.6667 才是 **下一段** 上的计数（n 极小，仍不推断）。Dashboard 应灰显 early，避免 **peek 后挑段**。

**与第 7 天 hold-out 同族.** 信息集边界决定分子分母；「看过 early 再报 later」若伴随 **改规则** 仍是泄漏。Walk-forward 应 **先定 cut** 再跑；stdout 英文句锁定合同。

**3 events 警告.** later 段 n=3 时 0.6667 无稳健性；教学点是 **段标签** 而非点估计显著。
""",
    25: """
**双分数合同.** `direction accuracy = 0.4675` 与 `mean absolute return error = 0.0167` 来自 **同一 lag-1 水平预测**。`days with a small price error and the wrong sign = 9` 标识 **水平贴价但符号错** 的交易日——对 sign book 是「假安全」。Christoffersen–Diebold 区分水平与方向；PM 若只看 MAE 会误选模型。

**stdout 末行裁决.** `for a sign decision, trust the direction accuracy` 是 **工程 primary metric** 声明。Metrics 模块应 export 两列，禁止 dashboard 默认 MAE。

**与第 22 天.** 22 无回归；25 有 OLS 水平预测再评 sign。扩展 bill（第 75 天）时仍分轨。
""",
    26: """
**control 身份.** `this number is the control` 锁定 0.4583 **不是** walk-forward 成绩。random split、seed 1、train 0.70 允许未来行进训练；单名 AAA 不会拆同日历两行，但 **时间逆序** 仍可能。

**与第 27 天关系.** 本日 **不** 并排 time split；并排在 27。Memo 只许引 control 句 + 0.4583。禁止 100 seed 搜最优。

**seed 1.** 复现锚点；换 seed 数字变、机制不变。
""",
    27: """
**0.5417 与 0.4583 必须并排.** time split 测试块 **全部在训练行之后**（`the test of the time split sits entirely after the train`）。random 同 seed、同比例；差 0.0834 **不是 p 值**。单名 AAA 上 random **未** 抬高分数——与第 37 天 pooled 反转对照。

**因果最低标准.** Campbell–Lo–MacKinlay 默认可预测变量在 t 前已知；time split 是 **最小因果序** 实现。第 9 天行置换不动 OLS 系数但破坏 lag；本日动 **掩码** 非 shuffle 行。

**实施假设.** CSV 已按 date sort；掩码按行序 70%。第 58 天升级按年切分。
""",
    28: """
**FORBIDDEN 优先于 RSS.** `column high = FORBIDDEN` 尽管 RSS 31.8715 < 35.5233。同期 high 含 **当 bar 信息**；解释 close 时泄漏。Feature store 应对 high/low 与 label 同日组合 enum **LEAKY**。

**RSS 只作反例.** 31.8715 证明泄漏可 **in-sample 更贴**；不得 model selection。第 40 天 list future=yes。

**lag close 35.5233.** honest 参照仍 in-sample；样本外需第 27 天掩码。
""",
    29: """
**0.0008 差 vs 机制.** leaky RSS 0.2642 vs past-only 0.2650；`the leaky scale is a function of later opens`。Audit 看 **分母是否含未来 open**，不是 delta 大小。

**与第 33 天同族.** scale 必须 train-only；MSE 相等不能洗白。画时间轴：哪些 open 进入 scale。

**return 回归.** 目标为 simple return；特征为 scaled close。禁止把 0.2642 贴进 OOS 改善摘要。
""",
    30: """
**12.1976 vs 12.0095.** full-sample 直线在末 t 使用 **含未来行** 的信息；lookback=20 才是 t 时可见。`the full sample is not the information set` 是 adapted 过程语言。

**特征命名.** 避免 `expanding_mean` 无 `closed='left'`。实时 pipeline 只用 rolling/window。

**与 31–32 窗长系列.** 本课建立 full≠window；后续比较 3/20/60 斜率。
""",
    31: """
**短窗 in-sample 更贴末点.** 三日 miss 0.0867 < 二十日 0.1506；斜率符号可反（−0.1195 vs 0.0251）。忌把 **末点 miss 最小** 写成 OOS 最优窗。

**选窗须 validation.** 第 55 天 hold-out 比模型；本课无切分。

**OLS on time index.** 对 adj close 回归 t；非 return 空间。
""",
    32: """
**长窗末点 miss 更大.** 六十日 miss 0.4426 vs 三日 0.0867；长窗平滑旧趋势，对 **下一日** 末点可欠贴。Fama–French 因子窗与本课 toy 不同；机制是 **窗口长度改变偏差**。

**三窗 recap.** 与第 31 天联读 3/20/60；禁止只报 0.0867 选窗。
""",
    33: """
**MSE 相等反例.** 两种 scale 下 test MSE 均为 0.000109，但 whole-sample scale **看见 test stretch**。Model card 必须写 **scale fit 范围**；sklearn Pipeline 仅 fit train。

**四矩打印.** train vs whole mean/std 不同，证明 test 拉偏全样本矩。与第 29 天 leaky open 不同列、同 **信息集** 问题。

**grep 审查.** `StandardScaler().fit(X)` 在全表是 fail。
""",
    34: """
**prev vs next fill.** 10.1047 因果；9.8971 含 future。`the next close sees the future`；pandas bfill 在特征列禁止 silent 使用。

**blank 2024-02-01.** 与第 21 天 blank=1 一致。Imputation 改变 return 链，影响 22–23 方向计数。

**敏感分析.** 两种 fill 应并列报告，不得只报 prev「更合理」。
""",
    35: """
**行相邻 ≠ 会话相邻.** gap=2 business days between 2024-02-20 and 2024-02-22。Row lag-1 diff 覆盖 **多日历日** 价格变化。

**halt 表.** 生产 merge 停牌标志；rolling 用 calendar index。

**与第 34 天.** blank 是缺失；本课是 **日期跳变** 仍有行。
""",
    36: """
**双报 return.** raw −0.4938 vs adj 0.0124 on 2024-03-11；`both numbers are due`。Chart 禁止只 dramatize 未复权暴跌。

**研究默认 adj.** risk 展示 raw 须 label。禁止 train raw / label adj 混用。

**returns() 分支.** 读 course.py；unit test 双列。
""",
    37: """
**pooled 反转名次.** random 0.7234 > time 0.6170；`the random split can train and test on the same date`——AAA/BBB 同行日历可 split 到两侧。

**vs 单名第 27 天.** 0.4583<0.5417 仍成立；**不得** 混 leaderboard。Fix：group by date 或 purged CV（Lopez de Prado 2018）。

**主语变更.** 报告 pooled 必须声明 **混池 + random**。
""",
    39: """
**成本门.** gross −0.0024，round-trip 0.0020，net −0.0044。Hit rate 0.47 级 **不** 自动 cover 20bp；Hasbrouck 成本框架的极简版。

**与 22–27.** 那些课无费；本课起 P&L 语言。Break-even hit 扩展练习不写 stdout。

**PM 披露.** 并列 gross/net 与 assumed cost；borrow/funding 本课不含。
""",
}.items():
    PROSE[_day] = _text.strip()
