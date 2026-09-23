<p align="center"><a href="day-51.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 51 · Linear weights on five lags

[Phase I · Models](../../README.en.md) · runs

What you learn today: On AAA, five lagged simple returns predict the same-day return. OLS: lag1=−0.1359, lag2=0.0829, lag3=0.1094, lag4=−0.1726, lag5=−0.0803, intercept=0.0023. Min −0.1726, max 0.1094, test MSE=0.000081. Same magnitude, not equal weights.

## Plain-language account

Each row is a card: five lagged simple returns on the left, same-day return on the right. Train is the first seventy-five percent in time order. The line picks five weights plus intercept to shrink train squared error.

Weights are not 0.2 each. lag4=−0.1726 has largest magnitude; lag3=0.1094 is largest positive; lag1=−0.1359. lag2=0.0829 and lag5=−0.0803 are smaller but same order of magnitude. Intercept 0.0023 is the stack constant, not a sixth lag.

Test MSE 0.000081 is on nineteen hold-out rows with frozen train coefficients. Min–max gap ~0.28 rejects equal weights. Alternating signs mean a weighted sum, not lag1 only.

Do not paste day-46 price SSE or day-42 full-sample slope here. The feature chain is five lags on same-day return.

## Core

```text
weight lag 1 = -0.1359
weight lag 2 = 0.0829
weight lag 3 = 0.1094
weight lag 4 = -0.1726
weight lag 5 = -0.0803
intercept = 0.0023
weight min = -0.1726  weight max = 0.1094
test MSE = 0.000081
```

## Further out

Equal-weight lags are a standard control on the same table. Magnitudes sit near 0.08–0.17, so every lag enters. Weights are not causal shares; another split, name, or volume column moves the vector.

Next lesson: one stump on the same table. 0.000081 is the line ruler on the later stretch. Do not read it as direction hit rate; this day prints return MSE only.

## What the run showed

```bash
python days/51-five-lag-weights/five_lag_weights.py
```

The script should print `lags = 1 through 5`, five `weight lag` lines, `intercept = 0.0023`, weight min/max, `test MSE = 0.000081`. The implementation is [`five_lag_weights.py`](../../days/51-five-lag-weights/five_lag_weights.py).

Hand in five lag weights and test MSE 0.000081. Next: one stump on the same lags.
