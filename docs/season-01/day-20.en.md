<p align="center"><a href="day-20.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 20 · A noise column

[Phase I · Models](../../README.en.md) · runs

The noise column uses seed 0, fixed in advance. In-sample RSS on the first four sessions falls from 42.0500 to 26.7061. The absolute error on session 5 rises from 11.6500 to 18.1513. A larger column space is allowed to lower the training sum of squares. The number allowed as the score is the holdout error, and it got worse.

```bash
python days/20-noise-column/noise.py
```

```text
fit on t=1..4, score on t=5
in-sample RSS without noise = 42.0500
in-sample RSS with noise = 26.7061
holdout absolute error without noise = 11.6500
holdout absolute error with noise = 18.1513
the in-sample drop is not an improvement
```

Next the closes come from a table frozen in the repository. They are no longer written into the formula.
