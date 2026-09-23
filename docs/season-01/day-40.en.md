<p align="center"><a href="day-40.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 40 · The leakage list

[Phase I · Models](../../README.en.md) · runs

What you learn today: the list has six lines, and every line is future=yes. Day 28 lets today's high explain today's close. Day 29's scale uses later opens. Day 33's scale uses the test stretch. Day 34 fills from the next close. Day 37's random split shares a date across names. Day 38 uses the same-day market return. A higher score on any of these lines is not a result.

## Plain-language account

Six lines stand together, and each is marked future=yes. The mark asks whether the inputs that produced the score include a number the label was not yet allowed to see. If they do, the line stops there. A higher score is not recorded as a better model.

On day 28, today's high and today's close are written on the same bar. In-sample residual sum of squares of close on high is 31.8715, and on yesterday's close it is 35.5233. The sum of squares is smaller by 3.6518, and the reduction comes from a bar that has already finished. On day 29, scaling the close by the mean and standard deviation of every open, including later opens, gives a residual sum of squares of 0.2642 for the return regression. Scaling by past closes only gives 0.2650. The difference is 0.0008. The difference is small, and the scale still contains later opens. On day 33 the whole-sample mean and standard deviation are 0.002470 and 0.019265, the training pair is 0.003241 and 0.022132, and test MSE is 0.000109 on both sides. The score did not move, and the test stretch is still inside the whole-sample moments.

On day 34 the blank close on 2024-02-01 fills from the previous close at 10.1047 and from the next close at 9.8971. 9.8971 is the next close. On day 37, AAA and BBB pooled, random-split test direction accuracy is 0.7234 and the time split is 0.6170. The random split can put the same date on both sides. On day 38, same-day market-sign accuracy is 0.6795, lagged one day it is 0.4026, and the 0.2769 in between was simultaneous. A higher score taken from any of the six lines is not a result.

## Core

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

The list is six designs that have already been run. It is not a new price table. The script prints future=yes on every line, and it ends by stating that a higher score is not a result.

The six lines share a structure: the inputs to the score depend on information from the same time as the label, or from later. Day 28 depends on the high of the same bar. Days 29 and 33 depend on later observations entering a scale. Day 34 depends on the next close. Day 37 depends on the other name's row on the same date, and on the same-day market. Day 38 depends on the same-day market return itself. Once the dependence is in place, a score that improves, a score that worsens, or a score that sits still at six decimals does not rewrite the line as future=no. Day 33 is the line whose score did not move, and future is still yes. Day 29 is the line whose scores differ by 0.0008, and future is still yes. Day 28's sum of squares is smaller by 3.6518, day 37's random split is 0.7234, and day 38's same-day alignment is 0.6795. Those lines look higher, and future is still yes.

## Further out

A leakage list is the negative page of a research log. Each line carries three things: the name of the design, where the information came from, and whether future is yes or no. A future=yes line may keep its print, so that later work can check how the score was obtained. The mark beside the print keeps it out of the result table. The result table takes lines whose inputs were fixed before the label, under a rule written down in advance. Day 39 already showed that a precommitted rule can still have a gross mean of −0.0024, and −0.0044 after subtracting 0.0020. That line is not one of these six. The list's job is to keep the other six scores, the higher ones and the ones that merely held still, outside the result table.

Prints that are not on these six lines stay with their own information sets. Day 31's three-day slope −0.1195 and twenty-day slope 0.0251 come from windows that exclude the last close. Day 32's sixty-day absolute miss 0.4426 is the distance of the old slope on that day. Day 35's business-day gap of 2 is a calendar fact. Day 36's −0.4938 and 0.0124 are returns that are each due on their own price series, and −0.4938 reads the corporate action. These numbers are not rewritten as an edge because a leakage list exists today, and they are not written into the six future=yes lines.

A new day that wants to be added answers first whether its inputs were fixed before the label could be known. Today's high, later opens, the moments of the test stretch, the next close, the same date across names, and the same-day market return are all answered yes today. Changing the model family does not turn the source into no. Linear regression, a tree, or a more flexible fit, as long as it still consumes these inputs, still does not produce a result.

**Negative list.** Six future=yes lines may stay in the log; a higher score on any of these lines is not a result.

## What the run showed

```bash
python days/40-leakage-list/leakage_list.py
```

The script should print six lines, each with future=yes, and the statement that a higher score on these lines is not a result. The implementation is [`leakage_list.py`](../../days/40-leakage-list/leakage_list.py).

Hand in these six lines. Day 28's high, day 29's later opens, day 33's test stretch, day 34's next close, day 37's shared date, and day 38's same-day market return are all future=yes. A higher score is not a result.
