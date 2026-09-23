<p align="center"><a href="day-44.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 44 · A shallow tree

[Phase I · Models](../../README.en.md) · runs

What you learn today: the training sample is the first 75 percent, the first 59 adjusted closes. One split sends t > 38.50 to the right; the implementation puts the left leaf at t ≤ 38.50. The left mean is 10.2690 and the right mean is 11.7467. Training SSE is 2.6315 for the stump and 10.1623 for the line. The slope is replaced by one step.

## Plain-language account

The first 59 sessions stay on the index t, and the label is adjusted close. A line on these 59 points is still a slope. A stump does not use a slope. It picks one cut on the index, uses one constant on the left, and another constant on the right. Each constant is the arithmetic mean of the labels on that side. The cut is the one that makes the sum of the two squared errors smallest.

The printed rule sends t > 38.50 to the right. The prediction implements the other direction of the same cut: t ≤ 38.50 uses the left leaf, and every larger t uses the right leaf. 38.50 is the midpoint of two adjacent training indices, printed to two decimals. The left mean is 10.2690. The right mean is 11.7467. The height of the step is the difference of those printed means, 11.7467 − 10.2690 = 1.4777. Past the cut, the prediction jumps from 10.2690 to 11.7467 and then does not rise with t inside the right leaf.

On the same 59 labels, the stump's residual sum of squares is 2.6315 and the line's is 10.1623. Both sums use the same training prices. The stump is smaller because the step replaces the slope, and the two levels of the step are the two side means. A mean is the best constant on its side under squared error. The line has to carry one slope across all 59 indices, and its training sum of squares is 10.1623.

This comparison lives on the training stretch. Sessions after the cut are not inside these two sums. The claim is: on the first 59 adjusted closes, one split replaces the slope with a step of height 1.4777, and the training SSE changes from the line's 10.1623 to the stump's 2.6315.

## Core

The cut is `int(0.75 × 79) = 59`. Training uses the first 59 rows of the index and of adjusted close. The later stretch is held back. Day 45 is where a sum of squares is computed on that stretch.

The stump search sorts the training index, tries a midpoint threshold wherever two adjacent indices differ, sets each side mean to the sample mean of that side, and keeps the threshold with the smallest sum of the two sums of squares. The prediction is

```text
ŷ(t) = 10.2690    when t ≤ 38.50
ŷ(t) = 11.7467    when t > 38.50
```

```text
train sessions = 59
split when t > 38.50
left mean = 10.2690
right mean = 11.7467
train SSE stump = 2.6315
train SSE line  = 10.1623
```

There is no slope inside a leaf. The right leaf is not a steeper line. It is the constant 11.7467. The line is still an affine function of the same kind as day 41, with coefficients refit on the first 59 rows only. Today's page does not print that 59-row slope. It prints the two training sums of squares.

2.6315 and 10.1623 are both sums on training labels. The query was not held out. A smaller stump SSE says the step fits these 59 points more tightly. It does not say which sum is smaller after the cut. That column is day 45.

## Further out

One split of a regression tree cuts the real line into two pieces and predicts each piece by its label mean. The mean minimizes squared error on that piece, so once the cut is chosen there is no slope parameter left inside the leaf. That is the opposite arrangement from ridge. Day 42 kept the slope and used λ = 20000 to pull it from 0.0299 to 0.0201. Today the slope leaves the prediction function and is replaced by the two levels 10.2690 and 11.7467.

The threshold 38.50 is a cut on the training index, not the name of a calendar event. It sits halfway between two adjacent sessions because the script uses a midpoint, and the left leaf includes the threshold. Only t greater than 38.50 enters 11.7467. Read the printed rule together with that inequality.

A smaller training SSE is what the extra capacity does. Two constants have one more location parameter than a line, and each piece uses the optimal mean under squared error. More capacity can lower the training sum of squares. The drop is not a score on the later stretch. Day 45 adds one more level of depth and prints training SSE beside later SSE. The two columns need not move in the same direction.

Today's print stops on the training column. 2.6315 and 10.1623 share the first 59 labels, and the stump is smaller. The sum of squares after the cut has not appeared. Day 45 prints depth 1's later SSE as 0.5669. That cell cannot be read out of today's training SSE, and 2.6315 is not a result after the sample changes. The step height 1.4777 likewise describes the two training means.

## What the run showed

```bash
python days/44-shallow-tree/shallow_tree.py
```

The script should print `train sessions = 59`, `split when t > 38.50`, left mean `10.2690`, right mean `11.7467`, `train SSE stump = 2.6315`, and `train SSE line = 10.1623`. The implementation is [`shallow_tree.py`](../../days/44-shallow-tree/shallow_tree.py).

Hand in one step on the training stretch. Day 45 allows a child to split again when it has at least 8 sessions, and prints the later SSE next to the training SSE.
