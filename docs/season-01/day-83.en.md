<p align="center"><a href="day-83.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 83 · Tree vs line on low-vol weeks

[Phase I · Models](../../README.en.md) · runs

What you learn today: Seven low-vol test days: line MSE 0.000059 beats stump and depth-2; deep vs stump flag is false

## Plain-language account

Day 81 labeled ISO weeks by realized volatility on hold-out rows. Day 83 fixes the seven low-volatility days and scores three frozen predictors on that slice: line MSE 0.000059, stump 0.000221, depth-2 0.000219. The line beats both trees; `deeper tree worse than stump on low vol = false` only means depth-2 slightly edges stump in MSE—not that trees beat OLS.

All splits and coefficients are train-frozen; test applies day-51 β̂ and day-52-style stump rules. Conditional MSE with n=7 is descriptive. Compare day 85, which picks line vs stump on high-vol weeks by MSE.

## Core

```text
regime = low volatility ISO weeks on test stretch
low vol week days = 7
line test MSE low vol weeks = 0.000059
stump test MSE low vol weeks = 0.000221
depth-2 tree test MSE low vol weeks = 0.000219
deeper tree worse than stump on low vol = false
```

Implementation slices `_lag5_line_test` and stump/depth-2 predictions with `_week_vol_high_low` low indices; MSE is mean squared error on the slice.

| Model | Low-vol test MSE |
|---|---|
| line | 0.000059 |
| stump | 0.000221 |
| depth-2 | 0.000219 |

Full-test line MSE remains 0.000081; 0.000059 is conditional. Forbidden columns per days 56–57; no test refit.

## Further reading

**Sample size.** Seven rows make MSE noisy; disclose n whenever comparing 0.000059 to 0.000081.

**Metric choice.** Days 81–82 use MAE; this day uses MSE to stay comparable to days 52–55 tree lessons.

**Depth-2 scope.** Single-column depth-2 is not an ensemble; the false flag compares only deep vs stump ordering.

**Leakage.** Same-day market remains forbidden (days 67, 91, 98).

**Next.** Day 84 crosses quiet/jump/direction with vol buckets; day 85 chooses models on high-vol MSE.

## Lab summary

```bash
python3 days/83-tree-low-vol/tree_low_vol.py
```

Or: `python3 -c "from days.run_day import main; main(83)"`.

Source: [`tree_low_vol.py`](../../days/83-tree-low-vol/tree_low_vol.py)。Keep the ```text``` block identical to stdout.
