<p align="center"><a href="day-62.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 62 · Top tenth by |ŷ|

[Phase I · Models](../../README.en.md) · runs

What you learn today: test=19, top=2, top MAE 0.007193, rest 0.006955; top tenth not more accurate

## Plain-language account

On nineteen test rows, the top tenth by |ŷ| is two days.

Their mean absolute error exceeds the rest—large |ŷ| is not higher accuracy.

This slice uses |ŷ|, not |y| like day 71 quiet/jump.

Data come from name AAA in days/data/panel.csv: simple returns from adjusted close ratios minus one. Usable rows start after the fifth return, so five fewer rows than the raw panel. The default split is the first seventy-five percent of those rows in time order for train and the rest for test (often fifty-four train, nineteen test). Same-bar high, low, and close must not explain same-day return; same-day market return is not a valid feature or label unless the day script says otherwise.

## Core

```text
test rows = 19
top tenth count = 2
top tenth mean absolute error = 0.007193
rest mean absolute error = 0.006955
```


Test MSE on returns is not the price-level SSE from days 45–46. Hold-out rows are the only score set; coefficients and thresholds are fit on train only.

| Idea | Changes this day? | Note |
|---|---|---|
| Five-lag line coeffs | Usually frozen | From day 51 train |
| test MSE 0.000081 | Reprinted on MSE days | Diagnostics use MAE/direction/bill |
| forbidden OHLC/market | Contract holds | See days 56–57, 67 |
| train/test rows | Default 54/19 | Day 58 calendar cut excepted |

## Core block, line by line

Day 62 prints 4 contract lines:

- `test rows = 19`: match the terminal verbatim—keys, spacing, signs, six decimals.
- `top tenth count = 2`: match the terminal verbatim—keys, spacing, signs, six decimals.
- `top tenth mean absolute error = 0.007193`: match the terminal verbatim—keys, spacing, signs, six decimals.
- `rest mean absolute error = 0.006955`: match the terminal verbatim—keys, spacing, signs, six decimals.

Lag-5 anchors: line test MSE 0.000081, volume helped false (day 54), total bill line −18.0000 (days 75 and 79). Do not paste anchors on days that do not print them; do not round or drop signs when they appear. Day 58’s 0.000782 belongs to the calendar split, not the 0.000081 ruler. BBB 0.000105 stays beside AAA—no auto-transfer.

## Further out

Days 77–78 threshold |ŷ| for speaking; this day foreshadows that.

Always print count=2 for the top decile here.

## How this day connects

Top tenth by |ŷ| is two days with higher MAE than the rest. Not the same as quiet/jump by |y|. Days 77–78 threshold |ŷ| for speaking.

Engineer reading order: run today's script first, then read the page; do not skip day 51 before diagnostics or the frozen coefficients lose context. Unit tests should assert hold-out scores against printed literals; common failures mix train rows or tickers. Screenshots should show English keys and six-decimal scores. Use python3; tiny float noise is fine, but contract integers like quiet=10, jump=5, and direction wrong=3 must not drift.

## What the run showed

```bash
python3 days/62-top-tenth/top_tenth.py
```

The script should print stdout matching the core block. Implementation: [`top_tenth.py`](../../days/62-top-tenth/top_tenth.py).



Checklist: train/test counts match the script; English keys, signs, and six-decimal literals match the terminal; FORBIDDEN and not-a-result lines stay verbatim; do not swap line versus tree MSE or bill columns; lag-5 anchors (MSE 0.000081, volume helped false, bill −18) stay untouched unless you re-run and update the whole contract.
