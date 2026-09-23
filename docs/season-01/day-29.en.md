<p align="center"><a href="day-29.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 29 · Standardize with a future open

[Phase I · Models](../../README.en.md) · runs

Scaling the close by the mean and standard deviation of every open, including opens after that close, gives a return-regression RSS of 0.2642. Scaling by past closes only gives 0.2650. The difference is 0.0008. Leakage is identified because later opens are arguments of the scale, not because the score improved.

```bash
python days/29-future-open/future_open.py
```

```text
leaky scale uses every open, including later ones
RSS of return on leaky close = 0.2642
RSS of return on past-only close = 0.2650
the leaky scale is a function of later opens
```

Next each day may see only a fixed window of the past. The whole history is no longer fit at once.
