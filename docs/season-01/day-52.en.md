<p align="center"><a href="day-52.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 52 · A tree on five lags

[Phase I · Models](../../README.en.md) · runs

What you learn today: lag4 threshold −0.020177, left 0.0319, right −0.0014, train MSE 0.000378, test MSE 0.000174, above line 0.000081

## Plain-language account

Day 52's numbers come from script stdout, not hand-filled values. 树桩只切 lag4 一刀：≤阈值预测 0.0319，>阈值 −0.0014. train 0.000378，test 0.000174. 直线 test 仍是 0.000081. 台阶差 0.0333，不是五系数斜率. 

The panel is days/data/panel.csv, name AAA, simple returns from adjusted close. Train is the first seventy-five percent in time order unless this script changes the cut. Hold-out rows score MSE only; coefficients are not re-fit there. Same-bar high, low, close are not features; same-day market is not a result.

Separate train from test: parameters on train, MSE on hold-out mean squared error. lag4 threshold −0.020177, left 0.0319, right −0.0014, train MSE 0.000378, test MSE 0.000174, above line 0.000081

Return MSE is not price-level SSE from days 45–46. Claims serve this print only.

## Core

```text
split column = lag 4
threshold = -0.020177
left mean = 0.0319  right mean = -0.0014
train MSE = 0.000378
test MSE = 0.000174
```

## Further out

Cross-check stdout against the page: key names, signs, and six decimals should match the terminal. lag4 threshold −0.020177, left 0.0319, right −0.0014, train MSE 0.000378, test MSE 0.000174, above line 0.000081

Keep forbidden rules beside MSE in the lab notebook. If the next lesson changes the cut or target, open a new log row instead of overwriting today's numbers.

## What the run showed

```bash
python days/52-five-lag-tree/five_lag_tree.py
```

The script should print stdout lines matching the core block. The implementation is [`five_lag_tree.py`](../../days/52-five-lag-tree/five_lag_tree.py).

Hand in the printed numbers and rule lines for day 52. Keep the script path for reruns.
