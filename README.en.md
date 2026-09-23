<p align="center"><a href="README.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

<h1 align="center">100 Days of Quant ML</h1>

<p align="center">
  <a href="#phase-1-en">📘 Phase I · Models</a>
  &nbsp;·&nbsp;
  <span>🔜 Factors</span>
  &nbsp;·&nbsp;
  <span>🔜 Portfolio</span>
  &nbsp;·&nbsp;
  <span>🔜 Execution</span>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8-blue?logo=python&logoColor=white" alt="Python 3.8" />
  <img src="https://img.shields.io/badge/Stack-NumPy%20%2B%20OLS-222?logo=numpy" alt="NumPy OLS" />
  <img src="https://img.shields.io/badge/Panel-frozen%20CSV-2ea44f" alt="panel" />
  <img src="https://img.shields.io/badge/Style-reproducible%20stdout-555" alt="stdout" />
</p>

---

## 📊 What this is

**100 Days of Quant ML** is a **price-research** track: each day **one readable note + one reproducible script**, with terminal lines **matched verbatim** in the docs. The goal is not a flashy backtest—it is to build the floor **losses, splits, leakage, baselines, lines vs trees** so you can explain **why this is not yet tradable** from stdout alone.

> 🎯 **Audience**: Python-ready learners aiming at **quant dev / research engineering**—comfortable with residuals, hold-outs, and saying **which column is forbidden** in a meeting.

---

## 🧭 Four phases (400 days planned)

| | Phase | Quant focus | In this repo |
|:---:|:---|:---|:---:|
| 📘 | **Models** | Return forecast · labels · panel lags · ridge/trees · vol regimes · failure narrative | **Active** |
| 📈 | Factors | Construction · tests · neutralization | Planned |
| ⚖️ | Portfolio | Weights · risk · constraints | Planned |
| 🛰 | Execution | Fills · slippage · costs · live gap | Planned |

---

## 🛠 Phase I skills you will drill

**Quant themes**

- 📉 **Prices & returns**: level fit → direction labels → next-day return · excess · zero baseline  
- 🧱 **Panel & lags**: frozen `panel.csv` · lag-5 design · names aligned · rerun on a second ticker  
- 🌊 **Regimes**: quiet / jump · ISO week volatility · error tables · pick a model from a cell  
- 🧪 **Research hygiene**: time split · deny lists · leak patches · ten-line manifest · full rerun  

**ML / stats core**

- 📐 **Losses**: L1 / L2 · RSS as a vector · level vs direction  
- ✂️ **Splits**: hold-out · random vs time · calendar hold-out · drop the dominant month  
- 🌲 **Model families**: OLS · ridge · shallow/deep trees · stumps · three-way vote  
- 📏 **Metrics**: MSE · direction hits · top-decile · mistake tariffs · line vs tree bill  

**Engineering habits**

- 🖥 **Repro**: run `python days/…` · doc ` ```text` ≡ terminal  
- 🚫 **Anti-leak**: same-row OHLC · future scaling · shifted market column — **rejected in code**  
- 📝 **Communication**: days 86–100 compress **dates, allowed columns, three failure days** into a talk track  

---

<a id="phase-1-en"></a>

## 📚 Phase I · Models · index

- [Day 01　最近邻与普通最小二乘](docs/season-01/day-01.en.md)
- [Day 02　绝对误差与平方误差](docs/season-01/day-02.en.md)
- [Day 03　五天残差并排](docs/season-01/day-03.en.md)
- [Day 04　端点连线](docs/season-01/day-04.en.md)
- [Day 05　去掉第四日再拟合](docs/season-01/day-05.en.md)
- [Day 06　训练支撑外的查询](docs/season-01/day-06.en.md)
- [Day 07　留出第五日](docs/season-01/day-07.en.md)
- [Day 08　三日窗口](docs/season-01/day-08.en.md)
- [Day 09　打乱日期](docs/season-01/day-09.en.md)
- [Day 10　涨跌方向](docs/season-01/day-10.en.md)
- [Day 11　涨跌标签](docs/season-01/day-11.en.md)
- [Day 12　阈值](docs/season-01/day-12.en.md)
- [Day 13　阈值灵敏度](docs/season-01/day-13.en.md)
- [Day 14　常数基准](docs/season-01/day-14.en.md)
- [Day 15　两类误分](docs/season-01/day-15.en.md)
- [Day 16　上涨程度](docs/season-01/day-16.en.md)
- [Day 17　置信核对](docs/season-01/day-17.en.md)
- [Day 18　涨幅与成交量](docs/season-01/day-18.en.md)
- [Day 19　未缩放的成交量](docs/season-01/day-19.en.md)
- [Day 20　噪声列](docs/season-01/day-20.en.md)
- [Day 21　固定收盘表](docs/season-01/day-21.en.md)
- [Day 22　滞后一日的方向](docs/season-01/day-22.en.md)
- [Day 23　连续三日同向](docs/season-01/day-23.en.md)
- [Day 24　规则移到下一段](docs/season-01/day-24.en.md)
- [Day 25　方向与价格并报](docs/season-01/day-25.en.md)
- [Day 26　随机切分](docs/season-01/day-26.en.md)
- [Day 27　按时间切分](docs/season-01/day-27.en.md)
- [Day 28　当日最高价](docs/season-01/day-28.en.md)
- [Day 29　用未来开盘标准化](docs/season-01/day-29.en.md)
- [Day 30　固定历史窗口](docs/season-01/day-30.en.md)
- [Day 31　三日窗口的噪声](docs/season-01/day-31.en.md)
- [Day 32　六十日窗口](docs/season-01/day-32.en.md)
- [Day 33　训练集标准化](docs/season-01/day-33.en.md)
- [Day 34　缺失的两种填法](docs/season-01/day-34.en.md)
- [Day 35　停牌后的间隔](docs/season-01/day-35.en.md)
- [Day 36　复权与未复权](docs/season-01/day-36.en.md)
- [Day 37　多标的混切](docs/season-01/day-37.en.md)
- [Day 38　信号滞后一日](docs/season-01/day-38.en.md)
- [Day 39　最小往返成本](docs/season-01/day-39.en.md)
- [Day 40　泄漏清单](docs/season-01/day-40.en.md)
- [Day 41　更长样本上的直线](docs/season-01/day-41.en.md)
- [Day 42　岭回归](docs/season-01/day-42.en.md)
- [Day 43　局部平均](docs/season-01/day-43.en.md)
- [Day 44　浅层树](docs/season-01/day-44.en.md)
- [Day 45　更深的树](docs/season-01/day-45.en.md)
- [Day 46　三种拟合换样本](docs/season-01/day-46.en.md)
- [Day 47　线性外推](docs/season-01/day-47.en.md)
- [Day 48　树不外推](docs/season-01/day-48.en.md)
- [Day 49　同一跳空日](docs/season-01/day-49.en.md)
- [Day 50　三模型投票](docs/season-01/day-50.en.md)
- [Day 51　五日收益的线性权重](docs/season-01/day-51.en.md)
- [Day 52　五日收益上的树](docs/season-01/day-52.en.md)
- [Day 53　随机种子](docs/season-01/day-53.en.md)
- [Day 54　去掉成交量](docs/season-01/day-54.en.md)
- [Day 55　三种失手](docs/season-01/day-55.en.md)
- [Day 56　下一日收益](docs/season-01/day-56.en.md)
- [Day 57　拒绝当日价格](docs/season-01/day-57.en.md)
- [Day 58　按年切分](docs/season-01/day-58.en.md)
- [Day 59　零收益基准](docs/season-01/day-59.en.md)
- [Day 60　线性相对基准](docs/season-01/day-60.en.md)
- [Day 61　树相对基准](docs/season-01/day-61.en.md)
- [Day 62　最高置信的十分之一](docs/season-01/day-62.en.md)
- [Day 63　按月残差](docs/season-01/day-63.en.md)
- [Day 64　去掉主导月份](docs/season-01/day-64.en.md)
- [Day 65　第二只股票](docs/season-01/day-65.en.md)
- [Day 66　超额收益](docs/season-01/day-66.en.md)
- [Day 67　市场列前移](docs/season-01/day-67.en.md)
- [Day 68　单一入口](docs/season-01/day-68.en.md)
- [Day 69　成交假设](docs/season-01/day-69.en.md)
- [Day 70　十行任务](docs/season-01/day-70.en.md)
- [Day 71　三类残差](docs/season-01/day-71.en.md)
- [Day 72　平静日](docs/season-01/day-72.en.md)
- [Day 73　方向错误的天数](docs/season-01/day-73.en.md)
- [Day 74　最大的五笔残差](docs/season-01/day-74.en.md)
- [Day 75　差异化计费](docs/season-01/day-75.en.md)
- [Day 76　漏报与误报](docs/season-01/day-76.en.md)
- [Day 77　提高阈值](docs/season-01/day-77.en.md)
- [Day 78　降低阈值](docs/season-01/day-78.en.md)
- [Day 79　计费后重排](docs/season-01/day-79.en.md)
- [Day 80　可承受的错误](docs/season-01/day-80.en.md)
- Day 81　波动分段
- Day 82　高波动周的跳空
- Day 83　低波动周的树
- Day 84　残差计数表
- Day 85　按表保留模型
- Day 86　样本区间与来源
- Day 87　列的可用性
- Day 88　再次复现
- Day 89　基准、线性、树并排
- Day 90　三个失手日
- Day 91　拒绝一个特征
- Day 92　成交假设三行
- Day 93　最小滑点
- Day 94　去掉最优月份
- Day 95　换股票，同一函数
- Day 96　一页说明
- Day 97　一处仍开放
- Day 98　补上该处
- Day 99　全流程再运行
- Day 100　讲完这次失败

---

<p align="right"><sub>📦 Notes from 2019: <a href="archive/2019">archive/2019</a></sub></p>
