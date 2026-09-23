<p align="center"><a href="day-61.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 61 · Tree vs baseline

[Phase I · Models](../../README.en.md) · runs

What you learn today: baseline 0.000101, tree 0.000174, improvement −0.000072; tree does NOT beat zero baseline

## Plain-language account

Day 61's numbers come from script stdout, not hand-filled values. 负 improvement：树比猜零更差. 0.000174 与第 52 天 test 树 MSE 一致. 

The panel is days/data/panel.csv, name AAA, simple returns from adjusted close. Train is the first seventy-five percent in time order unless this script changes the cut. Hold-out rows score MSE only; coefficients are not re-fit there. Same-bar high, low, close are not features; same-day market is not a result.

Separate train from test: parameters on train, MSE on hold-out mean squared error. baseline 0.000101, tree 0.000174, improvement −0.000072; tree does NOT beat zero baseline

Return MSE is not price-level SSE from days 45–46. Claims serve this print only.

## Core

```text
baseline test MSE = 0.000101
tree test MSE = 0.000174
MSE improvement over baseline = -0.000072
```

## Further out

Cross-check stdout against the page: key names, signs, and six decimals should match the terminal. baseline 0.000101, tree 0.000174, improvement −0.000072; tree does NOT beat zero baseline

Keep forbidden rules beside MSE in the lab notebook. If the next lesson changes the cut or target, open a new log row instead of overwriting today's numbers.

## What the run showed

```bash
python days/61-tree-vs-baseline/tree_vs_baseline.py
```

The script should print stdout lines matching the core block. The implementation is [`tree_vs_baseline.py`](../../days/61-tree-vs-baseline/tree_vs_baseline.py).

Hand in the printed numbers and rule lines for day 61. Keep the script path for reruns.
