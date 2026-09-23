<p align="center"><a href="day-80.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 80 · Acceptable mistake

[Phase I · Models](../../README.en.md) · runs

What you learn today: acceptable mistake names direction wrong at cost 1; three days; five jump days at cost 3

## Plain-language account

Day 80 names columns only; bills stay consistent with day 75 −18.

Phase I closes on diagnostics vocabulary, not a new fit.

Start phase II with a new contract instead of silently changing lag-5 literals.

Data come from name AAA in days/data/panel.csv: simple returns from adjusted close ratios minus one. Usable rows start after the fifth return, so five fewer rows than the raw panel. The default split is the first seventy-five percent of those rows in time order for train and the rest for test (often fifty-four train, nineteen test). Same-bar high, low, and close must not explain same-day return; same-day market return is not a valid feature or label unless the day script says otherwise.

Day 80 names acceptable mistakes and maps direction wrong and jump billing.

Treat English stdout keys as the diff authority—spaces around equals, signs, six decimals, and FORBIDDEN lines stay verbatim.

Line test MSE 0.000081 stays the frozen day-51 benchmark on nineteen hold-out rows unless this day explicitly changes the split or label.

## Core


Copy stdout literally: English keys, spacing, signs, and printed decimals. The ```text``` block must diff clean against the day script.

```text
acceptable mistake = direction wrong at cost 1
direction wrong days = 3
jump days billed at 3 = 5
this choice names column direction wrong in the bill table
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

Re-run with python3; keep anchors MSE 0.000081, volume helped false, bill −18 in the recap.

Names direction-wrong column at cost one; closes phase I diagnostics. Keep anchors MSE 0.000081, volume false, bill −18 unless the whole contract is re-run.

Reproduce by running today's script first; unit tests should assert hold-out literals; do not mix train rows or paste price SSE as return MSE.

Hand in one paragraph stating which part of the contract changes today, citing at least one printed anchor.

Volume helped false is stretch-specific on nineteen test rows—not a universal claim about volume.

Long Chinese prose is fine; append the stdout core block so peers can verify literals.

Nineteen hold-out rows are the only legitimate test MSE set; train RSS or train MSE is diagnostic, not a headline score beside 0.000081.

Days 56–57 print task and FORBIDDEN lines; default features remain five lagged returns unless the script says otherwise. Day 67’s market-leak run is not a valid result row.

Time-ordered split matches day 7 hold-out logic. Day 58’s 0.000782 belongs to a calendar cut experiment—it does not replace 0.000081.

Paper the train mask before hand-checking rows. Common failures: BBB rows in AAA, or price SSE pasted as return MSE.

## What the run showed

```bash
python3 days/80-acceptable-mistake/acceptable_mistake.py
```

The script should print stdout matching the core block. Implementation: [`acceptable_mistake.py`](../../days/80-acceptable-mistake/acceptable_mistake.py).

Checklist: train/test counts match the script; English keys, signs, and six-decimal literals match the terminal; FORBIDDEN and not-a-result lines stay verbatim; do not swap line versus tree MSE or bill columns; lag-5 anchors (MSE 0.000081, volume helped false, bill −18) stay untouched unless you re-run and update the whole contract.