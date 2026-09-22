<p align="center"><a href="README.md">中文</a> · <b>English</b></p>

# Observation Deck

**One session a day. One hundred days a season. The constraint only gets tighter.**

For people who already write programs. Each day you run one piece of code and leave one sentence another engineer can repeat: where this model is wrong on these prices.

The 2019 notes are in [`archive/2019`](archive/2019). The series index is in [`docs`](docs/README.en.md).

---

## Four seasons

| Season | The question | What day 100 must be able to say | Where |
|---|---|---|---|
| **01 · Models** | Is this line, or this tree, lying about its score | Through which date, which columns are forbidden, which three mistakes, and why there is no order | [Day list](docs/season-01/README.en.md) · day 1 runs |
| **02 · Factors** | Does this number have a stable cross-sectional link to the next return | Which factor clears the bar, and which one was dropped for peeking or for being a copy | [Outline](docs/seasons-outline.md) · not open |
| **03 · Books and constraints** | After missed fills and costs, does it still beat the benchmark | Universe, score, weights, constraints, excess return after costs | [Outline](docs/seasons-outline.md) · not open |
| **04 · Execution** | When the list becomes a book, how far are price and size from the plan | The gap between the signal price and the assumed fill, and why the season stops on paper | [Outline](docs/seasons-outline.md) · not open |

Season 2 opens after season 1 has finished leakage. Season 4 stops at a paper ledger.

---

## ✦ Day 1 is ready

Five sessions. Day 4 is pulled up to **20**. The other four sit near a line.

| Day | Close | Line |
|---|---:|---:|
| 1 | 2.1 | 1.98 |
| 2 | 3.9 | 5.25 |
| 3 | 6.2 | 8.52 |
| **4** | **20.0** | **11.79** |
| 5 | 10.4 | 15.06 |

| Habit | How it answers day 4 | Says | Miss |
|---|---|---:|---:|
| Memory | Copy the nearest close | 20.0 | 0 |
| Line | Fit all five days, then read day 4 | 11.79 | 8.2 |

The line is `y = 3.27x − 1.29`. It still has to respect the other four days, so it cannot reach 20. **8.2** is the cost of that route.

> A line does not store the prices it has seen. It chooses a route, and the day that sits off the route gets said wrong.

[Full lesson](docs/season-01/day-01.en.md) · [Code](days/01-line-that-misses) · [The hundred days](docs/season-01/README.en.md)

```bash
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
python days/01-line-that-misses/fit_line.py
```

The same numbers are drawn in [`site`](site). From that directory, run `npm install`, then `npm run dev`.

---

## ▣ The shape of a day

| | What you leave behind |
|---|---|
| **Compare** | Two habits, one set of prices |
| **Run** | One file, printed error |
| **Say** | One sentence on where the miss comes from |

No orders. Prices are historical closes. When this later meets the LAT backtest, the day still has these three steps.

Each day removes one shortcut that the previous day still allowed.
