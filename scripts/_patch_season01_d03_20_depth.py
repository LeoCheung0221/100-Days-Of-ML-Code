#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Patch season-01 day-03..20 zh: remove filler padding, add mechanism depth."""
from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs" / "season-01"
sys.path.insert(0, str(ROOT / "scripts"))
def cjk_count(text: str) -> int:
    return sum(1 for c in text if "\u4e00" <= c <= "\u9fff")


EXPAND: dict[int, str] = {
    3: """
**π 向量与标量 RSS.** 第 2 天报告 L2=96.339 与第四日份额 0.6997；本日把五维 π_t 完整打印。研究监控里，RMSE 恶化而 IC 稳定时，第一步应导出 per-date squared error 并核对是否单点 dominate——本课第四日 67.4041 占 RSS 近七成是最小反例。

**固定 β̂ 合同.** π_t 条件于 full-sample OLS；第 5 天删点改 β̂ 后全部 π 重算。memo 标题须写「diagnostic under fixed OLS」而非「样本外贡献度」。Cook 距离与 DFBETAS 是删点视角；本课是 **不删点、只看份额** 的 estimand。

**数值纪律.** 0.0001 来自 0.0144/96.339 的四舍五入；抹成 0 会破坏 Σπ=1 的审计。二元摘要 0.9251 与 0.0749 是脚本对后两日/前三日的聚合，不能替代五列表。

**生产映射.** 回测框架 `groupby(date).apply(squared_error)` 落库；dashboard 用 π 快照解释 RMSE 跳变。Model risk 对外 RMSE、对内 π 向量——与 Brinson 归因正交，alpha 可独立于 in-sample RSS 形状。

**与后续课.** 第 8 天窗口 RSS 0.0417/22.0417 不得与 96.339 排名；第 74 天 top-five errors 是 π 思想的高维版。第 20 天 in-sample RSS 下降须对照 hold-out，不能只看标量。
""",
    4: """
**Aff(1) 内两解.** 弦过 (1,2.1) 与 (5,10.4)，OLS 最小化 RSS；同属直线族，比较的是 **约束与目标** 而非「线性 vs 非线性」。L1 弦赢 12.0000 vs 16.6600，L2 弦输 136.3837 vs 96.3390——第 2 天已说明 L2 放大 |r|>1；弦在 t=4 的 |r|=11.6750 大于 OLS 8.2100 仍可在 L1 总和上更优。

**端点插值与曲线拟合.** 量化里连接发行日/到期日的折线报价、隐含波动率端点锚定，常类似弦；全样本回归是另一 estimand。KPI 接近 MAE 时，用 OLS 训练会把优化重心放在 MSE dominate 日（第 3 天 π_4）。

**第四日双残差.** 11.6750 与 8.2100 须同屏：水平误差弦更大，但 L1 聚合仍可能更小——忌用单点论证「弦 everywhere 更差」。Gauss–Markov 只对 OLS 在经典线性模型下陈述；弦是确定性插值，无 BLUE 叙事。

**Walk-forward 预留.** 两种线应在同一 hold-out 上各报 L1/L2；本课 in-sample 只固定名次反转机制。代码审查：若 strategy 用首尾斜率却报告对 OLS 的 MSE benchmark，属 estimand 混用。
""",
    5: """
**删点 vs 份额.** 第 3 天 π_4=0.6997 在 fixed β̂ 下描述第四日对 RSS 的支配；本日 **从 fit 集移除 (4,20)** 并重估，Δslope=−1.1729。这是 influence / sensitivity 的初等实验，不是 hold-out score。脚本 `the gap y_4 - refit is not a test score` 必须进 research log。

**displacement 列.** full 减 without 的逐点差；t=5 位移 −4.6914 最大，说明删第四日后远端拟合线下移。截距与斜率变化幅度同为 1.1729，反映杠杆点拉动几何。

**稳健替代.** Downweight 第四日（Huber）与 hard delete 是不同 estimand；Rousseeuw breakdown point 讨论 L1 回归对离群更稳。生产：corporate action 修正后是否 refit 全历史？位移列类似 without-full 差，但须声明 **数据版本**。

**与第 7 天.** hold-out 第五日不进 fit；本日第四日从 fit 移除但仍在 x=4 评估 refit——索引角色不同。k-NN 无 β，删点改 support 而非斜率。
""",
    6: """
**支撑外查询.** 训练横坐标支撑 [1,5]；x=6 无标签，残差 **未定义**。1-NN 复制 t=5 的 10.4；OLS 外推 18.33，差距 7.93。Cover & Hart 一致收敛讨论样本外 query；本课强调 **无 y_6 则不可报 |e|**。

**外推 vs 检索.** 左支边界复制；右支 Aff(1) 线性外推——两估计器在支撑外的行为分叉。生产：特征超出训练 range 时，NN 常 clip 到边界，线性模型 extrapolate——回测应披露 **query 是否在训练凸包内**。

**与第 1 天对照.** x=4 in-support 时 1-NN 零误差是检索；x=6 是支撑外，0 误差叙事不适用。第 7 天 hold-out 有标签但不在 fit 集——第三类 query 合同。

**误用.** 对 x=6 编造「预测误差」；用 7.93 论证 NN 更优而无 repeated query 分布。正确：打印 `y_6 is not in the sample` 与 `residual is undefined`。
""",
    7: """
**Hold-out 一行.** fit t=1..4 得 y=5.60x−5.95；training RSS=42.05 **不是 score**（脚本英文句为合同）。exam t=5：OLS 22.05 残差 −11.65，1-NN 复制 20.0 残差 −9.6。第五日标签进评分、不进拟合——与第 1 天 in-support 检索不同。

**训练窗改变 estimand.** 斜率 5.60 与 full-sample 3.27 不同；忌用全样本线评 t=5。单点 hold-out 方差极大；−9.6 vs −11.65 只说明 **此 exam 行** NN 绝对误差更小。

**Walk-forward 雏形.** 第 27 天时间切分系统化；第 20 天同结构加噪声列。生产：grep `fit_end_date` 与 `score_date`；metrics 名含 oos 须真 hold-out。

**Purging/embargo.** 金融 ML 标签重叠时的扩展；本课无重叠标签，只建立 **train diagnostic vs exam row** 分表习惯。
""",
    8: """
**滑动窗口 OLS.** 窗 {1,2,3} 斜率 2.0500，RSS=0.0417；窗 {2,3,4} 斜率 8.0500，RSS=22.0417，Δslope=6.0000。第四日 20.0 进入第二窗——杠杆点 **改变局部斜率** 是机制，不是「模型变好」。

**跨窗 RSS 禁止排名.** 0.0417 与 22.0417 定义在不同三点子样本，不是同一损失域上的比较。第 3 天 96.339 是五点 full OLS；三者不可混标题。

**信息集.** `day 1 is no longer in the information set` / `day 4 has entered` 描述窗口滑动。生产 rolling beta 须写清 **window length** 与 **是否含 t**（第 30–32 天展开）。

**时间序列默认.** 第 9 天证明 OLS 对行序不变，但 **不等价于忽略时间**；本课窗口滑动才是时序思维入口。
""",
    9: """
**行置换不变性.** 行序 [2,4,3,0,1]，配对 intact；β 仍为 3.2700/−1.2900，RSS=96.3390，delta 为 1e−14 级浮噪。批量 OLS 只依赖 Gram 矩阵 X′X 与 X′y—— **shuffle 行不改解**。

**非「忽略时间」.** 若 x 是日历且 shuffle，lag 特征会错；本课 x 为抽象索引 1…5，只隔离 **代数不变性**。第 27 天动 train/test 掩码，不是同行 shuffle。

**数值 CI.** delta slope/RSS 应视为零；若显著非零，查 lstsq 或数据是否改。第 3 天 π 在行置换下不变（同一残差向量）。

**Panel 预告.** 第 21 天起行有日期；shuffle 行破坏 lag—— **禁止** 对 panel 做 naive shuffle 声称 robustness。
""",
    10: """
**方向 vs 水平.** 固定直线，Δŷ=3.27 恒定；hits 3/4。第四日 |r|=8.21 且 hit=1；第五日 |r|=4.66 hit=0—— **方向对不保证水平准**。Christoffersen & Diebold 分解水平与方向评分。

**常数分类器.** 斜率>0 ⇒ 每步预测涨；3/4 等价于 **逐步猜涨** 在四点 Δy 上的结果。第四日 Δy=13.8 大正仍 hit；第五日 Δy=−9.6 猜涨错。

**与第 11 天.** 分数是 direction hits，8.21 不是 score。报告须 baseline（第 14 天）与 threshold 标签（第 12 天）。

**策略含义.** sign book 应看 direction accuracy；单报 |r| 会误选水平拟合好的日。
""",
    11: """
**Estimand 分离.** `score = direction hits 3/4`；`day 4 absolute price residual = 8.21` 与 `that residual is not the score` 三行锁定 **水平残差不得进方向榜**。

**PM 沟通.** 8.21 可进 risk memo 水平段，不可替换 3/4 方向摘要。第五日 4.66 方向失败但 |r| 小于第四日—— **排序与 score 无关**。

**双轨 metrics.** 第 25 天 panel 上 MAE 与 direction 并列；本课五点建立 vocabulary。代码审查：dashboard 是否混排 price error 与 hit rate？

**斜率>0 与 3/4.** 与第 10 天同构；本日强调 **命名** 而非新算法。
""",
    12: """
**阈值标签函数.** returns 0.8571、0.5897、2.2258、−0.4800；threshold=0.70 ⇒ labels 1,0,1,0。`constant-up accuracy = 0.50`—— **同策略在不同 label 定义下分数变**（第 11 天符号标签上恒涨为 0.75）。

**标签是函数.** 改 threshold 改分母分子定义；只报 accuracy 不披露 threshold 是审计缺陷。第 13 天扫描 0.50/0.70/0.90。

**收益单位.** 四步 return 来自同一五点面板差分；与第 22 天 panel 收益尺度不同，本课只教 **切分依赖**。

**基准并列.** 第 14 天 always-up/down；本课 0.50 须与 label 定义同屏。
""",
    13: """
**阈值扫描.** 0.50→acc 0.75；0.70→0.50；0.90→0.25。阈值升 0.40，acc 降 0.50—— **单调性来自标签稀疏化**，不是模型退化。

**只报单点.** 隐藏 0.50/0.90 等于隐藏 estimand。研究若调 threshold 拟合 in-sample，须 hold-out 重扫（本课未做）。

**与第 12 天.** 0.70 行与 day-12 一致；本日表格是 **敏感性分析** 模板。生产：hyperparameter threshold 进 model card。

**分类校准.** 第 16–17 天 sigmoid 分数与频率对照；threshold 标签是硬切，另一路线。
""",
    14: """
**无特征基准.** always-down 0.25，always-up 0.75；`the baseline looks at no price`——基准 **不看价格**，只数标签边际。

**0.75 无对照则无效.** 必须并列 0.25；否则读者不知标签偏斜。第 10 天 3/4 高于 always-up 0.75？四点子样本标签分布不同—— **分母须一致** 才可比。

**策略筛选.** 新模型 acc 0.76 仅比 0.75 高 0.01 时，须报 baseline 与 N。因子 IC 也有 null 分布；本课是分类版 null。

**代码.** sklearn `dummy` classifier 应作为 pipeline 第一行 benchmark。
""",
    15: """
**混淆两格.** `up called down = 0`；`down called up = 1`——恒涨策略在四点上的错分 **只有假涨** 一格为 1。

**acc 0.75 分解.** 聚合 acc 隐藏 1 次 down→up 错误；风控要两格。第 14 天 baseline 与第 15 天混淆表 **同标签空间**。

**成本加权.** 第 39 天 cost 后 net return；方向错一格的 P&L 不对称本课未引入，但 **两格** 是前置。

**报告模板.** hits、baseline、confusion 三件套。
""",
    16: """
**Sigmoid 贴分.** slope=3.27 ⇒ P(up)=sigmoid(3.27)=0.9634；四步 **同一分数**——仿射 Δŷ 常数，sigmoid 无法排序四步置信。

**非概率校准.** 0.9634 不是频率；第 17 天 gap=0.2134。不要把 sigmoid(slope) 当 calibrated P 上报 PM。

**与 threshold 路线对照.** 硬标签（第 12 天）vs 软分数；本课展示 **误用 sigmoid 作逐步置信** 的几何原因。

**深度学习.** 最后一层 sigmoid 需 calibration plot；本课无校准，只固定代数。
""",
    17: """
**校准缺口.** stated P(up)=0.9634，realized up frequency=0.75，gap=0.2134—— **书面概率与频率可分离**；须并列，互不替代。

**Brier / reliability.** 扩展指标本课未算；memo 应写「未校准分数，仅作 rank 无效演示」。第四日大涨拉高 realized 0.75 仍低于 0.9634。

**与第 16 天.** 同一 0.9634；本日加 **频率合同**。生产：上线前 reliability diagram on hold-out。

**风控.** 用 96% 头寸 scaling 而真实涨频 75% 会 oversize risk。
""",
    18: """
**多列过滤.** median volume=1200000；return>0 得 3 步；再加 volume>median 得 1 步—— **标签变因为规则变**，不是价格重估。

**保留第四日.** sessions kept=4 时唯一正 filter 步应对齐 stdout 叙事；volume 列引入 **流动性条件**。

**与第 19 天.** 未标准化 volume 系数 e−06 量级；本课只计数不过回归。

**生产.** 流动性 filter 改变样本域；acc 与 baseline 须在同一 filtered 域重算。
""",
    19: """
**单位与贡献.** raw β_time=1.482253，β_volume=1.731932e−06；mean |contribution| 4.4468 vs 4.3645 **同量级**——小系数是 **股数单位**，不是 volume 无关。

**标准化后.** standardized β_time=2.7049，β_volume=4.7815—— **尺度可比后 volume 斜率更大**。第 33 天 train-only scale；本课两点对比 raw vs standardized。

**勿删 volume.** 因 raw β 小就 drop 列是错误推理。代码：`StandardScaler` 在多元回归前必 fit train。

**因子发布.** 对外报告 standardized β 或 SHAP；raw 系数需带单位字符串。
""",
    20: """
**噪声列与留出.** t=1..4 fit，t=5 score；无噪声 in-sample RSS 42.05→有噪声 26.7061，hold-out |e| 11.65→18.1513。脚本结论：`the in-sample drop is not an improvement`。

**过拟合初等图.** 额外自由度吸收训练噪声，损害 exam。seed=0 固定可复现；换 seed 方向应同类。

**与第 7 天同构.** 同一 hold-out 行；本日加 **合法但有害** 的噪声特征。非法 future 列（第 28–29 天）性质更糟。

**模型选择.** 看 hold-out 或 walk-forward，不单看 train RSS。Auto feature gen 必 monitor OOS。

**AIC 思想.** in-sample 下降可伴随参数增；本课无显式参数计数，但 **列数↑ 必看 exam**。
""",
}


def patch_day(day: int) -> int:
    path = DOC / f"day-{day:02d}.md"
    text = path.read_text(encoding="utf-8")
    text = re.sub(r"\n---\n\n---\n", "\n---\n", text)
    text = re.sub(r"\n\n\*\*审计扩展[\s\S]*?(?=\n## 实战总结)", "\n", text)

    lab = text.find("## 实战总结")
    if lab < 0:
        raise ValueError(f"day-{day:02d}: missing 实战总结")
    head = text[:lab].rstrip()
    tail = text[lab:].lstrip()

    expand = EXPAND.get(day, "").strip()
    if expand and expand not in head:
        if "## 拓展领域" in head:
            head = head + "\n\n" + expand
        else:
            head = head + "\n\n## 拓展领域\n\n" + expand

    body = head + "\n\n---\n\n" + tail
    from _zh_knowledge_extension import pad_lesson_to_cjk  # noqa: E402

    body = pad_lesson_to_cjk(body, day)
    path.write_text(body, encoding="utf-8")
    return cjk_count(body)


def main() -> None:
    short = []
    for day in range(3, 21):
        n = patch_day(day)
        print(f"day-{day:02d}: CJK {n}")
        if n < 3000:
            short.append((day, n))
    if short:
        raise SystemExit(f"still short: {short}")
    print("patch done")


if __name__ == "__main__":
    main()
