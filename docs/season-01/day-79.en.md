<p align="center"><a href="day-79.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 79 · Billed ranking

[Phase I · Models](../../README.en.md) · runs

What you learn today: Same billing as day 75: line bill=−18, tree bill=−27; lower bill wins=line (less negative is better).

## Plain-language account

Day 79's numbers come from script stdout, not hand-filled values. 树桩用训练段 best stump 预测测试段，账单规则与直线相同. 树方向错更多或 jump 叠加更重，得 −27；直线 −18 更少负，故 line 赢. 

MSE 名次仍可能是 line 优于 tree（第 52 天），但账单同时罚 jump，树未必赢账单赛. 

The panel is days/data/panel.csv, name AAA, simple returns from adjusted close. Train is the first seventy-five percent in time order unless this script changes the cut. Hold-out rows are scored only; the five-lag line is not re-fit there. Same-bar high, low, close are not features; same-day market is not a result.

Separate train from test: coefficients on train, counts and MAE on nineteen hold-out rows. Same billing as day 75: line bill=−18, tree bill=−27; lower bill wins=line (less negative is better).

Return scores here are not price-level SSE from days 45–46. Claims serve this print only.

## Core

```text
total bill line = -18.0000
total bill tree = -27.0000
lower bill wins = line
```

## Further out

Cross-check stdout against the page: key names, signs, and decimals should match the terminal. Same billing as day 75: line bill=−18, tree bill=−27; lower bill wins=line (less negative is better).

Keep billing rules beside direction counts in the lab notebook. If the next lesson changes the cut or target, open a new log row instead of overwriting today's numbers.

## What the run showed

```bash
python days/79-billed-ranking/billed_ranking.py
```

The script should print stdout lines matching the core block. The implementation is [`billed_ranking.py`](../../days/79-billed-ranking/billed_ranking.py).

Hand in the printed numbers and rule lines for day 79. Keep the script path for reruns.
