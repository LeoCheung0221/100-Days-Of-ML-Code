<p align="center"><a href="README.md">中文</a> · <b>English</b></p>

# 🛰️ Observation Deck

**One session a day. One hundred days a season. The constraint only gets tighter.**

✨ For people who already write programs, this window looks at price.  
📉 Each day you run one piece of code and leave one sentence another engineer can repeat: where this model is wrong on these prices.  
🧭 The 2019 notes are in [`archive/2019`](archive/2019). The series index is in [`docs`](docs/README.en.md).

---

## 🗺️ Four seasons

| Season | The question | What day 100 must be able to say | Where |
|---|---|---|---|
| **01 · Models** | Is this line, or this tree, lying about its score | Through which date, which columns are forbidden, which three mistakes, and why there is no order | [Day list](docs/season-01/README.en.md) · day 1 runs |
| **02 · Factors** | Does this number have a stable cross-sectional link to the next return | Which factor clears the bar, and which one was dropped for peeking or for being a copy | [Outline](docs/seasons-outline.md) · not open |
| **03 · Books and constraints** | After missed fills and costs, does it still beat the benchmark | Universe, score, weights, constraints, excess return after costs | [Outline](docs/seasons-outline.md) · not open |
| **04 · Execution** | When the list becomes a book, how far are price and size from the plan | The gap between the signal price and the assumed fill, and why the season stops on paper | [Outline](docs/seasons-outline.md) · not open |

Season 2 opens after season 1 has finished leakage. Season 4 stops at a paper ledger.

---

## Day 1 · In-sample residual

The query `x = 4` lies in the training set. The nearest neighbor retrieves the close **20.0** and the residual is **0**. Ordinary least squares minimizes the residual sum of squares in the affine class, fits **11.79**, and leaves a residual of **8.2**. The zero is retrieval. The 8.2 is the part of the close an affine model cannot match.

| Day | Close y | OLS fit |
|---|---:|---:|
| 1 | 2.1 | 1.98 |
| 2 | 3.9 | 5.25 |
| 3 | 6.2 | 8.52 |
| **4** | **20.0** | **11.79** |
| 5 | 10.4 | 15.06 |

| Estimator | Output at x = 4 | Value | In-sample residual |
|---|---|---:|---:|
| Nearest neighbor | Query coincides with a training point, so the output is the label | 20.0 | 0 |
| OLS | `ŷ = 3.27x − 1.29` | 11.79 | 8.2 |

> A parameterized mean is not a retrieval of the training label. On the training support the nearest-neighbor residual is zero. The residual of the line is the approximation error of the model class.

[Full lesson](docs/season-01/day-01.en.md) · [Code](days/01-line-that-misses) · [The hundred days](docs/season-01/README.en.md)

```bash
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
python days/01-line-that-misses/fit_line.py
```

The same numbers are drawn in [`site`](site). From that directory, run `npm install`, then `npm run dev`.

---

## 🧭 The shape of a day

| | What you leave behind |
|---|---|
| **Compare** | Two habits, one set of prices |
| **Run** | One file, printed error |
| **Say** | One sentence on where the miss comes from |

No orders. Prices are historical closes. When this later meets the LAT backtest, the day still has these three steps.

Each day removes one shortcut that the previous day still allowed.
