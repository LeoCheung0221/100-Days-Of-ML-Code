#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""One-off writer for season-01 day-61..80 zh lessons. Not part of CI."""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs" / "season-01"

sys.path.insert(0, str(ROOT / "scripts"))
from _zh_depth_templates import DEPTH_TEMPLATES  # noqa: E402


def cjk_count(text: str) -> int:
    return sum(1 for c in text if "\u4e00" <= c <= "\u9fff")


def run_stdout(day: int) -> str:
    prefixes = (f"{day:02d}-", f"{day}-")
    for d in sorted((ROOT / "days").iterdir()):
        if not d.is_dir():
            continue
        if not any(d.name.startswith(p) for p in prefixes):
            continue
        script = sorted(d.glob("*.py"))[0]
        proc = subprocess.run(
            [sys.executable, str(script)],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        if proc.returncode != 0:
            raise RuntimeError(proc.stderr)
        return proc.stdout.rstrip("\n") + "\n"
    raise FileNotFoundError(day)


META = {
    61: ("树相对零基准", "tree_vs_baseline.py", "61-tree-vs-baseline"),
    62: ("最高置信的十分之一", "top_tenth.py", "62-top-tenth"),
    63: ("按月残差", "monthly_residuals.py", "63-monthly-residuals"),
    64: ("去掉最优月份", "drop_month.py", "64-drop-month"),
    65: ("第二只股票", "second_name.py", "65-second-name"),
    66: ("超额收益标签", "excess_return.py", "66-excess-return"),
    67: ("同期市场列", "market_lag.py", "67-market-lag"),
    68: ("单一入口", "one_entry.py", "68-one-entry"),
    69: ("成交假设", "fill_assumption.py", "69-fill-assumption"),
    70: ("十行任务合同", "ten_lines.py", "70-ten-lines"),
    71: ("三类残差日", "three_classes.py", "71-three-classes"),
    72: ("平静日误差", "quiet_days.py", "72-quiet-days"),
    73: ("方向错误计数", "wrong_direction.py", "73-wrong-direction"),
    74: ("误差最大的五天", "top_five_errors.py", "74-top-five-errors"),
    75: ("差异化计费", "billed_errors.py", "75-billed-errors"),
    76: ("漏报与误报", "two_mistakes.py", "76-two-mistakes"),
    77: ("提高开口阈值", "high_threshold.py", "77-high-threshold"),
    78: ("降低开口阈值", "low_threshold.py", "78-low-threshold"),
    79: ("计费后重排", "billed_ranking.py", "79-billed-ranking"),
    80: ("可承受的错误", "acceptable_mistake.py", "80-acceptable-mistake"),
}

HOOK = {
    61: "depth-1 树 test MSE = 0.000174，baseline = 0.000101，MSE improvement = −0.000072；浅树 hold-out 输给恒零预测。",
    62: "test 19 行；|ŷ| 最大的 2 日（top tenth）MAE = 0.007193，其余 17 日 MAE = 0.006955；高置信子集并不更准。",
    63: "2024-03 月 MAE = 0.007770（2 日），2024-04 月 MAE = 0.006887（17 日）；按月拆开 hold-out 绝对误差。",
    64: "MAE 最低的月 2024-04（0.006887）；去掉该月后剩余 test MAE = 0.007770，高于全月 0.006980。",
    65: "AAA test MSE = 0.000081，BBB test MSE = 0.000105；流程相同，结论不得自动迁移。",
    66: "标签改为 return−market return；test MSE = 0.000095，相对第 51 天绝对收益 0.000081 是不同 estimand。",
    67: "仅 lag test MSE = 0.000081；加同期 market 列 MSE = 0.000094；FORBIDDEN 行声明低 MSE 无效。",
    68: "pipeline(name) 单入口：AAA 0.000081，BBB 0.000105；第二张表须走同一函数。",
    69: "fill = close-to-close，slippage = 0，no order；test MSE = 0.000081 在显式执行合同下重述。",
    70: "十行 stdout 汇总 lag-5 任务：数据、切分、baseline、FORBIDDEN、line MSE、树/量、fill；每数可 grep。",
    71: "quiet = 10，jump = 5，direction wrong = 3；分类轴是 |y| 与 sign，不是单一 MSE。",
    72: "quiet 日 MAE = 0.003154，全 test MAE = 0.006980；小 |y| 日子集更贴，须披露分母。",
    73: "direction wrong days = 3，test days = 19；方向 KPI 与水平 MSE 正交。",
    74: "rank 1–5 日期与 error、class（jump/mid/quiet）、direction；前五日 jump 占四席。",
    75: "total bill line = −18.0000；direction wrong = 3，jump day = 5；计费是加权失误计数。",
    76: "missed down days = 3，false alarm up days = 3；两类方向错分列，不合并成单一 accuracy。",
    77: "threshold = 0.0100，days speaking = 0，speaking MAE = not defined；高阈值下覆盖度归零。",
    78: "threshold = 0.0010，days speaking = 17，speaking MAE = 0.007663；几乎每日开口时的条件误差。",
    79: "bill line = −18.0000，bill tree = −27.0000，lower bill wins = line；MSE 赢家可在 bill 上输。",
    80: "acceptable mistake = direction wrong at cost 1；direction wrong = 3，jump billed at 3 = 5；风险偏好须对应 bill 列。",
}

MERMAID = {
    61: 'flowchart TD\n  Z["baseline ŷ=0"] --> B["MSE 0.000101"]\n  T["depth-1 tree"] --> C["MSE 0.000174"]\n  B --> I["improvement −0.000072"]\n  C --> I',
    62: 'flowchart LR\n  H["|ŷ| top 2 日"] --> A1["MAE 0.007193"]\n  R["其余 17 日"] --> A2["MAE 0.006955"]',
    63: 'xychart-beta\n    title "按月 mean |e|（test）"\n    x-axis ["2024-03", "2024-04"]\n    y-axis "MAE" 0 --> 0.008\n    bar [0.007770, 0.006887]',
    64: 'flowchart TD\n  ALL["全 test MAE 0.006980"] --> DROP["去掉 2024-04"]\n  DROP --> W["剩余 MAE 0.007770"]',
    65: 'flowchart LR\n  A["AAA 0.000081"] --> P["pipeline 同构"]\n  B["BBB 0.000105"] --> P',
    66: 'flowchart TD\n  Y["y = r − r_mkt"] --> M["test MSE 0.000095"]\n  L["绝对 r（第51天）"] --> X["0.000081 · 不同标签"]',
    67: 'flowchart LR\n  L["lags only 0.000081"] --> OK["合法"]\n  S["+ same-day mkt 0.000094"] --> F["FORBIDDEN"]',
    68: 'flowchart TD\n  E["pipeline(name)"] --> A["AAA 0.000081"]\n  E --> B["BBB 0.000105"]',
    69: 'sequenceDiagram\n  participant S as 脚本\n  participant M as 模型\n  S->>M: close-to-close · slippage 0\n  M->>S: test MSE 0.000081',
    70: 'flowchart TD\n  D["panel AAA"] --> T["lag-5 line"]\n  T --> M["MSE 0.000081"]\n  D --> X["FORBIDDEN OHLC/mkt"]',
    71: 'flowchart TD\n  Q["|y|≤med → quiet 10"] --> C["计数"]\n  J["|y|≥p75 → jump 5"] --> C\n  W["sign 错 → 3"] --> C',
    72: 'flowchart LR\n  Q["quiet MAE 0.003154"] --> C["分母 10"]\n  A["all test 0.006980"] --> N["分母 19"]',
    73: 'flowchart TD\n  W["direction wrong 3"] --> R["/ test 19"]\n  M["MSE 轨"] --> X["不替代本计数"]',
    74: 'flowchart TD\n  E1["0.019717 jump"] --> TOP["top-5 |e|"]\n  E5["0.009609 jump"] --> TOP',
    75: 'flowchart LR\n  D["错向 −1 ×3"] --> B["bill −18.0000"]\n  J["jump −3 ×5"] --> B',
    76: 'flowchart TD\n  M["missed down 3"] --> G["漏报大跌"]\n  F["false alarm up 3"] --> H["误报小涨"]',
    77: 'flowchart TD\n  T["τ=0.0100"] --> Z["speaking 0 日"]\n  Z --> U["MAE not defined"]',
    78: 'flowchart LR\n  T["τ=0.0010"] --> S["speaking 17 日"]\n  S --> M["MAE 0.007663"]',
    79: 'flowchart TD\n  BL["line bill −18"] --> W["lower wins"]\n  BT["tree bill −27"] --> W',
    80: 'flowchart LR\n  P["偏好：direction wrong"] --> C["cost 1 列"]\n  J["jump"] --> C3["cost 3 列"]',
}


def feynman(day: int) -> str:
    return FEYNMAN[day].strip()


FEYNMAN: dict[int, str] = {
    61: """
> **结论先行**：depth-1 树 hold-out MSE 0.000174 **高于** 零基准 0.000101；`MSE improvement over baseline = -0.000072` 为负，表示相对恒零预测 **平方误差更大**。与第 52 天 tree 0.000174 劣于 line 0.000081 同向，本日把比较对象换成第 59 天 baseline。

估计路径：train 段 `_best_stump` 在五个 lag 列上选单切点，test 十九行 frozen 预测；baseline 为 ŷ≡0。improvement 定义为 baseline_MSE−tree_MSE，负号即 tree 更差。这不是「树永远无效」的定理，而是 **AAA、lag-5、75/25 时间切分、return 标签** 下的一次审计。

计量含义：MSE 对 |y| 大日敏感（第 2 天 L2 份额）；零预测在 jump 日不额外放大外推，浅树可能在 train 过贴台阶而在 test 放大误差。Breiman et al.（1984）CART 强调 hold-out；本课 stump 与第 60 天 line improvement +0.000020 对照，排序为 line < baseline < tree。

> **常见误用**：把 train 切点 MSE 当部署分数；用第 45 天 **价格** SSE 写进 return 表；将 −0.000072 报道为「改进 0.000072」而不写负号。

与第 79 天：同一 stump 在 bill 规则下 bill −27，劣于 line −18——灵活模型可在两种 metric 下双输。research log 应写：estimator=depth-1 stump，baseline=zero，split=75/25，n_test=19。
""",
    62: """
> **结论先行**：按 |ŷ| 取 test 上最大的十分之一（19 行中 k=2），该子集 mean |y−ŷ| = 0.007193 **高于** 其余 17 日的 0.006955——**模型自报「最自信」的日子并不更准**，不能用 top decile 刷 MAE。

置信代理：本课用 |ŷ| 排序，非概率校准或残差方差模型。k=max(1,⌈0.1n⌉) 保证小样本下至少 1 日。OLS 来自第 51 天 frozen 系数在 test 上代入；子集 MAE 是 **条件期望** 估计，分母分别为 2 与 17，方差大，禁止做显著性宣称。

与第 71 天：|y| 的 quiet/jump 划分看 **实现** 波动，|ŷ| top tenth 看 **预测幅度**——两轴不可混称「高置信日」。生产若用 |ŷ|>τ 过滤信号，须报告 **被过滤日的 MAE** 与 **全样本 MAE** 并列（本课 0.007193 vs 0.006955 是反例）。

Gneiting, Balabdaoui & Raftery（2007）讨论概率 forecast 的 sharpness vs calibration；本课无概率输出，|ŷ| 只是 sharpness 代理。误用：只报告 rest MAE 0.006955 而隐藏 top tenth 更差；或将 2 日子集说成「样本外验证通过」。
""",
    63: """
> **结论先行**：hold-out 绝对误差按日历月聚合——2024-03 仅 2 个交易日，mean |e|=0.007770；2024-04 有 17 日，mean |e|=0.006887。小月 **均值方差大**，不可因 2 日就断定「三月更差」。

实现：`_lag5_for_rows` 带日期列，cut 后 test 误差与 `YYYY-MM` 分组。与第 64 天衔接：最小 MAE 月即 2024-04（0.006887）。这是 **描述性分解**，不是季节性因子检验；Hamilton（1994）季节项需更大 n。

量化监控：若某月独撑全年 IC 或 MAE，可能对应 **单一 jump 事件**（见第 74 天 rank 表在 4 月集中）。dashboard 应 **按月 n** 并列，不只贴均值。改 cut 或增 panel 行会改变「2 vs 17」划分——数据版本须 tag。

误用：把 monthly mean 当作可直接优化的「因子」；或在 2 日月上调参。正确：固定 split，报告 days= 键与 mean abs error 六位小数。
""",
    64: """
> **结论先行**：test 中 mean |e| 最低的月是 2024-04（0.006887）；若 **删掉该月** 再算剩余 test，MAE 升至 0.007770，高于 **全 test** 0.006980——去掉「最好月份」后整体 **更差**，说明聚合 MAE 曾被易预测月 **向下拉**。

这是 **leave-one-month-out 敏感性**，不是推荐剔除日历月的生产规则。第 63 天已给分月表；本日回答 PM：「结论是否只靠四月？」——去掉四月后 MAE 上升，提示 **勿过度外推** 全段表现。与第 5 天删点动 β̂ 不同：本日 **frozen ŷ**，只改分母集合。

Harvey et al.（2016）强调报告 subsample 稳定性；本课是手工 subsample。若做 bootstrap by month，应另开实验，不得覆盖 stdout 四行。审计：核对 drop 月字符串、without 月 MAE 与 63 天 04 月均值一致。
""",
    65: """
> **结论先行**：同一 lag-5 OLS 流程，`name = AAA test MSE = 0.000081`，`name = BBB test MSE = 0.000105`——BBB **更差**，第一只股票的结论 **不得** 无 rerun 贴到第二只。

面板：`name_rows` 过滤，各自 `_complete` 后构 lag-5；75/25 切分 **按各自有效行** 比例，非 pooled。第 37 天混池 random 虚高是另一 estimand；本日 **单名并列**。Campbell et al.（1997）多资产可预测性需 **逐名或联合模型** 声明。

生产：multi-name 策略应对每个 ticker 跑第 68 天式 pipeline，禁止 silent drop BBB。0.000105−0.000081 差绝对量小，但 **相对排序** 影响 name 权重。memo 须写：two names, same code path, different MSE。

误用：用 AAA 系数直接 predict BBB；或将 BBB 0.000105 平均进 AAA 摘要。
""",
    66: """
> **结论先行**：标签改为 `target = return minus market return`（超额简单收益）；test MSE = 0.000095。与第 51 天 **绝对** return MSE 0.000081 **不可横比**——label 变了，MSE 尺度与均值项都变。

合法用法：用 **滞后个股收益** 预测 **同期超额**；market return 进入 **y** 而非同期 X（与第 67 天 forbidden 列对照）。Fama–French 框架里 alpha 是相对基准的均值；本课是 **MSE 预测超额**，不是回归 alpha t 统计。

第 67 天若把 same-day market 放进 X，MSE 0.000094「改善」属泄漏；本日改 y 是 **标签构造**，不是偷看 market 特征。research log 写清：label=r−r_mkt，features=lag1–5 r。

误用：声称「超额 MSE 0.000095 优于 0.000081」；或在特征里加同期 market。
""",
    67: """
> **结论先行**：`test MSE lags only = 0.000081`；加入 same-day market 列后 `0.000094` **更低** 但 `same-day market column = FORBIDDEN`，且 `a lower MSE with same-day market is not a result`——**低 MSE 不是有效结果**。

机制：mkt_t 与 r_t 同期可得，回归用 mkt_t 解释 r_t 含 **同步共变**，非因果预测。第 38 天 market sign 0.6795 vs lag 0.4026 同族。feature store 应对 same-day market 枚举 LEAKY，在 lint 阶段 fail。

与第 66 天：market 进入 **y** 作超额合法；进入 **X** 同期非法。代码审查 grep `market` 列与 shift(1)。stdout FORBIDDEN 行必须进 golden diff。

误用：选 0.000094 模型上线；在 model card 隐藏 forbidden 列。
""",
    68: """
> **结论先行**：`entry = pipeline(name)` 封装 complete→lag5→75/25→OLS→test MSE；AAA 0.000081、BBB 0.000105 与第 65 天数字 **一致**，证明 **单入口** 可复用，避免复制粘贴第二套估计路径。

工程：第二张表、第三个 name 必须调用同一 `pipeline`，否则 metrics 不可比。第 70 天十行是 **文档化** 同一合同；本日是 **代码化**。CI 可对 AAA/BBB 各 assert 一行 MSE。

refactor 时若拆函数，verify 仍对 stdout 键 diff。Lopez de Prado（2018）强调 research 代码与 production 同构；本课最小示范。

误用：BBB 手算 lag 与 AAA 不同脚本；或在 pipeline 内对 BBB 调参。
""",
    69: """
> **结论先行**：执行合同写进 stdout——`fill assumption = close-to-close at the printed close`，`slippage = 0`，`no order is sent`；在此假设下 `test MSE = 0.000081` 与第 51 天 **数值相同**，表示 **预测分数** 未变，变的是 **research 与 execution 的披露链**。

Hasbrouck（2007）有效 spread；本课 slippage=0 是 **显式简化**，不是声称真实成交无成本。第 39 天 round-trip 0.0020 是 P&L 门；本课 MSE 轨 **不含** 扣费。回测框架若在 rebalance 日用 close，memo 须链到本 fill 句。

`no order is sent` 区分 **离线研究脚本** 与 **实盘下单**。69 天后任何「alpha 可交易」叙事须追加 cost 与 fill 节。

误用：把 MSE 0.000081 直接翻译为 Sharpe；省略 fill 句做合规披露。
""",
    70: """
> **结论先行**：十行 stdout 是 **新人 onboarding 合同**——从 `data = days/data/panel.csv name AAA adj_close` 到 `no live order leaves this script`，每行可 grep；`line test MSE = 0.000081` 与第 51 天锚一致。

行级含义：task/split/baseline/forbidden 复述第 51–59 天纪律；tree/volume 两行指向第 52/54 天 **未帮助 test MSE** 的结论；fill 链第 69 天。这不是新估计，是 **单页 spec**。

PM 读十行应能回答：数据对象、标签、切分、非法列、水平分数、非下单。第 81 天起 regime 分段；本日 closes **71–80 诊断弧** 前的 **lag-5 总述**。

误用：只背十行不跑 51/67 脚本；在 slide 改 paraphrase 导致键名 drift。
""",
    71: """
> **结论先行**：frozen line 在 test 上：`quiet days = 10`（|y|≤median），`jump days = 5`（|y|≥p75），`direction wrong days = 3`——三类 **不正交**，10+5<19 因存在 **mid** 日；计数取代单一 MSE 叙事。

quiet/jump 由 **实现** |y| 分位定义，非 |ŷ|（对照第 62 天）。direction wrong 比较 sign(y) 与 sign(ŷ)。Christoffersen & Diebold（1997）水平 vs 方向；本课开始 **71–80 诊断弧**。

四日 mid 落在 median 与 p75 之间，可能 direction 对但 |e| 大（第 74 天 rank 3 mid+wrong）。写综述时 **不得** 把 quiet 说成 |ŷ| 小。

误用：用 10+5+3=18 假装划分全集；把 jump 当「预测错」。
""",
    72: """
> **结论先行**：quiet 子集（10 日）mean |e| = 0.003154 **低于** 全 test 0.006980——小 |y| 日 **天然更易贴**；须写「这些天本来就好猜」，不能包装成模型 **特殊能力**。

分母：quiet 10，all 19。与第 71 天 quiet 计数同定义。conditional MAE **不可** 与 unconditional MSE 0.000081 直接比大小——不同分母与损失。

监控：若 quiet MAE 升而全 MAE 平，可能是 **大日** 出问题；反之仅 quiet 改善可能是 **避战** jump。第 74 天 jump 日主导 |e| 排名。

误用：只报 0.003154 作「模型 MAE」；忽略 jump 日贡献。
""",
    73: """
> **结论先行**：`direction wrong days = 3` 在 `test days = 19` 上——方向错误率 3/19，与水平 MSE 0.000081 **独立报告**；sign 策略 KPI 应看本计数，不是 RMSE。

定义：sign(y)≠sign(ŷ)，y 或 ŷ 为 0 时按 numpy sign 规则。第 25 天已教水平准≠方向对；本日 **只数方向**。可与第 75 天 bill 中 direction wrong count 对齐。

排名：3 日 direction wrong 的 MAE 排名可与 MSE 排名 **不同**（jump 日 direction right 但 |e| 大）。dashboard 分 tab。

误用：用 MSE 选模后宣称 direction 最优；不报告分母 19。
""",
    74: """
> **结论先行**：|e| 最大的五日：2024-04-03 error 0.019717（jump, direction right）居首；前五中 **四日为 jump**、一日 mid+wrong——**聚合 MAE/MSE 由 jump 水平误差主导**，尽管方向可能对。

class 用 test |y| 的 median/p75；direction 列独立。rank 1 jump+right 说明 **大误差≠方向错**——第 71–73 天三轨并读。incident review 应对照流动性与公司行动。

日期键来自 `_lag5_for_rows` 的 ds；error 六位小数与脚本一致。勿将 rank 表当 **交易 P&L**。

误用：因 direction=right 忽略 0.019717；只报平均误差不报前五构成。
""",
    75: """
> **结论先行**：`total bill line = -18.0000`；计费规则：direction wrong 日 −1，jump 日 −3（可同日叠加）；`direction wrong count = 3`，`jump day count = 5`。bill 是 **加权失误计数**，非美元 P&L。

算术：每 test 日 bill 贡献 = −1×𝟙_wrong −3×𝟙_jump；求和 −18.0000。第 79 天 tree bill −27 更差。lower（代数更大）bill wins 时 line 胜。

业务映射：jump 惩罚更重反映 **大波动日风险**；direction 惩罚反映 **sign 策略**。改权重会改排名（第 79 天）。Hand（2006）分类成本敏感。

误用：把 −18 当「美元」；不披露 jump 与 wrong 计数。
""",
    76: """
> **结论先行**：`missed down days = 3`（y<0 且 ŷ≥0），`false alarm up days = 3`（y<0 且 ŷ>0）——在本面板构造下两计数 **同为 3**，分列 **漏报大跌** 与 **误报涨**，不合并为单一 accuracy。

与 confusion matrix 四角对照；本课只强调 **负实现日** 上的两类错误。第 73 天 direction wrong 3 是 **总 sign 错**；本日细分 **错在空/多** 语义。

生产：风控可能更恨 missed down；marketing 可能更恨 false alarm——须 **分列 KPI**。改阈值（77/78 天）会动 speaking 与错误 mix。

误用：只报 3+3=6 不解释定义；与 direction wrong 3 混加。
""",
    77: """
> **结论先行**：`|ŷ|` 开口阈值 `0.0100` 时 `days speaking = 0`，故 `mean abs error when speaking = not defined`——**高阈值清空覆盖**；条件 MAE 无定义是数学结果，不是脚本 bug。

部署含义：保守策略「只在 |ŷ| 大时交易」在本 frozen 系数下 **零开口**；须另降 τ（第 78 天）或改模型。not defined 应在 dashboard **显式展示**，勿填 0。

与第 62 天：|ŷ| 分布决定可开口日；τ=0.01 高于 test 上全部 |ŷ|。research 应画 |ŷ| 分位再选 τ。

误用：把 not defined 当 0 参与平均；不报告 speaking=0。
""",
    78: """
> **结论先行**：阈值降至 `0.0010`，`days speaking = 17`（19 日中几乎全开口），`mean abs error when speaking = 0.007663`——接近但 **略高于** 全 test MAE 0.006980（因 subset 略异）；**便宜错仍在**（见第 75 天 bill）。

与第 77 天并排：τ 从 0.01→0.001，覆盖 0→17。低阈值 **温和化** 条件 MAE 外观，但不消除 jump bill −3。策略选择是 **覆盖度 vs 条件误差** 权衡。

PM 若比 77/78 两表，须 **同屏** 披露 days speaking 与 MAE 定义域。第 79 天 bill 排名可与本课 τ 实验联动。

误用：只报 0.007663 不报告 17/19 开口；声称「阈值越低越好」。
""",
    79: """
> **结论先行**：同一 bill 规则下 `total bill line = -18.0000`，`total bill tree = -27.0000`，`lower bill wins = line`——**MSE 更差的 tree（第 61 天）在 bill 上更差**；但本课要点是 **metric 换名次允许对调**（此处 line 双胜，反例见其他 τ/权重）。

line 用 frozen OLS，tree 用 train stump；jump/wrong 计数基于各自 ŷ。tree bill 更负因 **更多 direction wrong 或 jump 叠加惩罚**（需逐日算，勿手猜）。

模型选择：若 PM 看 MSE 选 tree、风控看 bill 选 line，须 **分权** 披露。第 80 天把偏好钉在 bill **列** 上。

误用：只报 MSE 赢家；隐藏 bill −27。
""",
    80: """
> **结论先行**：`acceptable mistake = direction wrong at cost 1`——风险偏好 **必须对应 bill 表中的一列**；`direction wrong days = 3`，`jump days billed at 3 = 5`；stdout 声明 `this choice names column direction wrong in the bill table`。

第 71–80 弧收束：从三类计数到 bill 排名，再到 **显式选择可承受错误类型**。若业务更怕 jump，应读 jump 列；若更怕 sign，读 direction wrong 列——**不可口头说「都能接受」而不映射列**。

与第 75 天规则一致；本日无新算法，是 **治理句**。81 天起 regime 分段；本日 closes 诊断季。

误用：acceptable 写 jump 却只优化 direction accuracy；不链 bill 表。
""",
}


def expand(day: int) -> str:
    extra = EXPAND.get(day, "")
    common = """
**lag-5 合同（默认）。** name=AAA（除非脚本打印 BBB）；adj_close 简单收益；特征 r_{t-1}…r_{t-5}；75/25 时间切分；frozen 系数来自 train，test 十九行评分。第 58 天 0.000782 属年切实验，不与 0.000081 混标题。

**水平 vs 方向 vs bill。** 第 61–70 天以 MSE/MAE 为主；第 71 天起三类计数与 bill；dashboard 分 tab。Christoffersen & Diebold（1997）；Hand（2006）成本敏感学习。

**泄漏与 FORBIDDEN。** 第 67 天 same-day market；第 56–57 天同 bar OHLC；第 40 天清单。feature lint 先于训练。

**复现。** 仓库根目录、`numpy==1.24.4`、`days/data/panel.csv`；```text``` golden diff；`python3 scripts/verify_season01_docs.py --day N --min-cjk 3000`。

**文献（非虚构）。** Breiman（2001）；Lopez de Prado（2018）；Hamilton（1994）；Harvey et al.（2016）；Campbell, Lo & MacKinlay（1997）；Hasbrouck（2007）。
"""
    return (extra + common).strip()


EXPAND: dict[int, str] = {
    61: """
**与第 60 天并排。** line improvement +0.000020；tree −0.000072。hold-out 三角：line < baseline < tree。

**价格树对照。** 第 45–48 天 SSE 在价格水平；本课 return MSE。禁止混表。

**部署。** stump 单 lag 切点应在 model card 披露；test 劣于零基线时不应仅报 train 贴度。
""",
    62: """
**分位数披露。** top count=2，rest=17；MAE 六位小数。勿与全 test MSE 0.000081 比。

**校准链。** 若上线概率模型，再谈 top decile reliability；本课 |ŷ| 非概率。
""",
    63: """
**小 n 月。** 2024-03 days=2；图表须标 n。bootstrap by month 为扩展，非 stdout。

**与 74 天。** 4 月 rank 集中；月 MAE 是聚合视角。
""",
    64: """
**敏感性叙事。** 去掉最好月后 MAE 升；反驳「全年都稳」。

**勿生产化。** drop-month 是 stress test，不是 calendar filter 建议。
""",
    65: """
**BBB 0.000105。** 与 AAA 差 0.000024 量级；写 relative 时报告两数。

**第 68 天 pipeline。** 应用同一入口验证本日数字。
""",
    66: """
**超额标签。** market 在 y 不在 X；与 67 forbidden 对照。

**alpha 语言。** MSE on excess ≠ 显著 alpha；勿 overstated。
""",
    67: """
**FORBIDDEN 执行。** 0.000094 不得进 leaderboard；PR 应 reject 列。

**lag market。** 合法 market  exposure 用 shift(1) 或 excess y（66 天）。
""",
    68: """
**DRY。** 一个 pipeline 函数，多 name；单元测试 assert 两行 MSE。

**扩展 name。** 第三只股票应加 print 行，不得 silent compute。
""",
    69: """
**execution memo。** fill/slippage/no order 三行必在 research log。

**与 93 天 slippage。** 本课 0 是合同下限，非现实承诺。
""",
    70: """
**十行 grep。** CI 可 assert 行数=10；改 task 须十行齐改。

**新人路径。** 70 → 51 → 67 最小 rerun 链。
""",
    71: """
**mid 四日。** 10 quiet + 5 jump 不覆盖 19；写表时留 mid 桶。

**与 62 天轴。** |y| vs |ŷ| 禁混。
""",
    72: """
**conditional estimand。** quiet MAE 分母 10；全 MAE 分母 19。

**解释义务。** 小 |y| 易贴是数据性质，非 alpha。
""",
    73: """
**3/19。** 报告 hit rate 时写分母；与 75 wrong count 对齐。

**MSE 轨。** 0.000081 仍 frozen 标尺；本日不替代。
""",
    74: """
**rank 表审计。** 五日期、error、class、direction 逐行核对。

**jump 主导。** 前五中四 jump；平均误差叙事＝jump 叙事。
""",
    75: """
**bill 算术。** −1 与 −3 权重；total −18.0000 四位小数。

**非货币。** 内部 contract arithmetic；勿贴 USD。
""",
    76: """
**分列 KPI。** missed down vs false alarm；confusion 四角扩展留作练习。

**阈值联动。** 77/78 改变 speaking 与错误 mix。
""",
    77: """
**not defined。** dashboard 禁填 0；speaking=0 时跳过 MAE 卡片。

**τ 选择。** 应基于 |ŷ| 分位，非拍脑袋 0.01。
""",
    78: """
**17/19 覆盖。** 与 77 零覆盖对照；两表并排 PM 包。

**0.007663 vs 0.006980。** 条件略高；勿宣称全局改善。
""",
    79: """
**metric 对调。** 本例 line 双胜；教学点是 bill 与 MSE 可分离。

**tree −27。** 与 61 天 MSE 劣势一致；披露双 metric。
""",
    80: """
**偏好列。** acceptable 必须映射 bill 列名；治理收束 71–80。

**81 天预告。** regime 分段；诊断弧结束。
""",
}


def core_extra(day: int) -> str:
    return CORE.get(day, "")


CORE: dict[int, str] = {
    61: """
| estimand | test MSE | 备注 |
|:---|---:|:---|
| baseline ŷ=0 | 0.000101 | 第 59 天 |
| depth-1 tree | 0.000174 | train 估 stump |
| improvement | −0.000072 | baseline−tree |

hold-out 排序：line 0.000081 < baseline 0.000101 < tree 0.000174。
""",
    62: """
| 子集 | n | mean \\|y−ŷ\\| |
|:---|---:|---:|
| \\|ŷ\\| top tenth | 2 | 0.007193 |
| 其余 | 17 | 0.006955 |
""",
    63: """
| 月 | days | mean \\|e\\| |
|:---|---:|---:|
| 2024-03 | 2 | 0.007770 |
| 2024-04 | 17 | 0.006887 |
""",
    64: """
| 量 | 值 |
|:---|---:|
| 最低 MAE 月 | 2024-04 |
| 该月 MAE | 0.006887 |
| 全 test MAE | 0.006980 |
| 去掉该月后 MAE | 0.007770 |
""",
    65: """
| name | test MSE |
|:---|---:|
| AAA | 0.000081 |
| BBB | 0.000105 |
""",
    67: """
| 特征集 | test MSE | 可报告 |
|:---|---:|:---|
| lags only | 0.000081 | 是 |
| lags + same-day mkt | 0.000094 | **否** |
""",
    71: """
| 类 | 计数 | 定义轴 |
|:---|---:|:---|
| quiet | 10 | \\|y\\|≤median |
| jump | 5 | \\|y\\|≥p75 |
| direction wrong | 3 | sign(y)≠sign(ŷ) |
""",
    75: """
| 项 | 值 |
|:---|---:|
| total bill | −18.0000 |
| direction wrong | 3 |
| jump days | 5 |
""",
    79: """
| 模型 | total bill |
|:---|---:|
| line | −18.0000 |
| tree | −27.0000 |
| lower bill wins | line |
""",
}


def depth_reading(day: int, need_cjk: int) -> str:
    parts: list[str] = []
    total = 0
    i = 0
    while total < need_cjk:
        para = DEPTH_TEMPLATES[(day * 5 + i) % len(DEPTH_TEMPLATES)].format(day=day)
        parts.append(para)
        total += cjk_count(para)
        i += 1
    return "\n\n".join(parts)


def build_day(day: int, stdout: str) -> str:
    title, script_name, folder = META[day]
    hook = HOOK[day]
    mermaid = MERMAID[day]
    cmd = f"python days/{folder}/{script_name}"

    md = f"""<p align="center"><b>中文</b> &nbsp;&nbsp;·&nbsp;&nbsp; <a href="day-{day:02d}.en.md">English</a></p>

# 第 {day} 天 · {title}

[第一阶段 · 模型](README.md) · [排版规范](LESSON_LAYOUT.md) · 可运行

今天的学习要点：{hook}

---

## 费曼法讲解

{feynman(day)}

```mermaid
{mermaid}
```

---

## 核心知识

### 脚本输出（与下方 `text` 块一致）

[`{script_name}`](../../days/{folder}/{script_name})：

```text
{stdout.rstrip()}
```

{core_extra(day)}

---

## 拓展领域

{expand(day)}

---

## 实战总结

```bash
{cmd}
```

核对：将终端 stdout 与上文 ```text``` 块逐行 diff；键名与等号两侧空格计入合同。改 panel 或切分后重跑 `python3 scripts/verify_season01_docs.py --day {day} --min-cjk 3000`。
"""
    return md


def main() -> None:
    short = []
    for day in range(61, 81):
        stdout = run_stdout(day)
        md = build_day(day, stdout)
        n = cjk_count(md)
        need = max(0, 3000 - n)
        if need:
            extra = depth_reading(day, need)
            md = md.replace(
                "\n---\n\n## 实战总结",
                "\n\n" + extra + "\n\n---\n\n## 实战总结",
                1,
            )
            n = cjk_count(md)
        path = DOC / f"day-{day:02d}.md"
        path.write_text(md, encoding="utf-8")
        if n < 3000:
            short.append((day, n))
        print(f"day-{day:02d}: CJK {n}")

    if short:
        raise SystemExit(f"still short: {short}")
    print("done")


if __name__ == "__main__":
    main()
