<p align="center"><a href="day-24.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 24 · The rule on the next stretch

[Phase I · Models](../../README.en.md) · runs

What you learn today: the cut date is 2024-02-28. Under the same three-equal-signs rule, the early stretch has 8 events and accuracy 0.5000, and that is not the score. The later stretch has 3 events and accuracy 0.6667, and that is the score. Three events are not a distribution. They only stop the score from being the stretch that was already used to look.

## Plain-language account

The rule is the same as on day 23: three equal adjusted-move signs, none of them zero, and the fourth is predicted to match. On the AAA dates the program takes a cut, and the cut it prints is 2024-02-28. If the day being predicted is after that cut, the event goes to the later stretch. Otherwise it goes to the early stretch. The wording of the rule is not rewritten by the cut. What changes is which stretch is allowed into the score.

The early stretch has 8 events and accuracy 0.5000. Only a split of hits and misses in half on those eight events prints as that four-decimal number. The 0.5000 stays in the print, with the line that the early accuracy is not the score. The later stretch has 3 events and accuracy 0.6667. Only two hits in three events print as 0.6667. Three hits would print 1.0000, and one hit would print 0.3333. The number that enters the score is 0.6667.

Eight plus three is 11, which meets the event count from day 23. Day 23 kept all 11 together and got 0.5455. Today the same events are cut at 2024-02-28. The early 0.5000 is the stretch that can already be looked at. Using it as the score would report the stretch that was already used to look. The later stretch has only 3 events. Three events produce the ratio 0.6667, and that ratio is not a distribution. The sample is too small to read 0.6667 as a stable hit rate. Its job stops at one point: the score is the stretch that has not been treated as already looked at, rather than the early 0.5000.

## Core

```text
cut date = 2024-02-28
early events = 8 accuracy = 0.5000
early accuracy is not the score
later events = 3 accuracy = 0.6667
```

The cut date is 2024-02-28. An event is classified by the date of the day being predicted. A date after the cut goes to the later stretch. A date on or before the cut goes to the early stretch. Both stretches use the same three-day rule. Neither stretch is allowed to pick a new window length.

| Stretch | Events | Accuracy | Score |
|---|---:|---:|---|
| Early | 8 | 0.5000 | no |
| Later | 3 | 0.6667 | yes |

The early accuracy 0.5000 is printed from 8 events. The later accuracy 0.6667 is printed from 3 events. The score column takes only the later stretch. The early stretch is printed so that its exclusion is visible, not so that the higher column can be chosen afterwards. 0.6667 is above 0.5000. That ordering does not put the early stretch back into the score, and it does not make 3 events a distribution.

The whole content of the three events is two hits and one miss, printed as 0.6667. No fourth later event appears in this print. So 0.6667 cannot be replaced by a hit-rate estimate with a width. It is the count on the next stretch, and it keeps the score off the early stretch that was already available to look at.

## Further out

Looking a rule over on one stretch of history, then handing in the accuracy of that same stretch, hands in the stretch that was already seen. Fixing the rule and scoring only the later events separates the score from the stretch that was used to look. Today's cut is written down as 2024-02-28. The early 8 events at 0.5000 are the column left behind after that separation, and the program states that this column is not the score.

Separation does not turn the later stretch into a reliable distribution on its own. The later event count is 3. The ratio 0.6667 flips with each hit: the three events are two hits and one miss. One more miss, or one more hit, would replace this four-decimal number with another number. Today does not add that extra event. Calling 3 events something other than a distribution, while still placing 0.6667 in the score, is coherent because the score is answering a narrow question: is the reported number the early stretch that was already looked at? The answer is that the report is the later stretch, and the early 0.5000 is not the score.

Day 23's 0.5455 is the count on all 11 events together, and today it is no longer the score. The pooled count contains the early stretch. The early stretch already sits where it can be inspected. Once the score is the later 0.6667, the next day does not keep cutting these 3 events. It hands in direction accuracy and a price error side by side.

Cut 2024-02-28: early 8 events at 0.5000 is not the score; later 3 events at 0.6667 is. Three events do not form a distribution— they only move the score off the already-seen stretch.
Later stretch score 0.6667 on three events is a reporting choice, not a confidence interval.
Score is later-segment 0.6667 on three events; early 0.5000 on eight events is labeled not the score.
## What the run showed

```bash
python days/24-next-stretch/next_stretch.py
```

The script prints `cut date = 2024-02-28`, `early events = 8 accuracy = 0.5000`, `early accuracy is not the score`, and `later events = 3 accuracy = 0.6667`. The implementation is [`next_stretch.py`](../../days/24-next-stretch/next_stretch.py).

The score is 0.6667 on the 3 later events. The early accuracy 0.5000 on 8 events is not the score. Three events are not a distribution. They only move the score off the stretch that was already used to look. Next, direction accuracy and the mean absolute return error are handed in together, with a statement of which one a sign decision trusts.

