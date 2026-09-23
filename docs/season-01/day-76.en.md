<p align="center"><a href="day-76.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 76 · Two mistake modes

[Phase I · Models](../../README.en.md) · runs

What you learn today: missed down=3 (y<0 and ŷ≥0); false alarm up=3 (y<0 and ŷ>0).

## Plain-language account

Day 76's numbers come from script stdout, not hand-filled values. missed down 数真实下跌但预测非负. false alarm up 是 missed down 的子集：预测严格为正. 本跑 ŷ=0 的边界日若存在，会进 missed 不进 false alarm；此处两数同为 3，说明三天下跌失手日预测都严格为正. 

不要与 direction wrong=3 混名——符号比较与这两列定义等价计数，但列名服务后续阈值课. 

The panel is days/data/panel.csv, name AAA, simple returns from adjusted close. Train is the first seventy-five percent in time order unless this script changes the cut. Hold-out rows are scored only; the five-lag line is not re-fit there. Same-bar high, low, close are not features; same-day market is not a result.

Separate train from test: coefficients on train, counts and MAE on nineteen hold-out rows. missed down=3 (y<0 and ŷ≥0); false alarm up=3 (y<0 and ŷ>0).

Return scores here are not price-level SSE from days 45–46. Claims serve this print only.

## Core

```text
missed down days = 3
false alarm up days = 3
```

## Further out

Cross-check stdout against the page: key names, signs, and decimals should match the terminal. missed down=3 (y<0 and ŷ≥0); false alarm up=3 (y<0 and ŷ>0).

Keep billing rules beside direction counts in the lab notebook. If the next lesson changes the cut or target, open a new log row instead of overwriting today's numbers.

## What the run showed

```bash
python days/76-two-mistakes/two_mistakes.py
```

The script should print stdout lines matching the core block. The implementation is [`two_mistakes.py`](../../days/76-two-mistakes/two_mistakes.py).

Hand in the printed numbers and rule lines for day 76. Keep the script path for reruns.
