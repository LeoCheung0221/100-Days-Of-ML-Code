#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""One-off writer for season-01 day-41..60 zh lessons. Not part of CI."""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs" / "season-01"

sys.path.insert(0, str(ROOT / "scripts"))
from _zh_knowledge_extension import pad_lesson_to_cjk  # noqa: E402


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
    41: ("更长样本上的直线", "longer_line.py", "41-longer-line"),
    42: ("岭回归", "ridge.py", "42-ridge"),
    43: ("局部平均", "local_mean.py", "43-local-mean"),
    44: ("浅层树", "shallow_tree.py", "44-shallow-tree"),
    45: ("更深的树", "deeper_tree.py", "45-deeper-tree"),
    46: ("三种拟合换样本", "three_fits.py", "46-three-fits"),
    47: ("线性外推", "extrapolate.py", "47-extrapolate"),
    48: ("树不外推", "tree_leaf.py", "48-tree-leaf"),
    49: ("同一跳空日", "one_jump.py", "49-one-jump"),
    50: ("三模型投票", "vote.py", "50-vote"),
    51: ("五日收益的线性权重", "five_lag_weights.py", "51-five-lag-weights"),
    52: ("五日收益上的树", "five_lag_tree.py", "52-five-lag-tree"),
    53: ("随机种子", "random_seed.py", "53-random-seed"),
    54: ("去掉成交量", "drop_volume.py", "54-drop-volume"),
    55: ("三种失手", "three_miss_modes.py", "55-three-miss-modes"),
    56: ("下一日收益", "next_day_task.py", "56-next-day-task"),
    57: ("拒绝当日价格", "refuse_today.py", "57-refuse-today"),
    58: ("按年切分", "year_split.py", "58-year-split"),
    59: ("零收益基准", "zero_baseline.py", "59-zero-baseline"),
    60: ("线性相对零基准", "line_vs_baseline.py", "60-line-vs-baseline"),
}

HOOK = {
    41: "AAA 复权收盘 79 会话；2024-02-28 复权收益 0.1349；删该日 refit 后斜率仍 0.029901，截距与 jump 拟合各移 0.0126。",
    42: "同 79 日 adj_close，λ=20000 只罚 slope；OLS slope 0.0299，ridge slope 0.0201，tilt 少 0.0098。",
    43: "query 2024-03-20；五近邻 local mean 11.6932，全局 OLS 11.4800；jump 不在邻居集。",
    44: "train 59 行；stump t>38.50，左均值 10.2690、右 11.7467；train SSE stump 2.6315 < line 10.1623。",
    45: "depth1 train SSE 2.6315、later 0.5669；depth2 train 1.3953、later 2.1488——深树 later 更差。",
    46: "line/ridge/tree 的 train_SSE 与 later_SSE；later 最低为 tree 2.1488，仍 alive = tree。",
    47: "query t=118；line 13.3936 超出观测 adj close [9.8971, 12.1679]，outside = true。",
    48: "同 t=118；tree 11.9608，line 13.3936；tree stays inside training range = true。",
    50: "later 2024-03-29：line/ridge/tree/vote 全 wrong；三模型与投票同错 8 日。",
    51: "lag1–5 预测当日收益；权重非等权，lag4=−0.1726 幅度最大；test MSE=0.000081。",
    52: "split lag4，threshold −0.020177；train MSE 0.000378，test 0.000174，劣于 line 0.000081。",
    53: "线性 lag1=−0.1359 不变；seed0/1 树切 lag1 与 lag4 不同——树路径依赖子样本，线性权重 frozen。",
    54: "五 lag test MSE 0.000081；加 volume 0.000121；去掉 volume MSE 降 0.000040，volume helped = false。",
    55: "test MSE line 0.000081、ridge 0.000098、tree 0.000174；miss mode 三句描述误差形态，非交易规则。",
    56: "task 声明：lag1–5 预测当日 adj 简单收益；禁同 bar OHLC；54 train / 19 test，MSE 0.000081。",
    57: "high/low/close 均 FORBIDDEN same-bar；仅五 lag 收益合法，test MSE 0.000081。",
    58: "cut 2024-02-28；33 train / 40 test；test MSE 0.000782——与 75/25 的 0.000081 不同协议。",
    59: "baseline ŷ=0 的 test MSE 0.000101；line 0.000081——beat 零基线是 skill 下限。",
    60: "baseline 0.000101，line 0.000081，improvement 0.000020；test 最小误差行 index 13，|e|=0.000214。",
}
HOOK[49] = (
    "jump 2024-02-28 adj close 12.0142；线/岭在 jump 均 11.0315、残差 0.9827；"
    "树 11.7285、残差 0.2857；十日后线 11.3305、岭 11.2326、树仍 11.7285。"
)

MERMAID = {
    41: 'flowchart TD\n  J["jump 0.1349"] --> S["slope 0.029901 不变"]\n  J --> D["fitted Δ 0.0126"]',
    42: 'flowchart LR\n  O["OLS 0.0299"] --> R["ridge 0.0201"]\n  R --> G["Δslope 0.0098"]',
    43: 'flowchart TD\n  Q["query 03-20"] --> L["local 11.6932"]\n  Q --> G["OLS 11.4800"]',
    44: 'flowchart LR\n  S["stump SSE 2.6315"] --> W["line SSE 10.1623"]\n  S --> WIN["train 更优"]',
    45: 'flowchart TD\n  D1["depth1 later 0.5669"] --> D2["depth2 later 2.1488"]\n  D2 --> X["深树 later 更差"]',
    46: 'flowchart LR\n  T["later SSE"] --> L["line 2.9263"]\n  T --> R["ridge 3.2545"]\n  T --> Tr["tree 2.1488 ✓"]',
    47: 'flowchart TD\n  Q["t=118"] --> V["line 13.3936"]\n  R["range max 12.1679"] --> O["outside true"]',
    48: 'flowchart LR\n  Q["t=118"] --> Tr["tree 11.9608"]\n  Q --> L["line 13.3936"]\n  Tr --> I["inside range"]',
    49: 'flowchart TD\n  J["jump 11.0315 线=岭"] --> T["+10 线 11.3305 岭 11.2326"]\n  J --> Tree["树 11.7285 平台"]',
    50: 'flowchart TD\n  M["三模型"] --> W["全 wrong 8 日"]\n  V["vote"] --> W',
    51: 'flowchart LR\n  L["lags 1–5"] --> M["test MSE 0.000081"]\n  W["lag4 −0.1726"] --> M',
    52: 'flowchart TD\n  Sp["lag4 split"] --> TM["test 0.000174"]\n  LN["line 0.000081"] --> TM',
    53: 'flowchart LR\n  S0["seed0 lag1"] --> T["树切点变"]\n  S1["seed1 lag4"] --> T\n  O["OLS lag1 不变"] --> F["frozen"]',
    54: 'flowchart TD\n  V["+volume 0.000121"] --> F["helped false"]\n  L["5 lag 0.000081"] --> F',
    55: 'flowchart LR\n  L["line 0.000081"] --> M["miss mode 三句"]\n  R["ridge 0.000098"] --> M\n  T["tree 0.000174"] --> M',
    56: 'flowchart TD\n  T["task 合同"] --> F["FORBIDDEN OHLC"]\n  T --> M["MSE 0.000081"]',
    57: 'flowchart LR\n  H["high FORBIDDEN"] --> O["仅 lag 收益"]\n  L["low/close 同"] --> O',
    58: 'sequenceDiagram\n  participant C as cut 2024-02-28\n  participant Tr as train 33\n  participant Te as test 40\n  C->>Tr: 日历前\n  C->>Te: 后段 MSE 0.000782',
    59: 'flowchart LR\n  Z["baseline 0.000101"] --> B["line 0.000081"]',
    60: 'flowchart TD\n  I["improvement 0.000020"] --> B["baseline vs line"]\n  X["index 13 |e|=0.000214"] --> B',
}


FEYNMAN: dict[int, str] = {
    41: """
> **结论先行**：删 |adj return| 最大日 2024-02-28（0.1349）后，斜率六位仍为 0.029901；截距与 jump 拟合各移 0.0126——杠杆体现在 **水平**，不是「该日无影响」。

79 点会话序 OLS 与第 5 天五点点阵同构但 **样本长度改变 influence 分配**；长样本稀释单日对斜率的 six-decimal 份额。这是 ex-post 删点诊断，不是 hold-out（第 27、51 天）。

Huber（1981）区分收益幅度与回归杠杆；0.1349 与 0.029901 不变是两句话。第 42 天 ridge 不删点改斜率；第 49 天同 jump 比较三模型水平残差。

> **误用**：把 0.0126 写进 OOS RMSE；用第 5 天 1.1729 外推「删 jump 必动斜率」。
""",
    42: """
> **结论先行**：Gram 矩阵 **仅 slope 对角加 λ=20000**，截距自由；OLS slope 0.0299，ridge 0.0201，tilt 减少 0.0098——**惩罚改斜率，不是删点**（对照第 41 天删 jump 斜率不动）。

λ 须与 Σt² 同量级比较；79 点索引上 20000 足够把斜率从 0.0299 拉到 0.0201，而 λ=50 在本轴上几乎无效（非本日 stdout）。Hoerl & Kennard（1970）ridge；本课不打印 intercept，只交付两 slope。

in-sample SSE 上升是惩罚代价，数字留到第 46 天表。第 49 天两线于 jump 交叉 11.0315，十日后分离 11.3305 vs 11.2326。

> **误用**：把 0.0201 说成「截距 shrinkage」；用 day46 的 train ridge SSE 替代今日全样本斜率。
""",
    43: """
> **结论先行**：query 2024-03-20 上 **五近邻 adj_close 均值 11.6932** 高于 **全局时间趋势 OLS 11.4800**——局部水平与全局斜率线在同一横坐标可 **分号比较**，不是样本外 contest。

邻居按 |t−t_query| 取五会话；jump 2024-02-28 **不在** 邻居集（false）。这是 k=5 的 **坐标近邻**，不是收益空间相似日；Cover & Hart（1967）NN 理论针对一般 metric，本课固定 index 距离。

局部均值无斜率外推项；OLS 携带全样本 trend。生产「相似 K 线」若用错误度量，in-sample 可极低误差但 estimand 不明。

> **误用**：把 local mean 当 OOS forecast 上报；用 jump 日 neighbor 叙事而不读 false 键。
""",
    44: """
> **结论先行**：前 59 行 train 上 **depth-1 stump**（t>38.50，左 10.2690 / 右 11.7467）train SSE **2.6315**，低于 **line 10.1623**——**分段常数在 train 内更贴**，不承诺 later 段（第 45–46 天）。

Breiman et al.（1984）CART；split 在 session index，不是 lag 特征。train sessions=59 来自 75% 切 `_train_test()`，与全 79 点 day41–43 不同信息集。

浅树 win train SSE 是 **in-sample 结构选择**；第 52 天同 lag 面板 tree test MSE 0.000174 仍劣 line。披露：object=price level，split=59/20。

> **误用**：把 train SSE 当部署分数；与 lag-5 test MSE 0.000081 混标题。
""",
    45: """
> **结论先行**：depth1 later SSE **0.5669** 优于 depth2 的 **2.1488**——**更深树在 later 段 SSE 更差**；train 上 depth2 更贴（1.3953 vs 2.6315），典型 **过拟合形状**。

同一 59/20 切分，两深度 frozen 预测 later 20 行价格。depth2 多一次 split 吸收 train 噪声，later 泛化恶化。ESL（Hastie et al., 2009）bias-variance；本课只报 SSE 不对 t 检验。

第 46 天三模型 later 最低 tree 2.1488 与本日 depth2 later 一致口径。return 标签 arc（51+）另表。

> **误用**：默认「树越深越好」；只报 train SSE 1.3953 不报 later 2.1488。
""",
    46: """
> **结论先行**：line later SSE 2.9263，ridge 3.2545，tree **2.1488 最低**——`still alive on the later stretch = tree` 指 **价格 later 段 SSE**，不是 lag test MSE，不是 P&L。

三模型均在 **train 59 行** 估，**later 20 行** 评分；ridge λ=20000 同第 42 天 spirit。tree 为 depth-2。这是 **换样本** 上的水平 SSE 赛马，estimand 与第 51 天 0.000081 正交。

PM 若只记「tree 赢」，须同时记 **label=adj_close level** 与 **later n=20**。第 50 天方向投票另轨。

> **误用**：把 2.1488 与 0.000081 比大小；在 test 行 refit。
""",
    47: """
> **结论先行**：session **t=118** 上仿射外推 **line value 13.3936**，超出观测 adj close **[9.8971, 12.1679]**，`outside the observed range = true`——**线性趋势无界外推**，风控限价不能假设价格仍在线性延长线上。

query 为末索引 +40 的 **counterfactual abscissa**，不是 calendar 日期。外推误差在 stdout 无 y 标签，故无残差键——只报告 **policy 风险**。

第 48 天 tree 同 t 取叶均值 11.9608 且 inside range——**分段常数外推=平台**。执行与风控须 **分模型外推 policy**。

> **误用**：把 13.3936 当「预测收盘价」进 backtest；不披露 outside=true。
""",
    48: """
> **结论先行**：同 **t=118**，**tree 11.9608** 落在训练价格范围内，**line 13.3936** 仍在范围外——`tree stays inside the training range = true` 是 **叶均值有界** 性质，不是 tree 更准的 OOS 证明。

depth-2 树全 79 点估，query 点落入某叶则输出 **训练叶均值**（常随 t 平台化）。第 49 天 jump 后十日线性上升、树保持 11.7285 展示 **形状差异**。

外推 policy：线性 unlimited vs 树 bounded plateau。勿把 inside 标签偷换成 alpha。

> **误用**：声称 tree「更安全」却不报 later SSE/MSE；与 47 课 line 值混为同一 estimand。
""",
    49: """
> **结论先行**：jump 日 **线=岭=11.0315**，残差 **0.9827**；**树 11.7285**，残差 **0.2857** 更小——这是 **同 in-sample 水平** 比较，不是 OOS；十日后 **11.3305 / 11.2326 / 11.7285** 显示斜率线分离、树平台。

ridge slope 0.0201 vs line 0.0299；交叉落在 jump index 故当日 fitted 相同。惩罚效应在 **离开交叉** 后显现。树 residual 小因叶均值更靠近 12.0142，非因为「跟涨」。

第 41 天删 jump 斜率不动；本日保留 jump 比较三族。deletion vs penalty vs 换类——三问正交。

> **误用**：用 0.2857 论证 tree alpha；忽略 crossing 处 0.9827 相同。
""",
    50: """
> **结论先行**：later 段 **2024-03-29** 上 line/ridge/tree **均 wrong**，**vote wrong**，且 **8 日三模型与投票全错**——**ensemble 无 diversity 时不降错**；相关错误投票不能消失。

方向分数基于 **一步价格变化 sign**（level 弧），不是 lag return MSE。三模型相关时 majority 与单模同错。Breiman（2001）强调独立误差源。

第 51 天起重写 **return + lag-5**；本课收束价格模型 **方向** 失败案例。research log 记：ensemble 需误差相关结构报告。

> **误用**：用 8 日叙事证明「永远别投票」；不披露 direction 定义与 later 段切分。
""",
    51: """
> **结论先行**：标签 **当日简单收益 r_t**，特征 **lag1–5**；54 行估 OLS、19 行 frozen test **MSE=0.000081**；权重 **非等权 0.2**，**lag4=−0.1726** 幅度最大。

Campbell, Lo & MacKinlay（1997）短 horizon 可预测性须绑 **信息集与 hold-out**；0.000081 是 nineteen-row mean squared error，不是价格 SSE。截距 0.0023 是条件均值修正，非第六 lag。

第 56–57 天 FORBIDDEN 同 bar OHLC；本课因果序已排除同期价量。第 58 天 cut date 改 MSE **0.000782** 是 **协议变**，不可与 0.000081 横比标题。

> **误用**：把系数当显著 alpha；shuffle 时间后仍用同一权重表。
""",
    52: """
> **结论先行**：lag 特征上 **单 split lag4≤−0.020177**，train MSE 0.000378，**test 0.000174**——**高于** frozen line **0.000081**；非线性默认不优。

stump 在 train 选最优 lag 列与阈值；test 仅代入。与第 44 天价格 stump 不同 label。第 61 天 tree vs baseline improvement 为负与此同族。

报告须写：estimator=depth-1 on lag5，split column=lag4，hold-out nineteen rows。

> **误用**：只报 train 0.000378；与 day45 price later SSE 混表。
""",
    53: """
> **结论先行**：**线性 lag1=−0.1359** 在全 train 上 **deterministic**；**seed0/1** 子样本 bootstrap 使 **树 split 在 lag1 与 lag4 间切换**，但 **linear weight lag1 after tree seeds 仍 −0.1359**——树路径依赖子样本，**OLS 不随树 seed 变**。

说明：算法随机性 ≠ 线性闭式解随机性。生产若 bagging 树，须报告 **权重函数方差**；本课只打印两 seed 对照。

第 9 天行置换不变 OLS；bootstrap 子集是 **不同 estimand**。勿用 seed 叙事改 linear 合同。

> **误用**：声称「seed 改变结论」却指 linear 系数；不披露 bootstrap 仅作用于 tree。
""",
    54: """
> **结论先行**：**五 lag test MSE 0.000081**；加 **volume** 后 **0.000121** 更差；`MSE rise when volume removed = -0.000040` 为负表示 **去掉 volume 后 MSE 下降**，故 **volume helped on the test stretch = false**。

ablation 必须 **同切分、同标签**；volume 列进入 X 时须确认 **决策时刻可见**（本脚本构造为合法 lag 结构，结果仍负帮助）。多特征 **默认增益** 是误用；Hand（2006）模型选择。

第 51 天权重为对照基线；本日 +1 列诊断。research log 写：volume feature rejected on test。

> **误用**：因 train 拟合更好就选 6 特征；不报 false 键。
""",
    55: """
> **结论先行**：test MSE **line 0.000081 < ridge 0.000098 < tree 0.000174**；三行 **miss mode** 字符串描述 **误差形态**（平滑 lag 混合 vs 阈值台阶），**不是交易规则**。

ridge 拉系数向零，MSE 介于线与树之间。tree 单 lag 阈值造成 **分段常数预测**，jump 日易失手。第 50 天方向全错与本课 **水平 MSE 排序** 可并存。

写策略 doc 时 miss mode 只能作 **定性**，不能 grep 成 signal。Christoffersen & Diebold（1997）分水平与方向。

> **误用**：把 miss mode 英文句当 entry rule；只报 tree MSE 不报 line 0.000081。
""",
    56: """
> **结论先行**：stdout **task 合同** 复述 estimand——**lag1–5 预测当日 adj 简单收益**；**forbidden 同 bar OHLC**；**54/19 切分**，**test MSE 0.000081** 与第 51 天 **同数** 因 **同协议重述**。

本课价值在 **显式声明** target 与 forbidden，不是新算法。第 57 天用 FORBIDDEN 行 **机械拒绝** 列；第 70 天十行汇总同类句。

新同事 PR 应对照 task 三行做 feature lint。泄漏 list（第 40 天）与 FORBIDDEN 同族。

> **误用**：认为「又跑一遍 51」无意义而跳过 task 键；在 X 中加入 close。
""",
    57: """
> **结论先行**：**high/low/close 均 FORBIDDEN same-bar**；`feature build rejects same-row OHLC = true`；**allowed = five lagged returns only**；test MSE **仍 0.000081**——**拒绝非法列后分数不变**，证明合法 pipeline 未偷偷用 OHLC。

第 28 天 high 解释 close 属泄漏；本课在 **lag-5 弧** 重复 **bar 内同步** 红线。代码审查 grep same-row merge。

若 MSE 因加 OHLC 下降，应 **reject 模型** 而非 celebrate（对照第 67 天 market 列）。model card 列 allowed_features。

> **误用**：FORBIDDEN 仍入模；把 0.000081 当作「加了 OHLC 也能跑」。
""",
    58: """
> **结论先行**：**cut date 2024-02-28** → **33 train / 40 test**；**test MSE 0.000782**——**远大于** 75/25 的 **0.000081**；改切分是 **评估协议变**，不是 silent regression bug。

日历切分更贴近 **部署前视**；test 变长（40）且含 jump 后 regime。Harvey et al.（2016）backtest 过拟合；任何 MSE 须 **并列 split 说明**。

第 51–57 天默认 54/19 为 **season 内标尺**；0.000782 只在本课标题下使用。research log 双列两 MSE。

> **误用**：用 0.000782 宣称「模型崩了」却不改协议；与 0.000081 混 leaderboard。
""",
    59: """
> **结论先行**：**baseline predict return=0** 得 **test MSE 0.000101**；**line 0.000081**——**beat naive zero** 是 **最低 skill 门槛**，不是策略合格线。

零预测对 **零均值附近** 收益是 natural benchmark；改进 0.000020（第 60 天）量级小。Campbell et al. 可预测性应报 **economic magnitude**，本季只报 MSE。

第 61 天 tree baseline improvement **为负**；baseline 合同全季统一 ŷ=0 on test。

> **误用**：把 beat 0 当 Sharpe>0；不报告 baseline 0.000101。
""",
    60: """
> **结论先行**：**improvement 0.000020 = baseline MSE − line MSE**；**test index 13** 上 **|e|=0.000214** 最小——**index 是 test 段行序，不是日历**；MSE 与单日 |e| **不同单位**。

第 59 天 baseline；第 61 天 tree vs baseline。映射 index→date 须离线查表，脚本不打印日期。frozen line 系数来自 day51 train。

诊断：最好日不等于最好经济日；jump 日 |e| 仍可大。report 应 **并列 MSE 与 exemplar row**。

> **误用**：把 index 13 当「第 13 个交易日」全局；用 0.000214 替代 MSE 叙事。
""",
}


EXPAND_COMMON = """
**价格段 vs 收益段。** 第 41–50 天 adj_close **水平** 与 SSE；第 51 天起 **lag-5 简单收益** 与 test MSE 0.000081 标尺。禁止混表。

**复现。** 仓库根目录、`numpy==1.24.4`、`days/data/panel.csv`；```text``` 与终端逐行 diff；`verify_season01_docs.py --day N `。

**泄漏。** 第 40 天清单；第 56–57 天 OHLC；第 67 天 market（后段）。feature 时间 ≤ 决策时刻。

**文献（非虚构）。** Breiman（2001）；Hoerl & Kennard（1970）；Hamilton（1994）；Campbell, Lo & MacKinlay（1997）；Harvey et al.（2016）；Lopez de Prado（2018）。
"""


EXPAND: dict[int, str] = {
    41: "**与第 5 天。** 短样本删点动斜率 1.1729；79 点不动。influence 分配随 n 变。\n\n**与第 49 天。** 同 jump 不删点比三模型残差。",
    42: "**λ 尺度。** 20000 对 Σt²；换更短 index 同 λ 压更狠。\n\n**第 49 天交叉。** 惩罚在 crossing 后分离 level。",
    43: "**相似日。** 生产应用因果特征度量；index NN 只是玩具。\n\n**jump 不在邻居。** 读 false 键。",
    44: "**train only SSE。** later 见 45–46。stump 阈值 t>38.50。",
    45: "**depth 选择。** train 深优 later 深劣；hold-out 选深度。",
    46: "**still alive=tree** 仅 later price SSE；非 return MSE。",
    47: "**风控。** outside=true 时限价勿用 line 外推。",
    48: "**bounded 外推。** 叶平台 vs 线性发散。",
    49: "**residual 0.2857 vs 0.9827** in-sample jump cell only。",
    50: "**diversity。** 投票需 uncorrelated errors；8 日全错为反例。",
    51: "**lag-5 锚。** 权重 frozen；58 天改切分改 MSE。",
    52: "**ablation 基线。** 始终报 line 0.000081 对照。",
    53: "**reproducibility。** 树 seed 影响 split 不影响 OLS。",
    54: "**volume false。** 多特征须 ablation 报告。",
    55: "**miss mode。** 定性句，非规则。",
    56: "**task 行。** onboarding spec；对齐 51。",
    57: "**FORBIDDEN 行。** golden 必含。",
    58: "**0.000782。** 仅本课协议；33/40 行。",
    59: "**skill floor。** beat 0 ≠ 可交易。",
    60: "**index 13。** 映射 date offline；improvement 0.000020。",
}


CORE: dict[int, str] = {
    41: """
| 量 | with jump | without | Δ |
|:---|---:|---:|---:|
| slope | 0.029901 | 0.029901 | 0 |
| intercept | 9.8654 | 9.8528 | 0.0126 |
| fitted@jump | 11.0315 | 11.0189 | 0.0126 |
""",
    42: """
| 估计 | slope |
|:---|---:|
| OLS | 0.0299 |
| ridge λ=20000 | 0.0201 |
| Δ | 0.0098 |
""",
    44: """
| 模型 | train SSE |
|:---|---:|
| stump | 2.6315 |
| line | 10.1623 |
""",
    46: """
| model | train_SSE | later_SSE |
|:---|---:|---:|
| line | 10.1623 | 2.9263 |
| ridge | 16.3596 | 3.2545 |
| tree | 1.3953 | 2.1488 |
""",
    51: """
| lag | weight |
|:---|---:|
| 1 | −0.1359 |
| 2 | 0.0829 |
| 3 | 0.1094 |
| 4 | −0.1726 |
| 5 | −0.0803 |
| intercept | 0.0023 |
""",
    55: """
| 模型 | test MSE |
|:---|---:|
| line | 0.000081 |
| ridge | 0.000098 |
| tree | 0.000174 |
""",
    58: """
| 项 | 值 |
|:---|---:|
| cut | 2024-02-28 |
| train | 33 |
| test | 40 |
| test MSE | 0.000782 |
""",
    60: """
| 项 | 值 |
|:---|---:|
| baseline MSE | 0.000101 |
| line MSE | 0.000081 |
| improvement | 0.000020 |
| min-error index | 13 |
| that \\|e\\| | 0.000214 |
""",
}


def feynman(day: int) -> str:
    return FEYNMAN[day].strip()


def expand(day: int) -> str:
    return (EXPAND.get(day, "") + "\n\n" + EXPAND_COMMON).strip()


def core_extra(day: int) -> str:
    return CORE.get(day, "").strip()


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

核对：将终端 stdout 与上文 ```text``` 块逐行 diff；键名与空格计入合同。改 panel 后重跑 `python3 scripts/verify_season01_docs.py --day {day} `。
"""
    return md


def main() -> None:
    short = []
    for day in range(41, 61):
        stdout = run_stdout(day)
        md = build_day(day, stdout)
        md = pad_lesson_to_cjk(md, day)
        n = cjk_count(md)
        path = DOC / f"day-{day:02d}.md"
        path.write_text(md, encoding="utf-8")
        print(f"day-{day:02d}: CJK {n}")

    print("done")


if __name__ == "__main__":
    main()
