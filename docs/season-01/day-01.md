<p align="center"><b>中文</b> &nbsp;&nbsp;·&nbsp;&nbsp; <a href="day-01.en.md">English</a></p>

# 第 1 天 · 样本内最近邻与普通最小二乘

[第一阶段 · 模型](README.md) · [排版规范](LESSON_LAYOUT.md) · 可运行

今天的学习要点：查询点落在训练集内部时，最近邻残差为 0 只说明标签被检索到了；普通最小二乘的残差 8.2 是仿射函数类的近似误差。

---

## 费曼法讲解

> **结论先行**：在训练横坐标上查询且与某样本重合时，1-NN 的零残差是 **in-support 检索** 的定义结果，不是样本外预测能力；OLS 的 8.2 是 **仿射假设类** 在平方损失下的近似误差。

五个收盘价构成单行面板：2.1、3.9、6.2、20.0、10.4（横坐标为日序 1…5）。在 `x=4` 处评估：真实标签 20.0。**最近邻**取 `argmin_i |x_i−x|`，命中第四行，输出 20.0，残差 0.0。**OLS** 最小化 `‖y−Xβ‖²`，得 `y = 3.27x − 1.29`，在 `x=4` 处拟合值 11.79，绝对残差 8.2（脚本一位小数）。

二者不可比「谁更准」——比较的是 **估计器族** 与 **损失** 是否相同。零残差在这里等价于允许估计器在训练点上 **精确记忆**；8.2 则表明全局直线无法同时穿过五个点，第四日离拟合线最远（精确值 8.21，见 `train points` 段）。第四日对 RSS 的支配会在第 2–3 天用 L1/L2 份额量化；本日只固定 **同一查询、两种规则**。

查询落在凸包内且与训练点重合：既不是留出（第 7 天），也不是支撑外外推（第 6 天）。Gauss–Markov 框架下 OLS 为 BLUE；1-NN 在训练坐标上退化为 **查表**。Cover & Hart（1967）的一致收敛讨论针对样本外查询；**本日零误差不属于该渐近结论**。

```mermaid
flowchart TD
  Q["查询 x=4，标签 y=20.0"] --> NN["1-NN：训练点检索"]
  Q --> OLS["OLS：min Σ(y−ŷ)²"]
  NN --> R0["ŷ=20.0，|e|=0.0"]
  OLS --> R8["ŷ=11.79，|e|=8.2"]
  R0 --> N1["解释：in-support 记忆"]
  R8 --> N2["解释：仿射类残差"]
```

回测与研究中，须先披露：**query 是否在训练支撑上**、**函数类名称**、**水平损失定义**。缺任一项，样本内误差不可审计。

**误用模式（研究笔记里应打红标）**：（1）把 0.0 写进「样本外 IC / 命中率」摘要；（2）用 8.2 论证「线性模型失效」却不给出函数类与查询集合；（3）在每一训练行重复 `x=x_i` 查询再平均 |e|，等价于对本日 `x=4` 的检索游戏做全表复制。正确做法是固定 **查询分布** 与 **假设类**，再报告损失。

**与后续课程的合同**：第 7 天起引入 **留出**；第 27 天固定 **时间切分**；第 51 天起重写为 **lag-5 面板 + hold-out 行**。本课五点是玩具几何，但 **估计器披露三件套**（query、class、loss）全季不变。写 commit message 或 research log 时，宁可少报一个 R²，也要写清三件套。

从实现角度，1-NN 在代码里常表现为 `y[i]` 或索引命中；OLS 为 `lstsq`。两者 **CPU 成本** 在此可忽略，但 **统计成本** 不同：OLS 用五个点估两个参数，残差自由度为 3；1-NN 在命中训练点时 **不消耗邻域平滑带宽**。这不是说 OLS「更省数据」，而是说 **有效参数个数** 不同，样本外方差阶不同（此处不做渐近展开，只建立直觉）。

若把问题改写成「预测 `y_4`  given 过去四天」，估计器与损失都要改；本课 **不做时间因果重述**，只固定横坐标为日序、查询为 4。读文献时看到「in-sample fit at training covariates」应自动联想到本图左支，而不是样本外泛化。

---

## 核心知识

### 脚本输出（与下方 `text` 块一致）

[`fit_line.py`](../../days/01-line-that-misses/fit_line.py)：

```text
train points
  x=1.0  y=2.1  line=1.98
  x=2.0  y=3.9  line=5.25
  x=3.0  y=6.2  line=8.52
  x=4.0  y=20.0  line=11.79
  x=5.0  y=10.4  line=15.06

line: y = 3.27 x + -1.29
ask x=4.0, the stored y is 20.0
memorized neighbor says 20.0, miss 0.0
fitted line says 11.79, miss 8.2
```

设计矩阵行 `[x_t, 1]`，响应 `y_t`。1-NN：`î=argmin_i|x_i−x|`，`ŷ=y_î`。OLS：`β̂=argmin_β‖y−Xβ‖²`，本课用 `numpy.linalg.lstsq`（`numpy==1.24.4`），报告系数 3.27、−1.29 以打印为准。

```mermaid
xychart-beta
    title "观测 y 与 OLS 拟合 line=（同脚本）"
    x-axis [1, 2, 3, 4, 5]
    y-axis "price" 0 --> 22
    line [1.98, 5.25, 8.52, 11.79, 15.06]
    bar [2.1, 3.9, 6.2, 20.0, 10.4]
```

| 估计器 | x=4 输出 | |e| | 含义 |
|:---|---:|---:|:---|
| 1-NN | 20.0 | 0.0 | 查询点=训练点，输出=标签 |
| OLS | 11.79 | 8.2 | 仿射类平方损失最优 |

| | 本日 | 第 6 天 | 第 7 天 |
|:---|:---|:---|:---|
| 查询 | x=4，支撑内 | x=6，支撑外 | x=5，留出 |
| 标签用于评分 | 是 | 否（残差无定义） | 是，不进拟合 |
| 1-NN 行为 | 复制训练点 | 复制边界 10.4 | 复制 x=4 的 20.0 |

逐点残差（由 `train points` 行核对）：0.12、−1.35、−2.32、8.21、−4.66；第四日为唯一大幅正残差，OLS 为全局折中而非「忽略异常点」。

Gauss–Markov 定理前提在本玩具样本上 **未检验**：同方差、无自相关、外生 `X`。五点的异方差性已肉眼可见（第四日方差贡献大），故 **BLUE 陈述** 仅作「OLS 在线性无偏类中有效」的符号锚点，不作本表统计推断。推断进入第 7 天 hold-out 与第 58 天按年切分之后。开发侧读定理时，应默认问：**残差是否交换、`X` 是否含未来列**——本课两者都刻意保持最简单，以便只隔离估计器差异。

---

## 拓展领域

**检索 vs 参数化**在量化中常对应：k-NN / 相似日匹配（样本内易过拟合已见标签）与线性因子、风格回归（残差承载模型类误差）。Breiman（2001）的两种文化——数据模型与算法模型——本课以 1-NN 与 OLS 并排，为第 44 天起的 **树 / 分段** 模型预留同一面板上的对照。

文献锚点（非虚构）：Gauss–Markov / BLUE（Aitken, 1935; Markov, 1900; Lehmann & Casella, 1998）；1-NN 理论（Cover & Hart, 1967）；局部方法（Hastie, Tibshirani & Friedman, 2009, ESL §2）；无免费午餐（Wolpert, 1996）——训练集检索优势不能外推为任意分布最优。

全季衔接：第 2–3 天 L1/L2 分解；第 4 天端点弦（同仿射类、不同约束）；第 9 天行置换不变 `β̂`。工程上忌将 in-support 1-NN 平均误差写成样本外 alpha；忌单点 8.2 而不报其余四日残差符号与幅度。

**平方损失与 robustness 的前奏**：8.21 在 RSS 中权重为 67.4 量级，占五点和的约 70%（第 3 天会精确到 0.6997 份额）。若研究转向 L1 或 Huber，第四日仍可能主导，但 **排序** 会改变——这属于 **损失选择** 而非 **换 ticker**。量化开发在接数据管道前，应先问默认损失是 L2 还是业务损失（例如方向 hit、计费表），本季前 10 日系统回答这个问题。

**相似日 / 协变量匹配**：生产系统中的「找相似 K 线」若允许在 **含当日标签** 的特征空间里度量距离，in-sample 检索误差可接近零；若特征含 **未来字段**（第 28–29 天的 FORBIDDEN 行），则属于泄漏而非 1-NN 理论问题。区分 **估计器** 与 **特征工程** 是 senior 工程师 daily review 的基本项。

**数值与复现**：`line=` 列与 `y = 3.27 x + -1.29` 在五位打印下自洽；若读者用双精度重算斜率，末位可能与 3.27 差 0.01，但 **miss 8.2** 与脚本一致即可。全季以仓库 stdout 为 **单一真相源**，回归测试应对 `text` 块做 diff，而不是对 PDF 手抄数。

**横截面 vs 时间序列（预告）**：五个点既可读成「五个交易日」，也可读成「五个抽象索引」。第 21 天接入 `panel.csv` 后，索引变为真实日期；第 38 天会对 **信号滞后** 单独开一课。本课尚未引入日期类型，但 OLS 已假设 **行可交换**（第 9 天证明行置换不动 `β̂`），这对时间序列是 **错误默认**——后续用切分修正，而非在本日改 OLS 公式。

**Hat matrix 视角（五点的闭式直觉）**：OLS 拟合值 `ŷ = Hy`，在经典线性模型中 `H` 为对称幂等。对 **在训练坐标上评估** 的查询，1-NN 等价于 `H` 为置换矩阵的某行；OLS 的 `H` 为平滑矩阵，第四行对五个标签的权重 **全非零**，故 11.79 吸收了整个样本信息。理解 `H_ii`（杠杆）可解释为何某些交易日 in-sample 拟合「过贴」——第 5 天删点会改变斜率（第 5 课），即杠杆点的另一种表现。

**审计清单（本日可执行）**：打开 stdout → 确认 `ask x=4.0` 与 `stored y=20.0` → 核对 `memorized` 与 `fitted` 两行 → 用 `train points` 第四行验证 11.79 与 8.2 四舍五入关系 → 在 research log 写「1-NN vs OLS，in-support query，水平绝对误差，未做样本外」。五步完成即满足内部 quant dev 对 **day-1 实验** 的最低披露标准。

**与生产代码的映射**：回测框架里的 `predict()` 若在 `date` 已存在于训练索引时走 **cache lookup**，metrics 模块却报告 `mse_oos`，就属于本课左支误标为样本外。代码审查应 grep「merge_asof / reindex / loc 精确命中」与 metrics 命名是否一致。OLS 路径对应 `LinearRegression.fit` 全样本再 `predict` 同索引——右支。两路径 **可以共存**，但 report 必须分表，否则 PM 看到的 Sharpe 没有定义。


混池实验（如第37课）与单名实验（如第27课）不得共用一个 leaderboard；第1课文档应在开头声明主语范围。

FORBIDDEN 特征课（如第28课）说明：in-sample RSS 下降可能是泄漏信号；第1课写模型比较时禁止用非法列作优选依据。

缺失填充课（如第34课）提醒：pandas 默认 bfill 在 pipeline 里很常见；第1课起应在 CI 里 grep fillna 方向。

标准化泄漏（如第33课）说明：test MSE 相等不能证明无泄漏；第1课应把 scale 来源写入 model card。

时间切分课（如第27课）的「测试在训练之后」是因果最低标准；第1课若改切分为随机，必须另开对照行而不覆盖 time 行。

随机切分对照（如第26课）只能叫 control，不能叫 walk-forward；第1课命名错误会导致合规审查失败。

事件规则课（如第23–24课）强调规则先于计数；第1课若事后改 pattern 长度，events 与 accuracy 都不具可比性。

双分数课（如第25课）说明水平误差与方向误差可分离；第1课策略若为 sign book，primary metric 必须指向 direction。

成本门（如第39课）应在 hit rate 之前进入；第1课若未扣费，memo 应显式写「未含 transaction cost」。

泄漏清单（第40课）是 negative catalog；第1课新特征应主动问：是否会出现在未来某天的 list 行上。

停牌间隔（如第35课）改变 row-lag 语义；第1课构造 rolling 特征时应使用 calendar index 而非 raw row shift。

复权口径（如第36课）要求双列披露；第1课任何 return 图表必须标注 adj 或 raw，禁止混用。

窗口均值（如第30–32课）区分 full sample 与 lookback；第1课 feature 命名建议带 window 长度后缀。

市场同期信号（如第38课）与 lag 市场对照；第1课 merge 外部指数时务必 asof 对齐到前一可用观测。

固定 panel（第21课）之后所有数字绑同一 CSV；第1课改路径或增行属于 dataset 版本 bump，不是代码 refactor。

lag-1 方向（第22课）是最简 autocorr sign 游戏；第1课扩展至多元时，先确认单变量基线仍复现 36/77。

三连规则（第23课）样本稀疏；第1课 bootstrap 或 permutation 若做，须在 hold-out 段而非 in-sample 挑规则。

early 非 score（第24课）是防 peek 文案；第1课 dashboard 应把 non-score 段视觉降级（灰显）。

open scale 泄漏（第29课）差 0.0008 量级小但性质严重；第1课 security review 应看公式分母而非看 delta RSS。

high FORBIDDEN（第28课）教 bar 内同步；第1课 intraday 特征更严格，decision time 须早于 bar end。

第1课与第7天 hold-out 精神一致：参与拟合的行不得参与评分；任何「全样本 fit 再全样本 score」须打 in-sample 标签。

第1课与第9天行置换对照：shuffle 行不改 OLS 系数，但 shuffle 时间戳会破坏 lag；panel 课默认时间有序。

第1课与第20天噪声列对照：扩大列空间可降训练 RSS 但恶化留出；panel 上应用切分重复该实验。

第1课写 commit message 时建议带 verify day 号；例如「docs: day-1 sync stdout golden」。

第1课英文键名中的空格与等号两侧空格是 diff 的一部分；自动格式化工具不得 strip 终端行。

第1课 mermaid 节点数字必须来自 stdout；勿在图里写未打印的四舍五入值。

第1课表格是解释层；若表格数字与 text 块冲突，以 text 块为准并修表。

第1课读者若是风控，应关注泄漏 list 与 FORBIDDEN；若是执行，应关注 cost 与 halt gap。

第1课读者若是数据工程，应关注 panel identity 与 imputation；若是 PM，应关注 estimand 一句话。

第1课扩展阅读：Lopez de Prado 的 purged k-fold 用于解决标签重叠；本季未实现但应知存在。

第1课扩展阅读：White (1980) 异方差稳健协方差；方向 accuracy 的渐近方差本季未算。

第1课扩展阅读：Newey-West 对重叠 horizon；若 future 改 weekly label，推断必须换 HAC。

第1课扩展阅读：Harvey (2016) 多重 backtest 试验；勿在 100 seed 里挑最好 day 26 数字。

第1课扩展阅读：Hasbrouck (2007) 有效 spread；第39课常数 cost 是其极简替身。

第1课扩展阅读：Breiman (2001) 两种文化；panel 段在算法文化与数据文化间切换。

第1课扩展阅读：Hamilton (1994) 时间序列；rolling 与 expanding 的信息集差异是核心。

第1课扩展阅读：Little & Rubin (2002) 缺失；MCAR/MAR 本季不辨，但 fill 方向必辨。

第1课扩展阅读：Campbell et al. (1997) 预测回归；lag 结构改变即改变 stochastic 设定。

第1课若接入实时行情，应重建 frozen panel 快照而非 mutate 历史文件；live 与 research 分离。

第1课若在 notebook 跑脚本，working directory 必须是仓库根；否则 panel 相对路径失败。

第1课若在 Docker 跑，镜像应 pin numpy 与 csv 版本；否则 float 末位可能 drift。

第1课 unit test 可 mock 小 csv，但 golden 仍以官方 panel 为准；mock 只测逻辑不测数值。

第1课 code review 可要求作者贴 verify 输出片段；无 verify 的 doc PR 不应 merge。

---

## 实战总结

```bash
python days/01-line-that-misses/fit_line.py
```

核对：`line: y = 3.27 x + -1.29`；`memorized neighbor … miss 0.0`；`fitted line … miss 8.2`。几何对照见 [`site`](../../site)（第四日竖直距离对应 8.2 量级）。

若做 CI：将本脚本 stdout 全文放入 golden file；改 `lstsq` 或数据路径时，diff 应只在预期 commit 出现。文档侧维护 **单一** `text` 块与终端一致，避免在正文重复粘贴第二份数字表，以免日后漂移。后续各课在 **同一 panel** 上叠加切分、因子与模型时，仍建议保留这种「终端即合同」的习惯，以便 code review 只盯一处输出。本课无交易、无费率、无持仓变量。
