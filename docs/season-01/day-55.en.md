<p align="center"><a href="day-55.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 55 · Three miss modes

[Phase I · Models](../../README.en.md) · runs

What you learn today: line MSE 0.000081, ridge 0.000098, tree 0.000174; three miss-mode English sentences verbatim

## Plain-language account

All three models score the same nineteen test rows. MSE order: line, then ridge, then tree.

Ridge λ=20000 penalizes lag coefficients only; shrinkage toward zero raises test MSE here.

Miss-mode lines describe error shapes, not hit rates; keep English verbatim for stdout checks.

Data come from name AAA in days/data/panel.csv: simple returns from adjusted close ratios minus one. Usable rows start after the fifth return, so five fewer rows than the raw panel. The default split is the first seventy-five percent of those rows in time order for train and the rest for test (often fifty-four train, nineteen test). Same-bar high, low, and close must not explain same-day return; same-day market return is not a valid feature or label unless the day script says otherwise.

Three models share nineteen test rows and one label. MSE order: line 0.000081, ridge 0.000098, tree 0.000174. Miss-mode lines are error-shape signatures, not hit rates.

Ridge loses to the line here—λ=20000 shrinkage toward zero hurts this hold-out. Do not paste day-42 price ridge slopes into return tables.

Keep miss-mode English verbatim; store it separately from later direction/jump diagnostics. One slide for MSE, one for miss modes.

## Core


Copy stdout literally: English keys, spacing, signs, and printed decimals. The ```text``` block must diff clean against the day script.

```text
test MSE line = 0.000081
test MSE ridge = 0.000098
test MSE tree = 0.000174
line miss mode = smooth blend of lags misses sharp jumps
ridge miss mode = same blend pulled toward zero misses jumps and size
tree miss mode = one lag threshold leaves a constant on each side
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

Do not paste day-42 full-sample ridge slope into return tables.

Archive miss-mode sentences beside MSE for later direction/jump diagnostics.

Next: explicit task and forbidden lines in stdout.

Three test MSE lines plus English miss-mode sentences—keep both tables. Ridge 0.000098 sits between line and tree. Day 56 prints the task contract next.

Tree 0.000174 reinforces day 52: flexibility without test win. Only discuss regularization wins if ridge beats line—it does not today.

Split the team: MSE copy, miss-mode interpretation, literal diff on keys.

Compare tree and line on hold-out MSE; lower train MSE alone is not a generalization argument.

Merge panel on date and name, not row index—row-index merges break lag alignment like broken pairs.

Random and calendar splits change the test row set—rerun scripts instead of hand-editing one metric.

Name the baseline whenever you write improvement—zero forecast, naive mean, and day-51 line differ.

FORBIDDEN lines are executable policy, not decoration—silent column drops erase audit evidence.

## What the run showed

```bash
python3 days/55-three-miss-modes/three_miss_modes.py
```

The script should print stdout matching the core block. Implementation: [`three_miss_modes.py`](../../days/55-three-miss-modes/three_miss_modes.py).

Checklist: train/test counts match the script; English keys, signs, and six-decimal literals match the terminal; FORBIDDEN and not-a-result lines stay verbatim; do not swap line versus tree MSE or bill columns; lag-5 anchors (MSE 0.000081, volume helped false, bill −18) stay untouched unless you re-run and update the whole contract.