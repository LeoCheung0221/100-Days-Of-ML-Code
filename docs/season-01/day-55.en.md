<p align="center"><a href="day-55.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 55 · Three miss modes

[Phase I · Models](../../README.en.md) · runs

What you learn today: line 0.000081, ridge 0.000098, tree 0.000174; three miss-mode English lines match script

## Plain-language account

Day 55's numbers come from script stdout, not hand-filled values. 岭 λ=20000 惩罚五 lag，截距自由. line 最小 MSE. 三句失手描述形状，不是命中率. 

The panel is days/data/panel.csv, name AAA, simple returns from adjusted close. Train is the first seventy-five percent in time order unless this script changes the cut. Hold-out rows score MSE only; coefficients are not re-fit there. Same-bar high, low, close are not features; same-day market is not a result.

Separate train from test: parameters on train, MSE on hold-out mean squared error. line 0.000081, ridge 0.000098, tree 0.000174; three miss-mode English lines match script

Return MSE is not price-level SSE from days 45–46. Claims serve this print only.

## Core

```text
test MSE line = 0.000081
test MSE ridge = 0.000098
test MSE tree = 0.000174
line miss mode = smooth blend of lags misses sharp jumps
ridge miss mode = same blend pulled toward zero misses jumps and size
tree miss mode = one lag threshold leaves a constant on each side
```

## Further out

Cross-check stdout against the page: key names, signs, and six decimals should match the terminal. line 0.000081, ridge 0.000098, tree 0.000174; three miss-mode English lines match script

Keep forbidden rules beside MSE in the lab notebook. If the next lesson changes the cut or target, open a new log row instead of overwriting today's numbers.

## What the run showed

```bash
python days/55-three-miss-modes/three_miss_modes.py
```

The script should print stdout lines matching the core block. The implementation is [`three_miss_modes.py`](../../days/55-three-miss-modes/three_miss_modes.py).

Hand in the printed numbers and rule lines for day 55. Keep the script path for reruns.
