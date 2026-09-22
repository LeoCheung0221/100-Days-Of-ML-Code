<p align="center"><a href="README.md">中文</a> · <b>English</b></p>

# Observation Deck

Estimation on a price series. One runnable estimator a day, and the residual it leaves on that sample.

Day 1 reproduces. The query `x = 4` lies in the training set. The in-sample residual is 0 for the nearest neighbor and 8.2 for ordinary least squares. The note is [Day 1](docs/season-01/day-01.en.md). The implementation is [`fit_line.py`](days/01-line-that-misses/fit_line.py).

## Reproduce

Python 3.8 or newer.

```bash
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
python days/01-line-that-misses/fit_line.py
```

The same closes and fitted values are drawn in [`site`](site). From that directory, run `npm install`, then `npm run dev`.

## Contents

1. [Estimation](docs/season-01/README.en.md)
2. Factors
3. Portfolio construction
4. Execution

Notes from 2019 are in [`archive/2019`](archive/2019).
