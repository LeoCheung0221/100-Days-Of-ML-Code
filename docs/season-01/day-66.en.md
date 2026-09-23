<p align="center"><a href="day-66.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 66 · Excess return

[Phase I · Models](../../README.en.md) · runs

What you learn today: target return minus market; test MSE 0.000095

## Plain-language account

Day 66's numbers come from script stdout, not hand-filled values. 标签减 market 同期收益. 特征仍五 lag 自身. 0.000095 高于 raw 0.000081，是换目标的新分数. 

The panel is days/data/panel.csv, name AAA, simple returns from adjusted close. Train is the first seventy-five percent in time order unless this script changes the cut. Hold-out rows score MSE only; coefficients are not re-fit there. Same-bar high, low, close are not features; same-day market is not a result.

Separate train from test: parameters on train, MSE on hold-out mean squared error. target return minus market; test MSE 0.000095

Return MSE is not price-level SSE from days 45–46. Claims serve this print only.

## Core

```text
target = return minus market return
test MSE = 0.000095
```

## Further out

Cross-check stdout against the page: key names, signs, and six decimals should match the terminal. target return minus market; test MSE 0.000095

Keep forbidden rules beside MSE in the lab notebook. If the next lesson changes the cut or target, open a new log row instead of overwriting today's numbers.

## What the run showed

```bash
python days/66-excess-return/excess_return.py
```

The script should print stdout lines matching the core block. The implementation is [`excess_return.py`](../../days/66-excess-return/excess_return.py).

Hand in the printed numbers and rule lines for day 66. Keep the script path for reruns.
