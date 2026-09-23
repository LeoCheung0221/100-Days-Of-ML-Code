<p align="center"><a href="day-18.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 18 · Return and volume

[Phase I · Models](../../README.en.md) · runs

What you learn today: the median of the five volumes is 1200000. Up on return alone is 3. Up on return and on volume above that median is 1, and the kept session is session 4 only. The label changed because an extra column entered, not because the price was revalued.

## Plain-language account

The five volumes, one per session, are

```text
FIVE_V = [1.0e6, 1.2e6, 0.9e6, 8.0e6, 1.5e6]
```

The unit is shares. Sorted, they are 0.9e6, 1.0e6, 1.2e6, 1.5e6, and 8.0e6. The middle of the five is 1.2e6, which is 1200000. That is the median. It uses only these five volumes. It does not look at the closes.

On the sign of the return alone, three steps are up. Of the four returns 0.8571, 0.5897, 2.2258, and −0.4800, the first three are positive, and they are sessions 2, 3, and 4. Session 5 has return −0.4800, so it does not count. Up on return alone is 3.

Add a second condition: the volume on that step has to sit above 1200000. The volumes on the four steps are the last four sessions: 1.2e6, 0.9e6, 8.0e6, and 1.5e6. The comparison is strictly above.

Session 2 has volume 1.2e6, equal to the median, not above it. The return is positive, and the two conditions together fail. Session 3 has volume 0.9e6, below the median, so a positive return is not kept. Session 4 has a positive return and volume 8.0e6, which is above 1200000, so both conditions hold and the session is kept. Session 5 has volume 1.5e6, above the median, and its return is −0.4800, so it is not kept.

The only session left is session 4. The count goes from 3 to 1. The closes are still 2.1, 3.9, 6.2, 20.0, and 10.4. No price was rewritten. What changed is the definition: it used to ask for the sign of the return, and it now asks for that sign and for volume above the median at the same time. The column that entered is volume.

## Core

```text
median(FIVE_V) = 1200000
up on return alone = 3
up on return and volume > median = 1
session kept = 4
```

| session | return positive | volume | above 1200000 | both |
|---:|---:|---:|---:|---:|
| 2 | 1 | 1.2e6 | 0 | 0 |
| 3 | 1 | 0.9e6 | 0 | 0 |
| 4 | 1 | 8.0e6 | 1 | 1 |
| 5 | 0 | 1.5e6 | 1 | 0 |

The median is computed on all five volumes, including session 1 at 1.0e6. Session 1 has no return relative to a previous close, so it does not enter the four-step labels, and it does enter the median. The third value in the sorted list of five is 1.2e6. The comparison is strict. Session 2's volume 1.2e6 equals the median, strict inequality fails, and that step is excluded. Today's definition is "above," so session 2 is not in the kept set.

The count 3 is the number of 1s in the label built from the return column alone. The count 1 is the number of 1s after the return column and the volume column are combined with a logical and. The two steps that leave, going from 3 to 1, are session 2 and session 3. Their closes were not recomputed, and the price level was not replaced by another price. They leave the label because 1.2e6 and 0.9e6 are not above 1200000.

Session 4 is kept, and it is not kept because its absolute price residual is 8.21. The value 8.21 is the distance from the price to the line. Today's screen does not fit that line. Session 4 is kept because 8.0e6 is above the median and the return on that step is positive. Change the volume, and this step can be screened out even if the close is still 20.0. The label follows the columns that enter the definition. It does not follow a revaluation of the price.

## Further out

Each extra column in a multi-column label narrows the positive class, and the number of positive cases can fall. Today's fall from 3 to 1 is a minimal case of that narrowing. The reason can be pointed at two specific cells: 1.2e6 equals the median, and 0.9e6 is below it. The price does not have to be estimated again in order to explain the fall.

The price path is the same path under both labels. The kept set shrinking to session 4 is the screen going from one column to two. Session 4's volume 8.0e6 is the largest of the five, and its place above 1200000 is a fact about the ordering of these share counts. The label changed because the volume column entered, not because the price was revalued.

The median is reported together with the label. The value 1200000 comes from these five volumes. A sentence that says only "after also requiring heavy volume, one day remains," and that does not say the median is 1200000, leaves the line called "above" impossible to rebuild, and leaves it impossible to rebuild why session 2's 1.2e6 was excluded. The definition contains three things: the return is positive, the volume is taken from these five days, and the bar is their median under a strict inequality. With all three present, the count 3 and the count 1 are two numbers in one sentence.

Median volume 1200000 uses all five sessions including day 1; strict `>` excludes 1.2e6 on day 2. Count drops from 3 to 1 without revaluing any close—only the label definition gained a volume column.
Median 1200000 and strict `>` explain why 1.2e6 fails while 8.0e6 passes—closes are untouched.
Session 4 survives the AND rule; session 5 fails on negative return despite volume above median—closes unchanged throughout.
## What the run showed

```bash
python days/18-return-volume/volume_split.py
```

The script prints the median 1200000, 3 up steps on the return alone, 1 step on which return and volume both hold, and session 4 as the session kept. The implementation is [`volume_split.py`](../../days/18-return-volume/volume_split.py).

The five volumes are 1.0e6, 1.2e6, 0.9e6, 8.0e6, and 1.5e6. The price was not revalued. The label went from 3 steps to the single session 4 because the volume column entered the definition.

