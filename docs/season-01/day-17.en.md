<p align="center"><a href="day-17.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 17 · Checking the stated confidence

[Phase I · Models](../../README.en.md) · runs

What you learn today: the stated P(up) is 0.9634, the realized up frequency is 0.75, and the gap is 0.2134. Steps called ninety-six percent up were up only three quarters of the time. Confidence and frequency sit side by side and do not replace each other.

## Plain-language account

The left column writes the number the rule states: 0.9634. That is the score from day 16, the slope 3.27 passed through the sigmoid, and it is the score on all four steps. The right column does not read the slope. It counts signs. Of the four returns 0.8571, 0.5897, 2.2258, and −0.4800, the first three are positive and the last is negative. The number of up steps is 3, the number of steps is 4, and the frequency is 0.75.

Subtract the two columns: 0.9634 − 0.75 = 0.2134. The gap is positive. The stated confidence is higher than the frequency of up moves on these four steps. Put the two rates in one sentence: these steps were called ninety-six percent up, and they were up three quarters of the time. Ninety-six percent is the reading of 0.9634. Three quarters is the reading of 0.75. Between them sits 0.2134.

The value 0.9634 answers what degree the rule printed. The value 0.75 answers what share of these four steps has a positive sign. The first number can be written before any frequency is counted, because it uses only the slope. The second number can be written only after the four signs have been seen. They are two records. Replace 0.9634 with 0.75, and the record no longer contains the degree the rule stated. Replace 0.75 with 0.9634, and the record no longer contains the rate that occurred on these four steps. The two numbers sit side by side and do not replace each other.

## Core

```text
stated P(up) = σ(3.27) = 0.9634
realized up frequency = (1 + 1 + 1 + 0) / 4 = 0.75
gap = 0.9634 − 0.75 = 0.2134
```

| record | value | what it counts |
|---|---:|---|
| stated confidence | 0.9634 | the sigmoid applied to the slope 3.27 |
| realized frequency | 0.75 | the share of 1s in the four sign labels |
| gap | 0.2134 | confidence minus frequency |

The frequency 0.75 is the positive-class share on the day-14 sign labels: three steps are positive. It does not use 0.9634. The confidence 0.9634 does not use that count of three. After the slope is estimated, the sigmoid computes it once and copies it onto the four steps. The two sides use different information, so there is no reason to require them to be equal in advance. Today they are not equal. The gap is 0.2134.

The sign of the gap states which side is higher: the stated number is 0.2134 above the frequency. The check subtracts two numbers that already exist and keeps the result on a third line.

Given only 0.75, the slope 3.27 does not follow, and the sigmoid output 0.9634 does not follow. Given only 0.9634, it does not follow that three of the four steps are positive. Day 16 already showed that this confidence is the same on all four steps, so it does not mark which step supplied the one negative sign. The negative sign pulls the frequency from all 1s down to 0.75. In the confidence vector, no step is marked lower.

The two cells from day 15 are still there. The hard rule that matches always-up predicts up on every step, so up-called-down is 0 and down-called-up is 1. The value 0.9634 is the degree version of that hard rule, with the same degree on every step. The frequency 0.75 is the share of 1s in the hard labels. Degree, the two cells, and frequency are three objects. Today's check is between degree and frequency. The two cells cannot be read back out of 0.2134: the gap is one real number, and the cells are two counts. They stay in separate columns.

## Further out

The smallest check of a probability forecast is today's table: the forecast on one side, the rate at which the event occurred on the other, and the gap in the middle. The sample has four steps. The frequency 0.75 is 3/4, and the denominator is 4. This check is not a procedure that calibrates a forecast to a frequency in a large sample, and it does not estimate a separate calibration curve. It does one thing: it places the two numbers side by side and refuses to let one cover the other.

On these four steps the forecast is the constant 0.9634. A constant forecast has one group: the four steps share one stated value, and there is one frequency. The frequency inside the group is 0.75, the forecast for the group is 0.9634, and the gap is 0.2134. There is no second group to compare.

A citation carries all three numbers. Cite only 0.9634, and every step reads as nearly certain to be up. Cite only 0.75, and the degree the rule stated disappears, leaving the positive-class share. Cite only 0.2134, and both ends of the gap disappear. The full sentence is: stated 0.9634, realized 0.75, gap 0.2134. Steps called ninety-six percent up were up three quarters of the time. Confidence and frequency sit side by side and do not replace each other.

Calibration check in miniature: stated P(up) 0.9634, realized up frequency 0.75, gap 0.2134. Quote all three; do not replace one with the other. The gap is not the day-15 confusion matrix.
Quote stated, realized, and gap together—never one number alone.
Three-line report: stated, realized, gap—no substitution. Small-n frequency 0.75 is still a realized proportion, not the sigmoid output.
## What the run showed

```bash
python days/17-confidence-check/confidence.py
```

The script prints `stated P(up) = 0.9634`, `realized up frequency = 0.75`, and `gap = 0.2134`. The implementation is [`confidence.py`](../../days/17-confidence-check/confidence.py).

The gap 0.2134 is the stated confidence minus the realized frequency. Ninety-six percent and three quarters both stay in the result. Replace either number with the other, and the check has lost one of its two ends.
