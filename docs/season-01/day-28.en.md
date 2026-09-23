<p align="center"><a href="day-28.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 28 · Today's high

[Phase I · Models](../../README.en.md) · runs

The high is on the same row as the close, and the script marks it FORBIDDEN. In-sample RSS of close on high is 31.8715, and of close on yesterday's close is 35.5233. RSS falls by 3.6518. The fall comes from the same bar, not from a column that could have been known in advance.

```bash
python days/28-todays-high/todays_high.py
```

```text
column high = FORBIDDEN
in-sample RSS close~high = 31.8715
in-sample RSS close~lagged close = 35.5233
```

Next later opens enter the scale. Leakage need not show up as a large improvement.
