<p align="center"><a href="day-60.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 60 · Line vs baseline

[Phase I · Models](../../README.en.md) · runs

What you learn today: baseline 0.000101, line 0.000081, improvement 0.000020; index 13 error 0.000214

## Plain-language account

Improvement 0.000020 is baseline minus line on test MSE.

Index 13 is a test-segment row index, not a calendar date; absolute error 0.000214 is not comparable to MSE as a single-number contest.

Map index to dates offline; the script prints row order only.

Data come from name AAA in days/data/panel.csv: simple returns from adjusted close ratios minus one. Usable rows start after the fifth return, so five fewer rows than the raw panel. The default split is the first seventy-five percent of those rows in time order for train and the rest for test (often fifty-four train, nineteen test). Same-bar high, low, and close must not explain same-day return; same-day market return is not a valid feature or label unless the day script says otherwise.

Day 60 MSE improvement over baseline is 0.000020; smallest line error on test is index 13 at 0.000214.

Treat English stdout keys as the diff authority—spaces around equals, signs, six decimals, and FORBIDDEN lines stay verbatim.

Line test MSE 0.000081 stays the frozen day-51 benchmark on nineteen hold-out rows unless this day explicitly changes the split or label.

## Core


Copy stdout literally: English keys, spacing, signs, and printed decimals. The ```text``` block must diff clean against the day script.

```text
baseline test MSE = 0.000101
line test MSE = 0.000081
MSE improvement over baseline = 0.000020
smallest line error day index on test = 13
that day line error = 0.000214
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

Day 61 applies the same baseline to the tree; improvement goes negative.

Smallest error day is not necessarily the best economic day.

Improvement on MSE versus absolute error on row index 13—different units. Day 61 applies baseline to the tree with negative improvement.

Reproduce by running today's script first; unit tests should assert hold-out literals; do not mix train rows or paste price SSE as return MSE.

Hand in one paragraph stating which part of the contract changes today, citing at least one printed anchor.

Screenshots should show English keys and six-decimal literals; Chinese prose may be long but the terminal is the diff authority.

Frozen-coefficient days score test rows with ŷ=Xβ̂ only—no test refit. Later direction and bill days change the metric, not the day-51 line anchor.

Day 9 row-order invariance needs intact pairs in X; shuffling before lag construction breaks alignment.

Return labels come from adjusted close; do not paste day 1–10 price slopes or RSS into lag-5 return notes.

Slides should pair English stdout keys with Chinese prose—Chinese-only numbers fail literal diff grading.

Day 40 leakage checks column semantics; days 56–57 reject same-bar OHLC—the lists stack, not replace.

Quiet ten, jump five, direction-wrong three are contract integers from day 71—do not round them into percentages.

Compare tree and line on hold-out MSE; lower train MSE alone is not a generalization argument.

Merge panel on date and name, not row index—row-index merges break lag alignment like broken pairs.

## What the run showed

```bash
python3 days/60-line-vs-baseline/line_vs_baseline.py
```

The script should print stdout matching the core block. Implementation: [`line_vs_baseline.py`](../../days/60-line-vs-baseline/line_vs_baseline.py).

Checklist: train/test counts match the script; English keys, signs, and six-decimal literals match the terminal; FORBIDDEN and not-a-result lines stay verbatim; do not swap line versus tree MSE or bill columns; lag-5 anchors (MSE 0.000081, volume helped false, bill −18) stay untouched unless you re-run and update the whole contract.