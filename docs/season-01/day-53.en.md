<p align="center"><a href="day-53.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 53 · Random seed

[Phase I · Models](../../README.en.md) · runs

What you learn today: linear lag1=−0.1359; seed0 tree lag1 0.076142; seed1 tree lag4 −0.020177; line unchanged

## Plain-language account

Day 53's numbers come from script stdout, not hand-filled values. 直线用全训练 seventy-five percent. 树在 90% 子样本上重选 stump：seed0 切 lag1，seed1 切 lag4. 打印再次 linear lag1=−0.1359. 

The panel is days/data/panel.csv, name AAA, simple returns from adjusted close. Train is the first seventy-five percent in time order unless this script changes the cut. Hold-out rows score MSE only; coefficients are not re-fit there. Same-bar high, low, close are not features; same-day market is not a result.

Separate train from test: parameters on train, MSE on hold-out mean squared error. linear lag1=−0.1359; seed0 tree lag1 0.076142; seed1 tree lag4 −0.020177; line unchanged

Return MSE is not price-level SSE from days 45–46. Claims serve this print only.

## Core

```text
linear weight lag 1 = -0.1359
seed = 0 tree split lag = 1 threshold = 0.076142
seed = 1 tree split lag = 4 threshold = -0.020177
linear weight lag 1 after tree seeds = -0.1359
```

## Further out

Cross-check stdout against the page: key names, signs, and six decimals should match the terminal. linear lag1=−0.1359; seed0 tree lag1 0.076142; seed1 tree lag4 −0.020177; line unchanged

Keep forbidden rules beside MSE in the lab notebook. If the next lesson changes the cut or target, open a new log row instead of overwriting today's numbers.

## What the run showed

```bash
python days/53-random-seed/random_seed.py
```

The script should print stdout lines matching the core block. The implementation is [`random_seed.py`](../../days/53-random-seed/random_seed.py).

Hand in the printed numbers and rule lines for day 53. Keep the script path for reruns.
