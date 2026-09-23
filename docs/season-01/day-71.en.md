<p align="center"><a href="day-71.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 71 · Three day classes

[Phase I · Models](../../README.en.md) · runs

What you learn today: On AAA five-lag line hold-out, |return| splits quiet=10, jump=5; three direction-wrong days.

## Plain-language account

Frozen day-51 line on nineteen test rows; classes use |y|, not |ŷ|.

Quiet/jump thresholds are median and p75 on test |y|; direction wrong is three days.

Ten plus five plus three does not exhaust nineteen—four mid days sit between.

Data come from name AAA in days/data/panel.csv: simple returns from adjusted close ratios minus one. Usable rows start after the fifth return, so five fewer rows than the raw panel. The default split is the first seventy-five percent of those rows in time order for train and the rest for test (often fifty-four train, nineteen test). Same-bar high, low, and close must not explain same-day return; same-day market return is not a valid feature or label unless the day script says otherwise.

## Core

```text
quiet days = 10
jump days = 5
direction wrong days = 3
```


Test MSE on returns is not the price-level SSE from days 45–46. Hold-out rows are the only score set; coefficients and thresholds are fit on train only.

Days 71–80 mostly diagnose the same five-lag line frozen from day 51 train; this lesson may not reprint test MSE 0.000081, but predictions still use lag1=−0.1359, lag2=0.0829, lag3=0.1094, lag4=−0.1726, lag5=−0.0803, intercept 0.0023.

| Idea | Changes this day? | Note |
|---|---|---|
| Five-lag line coeffs | Usually frozen | From day 51 train |
| test MSE 0.000081 | Reprinted on MSE days | Diagnostics use MAE/direction/bill |
| forbidden OHLC/market | Contract holds | See days 56–57, 67 |
| train/test rows | Default 54/19 | Day 58 calendar cut excepted |

## Core block, line by line

Day 71 prints 3 contract lines:

- `quiet days = 10`: match the terminal verbatim—keys, spacing, signs, six decimals.
- `jump days = 5`: match the terminal verbatim—keys, spacing, signs, six decimals.
- `direction wrong days = 3`: match the terminal verbatim—keys, spacing, signs, six decimals.

Lag-5 anchors: line test MSE 0.000081, volume helped false (day 54), total bill line −18.0000 (days 75 and 79). Do not paste anchors on days that do not print them; do not round or drop signs when they appear. Day 58’s 0.000782 belongs to the calendar split, not the 0.000081 ruler. BBB 0.000105 stays beside AAA—no auto-transfer.

## Further out

Days 71–80 mostly diagnose the same five-lag line frozen from day 51 train; this lesson may not reprint test MSE 0.000081, but predictions still use lag1=−0.1359, lag2=0.0829, lag3=0.1094, lag4=−0.1726, lag5=−0.0803, intercept 0.0023.

Day 72 compares quiet MAE to whole-test MAE 0.006980.

## How this day connects

Quiet ten, jump five, direction wrong three—orthogonal views on nineteen test rows. Four mid days sit between classes.

Engineer reading order: run today's script first, then read the page; do not skip day 51 before diagnostics or the frozen coefficients lose context. Unit tests should assert hold-out scores against printed literals; common failures mix train rows or tickers. Screenshots should show English keys and six-decimal scores. Use python3; tiny float noise is fine, but contract integers like quiet=10, jump=5, and direction wrong=3 must not drift.

## What the run showed

```bash
python3 days/71-three-classes/three_classes.py
```

The script should print stdout matching the core block. Implementation: [`three_classes.py`](../../days/71-three-classes/three_classes.py).



Checklist: train/test counts match the script; English keys, signs, and six-decimal literals match the terminal; FORBIDDEN and not-a-result lines stay verbatim; do not swap line versus tree MSE or bill columns; lag-5 anchors (MSE 0.000081, volume helped false, bill −18) stay untouched unless you re-run and update the whole contract.
