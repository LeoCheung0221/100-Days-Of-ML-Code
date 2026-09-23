<p align="center"><a href="day-31.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 31 · Noise in a three-day window

[Phase I · Models](../../README.en.md) · runs

Predicting the last adjusted close, the three-day slope is −0.1195 and the twenty-day slope is 0.0251. The signs disagree. The three-day absolute miss is 0.0867 and the twenty-day miss is 0.1506. The short window is chasing a local direction. Its smaller miss on this one day is not a claim that it is more accurate. The miss is printed on its own.

```bash
python days/31-three-day-noise/three_day_noise.py
```

```text
three-day slope = -0.1195
twenty-day slope = 0.0251
three-day absolute miss = 0.0867
twenty-day absolute miss = 0.1506
```

Next the window is sixty sessions, set beside these three.
