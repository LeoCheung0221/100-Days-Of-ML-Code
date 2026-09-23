<p align="center"><a href="day-65.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 65 · Second name

[Phase I · Models](../../README.en.md) · runs

What you learn today: AAA MSE 0.000081; BBB 0.000105; do not auto-transfer

## Plain-language account

Day 65's numbers come from script stdout, not hand-filled values. 同一五 lag 线与 75% 切分. BBB 更差但同量级. 换 name 必须重印 MSE. 

The panel is days/data/panel.csv, name AAA, simple returns from adjusted close. Train is the first seventy-five percent in time order unless this script changes the cut. Hold-out rows score MSE only; coefficients are not re-fit there. Same-bar high, low, close are not features; same-day market is not a result.

Separate train from test: parameters on train, MSE on hold-out mean squared error. AAA MSE 0.000081; BBB 0.000105; do not auto-transfer

Return MSE is not price-level SSE from days 45–46. Claims serve this print only.

## Core

```text
name = AAA test MSE = 0.000081
name = BBB test MSE = 0.000105
```

## Further out

Cross-check stdout against the page: key names, signs, and six decimals should match the terminal. AAA MSE 0.000081; BBB 0.000105; do not auto-transfer

Keep forbidden rules beside MSE in the lab notebook. If the next lesson changes the cut or target, open a new log row instead of overwriting today's numbers.

## What the run showed

```bash
python days/65-second-name/second_name.py
```

The script should print stdout lines matching the core block. The implementation is [`second_name.py`](../../days/65-second-name/second_name.py).

Hand in the printed numbers and rule lines for day 65. Keep the script path for reruns.
