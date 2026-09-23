<p align="center"><a href="day-78.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 78 · Low threshold speech

[Phase I · Models](../../README.en.md) · runs

What you learn today: threshold=0.0010; speaking=17; speaking MAE=0.007663.

## Plain-language account

Day 78's numbers come from script stdout, not hand-filled values. τ=0.001 时十七日 |ŷ| 够大，speaking MAE 0.007663 接近全测试 0.006980. 仅 2 日静音，说明多数预测幅度超过 0.001. 

与第 77 天对照：门槛从 0.01 降到 0.001，发言从 0 到 17，说明 |ŷ| 分布集中在 0.001–0.01 之间. 

The panel is days/data/panel.csv, name AAA, simple returns from adjusted close. Train is the first seventy-five percent in time order unless this script changes the cut. Hold-out rows are scored only; the five-lag line is not re-fit there. Same-bar high, low, close are not features; same-day market is not a result.

Separate train from test: coefficients on train, counts and MAE on nineteen hold-out rows. threshold=0.0010; speaking=17; speaking MAE=0.007663.

Return scores here are not price-level SSE from days 45–46. Claims serve this print only.

## Core

```text
threshold = 0.0010
days speaking = 17
mean abs error when speaking = 0.007663
```

## Further out

Cross-check stdout against the page: key names, signs, and decimals should match the terminal. threshold=0.0010; speaking=17; speaking MAE=0.007663.

Keep billing rules beside direction counts in the lab notebook. If the next lesson changes the cut or target, open a new log row instead of overwriting today's numbers.

## What the run showed

```bash
python days/78-low-threshold/low_threshold.py
```

The script should print stdout lines matching the core block. The implementation is [`low_threshold.py`](../../days/78-low-threshold/low_threshold.py).

Hand in the printed numbers and rule lines for day 78. Keep the script path for reruns.
