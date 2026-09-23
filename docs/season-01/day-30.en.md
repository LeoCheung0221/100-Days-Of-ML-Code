<p align="center"><a href="day-30.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 30 · A fixed lookback

[Phase I · Models](../../README.en.md) · runs

On the last day the value from fitting every adjusted close is 12.1976. The value from the last 20 sessions is 12.0095. The difference is 0.1881. The information set is those 20 sessions, not the whole table.

```bash
python days/30-fixed-lookback/lookback.py
```

```text
lookback = 20
full-sample value at last t = 12.1976
window value at last t = 12.0095
the full sample is not the information set
```

Next the window shrinks to three sessions. The slope is allowed to change sign with local noise.
