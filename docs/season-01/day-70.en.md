<p align="center"><a href="day-70.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 70 · Ten-line recap

[Phase I · Models](../../README.en.md) · runs

What you learn today: Ten stdout recap lines including line test MSE 0.000081, verbatim

## Plain-language account

Day 70 compresses the season contract to ten stdout lines without a new fit.

Line test MSE 0.000081 must match day 51; volume line matches day 54.

Recap does not replace per-day scripts.

Data come from name AAA in days/data/panel.csv: simple returns from adjusted close ratios minus one. Usable rows start after the fifth return, so five fewer rows than the raw panel. The default split is the first seventy-five percent of those rows in time order for train and the rest for test (often fifty-four train, nineteen test). Same-bar high, low, and close must not explain same-day return; same-day market return is not a valid feature or label unless the day script says otherwise.

Day 70 ten-line stdout compresses the lag-5 contract without refitting new models.

Treat English stdout keys as the diff authority—spaces around equals, signs, six decimals, and FORBIDDEN lines stay verbatim.

Line test MSE 0.000081 stays the frozen day-51 benchmark on nineteen hold-out rows unless this day explicitly changes the split or label.

## Core


Copy stdout literally: English keys, spacing, signs, and printed decimals. The ```text``` block must diff clean against the day script.

```text
data = days/data/panel.csv name AAA adj_close
task = predict return from five lagged returns
split = first seventy-five percent train time-ordered
baseline = predict zero return
forbidden = same-row high low close and same-day market
line test MSE = 0.000081
tree splits one lag column on a subsample
volume on this stretch did not help test MSE
fill = close to close slippage zero
no live order leaves this script
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

From day 71 onward emphasizes direction and quiet/jump diagnostics.

Use the ten lines as onboarding before deep dives.

Ten-line contract recap including line MSE 0.000081 and volume did not help. Day 71 starts quiet/jump/direction diagnostics.

Reproduce by running today's script first; unit tests should assert hold-out literals; do not mix train rows or paste price SSE as return MSE.

Hand in one paragraph stating which part of the contract changes today, citing at least one printed anchor.

Merge panel on date and name, not row index—row-index merges break lag alignment like broken pairs.

Random and calendar splits change the test row set—rerun scripts instead of hand-editing one metric.

## What the run showed

```bash
python3 days/70-ten-lines/ten_lines.py
```

The script should print stdout matching the core block. Implementation: [`ten_lines.py`](../../days/70-ten-lines/ten_lines.py).

Checklist: train/test counts match the script; English keys, signs, and six-decimal literals match the terminal; FORBIDDEN and not-a-result lines stay verbatim; do not swap line versus tree MSE or bill columns; lag-5 anchors (MSE 0.000081, volume helped false, bill −18) stay untouched unless you re-run and update the whole contract.