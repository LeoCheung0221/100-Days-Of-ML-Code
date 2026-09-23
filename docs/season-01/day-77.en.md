<p align="center"><a href="day-77.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 77 · High threshold silence

[Phase I · Models](../../README.en.md) · runs

What you learn today: threshold=0.0100; days speaking=0; MAE when speaking=not defined.

## Plain-language account

Day 77's numbers come from script stdout, not hand-filled values. 发言日定义 |ŷ|≥0.01. frozen 直线在测试段上没有任何 |ŷ| 达到 0.01，故 speaking=0，条件 MAE 不定义. 

这与第 62 天「高 |ŷ| 子集」不同：那里按 |ŷ| 排序取 top tenth；这里用固定 τ. τ 太大则全体静音. 

The panel is days/data/panel.csv, name AAA, simple returns from adjusted close. Train is the first seventy-five percent in time order unless this script changes the cut. Hold-out rows are scored only; the five-lag line is not re-fit there. Same-bar high, low, close are not features; same-day market is not a result.

Separate train from test: coefficients on train, counts and MAE on nineteen hold-out rows. threshold=0.0100; days speaking=0; MAE when speaking=not defined.

Return scores here are not price-level SSE from days 45–46. Claims serve this print only.

## Core

```text
threshold = 0.0100
days speaking = 0
mean abs error when speaking = not defined
```

## Further out

Cross-check stdout against the page: key names, signs, and decimals should match the terminal. threshold=0.0100; days speaking=0; MAE when speaking=not defined.

Keep billing rules beside direction counts in the lab notebook. If the next lesson changes the cut or target, open a new log row instead of overwriting today's numbers.

## What the run showed

```bash
python days/77-high-threshold/high_threshold.py
```

The script should print stdout lines matching the core block. The implementation is [`high_threshold.py`](../../days/77-high-threshold/high_threshold.py).

Hand in the printed numbers and rule lines for day 77. Keep the script path for reruns.
