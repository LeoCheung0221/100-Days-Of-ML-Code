<p align="center"><a href="day-22.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 22 · Yesterday's sign

[Phase I · Models](../../README.en.md) · runs

What you learn today: yesterday's adjusted-move sign predicts today's adjusted-move sign and hits 36/77, accuracy 0.4675. The coin-flip baseline is 0.5000. The rule does not beat a baseline that ignores price.

## Plain-language account

The table is still the frozen file from day 21. The rule uses AAA only, and it first keeps rows whose close and adjusted close are both finite. Day 21 already counted 1 blank AAA close. Subtract neighboring adjusted closes and the result is a sequence of moves. From the second move on, the sign of the previous move is the prediction for today, and it is compared with today's sign. There are 77 comparisons. The signs match on 36 of them and disagree on the other 41. Printed to four decimals, 36/77 is 0.4675.

The coin-flip baseline prints 0.5000. It does not read yesterday's sign and it does not read any price. Each comparison is held against one half. 0.4675 is below 0.5000. The rule used yesterday's price direction, and the hit rate still sits under a baseline that ignores price. Thirty-six hits are not enough to lift the accuracy past 0.5000.

This is not a newly estimated line. The predicted sign is yesterday's adjusted-move sign itself. The size of the move does not enter the rule, only the sign: plus, minus, or zero. Zero appears only when a move is exactly 0. Today's score is the sign accuracy on these 77 comparisons, and the control beside it is 0.5000.

## Core

```text
predict today's adj move with yesterday's sign
hits = 36/77
accuracy = 0.4675
coin-flip baseline = 0.5000
```

Let `Δ_t` be the one-day difference of adjusted close. The rule predicts `sign(Δ_t)` by `sign(Δ_{t−1})`. A hit means the two signs are equal. Accuracy is the hit count divided by the number of comparisons:

```text
accuracy = 36 / 77 = 0.4675   (four decimals)
```

The division 36/77 prints as 0.4675 at four decimals. The denominator 77 is the number of moves that can still be compared after a one-day lag. It is not the 160-row table, and it is not BBB's 80 sessions. BBB does not enter the rule today. The row with the blank close does not enter the difference.

The baseline 0.5000 is a fixed constant. It is not the frequency of up-moves estimated on these 77 steps. The two columns side by side are the rule that reads yesterday's sign, and 0.5000, which reads no price. 0.4675 does not exceed 0.5000. The claim is one sentence: the rule does not beat a baseline that ignores price.

## Further out

A direction rule needs a control that does not use price before the accuracy has a place to stand. Day 14 wrote always-up and always-down on the five handwritten closes, and those two numbers came from the label mix of those five days. Today's control is the coin-flip 0.5000, because the comparison is on sign accuracy, not on a count of how often this table rose. Left alone, 0.4675 looks close to one half. Set beside 0.5000, the one-day lagged sign does not pass the control.

The denominator 77 belongs next to the score. It is the length, on AAA, of finite adjusted closes, after neighboring moves are lagged by one day. A different name, a difference that keeps the blank row, or another column, would be a different sequence of signs, and the denominator would no longer be 77. The number allowed as the score today is the printed 36/77, together with its position relative to 0.5000. The 41 misses say that a rule which uses yesterday's direction can still land below a rule which ignores price.

The place of 0.4675 relative to 0.5000 stays next to the score. Thirty-six hits against 77 steps leave 41 misses. The baseline writes one half as 0.5000. The realized hit count is 36, and the accuracy prints as 0.4675, below that baseline. Below the baseline means that reading yesterday's adjusted-move sign still did worse than a control that reads no price at all. The claim does not need another fitted line, because the rule has no coefficient left to estimate. It does not use BBB's 80 sessions. The denominator stays on AAA's 77 steps. Reading 36/77 by itself as "close to a coin" leaves the fact that it sits under 0.5000 outside the sentence.

The rule has no slope left to estimate. It was already written as "yesterday's sign" before these 77 steps were counted. Day 23 writes another rule into the program first, and only then counts how many events it covers. Today's claim stops here: 36/77, accuracy 0.4675, coin-flip baseline 0.5000, and the lagged sign does not beat a baseline that ignores price.

36/77 ⇒ 0.4675 below coin 0.5000. Baseline must sit beside the rule accuracy. Denominator 77 is AAA lagged segments, not the full 160-row panel.
36/77 beats nothing about coin 0.5000—0.4675 is strictly below the baseline.
Denominator 77, not 80; 0.4675 is strictly below coin 0.5000—state the inequality explicitly in write-ups.
## What the run showed

```bash
python days/22-lagged-direction/lagged_direction.py
```

The script prints `hits = 36/77`, `accuracy = 0.4675`, and `coin-flip baseline = 0.5000`. The implementation is [`lagged_direction.py`](../../days/22-lagged-direction/lagged_direction.py).

The prediction is yesterday's adjusted-move sign. The sample is 77 comparable moves on AAA, with 36 hits. 0.4675 is below 0.5000. Next the rule "three equal signs, then the fourth matches" is written into the program, and only then counted.

