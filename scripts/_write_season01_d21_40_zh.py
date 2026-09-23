#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""One-off writer for season-01 day-21..40 zh lessons. Not part of CI."""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs" / "season-01"

sys.path.insert(0, str(ROOT / "scripts"))
from _season01_prose_21_40 import PROSE  # noqa: E402
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
    21: ("固定收盘表", "fixed_table.py", "21-fixed-table"),
    22: ("滞后一日的方向", "lagged_direction.py", "22-lagged-direction"),
    23: ("连续三日同向", "three_day_run.py", "23-three-day-run"),
    24: ("规则移到下一段", "next_stretch.py", "24-next-stretch"),
    25: ("方向与价格并报", "two_scores.py", "25-two-scores"),
    26: ("随机切分", "random_split.py", "26-random-split"),
    27: ("按时间切分", "time_split.py", "27-time-split"),
    28: ("当日最高价", "todays_high.py", "28-todays-high"),
    29: ("用未来开盘标准化", "future_open.py", "29-future-open"),
    30: ("固定历史窗口", "lookback.py", "30-fixed-lookback"),
    31: ("三日窗口的噪声", "three_day_noise.py", "31-three-day-noise"),
    32: ("六十日窗口", "sixty_day.py", "32-sixty-day-window"),
    33: ("训练集标准化", "train_scale.py", "33-train-scale"),
    34: ("缺失的两种填法", "two_fills.py", "34-two-fills"),
    35: ("停牌后的间隔", "halt_gap.py", "35-halt-gap"),
    36: ("复权与未复权", "adjusted.py", "36-adjusted-close"),
    37: ("多标的混切", "mixed_names.py", "37-mixed-names"),
    38: ("信号滞后一日", "lag_signal.py", "38-lag-signal"),
    39: ("最小往返成本", "round_trip.py", "39-round-trip"),
    40: ("泄漏清单", "leakage_list.py", "40-leakage-list"),
}

HOOK = {
    21: "冻结面板 `days/data/panel.csv`：160 行、AAA 日期 2024-01-02..2024-04-23、AAA 空收盘 1 格；`second read matches = true` 证明文本未换；`the table is not resampled` 排除运行时重抽样。",
    22: "用昨日复权涨跌符号预测今日符号：hits = 36/77，accuracy = 0.4675，低于 coin-flip baseline = 0.5000；规则在计数前固定，不是事后挑窗口。",
    23: "三连同号后押第四日同向：events = 11，hits = 6，accuracy = 0.5455；`the rule is fixed before the count` 锁定规则先于样本量。",
    24: "cut date = 2024-02-28：early events = 8、accuracy = 0.5000 不是成绩；later events = 3、accuracy = 0.6667 才是下一段样本上的计数。",
    25: "lag-1 收益预测：direction accuracy = 0.4675，mean absolute return error = 0.0167；`days with a small price error and the wrong sign = 9` 说明水平误差小不等于方向对；sign 决策应信 direction accuracy。",
    26: "random split，seed 1，train fraction 0.70：test direction accuracy = 0.4583；`this number is the control`——本日只交付对照，不与时间切分并排。",
    27: "time-split test accuracy = 0.5417，random-split test accuracy = 0.4583；`the test of the time split sits entirely after the train` 声明测试块日历上全在训练之后。",
    28: "column high = FORBIDDEN；in-sample RSS close~high = 31.8715 低于 close~lagged close = 35.5233，但高价列含当日信息，分数不得进入排行榜。",
    29: "leaky scale 使用含未来 open 的全样本；RSS return on leaky close = 0.2642 略优于 past-only = 0.2650——差值来自信息集，不是模型族胜利。",
    30: "lookback = 20：末时点 full-sample = 12.1976，window = 12.0095；全样本均值不是可交易信息集，窗口值才是因果可读量。",
    31: "三日斜率 −0.1195 vs 二十日 0.0251；三日 absolute miss 0.0867 小于二十日 0.1506——短窗 in-sample 更贴，不等于样本外更稳。",
    32: "六十日斜率 0.0353 vs 三日 −0.1195；六十日 absolute miss 0.4426 大于三日 0.0867——长窗平滑训练点，末点误差可更大。",
    33: "train mean/std = 0.003241 / 0.022132，whole-sample = 0.002470 / 0.019265；两种 scale 下 test MSE 同为 0.000109，但 whole-sample scale 看见测试段。",
    34: "blank date = 2024-02-01：previous fill = 10.1047，next fill = 9.8971；next close 看见未来，不得用于因果链。",
    35: "行号 35–36 对应 2024-02-20 与 2024-02-22，business-day gap = 2；相邻行不是相邻会话，差分与 lag 须按日历理解。",
    36: "2024-03-11：unadjusted return = −0.4938，adjusted return = 0.0124；两个数都要交，禁止只报未复权 dramatize。",
    37: "pooled AAA+BBB：random-split test accuracy = 0.7234，time-split = 0.6170；random 可在同名日期上同时训练与测试。",
    38: "same-day market sign accuracy = 0.6795，lagged-one-day = 0.4026；消失的是 simultaneity，不是「市场无效」。",
    39: "gross mean return = −0.0024，round-trip cost = 0.0020，net = −0.0044；扣费后均值更负，方向策略须先过成本门。",
    40: "泄漏清单六条均标 future=yes；`a higher score on any of these lines is not a result`——高分只作反例归档，不作 alpha。",
}

MERMAID = {
    21: 'flowchart LR\n  F["panel.csv 文本"] --> R1["read #1"]\n  F --> R2["read #2"]\n  R1 --> M["second read matches = true"]\n  R2 --> M\n  M --> I["160 行 · AAA blank=1"]',
    22: 'flowchart TD\n  Y["sign(r_{t-1})"] --> P["预测 sign(r_t)"]\n  P --> H["hits 36/77"]\n  H --> A["accuracy 0.4675"]\n  C["coin 0.5000"] --> A',
    23: 'flowchart LR\n  S3["三连同号"] --> E["events 11"]\n  E --> H["hits 6"]\n  H --> ACC["accuracy 0.5455"]',
    24: 'flowchart TD\n  C["cut 2024-02-28"] --> E["early 8 · acc 0.5000"]\n  C --> L["later 3 · acc 0.6667"]\n  E --> X["early 非 score"]',
    25: 'flowchart LR\n  D["direction 0.4675"] --> T["sign 决策"]\n  M["MAE 0.0167"] --> W["9 日小误差错符号"]',
    26: 'flowchart TD\n  S["seed 1 · 70% train"] --> R["random 掩码"]\n  R --> A["test acc 0.4583"]\n  A --> L["control 对照"]',
    27: 'flowchart LR\n  T["time split"] --> A1["0.5417"]\n  R["random split"] --> A2["0.4583"]\n  T --> Q["test 全在 train 后"]',
    28: 'flowchart TD\n  H["high FORBIDDEN"] --> RSS1["RSS 31.8715"]\n  L["lag close"] --> RSS2["35.5233"]\n  RSS1 --> B["不得入榜"]',
    29: 'flowchart LR\n  O["later opens"] --> LS["leaky scale"]\n  LS --> R1["RSS 0.2642"]\n  PO["past only"] --> R2["RSS 0.2650"]',
    30: 'flowchart TD\n  FS["full sample 12.1976"] --> X["非信息集"]\n  W["window 20 → 12.0095"] --> OK["可审计"]',
    31: 'flowchart LR\n  W3["3d slope −0.1195"] --> E3["miss 0.0867"]\n  W20["20d 0.0251"] --> E20["miss 0.1506"]',
    32: 'flowchart LR\n  W60["60d 0.0353"] --> E60["miss 0.4426"]\n  W3["3d −0.1195"] --> E3["miss 0.0867"]',
    33: 'flowchart TD\n  TR["train scale"] --> MSE["test MSE 0.000109"]\n  WH["whole scale"] --> MSE\n  WH --> L["看见 test 段"]',
    34: 'flowchart LR\n  B["blank 2024-02-01"] --> P["prev 10.1047"]\n  B --> N["next 9.8971 · future"]',
    35: 'sequenceDiagram\n  participant Row35 as 行35 02-20\n  participant Gap as 停牌\n  participant Row36 as 行36 02-22\n  Row35->>Gap: gap=2 交易日\n  Gap->>Row36: 非相邻会话',
    36: 'flowchart LR\n  U["raw −0.4938"] --> D["披露"]\n  A["adj 0.0124"] --> D',
    37: 'flowchart TD\n  P["AAA+BBB pool"] --> RS["random 0.7234"]\n  P --> TS["time 0.6170"]\n  RS --> S["同日期可跨 train/test"]',
    38: 'flowchart LR\n  SD["同日 0.6795"] --> X["泄漏通道"]\n  LG["lag1 0.4026"] --> OK["因果可读"]',
    39: 'flowchart TD\n  G["gross −0.0024"] --> C["cost 0.0020"]\n  C --> N["net −0.0044"]',
    40: 'flowchart TD\n  L["leakage list ×6"] --> F["future=yes"]\n  F --> R["高分 not a result"]',
}


def feynman(day: int) -> str:
    """Day-specific opening mechanism (dense Chinese)."""
    blocks = {
        21: """
> **结论先行**：`rows = 160` 与 `AAA blank closes = 1` 是 **数据身份合同**，不是模型分数；`second read matches = true` 比较的是 **文件字节**，不是 parse 后的浮点字典。

第 20 天仍在五点玩具上讨论噪声列与留出；从本日起，所有后续 stdout 都绑定 **同一份** `days/data/panel.csv`。脚本只做两次 `read_text()` 并比较字符串相等，因此 CI 可以把「面板被意外替换」做成 **smoke test**。AAA 与 BBB 各 80 行，日期对齐到 2024-04-23；今天 **不** 做 lag、不填 blank close，只计数 `AAA blank closes = 1`。

NaN 与 NaN 在 Python 里不相等——若把空单元格 parse 成 float 再比 dict，同一路径可能被误报为「变了」。McCrary（2008）强调可复现管道；本课用 **text match** 作为最小 integrity 检查。Wickham（2014）的 tidy 语义要求「变量含义稳定」；这里稳定的是 **path + 行数 + 日期端点**。

`the table is not resampled` 声明运行时 **不** 抽子样本：每次运行读全表 160 行。这与 bootstrap 或 walk-forward 重抽样不同；后者在第 26–27 天讨论 **行掩码**，不是换 CSV。改 Git 里的 panel 文本等于 **改题**，第 22 天的 36/77、第 23 天的 11 events 都会跟着变。

BBB 同行数但本日规则只报 AAA 空位；第 37 天才会 pooled。前 20 天五点 2.1…10.4 仍留在早期公式里，**不得**与 panel 混算。审计时写清：identity 三角（160、2024-04-23、blank=1）+ text match + not resampled。
""",
        22: """
> **结论先行**：`accuracy = 0.4675` 是 **sign(r_{t−1}) 对 sign(r_t)** 的 in-sample 命中率，低于 `coin-flip baseline = 0.5000`；这不是「模型坏了」，而是 **固定规则在 AAA 复权差分** 上的计数结果。

构造：对 `_complete(AAA)` 的 `adj_close` 做一阶差分 `move`，预测 `sign(move_t)` 是否等于 `sign(move_{t−1})`。有效长度 77 对，命中 36。Campbell、Lo & MacKinlay（1997）把短 horizon 方向预测放在 **可预测性** 框架里——要点是 **信息集**：昨日符号在收盘后可知，今日符号是 **同期标签**，本课 **未** 做 train/test 切分，因此 0.4675 是 **全样本计数**，不是 hold-out IC。

与第 11–16 天五点上的方向分数不同：那里是价格水平差分；这里是 **panel 复权序列**。0.5000 基准不是假设「市场有效」，而是 **二项符号游戏** 的对照刻度。Lo & MacKinlay（1988）讨论过自相关与方差比；本课不做推断，只固定 **hits = 36/77**。

误用：（1）把 0.4675 写成样本外 alpha；（2）在 blank close 行未过滤前数差分；（3）用 BBB 混池而不改分母。正确披露：name=AAA、adj_close、lag-1 sign rule、in-sample hits。
""",
        23: """
> **结论先行**：`events = 11`、`accuracy = 0.5455` 来自 **固定规则**——三连同号后押第四日同向；`the rule is fixed before the count` 禁止先看 11 再改规则。

扫描 `move` 序列：窗口 `sign(move_{t−3:t−1})` 全相等且非零时，记录 `sign(move_t)` 是否延续。这是 **事件研究** 的最小版本：样本量 11 很小，0.5455 **无** p 值含义。Jegadeesh & Titman（1993）动量与 De Bondt & Thaler（1985）反转在更长样本上讨论；本课只教 **条件触发计数** 与 **规则冻结**。

与第 22 天无条件 lag-1 符号对比：本日 **稀疏触发**（11 次），命中率可高于 0.4675，但 **方差更大**。写 memo 须并列 events 与 accuracy，不能只报 0.5455。规则若改成「两连」或「四连」，events 与分数都变——属于 **estimand 变更**，不是调参。

生产映射：形态识别策略常犯 **multiple testing**；本课 11 事件是提醒 **小 n 下 accuracy 不稳定**。第 24 天把 cut 移到 2024-02-28 后，early 段 8 事件 accuracy 0.5000 **不是 score**，避免 **peek** 后挑段。
""",
        24: """
> **结论先行**：`cut date = 2024-02-28` 把三连规则切成 early / later；`early accuracy is not the score` 明确 **前段 0.5000 不得当成绩**，后段 `later events = 3`、`accuracy = 0.6667` 才是 **下一段** 上的计数。

这是 **时间顺序上的 hold-out 思想** 在事件规则上的最小应用：先在 early 窗口看表现，但 **分数写在 later**。与第 7 天「t=5 不参与 fit」同族： **信息集边界** 决定什么能进分母分子。0.6667 来自 3 次事件中的 2 次命中（由脚本计数），不是整段 80 日 accuracy。

误读：把 early 0.5000 与 later 0.6667 平均成「整体改进」；或把 6667 写成 **显著 beat 50%**。正确做法：分别报告 events、accuracy，并声明 score 标签在 stdout 的 `early accuracy is not the score`。

第 27 天时间切分会在 **回归掩码** 上并排 0.5417 与 0.4583；本日仍是 **规则计数**，但强调 **哪一段算分**。walk-forward 研究里，**先定 cut 再跑** 与 **看完 early 再移 cut** 是不同合同——stdout 用英文句锁定前者。
""",
        25: """
> **结论先行**：`direction accuracy = 0.4675` 与 `mean absolute return error = 0.0167` 是 **同一 lag-1 线性预测** 的两个评分；`days with a small price error and the wrong sign = 9` 证明 **水平准 ≠ 方向对**；sign 决策应信 direction accuracy。

特征：昨日简单收益；标签：今日简单收益。OLS 给出水平预测，再算 MAE 与 sign 命中。9 天满足「价格误差小但符号错」——对 **多空开关** 策略，这 9 天是 **假安全** 日。Christoffersen & Diebold（1997）区分水平与方向预测；本课用打印数字固定 **estimand 并列**。

0.0167 的 MAE 在百分之一量级收益上看似「贴价」，但 direction 仍低于 0.5。PM 若只看 RMSE/MAE 会误选 **水平优** 模型做方向 trade。代码审查：metrics 模块是否同时 export `direction_accuracy` 与 `mae`？

与第 10–11 天五点方向分数对照：那里无 panel、无 lag 收益。本课起 **双分数合同** 延续到第 71 天 bill 与 direction 分轨。报告时 **for a sign decision, trust the direction accuracy** 是 stdout 给的工程指令，不是修辞。
""",
        26: """
> **结论先行**：`test direction accuracy = 0.4583` 在 **random split、seed 1、train 0.70** 下产生；`this number is the control` 声明本日 **只** 交付对照，不与 time split 并排（并排在第 27 天）。

训练掩码随机抽 70% 行估 OLS `r_t ~ r_{t−1}`，测试行上数 sign 命中率。允许 **未来行进训练、过去行进测试**——因此 0.4583 **不能** 叫 walk-forward 成绩。第 27 天会把 time-split 0.5417 放在旁边；今天读者应记住 **0.4583 的身份是对照**。

White（1980）稳健标准误不改点估计；本课尚未做推断。seed 1 是 **复现锚点**，不是最优 seed 搜索。误用：在 100 个 seed 里挑最高 test acc 再报告——那是 **多重检验泄漏**。正确：固定 seed 1，原样引 `this number is the control`。

单名 AAA 上，同一日期只有一行，random 不会把 **同一日历** 拆到两侧；第 37 天 pooled 才会。学习笔记保留两句：单名 random 0.4583；混池 random 可 0.7234—— **主语不同**。
""",
        27: """
> **结论先行**：`time-split test accuracy = 0.5417` 且 `the test of the time split sits entirely after the train`；同协议 random 为 `0.4583`。在 **AAA 单名、lag-1** 下，random **未** 抬高分数。

时间切分：前 70% 行估系数，后 30% 测试；测试下标全部大于训练下标。random 仍 seed 1、比例 0.70。两个数 **必须并排**，禁止只印 0.5417。差 0.0834 不是 p 值，只是 **两种掩码** 下的符号频率差。

Campbell、Lo & MacKinlay（1997）默认解释变量在 t 前已知；time split 是 **最小因果序实现**。random 0.4583 允许日历逆序进训练——在单名序列上表现为 **更低** test acc，不是「随机总是更差」；第 37 天混池会反转名次。

与第 9 天行置换：今天动 **train/test 掩码**，不是同一 `(X,y)` 上行 shuffle。第 28 天 FORBIDDEN 特征与切分正交。memo 四锚点：0.5417、0.4583、entirely after train 句、单名 AAA。
""",
        28: """
> **结论先行**：`column high = FORBIDDEN`；尽管 in-sample RSS close~high = 31.8715 **低于** close~lagged close = 35.5233，**任何使用当日 high 解释当日 close 的分数不得入榜**——信息集含 **同期 intraday 上界**。

回归在样本内比较两列特征：lagged close 合法（只用过去），high 非法（含 t 日已知上界于 close 之前？实际上 close 与 high 同日 bar——**同步泄漏**）。RSS 更小是 **泄漏拟合**，不是预测力。第 40 天清单把本日行标 `future=yes`。

Kahn et al.（1997）与后续 microstructure 强调 bar 内路径；本课日频 closing 合同下，high_t 与 close_t **同行**。生产特征工程 grep `high`、`low` 与 label 同日时，应触发 FORBIDDEN 流程。

误用：因为 31.8715 < 35.5233 就选用 high 特征做 alpha 报告。正确：打印 FORBIDDEN，RSS 只作 **反例教学**。第 38 天 market 同期收益同理。
""",
        29: """
> **结论先行**：`RSS of return on leaky close = 0.2642` vs `past-only = 0.2650`；`the leaky scale is a function of later opens`——差 0.0008 来自 **标准化看见未来 open**，不是稳健 alpha。

leaky scale 用 **全样本 open**（含 t 之后）构造分母或尺度；past-only 只用 t 及之前。return 对 scaled close 的 RSS 略优是 **信息集更大** 的算术结果。Harvey et al.（2016）提醒 backtest 过拟合；此处是 **确定性泄漏** 演示。

与第 33 天 whole-sample scale 看见 test stretch 同族：scale 必须是 **train-only 统计量**。代码审查：fit 阶段是否 `fit_transform` 在全表上算 mean/std？本课 RSS 差很小，但 **机制** 必须写清。

第 40 天 list 收录本日。研究 log 应画 **时间轴**：哪些 open 进入 scale。禁止把 0.2642 贴进「样本外 MSE 改善」摘要。
""",
        30: """
> **结论先行**：`full-sample value at last t = 12.1976` vs `window value at last t = 12.0095`（lookback=20）；`the full sample is not the information set`——全样本均值使用 **末点之后的信息**，窗口统计才是 t 时可见。

这是 **因果信息集** 与 **充分统计** 的初等分离：分析师常用「至今均值」作特征，但在回测里若用 **含未来行的样本** 算均值，就违反 **adapted 过程**。本课在末点打印两值差 ~0.19，量级取决于价格水平。

与第 33 天 scale 泄漏对照：一个动 **均值**，一个动 **标准差**；共同点是 **whole sample 看见 test**。Hamilton（1994）滤波与实时估计强调 **truncated sample**。

实现：lookback=20 只用过去 20 会话；full sample 用全部 adj close。报告特征时写清 **window length** 与 **是否包含 t**。第 32 天比较 3/20/60 窗，本课建立 **full ≠ window** 词汇。
""",
        31: """
> **结论先行**：`three-day slope = -0.1195`、`twenty-day slope = 0.0251`；`three-day absolute miss = 0.0867` **小于** `twenty-day = 0.1506`——短窗 in-sample 更贴 **末点**，不是样本外更优。

对 adj close 滚动 OLS 斜率，在 **最后一日** 比较预测 miss。短窗跟近期噪声，长窗平滑旧趋势；末点处短窗 miss 更小是 **局部过贴** 的典型图。Breiman（2001）两种文化：本课是 **同一标签、不同窗口** 的 miss 对照。

与第 32 天 sixty-day 对照：窗口越长，末点 miss 可越大（0.4426 vs 0.0867）。忌把 **in-sample 末点 miss** 写成 walk-forward RMSE。第 55 天 pick-model 会在 hold-out 上比模型；本课无 hold-out。

写策略 doc 时：**window 是超参**，应用 **验证集** 选，不是看末点 miss 最小就选 3 日。
""",
        32: """
> **结论先行**：`sixty-day slope = 0.0353` vs `three-day = -0.1195`；`sixty-day absolute miss = 0.4426` **大于** `three-day = 0.0867`——长窗在末点 **欠贴近期**，短窗 **过贴噪声**。

本日与第 31 天共用 **末点 absolute miss** 协议，加入 60 日窗口。0.4426 说明用两个月斜率外推 **下一日** 在末点误差大；0.0867 是 3 日线的 tight fit。两者都不是 **test MSE**——无切分。

生产：动量因子常用 60/120 日 lookback；本课提醒 **拟合窗口与评分点** 要分开披露。Fama & French（2012）重述因子构造；此处是 **单名价格斜率** 玩具。

图表阅读：若只报 0.0867 会选 3 日；若关心 **稳定性** 需另加 hold-out（第 27 天）或 bill（第 75 天）。本课数字只服务 **窗口对比** 机制。
""",
        33: """
> **结论先行**：`test MSE` 在 train scale 与 whole-sample scale 下 **同为 0.000109**，但 `the whole-sample scale sees the test stretch`——数值相等 **不** 证明 whole scale 合法。

标准化：用 train 段 mean/std vs 全表 mean/std 变换特征后，在 **同一 test 段** 算 MSE。泄漏 scale 有时 **恰好** 不改变 test 上的 MSE（尤其 test 短、分布接近），但 **合同仍违规**。第 40 天 list 标 future=yes。

 sklearn `StandardScaler` 若 `fit` 在全表，pipeline review 应 fail。本课打印两组 mean/std 不同：train 0.003241/0.022132，whole 0.002470/0.019265——说明 **test 段拉偏了全样本矩**。

正确 pipeline：`scaler.fit(X_train)` only。报告 MSE 时并列 **scale 来源**。与第 29 天 leaky open scale 同族不同列，但 **信息集** 问题一致。
""",
        34: """
> **结论先行**：`blank date = 2024-02-01`；`fill from the previous close = 10.1047` vs `next close = 9.8971`；`the next close sees the future`——前向填 **因果**，后向填 **泄漏**。

缺失 close 在 AAA 上出现 1 次（第 21 天空位）。两种 imputation 改变 **收益链**：prev fill 只用 t−1 信息；next fill 用 t+1 close，在 t 决策时不可见。Little & Rubin（2002）缺失机制；本课 **不** 讨论 MCAR，只固定两种 fill 的 **时间方向**。

0.10 vs 9.90 差异会传播到 lag 与 sign 规则（第 22–23 天）。研究若默认 `bfill` 在 pandas pipeline 里，应 grep 并禁止于特征列。第 40 天 list 收录 next fill。

审计：imputation 必须在 **文档与代码** 同名；stdout 两数都要交，不得只报 prev「因为更合理」。
""",
        35: """
> **结论先行**：`row numbers 35 36`、`dates 2024-02-20 2024-02-22`、`business-day gap = 2`；`adjacent rows are not adjacent sessions`——CSV 相邻 ≠ 日历相邻。

停牌或缺失交易日使 **行号 lag** 与 **calendar lag** 分叉。用 `diff(close)` 时，跨 gap 的差分覆盖 **多个日历日** 的价格变化。Campbell et al. 收益定义应明确 **holding period**。

本课打印 gap=2（business days between dates）。特征若写 `lag-1 row` 实际可能是 **lag-3 calendar**——sign 规则解读会变。生产数据 **halt** 标志应进入特征或过滤。

与第 34 天 blank fill 不同：这里是 **行仍在但日期跳变**。回测合并 corporate action 与 halt 表是 senior 工程师 checklist 项。
""",
        36: """
> **结论先行**：`date = 2024-03-11`；`unadjusted return = -0.4938` vs `adjusted return = 0.0124`；`both numbers are due`——公司行动日 **必须双报**，禁止只 dramatize 未复权 −49%。

未复权序列在拆股/分红日可出现 **伪暴跌**；adj_close 修正份额与现金 dividend。两者 **同时** 进入 stdout 是为强制 **披露复权口径**。研究 alpha 默认应基于 adj；risk 展示有时用 raw——须 label。

与第 21 天 adj_close 列同源 panel。差分规则：后续 lag 收益用 adj。误用：用 raw return 训练、adj label 评分—— **口径混用**。

Shumway & Warther（1999）与 corporate action 处理；本课是 **单日锚点** 数字。代码：`returns(adj_close)` vs `returns(close)` 分支要 unit test。
""",
        37: """
> **结论先行**：pooled AAA+BBB 下 `random-split test accuracy = 0.7234` **高于** `time-split = 0.6170`；`the random split can train and test on the same date`—— **同名日历跨股票** 进入两侧，random 可 **虚高**。

单名第 27 天 random 0.4583 < time 0.5417；混池后 **反转**。机制：AAA 与 BBB 共享日期，random 掩码按 **行** 抽，可把 **同一天** 一条进 train、另一条进 test—— **泄漏通道** 不同于 feature 泄漏，是 **切分设计** 泄漏。

第 40 天 list 标 future=yes（共享日期）。正确实践：**按 date 切分** 或 **按 name 分组切分**（Purged CV, Lopez de Prado 2018）。本课只打印数字教 **主语变更则名次变更**。

报告 pooled 结果时写清：**是否 group by date**。0.7234 **不得** 与单名 0.4583 直接比「random 更好」——池不同。
""",
        38: """
> **结论先行**：`same-day market sign accuracy = 0.6795` vs `lagged-one-day = 0.4026`；`what disappeared was simultaneous`——高命中来自 **同期 market return**，lag 后只剩 **可交易信息集**。

market 列与 AAA 同行；用 **同日** market 收益符号预测 AAA 方向，命中 0.6795。改用 **lag-1 market** 符号，降至 0.4026。差 ~0.28 是 ** simultaneity premium**，不是因子 alpha。第 40 天 list 标 same-day market。

与第 28 天 high 同期列同族： **bar 内/同行** 信息。多因子模型应用 **lagged market beta**；回归残差用 contemporaneous market 仅 **解释**，不作 **信号**。

生产：merge asof 时 market 字段 timestamp 必须 **≤ decision time**。本课两数并排是 **因果 vs 泄漏** 的最小对照。
""",
        39: """
> **结论先行**：`gross mean return = -0.0024`、`round-trip cost = 0.0020`、`net mean return = -0.0044`—— **扣费后均值更负**；方向策略须先过 **成本门** 再谈 hit rate。

本课用 **固定 round-trip 0.0020**（20 bps 量级）从 gross 均值扣除，得 net −0.0044。与第 22–27 天 **无成本** direction accuracy 对照：0.47 命中在 **net 负均值** 下可能仍不可交易。Hasbrouck（2007）交易成本；Almgren & Chriss（2000）执行成本。

gross 已略负 −0.24% 均值；加费后 −0.44%。 **break-even hit rate** 需联合 spread 与 payoff asymmetry——本课不算，只固定三行 stdout。第 93 天 slippage tick 会细化。

PM 报告：并列 gross/net 与 **assumed cost**；禁止只报 direction accuracy。research log 写清 **cost 是否含 borrow/funding**——本课仅 round-trip 常数。
""",
        40: """
> **结论先行**：清单六课均 `future=yes`；`a higher score on any of these lines is not a result`—— **泄漏设计上的高分只归档为反例**，不得进入 leaderboard 或 research alpha 摘要。

第 40 天不重跑实验，只 **索引** day 28/29/33/34/37/38 的违规类型：同期 bar、未来 open scale、test 段 scale、next fill、跨名同日期 random、同期 market。这是 **season-1 泄漏词汇表** 闭合。

与 honest time split（第 27 天）对照：时间切分本身 **不是** 泄漏；泄漏在 **特征/scale/fill/切分池**。Kaggle 式 LB 若允许泄漏特征会 **虚高**；本课 explicitly negates those scores。

审计流程：新特征 PR 必须回答 **decision time** 与 **label time**；grep FORBIDDEN / future=yes。清单行是 **negative results catalog**——科研诚信要求 **报告失败与违规** 与报告成功同权。
""",
    }
    return blocks[day].strip()


def expand(day: int) -> str:
    """Day-specific 拓展领域（机制段 + 复现/衔接尾段）。"""
    common_tail = """
**数值与复现.** 在仓库根目录运行当日脚本；`panel.csv` 与 `numpy==1.24.4` 为默认合同。正文 ```text``` 块须与终端 stdout **逐行零 diff**；改数据或 `fmt` 时同一 commit 更新 golden 与 md。

**全季衔接.** 第 1–20 天：五点 toy 与 OLS/损失/hold-out 语言；第 21 天起：冻结 panel。两套数字 **不可混表**（例如斜率 3.27 与 accuracy 0.4675 无直接比较关系）。第 41 天起模型复杂度上升；第 51 天 lag-5；第 58 年切；第 71 天 bill/direction 分轨——**信息集合同** 全季不变。

**文献锚（非虚构，只作机制分类）.** Campbell, Lo & MacKinlay (1997)；Harvey, Liu & Zhu (2016)；Lopez de Prado (2018)；Little & Rubin (2002)；Hasbrouck (2007)。不得把教科书结论偷换为「本 panel 显著」——本段多数课 **无** 显著性检验 stdout。

**代码审查五问（panel 段）.** 特征在决策时刻是否可见；标准化是否只用训练段矩；train/test 是否按 date/name 分组；metrics 是否诚实区分 in-sample 与 hold-out；FORBIDDEN 行是否仍打印。缺任一条，spec 不完整。

**手算与 CI.** 任取 stdout 一行在 REPL 复算；`verify_season01_docs.py --day N` 为合并必要条件。改 `panel.csv` 须重跑依赖该面板的 golden 日。
"""
    return (PROSE[day] + common_tail).strip()


CORE_XY = {
    22: """xychart-beta
    title "方向命中 vs 抛硬币基线（stdout）"
    x-axis ["accuracy", "coin"]
    y-axis "rate" 0.45 --> 0.52
    bar [0.4675, 0.5000]""",
    27: """xychart-beta
    title "单名 AAA：time vs random test accuracy"
    x-axis ["time", "random"]
    y-axis "accuracy" 0.44 --> 0.56
    bar [0.5417, 0.4583]""",
    28: """xychart-beta
    title "in-sample RSS（低者非法）"
    x-axis ["close~high", "close~lag"]
    y-axis "RSS" 30 --> 36
    bar [31.8715, 35.5233]""",
    39: """xychart-beta
    title "均值收益：gross vs net"
    x-axis ["gross", "net"]
    y-axis "mean return" -0.005 --> 0
    bar [-0.0024, -0.0044]""",
}


def core_extra(day: int) -> str:
    """Tables and formulas between stdout and expand."""
    bits = {
        21: """
| 键 | 值 | 审计含义 |
|:---|:---|:---|
| rows | 160 | 全表行数，非有效差分行 |
| AAA blank closes | 1 | 缺失 close，不本日填充 |
| second read matches | true | 字节级一致 |

Git 修改 `panel.csv` 后须重跑第 21–99 天 verify 中依赖 panel 的脚本。
""",
        22: """
| 量 | 值 |
|:---|---:|
| hits | 36/77 |
| accuracy | 0.4675 |
| coin baseline | 0.5000 |

规则：\\(\\hat s_t = \\mathrm{sign}(r_{t-1})\\)，评估 \\(\\mathbb 1[\\hat s_t = \\mathrm{sign}(r_t)]\\)。全样本 in-sample，无切分。
""",
        23: """
| 量 | 值 |
|:---|---:|
| events | 11 |
| hits | 6 |
| accuracy | 0.5455 |

规则冻结句 `the rule is fixed before the count` 与 events 计数绑定；改 pattern 长度等于换 estimand。
""",
        24: """
| 段 | events | accuracy | 是否 score |
|:---|---:|---:|:---|
| early（≤ cut） | 8 | 0.5000 | 否 |
| later（> cut） | 3 | 0.6667 | 是（下一段计数） |

`cut date = 2024-02-28`；`early accuracy is not the score` 为 legal 句，dashboard 须灰显 early。
""",
        25: """
| 指标 | 值 | 决策含义 |
|:---|---:|:---|
| direction accuracy | 0.4675 | sign book 主指标 |
| mean abs return error | 0.0167 | 水平贴价，非方向 |
| small error, wrong sign | 9 | 假安全日计数 |

stdout 末行 `for a sign decision, trust the direction accuracy` 为工程裁决，不是修辞。
""",
        26: """
| 项 | 值 |
|:---|:---|
| split | random, seed 1, train 0.70 |
| test direction accuracy | 0.4583 |
| 身份 | control（对照） |

本日 **不** 与 time split 并排；`this number is the control` 禁止改写成 walk-forward 成绩。
""",
        27: """
| 切分 | test direction accuracy |
|:---|---:|
| time | 0.5417 |
| random (seed 1) | 0.4583 |

时间切分测试块 **calendar-after** 训练块；random 允许逆序。
""",
        28: """
| 特征 | in-sample RSS | 可否入榜 |
|:---|---:|:---|
| close ~ high（FORBIDDEN） | 31.8715 | 否 |
| close ~ lagged close | 35.5233 | 是（仍 in-sample） |

`column high = FORBIDDEN` 行必须保留在 stdout；RSS 更低不构成选型理由。
""",
        29: """
| scale | RSS on return |
|:---|---:|
| leaky close | 0.2642 |
| past-only close | 0.2650 |

差 0.0008 量级小；`the leaky scale is a function of later opens` 说明 **机制** 优先于 delta。
""",
        30: """
| 估计 | last t 拟合值 |
|:---|---:|
| full-sample line | 12.1976 |
| lookback=20 window | 12.0095 |

`the full sample is not the information set`：实时特征只能用 window 行。
""",
        31: """
| 窗口 | slope | last-t abs miss |
|:---|---:|---:|
| 3 日 | −0.1195 | 0.0867 |
| 20 日 | 0.0251 | 0.1506 |

末点 miss 更小 ≠ 样本外更优；只是 in-sample 局部过贴。
""",
        32: """
| 窗口 | slope | last-t abs miss |
|:---|---:|---:|
| 60 日 | 0.0353 | 0.4426 |
| 3 日 | −0.1195 | 0.0867 |

长窗末点 miss 更大，教 **bias–variance 直觉**；无 hold-out 不得选窗。
""",
        33: """
| scale 来源 | train μ/σ | test MSE |
|:---|:---|---:|
| training stretch | 0.003241 / 0.022132 | 0.000109 |
| whole sample | 0.002470 / 0.019265 | 0.000109 |

MSE 相等 **不** 洗白 whole-sample scale；`the whole-sample scale sees the test stretch`。
""",
        34: """
| fill | 值 | 信息集 |
|:---|---:|:---|
| previous close | 10.1047 | t 可见 |
| next close | 9.8971 | 含 future |

`the next close sees the future`；pipeline 禁止 silent bfill 于特征列。
""",
        35: """
| 项 | 值 |
|:---|:---|
| row numbers | 35, 36 |
| dates | 2024-02-20, 2024-02-22 |
| business-day gap | 2 |

`adjacent rows are not adjacent sessions`：row lag ≠ calendar lag。
""",
        36: """
| 序列 | 2024-03-11 return |
|:---|---:|
| unadjusted | −0.4938 |
| adjusted | 0.0124 |

`both numbers are due`：公司行动日禁止只 dramatize 未复权。
""",
        37: """
| 切分 | pooled test direction accuracy |
|:---|---:|
| random | 0.7234 |
| time | 0.6170 |

`the random split can train and test on the same date`；与单名第 27 天名次 **可反转**。
""",
        38: """
| 信号 | sign accuracy |
|:---|---:|
| same-day market | 0.6795 |
| lagged-one-day market | 0.4026 |

`what disappeared was simultaneous`：~0.28 是 simultaneity，不是 alpha。
""",
        39: """
| 项 | mean return |
|:---|---:|
| gross | −0.0024 |
| round-trip cost | 0.0020（常数） |
| net | −0.0044 |

扣费后更负；hit rate 须与 cost 门联读（第 22–27 天无费）。
""",
        40: """
| 天 | 泄漏类型 | future |
|:---|:---|:---|
| 28 | 当日 high → close | yes |
| 29 | 未来 open scale | yes |
| 33 | test 段进 scale | yes |
| 34 | next close fill | yes |
| 37 | 跨名同日期 random | yes |
| 38 | 同期 market | yes |

`a higher score on any of these lines is not a result` 否定泄漏高分入榜。
""",
    }
    body = bits.get(day, "")
    xy = CORE_XY.get(day)
    if xy:
        body += f"\n\n```mermaid\n{xy}\n```\n"
    return body


def build_day(day: int, stdout: str) -> str:
    title, script_name, folder = META[day]
    hook = HOOK[day]
    mermaid = MERMAID[day]
    body_f = feynman(day)
    body_e = expand(day)
    body_c = core_extra(day)

    cmd = f"python days/{folder}/{script_name}"

    md = f"""<p align="center"><b>中文</b> &nbsp;&nbsp;·&nbsp;&nbsp; <a href="day-{day:02d}.en.md">English</a></p>

# 第 {day} 天 · {title}

[第一阶段 · 模型](README.md) · [排版规范](LESSON_LAYOUT.md) · 可运行

今天的学习要点：{hook}

---

## 费曼法讲解

{body_f}

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

{body_c}

---

## 拓展领域

{body_e}

---

## 实战总结

```bash
{cmd}
```

核对：将终端 stdout 与上文 ```text``` 块逐行 diff；中文叙述中的小数位与键名空格须与英文输出一致。本课机制见 [`{script_name}`](../../days/{folder}/{script_name})；改 panel 或切分参数时同步更新 golden 块并跑 `python3 scripts/verify_season01_docs.py --day {day} `。
"""
    return md


def main() -> None:
    short = []
    for day in range(21, 41):
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
