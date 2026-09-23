<p align="center"><a href="day-15.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 15 · Two kinds of mistake

[Phase I · Models](../../README.en.md) · runs

What you learn today: always-up records up-called-down as 0 and down-called-up as 1. Accuracy 0.75 collapses those two cells into one number. Both cells are required.

## Plain-language account

The sign labels are still 1 1 1 0 on the four steps, from the returns 0.8571, 0.5897, and 2.2258 being positive and −0.4800 being negative. The always-up prediction is 1 1 1 1.

Draw the result as four cells, rows for the actual class and columns for the prediction. Actual up, predicted down: that cell is 0. Always-up never writes down, so it never calls an up step down. Actual down, predicted up: that cell is 1. Only the last step is down, the return −0.4800, and the prediction wrote up.

The other two cells can be counted back from these four steps. The errors total 0 + 1 = 1 step. Four steps minus that one step leaves three steps called correctly, and 3/4 = 0.75. Those three steps all sit in "actual up, predicted up," because the single error already used the only down step. "Actual down, predicted down" is 0: that one down step was not called down.

The accuracy 0.75 folds the four cells into one rate. After the fold, what remains visible is that three quarters of the steps were hits. What is no longer visible is that the entire error sits in down-called-up, and that up-called-down is 0. The 0 in that cell is not the rule recognizing each up step one by one. The rule has no down output, so this cell is 0 on any sample. The cell equal to 1 is the disagreement that actually occurred on these four steps. Both cells have to stay. An accuracy left by itself cannot separate the two kinds of mistake.

## Core

Always-up, on the sign labels:

```text
up called down = 0
down called up = 1
accuracy = 0.75 = (4 − 0 − 1) / 4
```

|  | predict down | predict up |
|---|---:|---:|
| actual up | 0 | 3 |
| actual down | 0 | 1 |

The lower right cell is down called up, equal to 1. The upper left cell is up called down, equal to 0. The upper right cell, 3, is the three positive returns called up. The lower left cell is 0, because the only down step went to the lower right.

Accuracy uses the steps that were called correctly and divides by 4:

```text
(3 + 0) / 4 = 0.75
```

The two error cells cannot be recovered from 0.75. Any four-cell table with three steps right and one step wrong produces 0.75. The error can be an up called down, or a down called up. Today's table is the second kind, and the counts are 1 against 0. A rule that also writes 0 can pair the same 0.75 with different cells. So 0.75 does not stand in for the two cells.

Always-up has a structural fact that is prior to the particular returns on these four steps: the prediction column contains no 0, so the count of up-called-down is identically 0, whatever the returns are. The 0 in that cell is produced by the range of the rule. It is not extra evidence that the rule rarely misses an up move. A missed up move cannot be recorded under this rule, because the rule refuses to predict down. The error cell that can change with the sample is down-called-up. Today it equals 1, which is the number of down steps in the sample. However many down steps there are, that cell equals that count, as long as the rule remains all 1s.

Day 14 reported two accuracies, 0.75 and 0.25. Today opens the 0.75. Once it is open, the summary contains two cells: 0 and 1.

## Further out

The two kinds of mistake are two different records. Calling an up move down places a positive return in the down class. Calling a down move up places a negative return in the up class. A rule that calls up on every step accumulates only the second record. The first record stays at 0. An evaluation that looks only at accuracy shows 0.75 for this rule on labels with three ups and one down, and it folds the only error type into that one rate.

If the two cells have different costs, one number is even less of a summary. Today assigns no price to either cell. The cells have to exist before a weight has a place to multiply. Zero times any weight is still 0. One times a weight is the whole cost of that single down-called-up. The accuracy 0.75 keeps neither the weight nor which cell is nonzero. The cells are written out first.

The same accuracy with different cells also changes how a later score of "how up" is read. A rule that hands in a high up-score on every step, and never hands in down, will also show 0 in up-called-down. That 0 has nothing to do with how high the score is. It has to do with whether the rule ever output down. Today's rule has no score at all, only a hard 1. It already shows that 0.75 has to appear together with the two cells. The cells are 0 and 1. Leave one cell out, and the meaning of the other cell changes.

The confusion matrix cells `up called down = 0` and `down called up = 1` explain the 0.75 accuracy—error type is entirely "down called up" because the rule never emits down. Accuracy alone cannot recover which cell was nonzero.

Keep both cells in the write-up even when 0.75 is quoted as a summary.
Both confusion cells belong in the write-up; 0.75 is derived from `(4−0−1)/4`, not from level residuals.
Show the full 2×2 matrix before quoting 0.75; the structural zero in up-called-down comes from never predicting down.
## What the run showed

```bash
python days/15-two-mistakes/mistakes.py
```

The script prints `up called down = 0` and `down called up = 1`. Folding those two cells into one rate gives the accuracy 0.75, that is `(4 − 0 − 1) / 4`. The implementation is [`mistakes.py`](../../days/15-two-mistakes/mistakes.py).

The 0.75 can stay in the summary, and it cannot be the only thing that stays. Up called down is 0. Down called up is 1. Both cells appear in the result.

