<p align="center"><b>中文</b> &nbsp;&nbsp;·&nbsp;&nbsp; <a href="day-42.en.md">English</a></p>

# 第 42 天 · 岭回归

[第一阶段 · 模型](README.md) · [排版规范](LESSON_LAYOUT.md) · 可运行

今天的学习要点：同 79 日 adj_close，λ=20000 只罚 slope；OLS slope 0.0299，ridge slope 0.0201，tilt 少 0.0098。

## 费曼法讲解

> **结论先行**：Gram 矩阵 **仅 slope 对角加 λ=20000**，截距自由；OLS slope 0.0299，ridge 0.0201，tilt 减少 0.0098——**惩罚改斜率，不是删点**（对照第 41 天删 jump 斜率不动）。

λ 须与 Σt² 同量级比较；79 点索引上 20000 足够把斜率从 0.0299 拉到 0.0201，而 λ=50 在本轴上几乎无效（非本日 stdout）。Hoerl & Kennard（1970）ridge；本课不打印 intercept，只交付两 slope。

in-sample SSE 上升是惩罚代价，数字留到第 46 天表。第 49 天两线于 jump 交叉 11.0315，十日后分离 11.3305 vs 11.2326。

> **误用**：把 0.0201 说成「截距 shrinkage」；用 day46 的 train ridge SSE 替代今日全样本斜率。

```mermaid
flowchart LR
  O["OLS 0.0299"] --> R["ridge 0.0201"]
  R --> G["Δslope 0.0098"]
```

## 核心知识

### 脚本输出（与下方 `text` 块一致）

[`ridge.py`](../../days/42-ridge/ridge.py)：

```text
lambda = 20000, penalty on the slope only
ols slope = 0.0299
ridge slope = 0.0201
```

| 估计 | slope |
|:---|---:|
| OLS | 0.0299 |
| ridge λ=20000 | 0.0201 |
| Δ | 0.0098 |

## 拓展领域

**λ 尺度。** 20000 对 Σt²；换更短 index 同 λ 压更狠。

**第 49 天交叉。** 惩罚在 crossing 后分离 level。

**价格段 vs 收益段。** 第 41–50 天 adj_close **水平** 与 SSE；第 51 天起 **lag-5 简单收益** 与 test MSE 0.000081 标尺。禁止混表。

**复现。** 仓库根目录、`numpy==1.24.4`、`days/data/panel.csv`；```text``` 与终端逐行 diff；`verify_season01_docs.py --day N`。

**泄漏。** 第 40 天清单；第 56–57 天 OHLC；第 67 天 market（后段）。feature 时间 ≤ 决策时刻。

**文献（非虚构）。** Breiman（2001）；Hoerl & Kennard（1970）；Hamilton（1994）；Campbell, Lo & MacKinlay（1997）；Harvey et al.（2016）；Lopez de Prado（2018）。

## 实战总结

```bash
python days/42-ridge/ridge.py
```

核对：将终端 stdout 与上文 ```text``` 块逐行 diff；键名与空格计入合同。改 panel 后重跑 `python3 scripts/verify_season01_docs.py --day 42`。
