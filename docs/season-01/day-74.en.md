<p align="center"><a href="day-74.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 74 · Top five errors

[Phase I · Models](../../README.en.md) · runs

What you learn today: Top five errors with dates, classes, and direction flags per stdout

## Plain-language account

Top five by absolute error: four jump, one mid on 2024-04-22 with wrong direction.

Large error without jump class happens; jump with right direction also happens.

Keep English class and direction tokens verbatim.

Data come from name AAA in days/data/panel.csv: simple returns from adjusted close ratios minus one. Usable rows start after the fifth return, so five fewer rows than the raw panel. The default split is the first seventy-five percent of those rows in time order for train and the rest for test (often fifty-four train, nineteen test). Same-bar high, low, and close must not explain same-day return; same-day market return is not a valid feature or label unless the day script says otherwise.

Day 74 top-five error table with date, error, class, direction literals.

Treat English stdout keys as the diff authority—spaces around equals, signs, six decimals, and FORBIDDEN lines stay verbatim.

Line test MSE 0.000081 stays the frozen day-51 benchmark on nineteen hold-out rows unless this day explicitly changes the split or label.

## Core


Copy stdout literally: English keys, spacing, signs, and printed decimals. The ```text``` block must diff clean against the day script.

```text
rank 1 date = 2024-04-03 error = 0.019717 class = jump direction = right
rank 2 date = 2024-04-18 error = 0.017449 class = jump direction = right
rank 3 date = 2024-04-22 error = 0.014328 class = mid direction = wrong
rank 4 date = 2024-03-28 error = 0.013401 class = jump direction = right
rank 5 date = 2024-04-02 error = 0.009609 class = jump direction = right
```

Test MSE on returns is not the price-level SSE from days 45–46. Hold-out rows are the only score set; coefficients and thresholds are fit on train only.

Days 71–80 mostly diagnose the same five-lag line frozen from day 51 train; this lesson may not reprint test MSE 0.000081, but predictions still use lag1=−0.1359, lag2=0.0829, lag3=0.1094, lag4=−0.1726, lag5=−0.0803, intercept 0.0023.

| Idea | Changes this day? | Note |
|---|---|---|
| Five-lag line coeffs | Usually frozen | From day 51 train |
| test MSE 0.000081 | Reprinted on MSE days | Diagnostics use MAE/direction/bill |
| forbidden OHLC/market | Contract holds | See days 56–57, 67 |
| train/test rows | Default 54/19 | Day 58 calendar cut excepted |

Lag-5 anchors: line test MSE 0.000081, volume helped false (day 54), total bill line −18.0000 (days 75 and 79). Do not paste anchors on days that do not print them; do not round or drop signs when they appear. Day 58’s 0.000782 belongs to the calendar split, not the 0.000081 ruler. BBB 0.000105 stays beside AAA—no auto-transfer.

## Further out

Days 71–80 mostly diagnose the same five-lag line frozen from day 51 train; this lesson may not reprint test MSE 0.000081, but predictions still use lag1=−0.1359, lag2=0.0829, lag3=0.1094, lag4=−0.1726, lag5=−0.0803, intercept 0.0023.

Day 75 bills errors: total bill line −18.

Top five absolute errors with classes; 2024-04-22 mid and wrong direction. Day 75 bills −18.

Reproduce by running today's script first; unit tests should assert hold-out literals; do not mix train rows or paste price SSE as return MSE.

Hand in one paragraph stating which part of the contract changes today, citing at least one printed anchor.

Time-ordered split matches day 7 hold-out logic. Day 58’s 0.000782 belongs to a calendar cut experiment—it does not replace 0.000081.

Paper the train mask before hand-checking rows. Common failures: BBB rows in AAA, or price SSE pasted as return MSE.

Screenshots should show English keys and six-decimal literals; Chinese prose may be long but the terminal is the diff authority.

Frozen-coefficient days score test rows with ŷ=Xβ̂ only—no test refit. Later direction and bill days change the metric, not the day-51 line anchor.

Day 9 row-order invariance needs intact pairs in X; shuffling before lag construction breaks alignment.

## What the run showed

```bash
python3 days/74-top-five-errors/top_five_errors.py
```

The script should print stdout matching the core block. Implementation: [`top_five_errors.py`](../../days/74-top-five-errors/top_five_errors.py).

Checklist: train/test counts match the script; English keys, signs, and six-decimal literals match the terminal; FORBIDDEN and not-a-result lines stay verbatim; do not swap line versus tree MSE or bill columns; lag-5 anchors (MSE 0.000081, volume helped false, bill −18) stay untouched unless you re-run and update the whole contract.