<p align="center"><a href="day-58.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 58 · Year split

[Phase I · Models](../../README.en.md) · runs

What you learn today: Cut 2024-02-28, train=33, test=40, test MSE=0.000782, worse than seventy-five percent 0.000081

## Plain-language account

Same five-lag line, new split, new score: cut 2024-02-28 yields train 33, test 40, test MSE 0.000782.

The formula is unchanged; the information set and hold-out window changed.

Never compare 0.000782 to 0.000081 without naming the split.

Data come from name AAA in days/data/panel.csv: simple returns from adjusted close ratios minus one. Usable rows start after the fifth return, so five fewer rows than the raw panel. The default split is the first seventy-five percent of those rows in time order for train and the rest for test (often fifty-four train, nineteen test). Same-bar high, low, and close must not explain same-day return; same-day market return is not a valid feature or label unless the day script says otherwise.

Day 58 calendar cut at 2024-02-28 yields thirty-three train and forty test rows; test MSE 0.000782 is split-specific, not the 0.000081 benchmark.

Treat English stdout keys as the diff authority—spaces around equals, signs, six decimals, and FORBIDDEN lines stay verbatim.

Line test MSE 0.000081 stays the frozen day-51 benchmark on nineteen hold-out rows unless this day explicitly changes the split or label.

## Core


Copy stdout literally: English keys, spacing, signs, and printed decimals. The ```text``` block must diff clean against the day script.

```text
cut date = 2024-02-28
train rows = 33 test rows = 40
test MSE = 0.000782
```

Test MSE on returns is not the price-level SSE from days 45–46. Hold-out rows are the only score set; coefficients and thresholds are fit on train only.

| Idea | Changes this day? | Note |
|---|---|---|
| Five-lag line coeffs | Usually frozen | From day 51 train |
| test MSE 0.000081 | Reprinted on MSE days | Diagnostics use MAE/direction/bill |
| forbidden OHLC/market | Contract holds | See days 56–57, 67 |
| train/test rows | Default 54/19 | Day 58 calendar cut excepted |

Lag-5 anchors: line test MSE 0.000081, volume helped false (day 54), total bill line −18.0000 (days 75 and 79). Do not paste anchors on days that do not print them; do not round or drop signs when they appear. Day 58’s 0.000782 belongs to the calendar split, not the 0.000081 ruler. BBB 0.000105 stays beside AAA—no auto-transfer.

## Further out

Day 59 returns to seventy-five percent with nineteen test rows.

Walk-forward splits are common in production; this day is a teaching contrast.

Calendar cut 2024-02-28: train 33, test 40, MSE 0.000782. Compare splits, not just scores. Day 59 restores seventy-five percent and 0.000081.

Reproduce by running today's script first; unit tests should assert hold-out literals; do not mix train rows or paste price SSE as return MSE.

Hand in one paragraph stating which part of the contract changes today, citing at least one printed anchor.

Volume helped false is stretch-specific on nineteen test rows—not a universal claim about volume.

Long Chinese prose is fine; append the stdout core block so peers can verify literals.

Nineteen hold-out rows are the only legitimate test MSE set; train RSS or train MSE is diagnostic, not a headline score beside 0.000081.

Days 56–57 print task and FORBIDDEN lines; default features remain five lagged returns unless the script says otherwise. Day 67’s market-leak run is not a valid result row.

Time-ordered split matches day 7 hold-out logic. Day 58’s 0.000782 belongs to a calendar cut experiment—it does not replace 0.000081.

Paper the train mask before hand-checking rows. Common failures: BBB rows in AAA, or price SSE pasted as return MSE.

Screenshots should show English keys and six-decimal literals; Chinese prose may be long but the terminal is the diff authority.

Frozen-coefficient days score test rows with ŷ=Xβ̂ only—no test refit. Later direction and bill days change the metric, not the day-51 line anchor.

Day 9 row-order invariance needs intact pairs in X; shuffling before lag construction breaks alignment.

Return labels come from adjusted close; do not paste day 1–10 price slopes or RSS into lag-5 return notes.

## What the run showed

```bash
python3 days/58-year-split/year_split.py
```

The script should print stdout matching the core block. Implementation: [`year_split.py`](../../days/58-year-split/year_split.py).

Checklist: train/test counts match the script; English keys, signs, and six-decimal literals match the terminal; FORBIDDEN and not-a-result lines stay verbatim; do not swap line versus tree MSE or bill columns; lag-5 anchors (MSE 0.000081, volume helped false, bill −18) stay untouched unless you re-run and update the whole contract.