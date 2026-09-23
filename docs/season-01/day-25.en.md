<p align="center"><a href="day-25.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 25 · Direction and price together

[Phase I · Models](../../README.en.md) · runs

Yesterday's return predicts today's return. Direction accuracy is 0.4675 and the mean absolute return error is 0.0167. On 9 days the price error is no larger than the median and the sign is still wrong. For a sign decision, trust the accuracy, not 0.0167.

```bash
python days/25-two-scores/two_scores.py
```

```text
lag-1 return forecast
direction accuracy = 0.4675
mean absolute return error = 0.0167
days with a small price error and the wrong sign = 9
for a sign decision, trust the direction accuracy
```

Next the rows are split into train and test at random. That number is only the control.
