<p align="center"><a href="day-47.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 47 · Linear extrapolation

[Phase I · Models](../../README.en.md) · runs

The query is t = 118, forty steps past the last training abscissa. The line returns 13.3936. Observed adjusted closes run from 9.8971 to 12.1679. 13.3936 lies outside that interval. The affine class is defined off the support. Being defined is not the same as staying inside the observed prices.

```bash
python days/47-extrapolate/extrapolate.py
```

```text
query t = 118
line value = 13.3936
observed adj close min = 9.8971
observed adj close max = 12.1679
outside the observed range = true
```

Next the same query is given to the tree. The tree can only repeat a leaf.
