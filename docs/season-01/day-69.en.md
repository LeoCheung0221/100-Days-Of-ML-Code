<p align="center"><a href="day-69.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 69 · Fill assumption

[Phase I · Models](../../README.en.md) · runs

What you learn today: close-to-close, slippage 0, no order; test MSE 0.000081

## Plain-language account

Day 69's numbers come from script stdout, not hand-filled values. 三行假设：可复算收盘、无滑点、无下单. MSE 在该摩擦假设下仍 0.000081. 

The panel is days/data/panel.csv, name AAA, simple returns from adjusted close. Train is the first seventy-five percent in time order unless this script changes the cut. Hold-out rows score MSE only; coefficients are not re-fit there. Same-bar high, low, close are not features; same-day market is not a result.

Separate train from test: parameters on train, MSE on hold-out mean squared error. close-to-close, slippage 0, no order; test MSE 0.000081

Return MSE is not price-level SSE from days 45–46. Claims serve this print only.

## Core

```text
fill assumption = close-to-close at the printed close
slippage = 0
no order is sent
test MSE under this assumption = 0.000081
```

## Further out

Cross-check stdout against the page: key names, signs, and six decimals should match the terminal. close-to-close, slippage 0, no order; test MSE 0.000081

Keep forbidden rules beside MSE in the lab notebook. If the next lesson changes the cut or target, open a new log row instead of overwriting today's numbers.

## What the run showed

```bash
python days/69-fill-assumption/fill_assumption.py
```

The script should print stdout lines matching the core block. The implementation is [`fill_assumption.py`](../../days/69-fill-assumption/fill_assumption.py).

Hand in the printed numbers and rule lines for day 69. Keep the script path for reruns.
