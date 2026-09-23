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

- [第01天　最近邻与普通最小二乘](docs/season-01/day-01.md)
- [第02天　绝对误差与平方误差](docs/season-01/day-02.md)
- [第03天　五天残差并排](docs/season-01/day-03.md)
- [第04天　端点连线](docs/season-01/day-04.md)
- [第05天　去掉第四日再拟合](docs/season-01/day-05.md)
- [第06天　训练支撑外的查询](docs/season-01/day-06.md)
- [第07天　留出第五日](docs/season-01/day-07.md)
- [第08天　三日窗口](docs/season-01/day-08.md)
- [第09天　打乱日期](docs/season-01/day-09.md)
- [第10天　涨跌方向](docs/season-01/day-10.md)
- [第11天　涨跌标签](docs/season-01/day-11.md)
- [第12天　阈值](docs/season-01/day-12.md)
- [第13天　阈值灵敏度](docs/season-01/day-13.md)
- [第14天　常数基准](docs/season-01/day-14.md)
- [第15天　两类误分](docs/season-01/day-15.md)
- [第16天　上涨程度](docs/season-01/day-16.md)
- [第17天　置信核对](docs/season-01/day-17.md)
- [第18天　涨幅与成交量](docs/season-01/day-18.md)
- [第19天　未缩放的成交量](docs/season-01/day-19.md)
- [第20天　噪声列](docs/season-01/day-20.md)
- [第21天　固定收盘表](docs/season-01/day-21.md)
- [第22天　滞后一日的方向](docs/season-01/day-22.md)
- [第23天　连续三日同向](docs/season-01/day-23.md)
- [第24天　规则移到下一段](docs/season-01/day-24.md)
- [第25天　方向与价格并报](docs/season-01/day-25.md)
- [第26天　随机切分](docs/season-01/day-26.md)
- [第27天　按时间切分](docs/season-01/day-27.md)
- [第28天　当日最高价](docs/season-01/day-28.md)
- [第29天　用未来开盘标准化](docs/season-01/day-29.md)
- [第30天　固定历史窗口](docs/season-01/day-30.md)
- [第31天　三日窗口的噪声](docs/season-01/day-31.md)
- [第32天　六十日窗口](docs/season-01/day-32.md)
- [第33天　训练集标准化](docs/season-01/day-33.md)
- [第34天　缺失的两种填法](docs/season-01/day-34.md)
- [第35天　停牌后的间隔](docs/season-01/day-35.md)
- [第36天　复权与未复权](docs/season-01/day-36.md)
- [第37天　多标的混切](docs/season-01/day-37.md)
- [第38天　信号滞后一日](docs/season-01/day-38.md)
- [第39天　最小往返成本](docs/season-01/day-39.md)
- [第40天　泄漏清单](docs/season-01/day-40.md)
- [第41天　更长样本上的直线](docs/season-01/day-41.md)
- [第42天　岭回归](docs/season-01/day-42.md)
- [第43天　局部平均](docs/season-01/day-43.md)
- [第44天　浅层树](docs/season-01/day-44.md)
- [第45天　更深的树](docs/season-01/day-45.md)
- [第46天　三种拟合换样本](docs/season-01/day-46.md)
- [第47天　线性外推](docs/season-01/day-47.md)
- [第48天　树不外推](docs/season-01/day-48.md)
- [第49天　同一跳空日](docs/season-01/day-49.md)
- [第50天　三模型投票](docs/season-01/day-50.md)
- [第51天　五日收益的线性权重](docs/season-01/day-51.md)
- [第52天　五日收益上的树](docs/season-01/day-52.md)
- [第53天　随机种子](docs/season-01/day-53.md)
- [第54天　去掉成交量](docs/season-01/day-54.md)
- [第55天　三种失手](docs/season-01/day-55.md)
- [第56天　下一日收益](docs/season-01/day-56.md)
- [第57天　拒绝当日价格](docs/season-01/day-57.md)
- [第58天　按年切分](docs/season-01/day-58.md)
- [第59天　零收益基准](docs/season-01/day-59.md)
- [第60天　线性相对基准](docs/season-01/day-60.md)
- [第61天　树相对基准](docs/season-01/day-61.md)
- [第62天　最高置信的十分之一](docs/season-01/day-62.md)
- [第63天　按月残差](docs/season-01/day-63.md)
- [第64天　去掉主导月份](docs/season-01/day-64.md)
- [第65天　第二只股票](docs/season-01/day-65.md)
- [第66天　超额收益](docs/season-01/day-66.md)
- [第67天　市场列前移](docs/season-01/day-67.md)
- [第68天　单一入口](docs/season-01/day-68.md)
- [第69天　成交假设](docs/season-01/day-69.md)
- [第70天　十行任务](docs/season-01/day-70.md)
- [第71天　三类残差](docs/season-01/day-71.md)
- [第72天　平静日](docs/season-01/day-72.md)
- [第73天　方向错误的天数](docs/season-01/day-73.md)
- [第74天　最大的五笔残差](docs/season-01/day-74.md)
- [第75天　差异化计费](docs/season-01/day-75.md)
- [第76天　漏报与误报](docs/season-01/day-76.md)
- [第77天　提高阈值](docs/season-01/day-77.md)
- [第78天　降低阈值](docs/season-01/day-78.md)
- [第79天　计费后重排](docs/season-01/day-79.md)
- [第80天　可承受的错误](docs/season-01/day-80.md)
- 第81天　波动分段
- 第82天　高波动周的跳空
- 第83天　低波动周的树
- 第84天　残差计数表
- 第85天　按表保留模型
- 第86天　样本区间与来源
- 第87天　列的可用性
- 第88天　再次复现
- 第89天　基准、线性、树并排
- 第90天　三个失手日
- 第91天　拒绝一个特征
- 第92天　成交假设三行
- 第93天　最小滑点
- 第94天　去掉最优月份
- 第95天　换股票，同一函数
- 第96天　一页说明
- 第97天　一处仍开放
- 第98天　补上该处
- 第99天　全流程再运行
- 第100天　讲完这次失败

---

<p align="right"><sub>📦 2019 年笔记见 <a href="archive/2019">archive/2019</a></sub></p>
