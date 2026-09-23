<p align="center"><b>中文</b> &nbsp;&nbsp;·&nbsp;&nbsp; <a href="README.en.md">English</a></p>

<h1 align="center">100 Days of Quant ML</h1>

<p align="center">
  <a href="#phase-1">📘 第一阶段 · 模型</a>
  &nbsp;·&nbsp;
  <span>🔜 因子</span>
  &nbsp;·&nbsp;
  <span>🔜 组合与约束</span>
  &nbsp;·&nbsp;
  <span>🔜 执行</span>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8-blue?logo=python&logoColor=white" alt="Python 3.8" />
  <img src="https://img.shields.io/badge/Stack-NumPy%20%2B%20OLS-222?logo=numpy" alt="NumPy OLS" />
  <img src="https://img.shields.io/badge/Panel-frozen%20CSV-2ea44f" alt="panel" />
  <img src="https://img.shields.io/badge/Style-reproducible%20stdout-555" alt="stdout" />
</p>

---

## 📊 项目定位

**100 Days of Quant ML** 是一套 **价格研究向** 的百日练手：每天 **一篇可读笔记 + 一段可复现脚本**，终端输出与文档里的数字 **逐行对齐**。不是「调包跑策略」，而是从 **损失函数、切分、泄漏、基准、树与直线** 把量化 ML 的底盘练到能 **对着 stdout 讲清楚为什么还没法下单**。

> 🎯 **适合谁**：有 Python 基础、想走 **量化开发 / 研究工程师** 路线的人——需要会看残差、会写 hold-out、敢在组里解释 **哪一列不能用**。

---

## 🧭 四阶段地图（400 日规划）

| | 阶段 | 量化方向 | 本仓库状态 |
|:---:|:---|:---|:---:|
| 📘 | **模型** | 收益预测 · 分类 · 面板 lag · 树/岭/基准 · 波动 regime · 失败叙事 | **进行中** |
| 📈 | 因子 | 因子构造 · 检验 · 中性化 | 规划中 |
| ⚖️ | 组合与约束 | 权重 · 风险预算 · 约束优化 | 规划中 |
| 🛰 | 执行 | 成交 · 滑点 · 成本 · 实盘差距 | 规划中 |

---

## 🛠 第一阶段会碰到的技巧与基本功

**量化方向（Phase I 覆盖）**

- 📉 **价格与收益**：水平拟合 → 方向标签 → 下一日收益 · 超额 · 零基准  
- 🧱 **面板与 lag**：冻结 `panel.csv` · lag-5 设计矩阵 · 多标的对齐 · 换名复跑  
- 🌊 **状态与 regime**：quiet / jump · ISO 周波动分层 · 残差计数表 · 按表选型  
- 🧪 **研究纪律**：时间切分 · 拒绝清单 · 泄漏修补 · 十行 manifest · 全流程复跑  

**ML / 统计基本功**

- 📐 **损失与误差**：L1 / L2 · RSS 拆向量 · 水平 vs 方向  
- ✂️ **切分与验证**：留出 · 随机 vs 时间 · 按年 hold-out · 删主导月  
- 🌲 **模型族**：OLS · 岭 · 浅层/深层树 ·  stump · 三模型投票  
- 📏 **评价与对比**：MSE · 方向命中 · 置信分位 · 差异化计费 · 树线账单  

**工程习惯**

- 🖥 **可复现**：每课 `python days/…` · ` ```text` 块 ≡ 终端  
- 🚫 **反泄漏**：同日 OHLC · 未来标准化 · 市场列前移 —— 用脚本 **拒绝** 而非口头  
- 📝 **可沟通**：第 86–100 日把 **数据区间、列可用性、三个失手日** 写成他人可复述的讲稿  

---

<a id="phase-1"></a>

## 📚 第一阶段 · 模型 · 目录

<!-- DAY_LIST -->

---

<p align="right"><sub>📦 2019 年笔记见 <a href="archive/2019">archive/2019</a></sub></p>
