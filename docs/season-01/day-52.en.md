<p align="center"><a href="day-52.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 52 · One stump on five lags

[Phase I · Models](../../README.en.md) · runs

What you learn today: lag4 threshold −0.020177, left 0.0319, right −0.0014, train MSE 0.000378, test MSE 0.000174, worse than line 0.000081

## Plain-language account

The stump splits only lag4 on train: below −0.020177 predict 0.0319, else −0.0014—a step, not five smooth weights.

Train MSE 0.000378 is optimistic because the cut and leaf means saw those rows. Test MSE 0.000174 beats neither the line at 0.000081.

Train and test share one threshold and two constants; only the row set changes. Never sell train MSE as generalization.

Data come from name AAA in days/data/panel.csv: simple returns from adjusted close ratios minus one. Usable rows start after the fifth return, so five fewer rows than the raw panel. The default split is the first seventy-five percent of those rows in time order for train and the rest for test (often fifty-four train, nineteen test). Same-bar high, low, and close must not explain same-day return; same-day market return is not a valid feature or label unless the day script says otherwise.

## Core

```text
split column = lag 4
threshold = -0.020177
left mean = 0.0319  right mean = -0.0014
train MSE = 0.000378
test MSE = 0.000174
```


Test MSE on returns is not the price-level SSE from days 45–46. Hold-out rows are the only score set; coefficients and thresholds are fit on train only.

| Idea | Changes this day? | Note |
|---|---|---|
| Five-lag line coeffs | Usually frozen | From day 51 train |
| test MSE 0.000081 | Reprinted on MSE days | Diagnostics use MAE/direction/bill |
| forbidden OHLC/market | Contract holds | See days 56–57, 67 |
| train/test rows | Default 54/19 | Day 58 calendar cut excepted |

## Core block, line by line

Day 52 prints 5 contract lines:

- `split column = lag 4`: match the terminal verbatim—keys, spacing, signs, six decimals.
- `threshold = -0.020177`: match the terminal verbatim—keys, spacing, signs, six decimals.
- `left mean = 0.0319  right mean = -0.0014`: match the terminal verbatim—keys, spacing, signs, six decimals.
- `train MSE = 0.000378`: match the terminal verbatim—keys, spacing, signs, six decimals.
- `test MSE = 0.000174`: match the terminal verbatim—keys, spacing, signs, six decimals.

Lag-5 anchors: line test MSE 0.000081, volume helped false (day 54), total bill line −18.0000 (days 75 and 79). Do not paste anchors on days that do not print them; do not round or drop signs when they appear. Day 58’s 0.000782 belongs to the calendar split, not the 0.000081 ruler. BBB 0.000105 stays beside AAA—no auto-transfer.

## Further out

Price-level trees from days 44–48 use a different label; do not paste those SSE numbers here.

Day 53 varies tree seeds; line weights should stay fixed.

Flexibility did not win on test: 0.000174>0.000081.

## How this day connects

The stump splits lag4 at −0.020177; train MSE 0.000378 tempts overfitting stories but test 0.000174 loses to the line at 0.000081. Day 53 perturbs tree seeds; line weights should not move. Sketch a step function versus a weighted sum in your notes.

Engineer reading order: run today's script first, then read the page; do not skip day 51 before diagnostics or the frozen coefficients lose context. Unit tests should assert hold-out scores against printed literals; common failures mix train rows or tickers. Screenshots should show English keys and six-decimal scores. Use python3; tiny float noise is fine, but contract integers like quiet=10, jump=5, and direction wrong=3 must not drift.

## What the run showed

```bash
python3 days/52-five-lag-tree/five_lag_tree.py
```

The script should print stdout matching the core block. Implementation: [`five_lag_tree.py`](../../days/52-five-lag-tree/five_lag_tree.py).

Hand in split column, threshold, leaf means, and train/test MSE. Next: fix the line, perturb tree seeds.

Checklist: train/test counts match the script; English keys, signs, and six-decimal literals match the terminal; FORBIDDEN and not-a-result lines stay verbatim; do not swap line versus tree MSE or bill columns; lag-5 anchors (MSE 0.000081, volume helped false, bill −18) stay untouched unless you re-run and update the whole contract.
