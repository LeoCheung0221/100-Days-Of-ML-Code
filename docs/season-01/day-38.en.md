<p align="center"><a href="day-38.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 38 · Lag the signal one day

[Phase I · Models](../../README.en.md) · runs

The same-day market sign matches the same-day adjusted sign on 0.6795 of sessions. Lagged one day, the rate is 0.4026. The 0.2769 that disappeared was simultaneous. The 0.4026 that remains is below 0.5, and it is not a usable forecast.

```bash
python days/38-lag-signal/lag_signal.py
```

```text
same-day market sign accuracy = 0.6795
lagged-one-day market sign accuracy = 0.4026
what disappeared was simultaneous
```

Next one minimum round-trip cost is subtracted from the strategy return.
