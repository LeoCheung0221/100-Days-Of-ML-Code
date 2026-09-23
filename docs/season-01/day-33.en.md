<p align="center"><a href="day-33.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 33 · Standardize on the training stretch

[Phase I · Models](../../README.en.md) · runs

The training-stretch mean and standard deviation of the return are 0.003241 and 0.022132. Including the test stretch, they are 0.002470 and 0.019265. Test MSE under both scales is 0.000109 to six decimals. The score did not move. The whole-sample scale still saw the test stretch. Seeing it and improving on it are not the same event.

```bash
python days/33-train-scale/train_scale.py
```

```text
train mean/std = 0.003241 0.022132
whole-sample mean/std = 0.002470 0.019265
test MSE, scale from the training stretch = 0.000109
test MSE, scale from the whole sample = 0.000109
the whole-sample scale sees the test stretch
```

Next a blank close is filled from the previous session and from the next one. The second fill is marked as a peek.
