<p align="center"><a href="day-46.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 46 · Three fits on a new stretch

[Phase I · Models](../../README.en.md) · runs

What you learn today: on the first 59 adjusted closes, training SSE is 10.1623 for the line, 16.3596 for ridge, and 1.3953 for the tree. Later SSE is 2.9263 for the line, 3.2545 for ridge, and 2.1488 for the tree. The smallest later SSE is the tree. The three training numbers sit far apart. The later ranking is read on its own. The smallest training SSE does not fill the later cell.

## Plain-language account

All three models are fit on the first 59 adjusted closes, then scored by residual sum of squares on the sessions after the cut. The line is ordinary least squares. Ridge is still λ = 20000 on the slope only, intercept free, except that Σt² now comes from the training indices rather than from the 79 points of day 42. The tree is the depth-2 tree of day 45. A child still splits only when n ≥ 8.

Read the training column first. The line is 10.1623, the same training SSE as the line on day 44. Ridge is 16.3596, larger than the line, because the penalty pulls the slope and the training sum of squares rises. The tree is 1.3953, the same training SSE as depth 2 on day 45. The three numbers 1.3953, 10.1623, and 16.3596 sit far apart. Inside the training column the order is tree, line, ridge.

The later stretch is a separate column. The line is 2.9263, ridge is 3.2545, and the tree is 2.1488. The order is again tree, line, ridge, and the numbers are a different set. The tree's later SSE 2.1488 is depth 2's later SSE from day 45, not depth 1's 0.5669. The script prints the name with the smallest later SSE as tree. That name is the minimum of the later column. It is not the training number 1.3953 read out a second time.

The winner of both columns happens to be the tree. The reading does not change. The later scores are 2.1488, 2.9263, and 3.2545. The training scores are 1.3953, 10.1623, and 16.3596. Day 45 already supplied a counterexample: depth 2's training SSE is smaller than depth 1's, and its later SSE is larger. "Smallest on the training column" does not fill the later cell. Today's later cell is the printed 2.1488.

## Core

```text
model  train_SSE  later_SSE
line  10.1623  2.9263
ridge  16.3596  3.2545
tree  1.3953  2.1488
still alive on the later stretch = tree
```

The training column, largest to smallest, is ridge 16.3596, line 10.1623, tree 1.3953. The later column, smallest to largest, is tree 2.1488, line 2.9263, ridge 3.2545. In the script, `still alive` is the name with the smallest later SSE. On this table that name is tree.

Ridge uses λ = 20000 on the slope entry of the training design, and the intercept is unpenalized. Do not copy day 42's full-sample slope 0.0201 onto these 59 rows. Today's script does not print a slope. It prints sums of squares. 16.3596 is larger than 10.1623, so the penalized fit is worse on the training labels. That is the same fact as the penalty pulling the slope off least squares. The slope itself is not reported today.

The tree row is not day 44's stump. The stump's training SSE is 2.6315, and depth 1's later SSE is 0.5669. Depth 2 is the pair 1.3953 and 2.1488. The tree in the three-model table is depth 2.

Each later number is smaller than that model's training SSE, and the later stretch is also shorter. Comparing 2.1488 with 1.3953 across columns compares sums of squares on different lengths. Rank models inside a column. Inside the later column, the smallest entry is 2.1488.

## Further out

A ranking after the sample changes is the ranking in the column that changed. The training column answers which sum of squares is smaller on these 59 points. The later column answers which sum of squares is smaller on the stretch that did not enter the fit. Both sentences stay on the page. The training column alone puts ridge last at 16.3596 and the tree first at 1.3953, and neither of those cells is a later error. On the later stretch ridge is 3.2545, the tree is 2.1488, and the line sits between them at 2.9263.

The training triple is 1.3953, 10.1623, and 16.3596, with the line sitting between the other two. The line has one slope. Ridge has that slope pulled by 20000, and the training sum rises to 16.3596. The depth-2 tree has several constants, and the training sum falls to 1.3953. Write the training error cell by cell. Write the later stretch as 2.1488, 2.9263, and 3.2545. The smallest later cell is the tree's 2.1488. Day 45's depth-1 later SSE 0.5669 is smaller than 2.1488, and depth 1 is not in this three-model table.

`still alive = tree` is a conclusion about the later column. It does not rewrite day 45's four cells. Depth 1's later SSE is 0.5669, which is smaller than depth 2's 2.1488. The three-model comparison does not put depth 1 in the table. The tree that is smallest there is the depth-2 tree, relative to the line and to ridge, not relative to depth 1.

**Later stretch winner.** Tree SSE 2.1488 is smallest on the later segment; ridge train SSE 16.3596 is not the score column.

## What the run showed

```bash
python days/46-three-fits/three_fits.py
```

The script should print three rows of sums of squares: the line `10.1623` and `2.9263`, ridge `16.3596` and `3.2545`, the tree `1.3953` and `2.1488`, and `still alive on the later stretch = tree`. The implementation is [`three_fits.py`](../../days/46-three-fits/three_fits.py).

Hand in both rankings, with the later column's minimum at the tree. Day 47 takes the line outside the observed abscissae. The query is 40 past the last index, t = 118.
