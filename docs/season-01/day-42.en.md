<p align="center"><a href="day-42.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 42 · Ridge

[Phase I · Models](../../README.en.md) · runs

The penalty is on the slope only, λ = 20000, and the intercept is free. The OLS slope is 0.0299 and the ridge slope is 0.0201. On the same adjusted closes the line is required to tilt 0.0098 less.

```bash
python days/42-ridge/ridge.py
```

```text
lambda = 20000, penalty on the slope only
ols slope = 0.0299
ridge slope = 0.0201
```

Next only the five nearby sessions are averaged. A distant jump cannot enter those neighbors.
