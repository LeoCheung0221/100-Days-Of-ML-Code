<p align="center"><a href="day-48.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 48 · The tree does not extrapolate

[Phase I · Models](../../README.en.md) · runs

What you learn today: the same query, t = 118. A depth-2 tree returns 11.9608, inside the minimum and maximum of the adjusted closes it was fit on. The line is still 13.3936, outside that interval. The tree has no slope outside the support. It repeats the rightmost leaf mean.

## Plain-language account

Day 47 substituted the line at t = 118 and got 13.3936, above the maximum adjusted close already seen, 12.1679. Today the prediction function changes and the query stays. The tree is fit on all 79 adjusted closes, at depth 2, and a child still splits only with at least 8 sessions. Prediction walks the index down from the root threshold. Each side is a constant, or one more layer of constants. Once the query falls to the right of every threshold, the path is in the rightmost leaf, the prediction equals that leaf's mean, and it is not multiplied by t.

t = 118 is 40 steps past the last observed index, so it lands in the rightmost leaf. The printed tree value is 11.9608. The number does not increase because the query is another 40 steps out. The line at the same query is 13.3936, and it does keep increasing with the slope. Outside the support, 11.9608 stays put and 13.3936 does not.

Compare 11.9608 with the ends of the sample: minimum 9.8971, maximum 12.1679. 11.9608 sits between them. The script prints tree stays inside the training range = true. The range is the minimum and maximum of the 79 labels the tree was fit on, the same pair day 47 printed. 13.3936 is not between that pair. Day 47 already marked the line outside the observed range = true.

The claim is the pair of readings. At t = 118 the tree's value is the rightmost leaf mean 11.9608, inside [9.8971, 12.1679]. The line at the same query is 13.3936, outside that interval. No slope outside the support carries the tree any higher.

## Core

The tree and the line are both fit on all 79 adjusted closes, not on day 44's 59-row cut. So 11.9608 is not the right leaf 11.7467 of the stump on the training cut, and it is not the 11.7285 that day 49 will read on the jump date. If the jump date falls in an interior leaf, that constant can differ from the rightmost leaf. t = 118 takes the rightmost leaf, and the leaf mean is 11.9608.

```text
query t = 118
tree value = 11.9608
line value = 13.3936
tree stays inside the training range = true
```

Inside a leaf the prediction has derivative 0 in t. To the right of the last threshold the rightmost leaf is one constant, so 118 and any farther query — there is no new threshold outside the support — both read 11.9608. The line's slope in t is not 0, so another 40 steps can leave 12.1679.

In this printout, `training range` means the range of the labels in the fit, the 79 adjusted closes. The test allows a numerical tolerance, and the printed result is true. 11.9608 itself lies between 9.8971 and 12.1679 without needing the tolerance.

There is no label at t = 118, so neither 11.9608 nor 13.3936 is a residual. The comparison is two function values, and where they sit relative to the labels already seen.

## Further out

A piecewise constant extrapolated past the last cut equals the mean of the rightmost piece. That is the shape of the function class, not an extra constraint that clips 11.9608 into the price interval. It lands inside the interval because the leaf mean is a mean of labels in the sample, and a mean lies between the minimum and maximum of those labels. The line's 13.3936 has no such restriction from a mean. It can sit above every label in the fit.

When a tree is read past the end of a sample, the reading is the level of the latest piece, not a slope times the remaining horizon. Move the query farther out and this tree's answer in t is still 11.9608. The line keeps walking at the full-sample slope 0.029901. The two extrapolations answer different questions. The tree answers what the average adjusted close is in the rightmost leaf. The line answers what the in-sample tilt produces at t = 118.

11.9608 lying inside the observed range means it is a mean of labels in the sample. It does not mean the price at t = 118 will be 11.9608. That session was not observed. Day 47 keeps the same reservation about 13.3936: a function value is not a close that has not arrived.


<!-- uniq-exp-en-27-50 -->

Same t: tree 11.9608 flat leaf vs line 13.3936; tree stays inside training range.

## What the run showed

```bash
python days/48-tree-leaf/tree_leaf.py
```

The script should print `query t = 118`, `tree value = 11.9608`, `line value = 13.3936`, and `tree stays inside the training range = true`. The implementation is [`tree_leaf.py`](../../days/48-tree-leaf/tree_leaf.py).

Hand in the leaf constant 11.9608 outside the support, next to the line's 13.3936. Day 49 returns to the jump date 2024-02-28 and places the full-sample line, ridge with λ = 20000, and this tree on the same index. The two lines meet on that index.
