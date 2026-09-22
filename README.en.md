<p align="center"><a href="README.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

<h1 align="center">Observation Deck</h1>

<p align="center">A price study in four phases. One hundred days in each phase. One reproducible calculation each day.</p>

<br>

Query `x = 4`, inside the training set.

| | Nearest neighbor | Ordinary least squares |
|---|---:|---:|
| In-sample residual | 0 | 8.2 |
| Output | 20.0 | 11.79 |

<p align="center">Fit &nbsp; <code>ŷ = 3.27x − 1.29</code></p>

<p align="center">
<a href="docs/season-01/day-01.en.md">Day 1</a>
&nbsp;&nbsp;·&nbsp;&nbsp;
<a href="days/01-line-that-misses/fit_line.py">Implementation</a>
&nbsp;&nbsp;·&nbsp;&nbsp;
<a href="site">Curve</a>
</p>

## Reproduce

Python 3.8 or newer, from the repository root.

```bash
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
python days/01-line-that-misses/fit_line.py
```

The curve is in [`site`](site). From that directory, run `npm install`, then `npm run dev`.

## Phases

| Phase | Subject |
|---|---|
| Phase I | [**Models**](docs/season-01/README.en.md) |
| Phase II | **Factors** |
| Phase III | **Portfolio and constraints** |
| Phase IV | **Execution** |

<p align="right"><sub>Notes from 2019 are in <a href="archive/2019">archive/2019</a></sub></p>
