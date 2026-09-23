<p align="center"><a href="day-53.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 53 · Random seed

[Phase I · Models](../../README.en.md) · runs

What you learn today: linear lag1=−0.1359; seed0 tree lag1 threshold 0.076142; seed1 tree lag4 −0.020177; line unchanged

## Plain-language account

Separate two randomness sources: OLS is deterministic on a fixed design; the tree may move with seed on subsamples or tie breaks.

Seed 0 picks lag1 at 0.076142; seed 1 returns lag4 at −0.020177 like day 52.

Linear lag1 stays −0.1359 before and after tree seeds—the line is not edited by tree output.

Data come from name AAA in days/data/panel.csv: simple returns from adjusted close ratios minus one. Usable rows start after the fifth return, so five fewer rows than the raw panel. The default split is the first seventy-five percent of those rows in time order for train and the rest for test (often fifty-four train, nineteen test). Same-bar high, low, and close must not explain same-day return; same-day market return is not a valid feature or label unless the day script says otherwise.

Day 53 freezes the line and perturbs tree seeds only. Seed 0 splits lag1 at 0.076142; seed 1 splits lag4 at −0.020177 matching day 52. The line `linear weight lag 1 after tree seeds = -0.1359` shows OLS weights ignore tree seeds.

Separate two randomness sources: tree seeds may move the cut; linear regression on a fixed train design should not move β̂. If lag1 drifts locally, check for test refits or BBB rows mixed into AAA.

When writing that nonlinear fits are seed-sensitive, point at split column/threshold jumps—not at lag1 coefficients moving. Day 54 adds volume on the same nineteen-row score set.

## Core


Copy stdout literally: English keys, spacing, signs, and printed decimals. The ```text``` block must diff clean against the day script.

```text
linear weight lag 1 = -0.1359
seed = 0 tree split lag = 1 threshold = 0.076142
seed = 1 tree split lag = 4 threshold = -0.020177
linear weight lag 1 after tree seeds = -0.1359
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

Log which code paths honor seed versus pure lstsq.

When reproducing day 52, match seed 1 column and threshold, not leaf means with a wrong cut.

Day 54 adds volume; today's line baseline remains test MSE 0.000081.

Tree seeds move cuts; OLS stays at lag1 −0.1359. If linear weights change, that is a bug. Day 54 adds volume and hurts test MSE with helped=false.

Day 9 row-order invariance applies to OLS sums, not to shuffling before lag construction. Tree seeds affect tie-breaking in greedy splits, not the linear contract.

Run day 51 first, then this script; diff lag1 must stay −0.1359.

Frozen-coefficient days score test rows with ŷ=Xβ̂ only—no test refit. Later direction and bill days change the metric, not the day-51 line anchor.

Day 9 row-order invariance needs intact pairs in X; shuffling before lag construction breaks alignment.

Return labels come from adjusted close; do not paste day 1–10 price slopes or RSS into lag-5 return notes.

Slides should pair English stdout keys with Chinese prose—Chinese-only numbers fail literal diff grading.

Day 40 leakage checks column semantics; days 56–57 reject same-bar OHLC—the lists stack, not replace.

Quiet ten, jump five, direction-wrong three are contract integers from day 71—do not round them into percentages.

## What the run showed

```bash
python3 days/53-random-seed/random_seed.py
```

The script should print stdout matching the core block. Implementation: [`random_seed.py`](../../days/53-random-seed/random_seed.py).

Checklist: train/test counts match the script; English keys, signs, and six-decimal literals match the terminal; FORBIDDEN and not-a-result lines stay verbatim; do not swap line versus tree MSE or bill columns; lag-5 anchors (MSE 0.000081, volume helped false, bill −18) stay untouched unless you re-run and update the whole contract.