<p align="center"><a href="#zh"><b>中文</b></a> &nbsp;&nbsp;·&nbsp;&nbsp; <a href="#en">English</a></p>

<a id="zh"></a>

# 第 1 天 · 样本内最近邻与普通最小二乘

[第一阶段 · 模型](README.md) · 可运行

本日比较两个估计器在同一次查询上的样本内残差。数据是五个交易日的收盘价。查询点 `x = 4` 落在训练集内部，不是留出点。

最近邻因此复述该点标签，残差为 0。普通最小二乘在仿射函数类里最小化残差平方和，拟合值到不了 20，残差为 8.2。零残差来自查表，非零残差来自模型类。

---

## 样本

记第 `t` 个交易日的收盘为 `y_t`，`t = 1,…,5`。除第四日外，序列大致以每日约 2 的斜率上升。第四日收盘为 20，是这五个点里对平方损失影响最大的观测。

| t | 收盘 y | OLS 拟合值 ŷ | 残差 y − ŷ |
|---:|---:|---:|---:|
| 1 | 2.1 | 1.98 | 0.12 |
| 2 | 3.9 | 5.25 | −1.35 |
| 3 | 6.2 | 8.52 | −2.32 |
| **4** | **20.0** | **11.79** | **8.21** |
| 5 | 10.4 | 15.06 | −4.66 |

拟合值取自脚本的两位小数。第四日残差 `20.0 − 11.79 = 8.21`，输出记为 **8.2**。

---

## 估计器一 · 最近邻

查询 `x`，在训练集里取

```text
î = argmin_i |x_i − x|
ŷ = y_î
```

这里 `x_i = i`。查询恰好等于某个训练横坐标时，最近邻就是该点本身，估计值等于标签，样本内残差恒为 0。

对 `x = 4`：

| | |
|---|---|
| 估计 | 20.0 |
| 残差 | 0 |

这个 0 没有使用其余四个收盘。它只说明查询点落在训练支撑上，标签被原样检索。把同一规则用到训练支撑之外，估计值只能复制最近的已见标签。那是第 6 天的题目。

---

## 估计器二 · 普通最小二乘

假设类是仿射函数 `ŷ = β₁ x + β₀`。设计矩阵的第 `i` 行是 `[x_i, 1]`。系数是残差平方和的最小值点：

```text
β̂ = argmin_β || y − Xβ ||²
```

五个点上的闭式解，打印到两位小数，为

```text
ŷ = 3.27x − 1.29
```

在查询点代入：`3.27 × 4 − 1.29 = 11.79`。

| | |
|---|---|
| 估计 | 11.79 |
| 残差 | 8.2 |

平方损失让离群收盘的权重高于贴近直线的点。即便如此，OLS 也不会把整条直线抬到 20：那样做会增大其余四点的残差平方，总损失上升。11.79 是这条直线对五个点的妥协，8.2 是第四日为此付出的样本内残差。

五个残差有正有负。直线没有「放过」某一个点的特殊规则，它只是不能同时零化五个残差。第四日的残差最大，因为它离开其余四点所支撑的斜率最远。

---

## 并排

| 估计器 | 在 x = 4 的输出 | 样本内残差 | 残差为何是这个数 |
|---|---:|---:|---|
| 最近邻 | 20.0 | 0 | 查询点与训练点重合，输出等于标签 |
| OLS | 11.79 | 8.2 | 仿射函数类下的残差平方和最小解 |

> 参数化均值不是训练标签的检索。查询点落在训练支撑上时，最近邻残差为零；直线的残差是模型类的近似误差。

---

## 复现

仓库根目录，Python 3.8 及以上：

```bash
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
python days/01-line-that-misses/fit_line.py
```

脚本应打印 `y = 3.27 x + -1.29`、最近邻残差 `0.0`、直线残差 `8.2`。实现是 [`fit_line.py`](../../days/01-line-that-misses/fit_line.py)，用 `numpy.linalg.lstsq` 解上述最小二乘，没有迭代。

同一组 `y` 与拟合值画在 [`site`](../../site)。该目录执行 `npm install`，再执行 `npm run dev`。第四日的点在 20，直线过 11.79，竖线标出残差 8.2。页面不生成订单。后续回测使用历史行情，不接实盘。

---

## 本日的边界

这不是样本外评估。查询点属于训练集，最近邻的零残差不能外推成「模型有效」。

| 后续 | 收走的便利 |
|---|---|
| 第 2 天 | 同一残差要同时报告绝对损失与平方损失。平方损失会进一步提高第四日的权重 |
| 第 6 天 | 查询训练支撑之外的点。最近邻只能复制邻点，直线必须外推 |
| 第 7 天 | 将第五日留出。训练集上的残差不再作为成绩 |

---

<a id="en"></a>

<p align="center"><a href="#zh">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <a href="#en"><b>English</b></a></p>

# Day 1 · In-sample nearest neighbor and ordinary least squares

[Phase I · Models](README.en.md) · runs

Two estimators, one query, in-sample residuals only. The series is five closing prices. The query `x = 4` lies inside the training set. It is not a holdout.

The nearest neighbor therefore repeats that point's label and the residual is 0. Ordinary least squares minimizes the residual sum of squares inside the affine class, cannot place the fitted value at 20, and leaves a residual of 8.2. A zero residual here is retrieval. A nonzero residual is the approximation error of the model class.

---

## Sample

Let `y_t` be the close on session `t`, for `t = 1,…,5`. Aside from session 4, the path rises by about 2 per day. The close at 20 is the observation with the largest pull on squared loss.

| t | Close y | OLS fit ŷ | Residual y − ŷ |
|---:|---:|---:|---:|
| 1 | 2.1 | 1.98 | 0.12 |
| 2 | 3.9 | 5.25 | −1.35 |
| 3 | 6.2 | 8.52 | −2.32 |
| **4** | **20.0** | **11.79** | **8.21** |
| 5 | 10.4 | 15.06 | −4.66 |

Fitted values are the script's two-decimal print. The session-4 residual is `20.0 − 11.79 = 8.21`, reported as **8.2**.

---

## Estimator 1 · Nearest neighbor

For a query `x`,

```text
î = argmin_i |x_i − x|
ŷ = y_î
```

with `x_i = i`. When the query coincides with a training abscissa, the neighbor is that point, the estimate equals the label, and the in-sample residual is identically 0.

At `x = 4`:

| | |
|---|---|
| Estimate | 20.0 |
| Residual | 0 |

That 0 does not use the other four closes. It records that the query sits on the training support and the label was retrieved. Outside that support the same rule can only copy the nearest observed label. That is day 6.

---

## Estimator 2 · Ordinary least squares

The hypothesis class is the affine map `ŷ = β₁ x + β₀`. Row `i` of the design matrix is `[x_i, 1]`. The coefficient is the minimizer of the residual sum of squares:

```text
β̂ = argmin_β || y − Xβ ||²
```

The closed form on these five points, printed to two decimals, is

```text
ŷ = 3.27x − 1.29
```

At the query: `3.27 × 4 − 1.29 = 11.79`.

| | |
|---|---|
| Estimate | 11.79 |
| Residual | 8.2 |

Squared loss weights the outlying close more than the points that already lie near a line. OLS still does not lift the whole line to 20. Doing so would increase the squared residuals of the other four points, and the total loss would rise. 11.79 is the compromise of one line across five points. 8.2 is the in-sample residual session 4 pays for that compromise.

The five residuals change sign. The line has no special rule that spares one point. An affine function cannot zero all five residuals at once. Session 4 has the largest residual because it sits farthest from the slope supported by the other four.

---

## Side by side

| Estimator | Output at x = 4 | In-sample residual | Why the residual is this number |
|---|---:|---:|---|
| Nearest neighbor | 20.0 | 0 | The query coincides with a training point, so the output is the label |
| OLS | 11.79 | 8.2 | Minimizer of residual sum of squares in the affine class |

> A parameterized mean is not a retrieval of the training label. On the training support the nearest-neighbor residual is zero. The residual of the line is the approximation error of the model class.

---

## Reproduce

From the repository root, Python 3.8 or newer:

```bash
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
python days/01-line-that-misses/fit_line.py
```

The script should print `y = 3.27 x + -1.29`, a nearest-neighbor residual of `0.0`, and a line residual of `8.2`. The implementation is [`fit_line.py`](../../days/01-line-that-misses/fit_line.py). It calls `numpy.linalg.lstsq` for the least squares above. There is no iteration.

The same `y` and fitted values are drawn in [`site`](../../site). From that directory, run `npm install`, then `npm run dev`. Session 4 sits at 20, the line passes through 11.79, and the vertical segment marks the residual 8.2. The page does not emit an order. Later backtests use historical prices, not a live book.

---

## What this day is not

This is not an out-of-sample evaluation. The query belongs to the training set. A zero nearest-neighbor residual does not transfer into a claim that the estimator works.

| Later | Convenience removed |
|---|---|
| Day 2 | The same residual must be reported as absolute loss and as squared loss. Squared loss raises the weight of session 4 further |
| Day 6 | Query a point outside the training support. The neighbor can only copy. The line must extrapolate |
| Day 7 | Hold out session 5. Residuals on the fitting set no longer count as the score |

---

<p align="center"><a href="day-01.md#zh">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <a href="day-01.md#en"><b>English</b></a></p>

English is on the [same note](day-01.md#en).
