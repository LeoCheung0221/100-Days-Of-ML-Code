<p align="center"><a href="day-62.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 62 · Top tenth by |ŷ|

[Phase I · Models](../../README.en.md) · runs

What you learn today: test=19, top=2, top MAE 0.007193, rest 0.006955; top tenth not more accurate

## Plain-language account

On nineteen test rows, the top tenth by |ŷ| is two days.

Their mean absolute error exceeds the rest—large |ŷ| is not higher accuracy.

This slice uses |ŷ|, not |y| like day 71 quiet/jump.

Data come from name AAA in days/data/panel.csv: simple returns from adjusted close ratios minus one. Usable rows start after the fifth return, so five fewer rows than the raw panel. The default split is the first seventy-five percent of those rows in time order for train and the rest for test (often fifty-four train, nineteen test). Same-bar high, low, and close must not explain same-day return; same-day market return is not a valid feature or label unless the day script says otherwise.

Day 62 tail diagnostics: two rows in top tenth; mean abs error 0.007193 vs rest 0.006955 on nineteen test rows.

Treat English stdout keys as the diff authority—spaces around equals, signs, six decimals, and FORBIDDEN lines stay verbatim.

Line test MSE 0.000081 stays the frozen day-51 benchmark on nineteen hold-out rows unless this day explicitly changes the split or label.

## Core


Copy stdout literally: English keys, spacing, signs, and printed decimals. The ```text``` block must diff clean against the day script.

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

Lag-5 anchors: line test MSE 0.000081, volume helped false (day 54), total bill line −18.0000 (days 75 and 79). Do not paste anchors on days that do not print them; do not round or drop signs when they appear. Day 58’s 0.000782 belongs to the calendar split, not the 0.000081 ruler. BBB 0.000105 stays beside AAA—no auto-transfer.

## Further out

Days 77–78 threshold |ŷ| for speaking; this day foreshadows that.

Always print count=2 for the top decile here.

Top tenth by |ŷ| is two days with higher MAE than the rest. Not the same as quiet/jump by |y|. Days 77–78 threshold |ŷ| for speaking.

Reproduce by running today's script first; unit tests should assert hold-out literals; do not mix train rows or paste price SSE as return MSE.

Hand in one paragraph stating which part of the contract changes today, citing at least one printed anchor.

Quiet ten, jump five, direction-wrong three are contract integers from day 71—do not round them into percentages.

Compare tree and line on hold-out MSE; lower train MSE alone is not a generalization argument.

Merge panel on date and name, not row index—row-index merges break lag alignment like broken pairs.

Random and calendar splits change the test row set—rerun scripts instead of hand-editing one metric.

Name the baseline whenever you write improvement—zero forecast, naive mean, and day-51 line differ.

FORBIDDEN lines are executable policy, not decoration—silent column drops erase audit evidence.

Day 70’s ten lines onboard newcomers but do not replace rerunning days 51, 56, and 67.

Direction scores use signs; level scores use squared or absolute error—do not mix the narratives.

Bill totals are weighted mistake counts, not currency—read −18.0000 as contract arithmetic.

Lag1 means previous trading day, not previous CSV row—sort by date before shifting.

Volume helped false is stretch-specific on nineteen test rows—not a universal claim about volume.

Long Chinese prose is fine; append the stdout core block so peers can verify literals.

## What the run showed

```bash
python3 days/62-top-tenth/top_tenth.py
```

The script should print stdout matching the core block. Implementation: [`top_tenth.py`](../../days/62-top-tenth/top_tenth.py).

Checklist: train/test counts match the script; English keys, signs, and six-decimal literals match the terminal; FORBIDDEN and not-a-result lines stay verbatim; do not swap line versus tree MSE or bill columns; lag-5 anchors (MSE 0.000081, volume helped false, bill −18) stay untouched unless you re-run and update the whole contract.