<p align="center"><a href="day-58.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 58 · Year split

[Phase I · Models](../../README.en.md) · runs

What you learn today: cut 2024-02-28, train=33, test=40, test MSE=0.000782, worse than 75% split 0.000081

## Plain-language account

Day 58's numbers come from script stdout, not hand-filled values. 按日期切：早于 2024-02-28 训练. 四十行测试. 0.000782 远大于 0.000081，切分规则改变分数. 

The panel is days/data/panel.csv, name AAA, simple returns from adjusted close. Train is the first seventy-five percent in time order unless this script changes the cut. Hold-out rows score MSE only; coefficients are not re-fit there. Same-bar high, low, close are not features; same-day market is not a result.

Separate train from test: parameters on train, MSE on hold-out mean squared error. cut 2024-02-28, train=33, test=40, test MSE=0.000782, worse than 75% split 0.000081

Return MSE is not price-level SSE from days 45–46. Claims serve this print only.

## Core

```text
cut date = 2024-02-28
train rows = 33  test rows = 40
test MSE = 0.000782
```

## Further out

Cross-check stdout against the page: key names, signs, and six decimals should match the terminal. cut 2024-02-28, train=33, test=40, test MSE=0.000782, worse than 75% split 0.000081

Keep forbidden rules beside MSE in the lab notebook. If the next lesson changes the cut or target, open a new log row instead of overwriting today's numbers.

## What the run showed

```bash
python days/58-year-split/year_split.py
```

The script should print stdout lines matching the core block. The implementation is [`year_split.py`](../../days/58-year-split/year_split.py).

Hand in the printed numbers and rule lines for day 58. Keep the script path for reruns.
