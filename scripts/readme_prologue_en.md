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

<!-- DAY_LIST -->

---

<p align="right"><sub>📦 Notes from 2019: <a href="archive/2019">archive/2019</a></sub></p>
