<p align="center"><a href="day-46.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 46 · Three fits, next sample

[Phase I · Models](../../README.en.md) · runs

Train SSE is 10.1623 for the line, 16.3596 for ridge, and 1.3953 for the tree. Later SSE is 2.9263, 3.2545, and 2.1488. The fit that is still ahead on the later stretch is the tree. The three training errors are not close. The later ranking is still written on its own. The smallest train SSE is not a substitute for it.

```bash
python days/46-three-fits/three_fits.py
```

```text
model  train_SSE  later_SSE
line  10.1623  2.9263
ridge  16.3596  3.2545
tree  1.3953  2.1488
still alive on the later stretch = tree
```

Next the line is evaluated far outside the training abscissae.
