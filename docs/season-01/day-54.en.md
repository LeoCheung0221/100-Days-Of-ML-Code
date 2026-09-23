<p align="center"><a href="day-54.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 54 · Drop volume

[Phase I · Models](../../README.en.md) · runs

What you learn today: Five-lag test MSE 0.000081; with volume 0.000121; MSE rise −0.000040; volume helped=false

## Plain-language account

Control: five lags alone score 0.000081; add volume on the same split and test becomes 0.000121.

MSE rise −0.000040 means mse5−mse6; negative means five lags alone win.

volume helped=false means adding volume hurt test MSE, not that volume is missing.

Data come from name AAA in days/data/panel.csv: simple returns from adjusted close ratios minus one. Usable rows start after the fifth return, so five fewer rows than the raw panel. The default split is the first seventy-five percent of those rows in time order for train and the rest for test (often fifty-four train, nineteen test). Same-bar high, low, and close must not explain same-day return; same-day market return is not a valid feature or label unless the day script says otherwise.

## Core

```text
test MSE five lags only = 0.000081
test MSE five lags and volume = 0.000121
MSE rise when volume removed = -0.000040
volume helped on the test stretch = false
```


Test MSE on returns is not the price-level SSE from days 45–46. Hold-out rows are the only score set; coefficients and thresholds are fit on train only.

| Idea | Changes this day? | Note |
|---|---|---|
| Five-lag line coeffs | Usually frozen | From day 51 train |
| test MSE 0.000081 | Reprinted on MSE days | Diagnostics use MAE/direction/bill |
| forbidden OHLC/market | Contract holds | See days 56–57, 67 |
| train/test rows | Default 54/19 | Day 58 calendar cut excepted |

## Core block, line by line

Day 54 prints 4 contract lines:

- `test MSE five lags only = 0.000081`: match the terminal verbatim—keys, spacing, signs, six decimals.
- `test MSE five lags and volume = 0.000121`: match the terminal verbatim—keys, spacing, signs, six decimals.
- `MSE rise when volume removed = -0.000040`: match the terminal verbatim—keys, spacing, signs, six decimals.
- `volume helped on the test stretch = false`: match the terminal verbatim—keys, spacing, signs, six decimals.

Lag-5 anchors: line test MSE 0.000081, volume helped false (day 54), total bill line −18.0000 (days 75 and 79). Do not paste anchors on days that do not print them; do not round or drop signs when they appear. Day 58’s 0.000782 belongs to the calendar split, not the 0.000081 ruler. BBB 0.000105 stays beside AAA—no auto-transfer.

## Further out

Name ablations explicitly; do not claim «more features helped» here.

Day 70 recap repeats that volume did not help—consistent with false today.

Next: three-model MSE and miss-mode sentences.

## How this day connects

Baseline five lags 0.000081; with volume 0.000121; rise −0.000040; helped=false. Day 70 recap repeats volume did not help. Train R² is not delivery evidence.

Engineer reading order: run today's script first, then read the page; do not skip day 51 before diagnostics or the frozen coefficients lose context. Unit tests should assert hold-out scores against printed literals; common failures mix train rows or tickers. Screenshots should show English keys and six-decimal scores. Use python3; tiny float noise is fine, but contract integers like quiet=10, jump=5, and direction wrong=3 must not drift.

## What the run showed

```bash
python3 days/54-drop-volume/drop_volume.py
```

The script should print stdout matching the core block. Implementation: [`drop_volume.py`](../../days/54-drop-volume/drop_volume.py).



Checklist: train/test counts match the script; English keys, signs, and six-decimal literals match the terminal; FORBIDDEN and not-a-result lines stay verbatim; do not swap line versus tree MSE or bill columns; lag-5 anchors (MSE 0.000081, volume helped false, bill −18) stay untouched unless you re-run and update the whole contract.
