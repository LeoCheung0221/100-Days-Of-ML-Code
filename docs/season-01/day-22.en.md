<p align="center"><a href="day-22.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 22 · Yesterday's direction

[Phase I · Models](../../README.en.md) · runs

Yesterday's adjusted sign predicts today and hits 36/77, accuracy 0.4675. The coin-flip baseline is 0.5000. The rule does not beat a baseline that looks at no price.

```bash
python days/22-lagged-direction/lagged_direction.py
```

```text
predict today's adj move with yesterday's sign
hits = 36/77
accuracy = 0.4675
coin-flip baseline = 0.5000
```

Next the rule 'three equal signs, the fourth matches' is frozen, and only then counted.
