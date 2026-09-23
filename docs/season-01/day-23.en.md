<p align="center"><a href="day-23.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 23 · Three equal signs

[Phase I · Models](../../README.en.md) · runs

What you learn today: the rule is written in the program before the count. After three equal adjusted-move signs, and that sign is not 0, predict that the fourth matches. There are 11 events, 6 hits, accuracy 0.5455. The condition was not changed after the result was seen.

## Plain-language account

The series is still the signs of neighboring adjusted closes on the finite AAA rows. The rule is fixed in advance. Starting at the fourth move, if the three signs before it are identical and that sign is not 0, those three signs are the prediction for the fourth. A window that contains a different sign, or three zeros, is not an event. The program walks the series once under that condition and records whether each event hit.

After the walk, there are 11 events and 6 hits. Printed to four decimals, 6/11 is 0.5455. The misses are the other 5. The printed 0.5455 sits above the coin-flip baseline 0.5000 from day 22, and above day 22's 0.4675. Today does not turn that ordering into "the rule has already won." The order that has to stay fixed is this: the condition was written before the count, and after the count the program's "three days" and "equal signs" were not rewritten as another length or another sign.

If 6/11 were seen first, and the window were then changed from three days to two or to four until the accuracy looked better, 0.5455 would no longer be the score of the rule that was written down. It would be the window selected on the same sequence of signs. The program does not do that. The last printed line says the rule is fixed before the count.

## Core

```text
rule = after three equal signs, predict the fourth matches
events = 11
hits = 6
accuracy = 0.5455
the rule is fixed before the count
```

For a move index `i ≥ 3`, the window is `sign(Δ_{i−3})`, `sign(Δ_{i−2})`, `sign(Δ_{i−1})`. When the three are equal and not 0, the prediction for `sign(Δ_i)` is that common sign. The event count is the number of times the window holds. The hit count is the number of times the predicted sign equals `sign(Δ_i)`.

```text
accuracy = 6 / 11 = 0.5455   (four decimals)
```

The 11 and the 6 are the counts from walking this fixed rule across the AAA differences. They are not a window solved backwards from a target accuracy. The denominator is the event count, not the 77 from day 22. Moves that never form three equal signs do not enter 0.5455.

The condition stays "three equal signs" after 0.5455 has been seen. An accuracy whose print sits above 0.5000 does not license a rewrite to another lag. Today's score is 11 events, 6 hits, accuracy 0.5455, and the sentence that the rule was written before it was counted.

## Further out

A rule that is allowed to change after the result is in describes the selection, not the rule. Three equal signs, four equal signs, and five equal signs each produce their own event table on the same signs. If the length may be chosen after the hits are seen, the highest accuracy that gets reported is the length that was picked, and 0.5455 does not say which other lengths were looked at and set down. Writing the rule into the program before the run fixes the length before the run.

Eleven events are also a narrow cover. Day 22's lagged sign makes a prediction on every step, and the denominator is 77. Today a prediction is made only when three equal signs occur, and the denominator shrinks to 11. The number 0.5455 is the hit rate on those 11. It does not estimate what the rule would do on an arbitrary day, because most days never become an event. Six hits and five misses are the whole of those 11.

The 6 and the 11 belong beside 0.5455. The number 0.5455 is not a target accuracy specified in advance. It is what 6 hits divided by 11 events prints at four decimals. The 5 misses stay inside those 11. Shortening or lengthening the window after those 5 misses are seen would replace the event table with another string of hits and misses, and the accuracy would no longer be 0.5455. The program does not change the window. The counts that can be cited today are this set: 11 events, 6 hits, accuracy 0.5455.

Day 24 keeps this same rule, and the score is no longer the full-sample 0.5455. Today's count stays as the result of writing the rule first and counting second. It has not yet been cut into a stretch that was already used to look and a later stretch that is the score. That cut begins at the date 2024-02-28.

Eleven events, six hits, 0.5455—with the three-day rule fixed before counting. Do not retro-fit window length after seeing hits. Denominator is events, not 77.
Eleven conditional events, rule frozen before the count—do not tune window length after seeing 6/11.
Pre-registered three-day rule, eleven events—window length is not a post-hoc knob after seeing six hits.
## What the run showed

```bash
python days/23-three-day-run/three_day_run.py
```

The script prints `events = 11`, `hits = 6`, `accuracy = 0.5455`, and `the rule is fixed before the count`. The implementation is [`three_day_run.py`](../../days/23-three-day-run/three_day_run.py).

The rule is three equal adjusted-move signs, none of them zero, and the fourth is predicted to match. Eleven events produce 6 hits, accuracy 0.5455. The condition was not changed after the result. Next the same rule scores only the later stretch. The earlier accuracy is printed and is not the score.
