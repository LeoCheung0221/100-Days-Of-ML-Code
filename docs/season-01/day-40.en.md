<p align="center"><a href="day-40.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 40 · A leakage list

[Phase I · Models](../../README.en.md) · runs

The list has six lines, and every line has future=yes: today's high on day 28, later opens in the scale on day 29, the whole-sample scale on day 33, the next-close fill on day 34, a shared date across names on day 37, and the same-day market return on day 38. A score on any of these lines is not a result.

```bash
python days/40-leakage-list/leakage_list.py
```

```text
leakage list
day 28  today's high explains today's close  future=yes
day 29  scale uses later opens  future=yes
day 33  scale uses the test stretch  future=yes
day 34  fill from the next close  future=yes
day 37  random split shares a date across names  future=yes
day 38  same-day market return  future=yes
a higher score on any of these lines is not a result
```

Next the line is fit again on the longer adjusted series, and one jump is checked for whether it still moves the slope.
