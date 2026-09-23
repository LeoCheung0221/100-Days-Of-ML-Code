<p align="center"><a href="day-19.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 19 · Unscaled volume

[Phase I · Models](../../README.en.md) · runs

The raw coefficient on volume is 1.731932e-06 and the raw coefficient on the date is 1.482253. Read as coefficients, volume looks disposable. The mean absolute contributions are 4.3645 and 4.4468, the same order. After standardizing, volume's coefficient is 4.7815 and the date's is 2.7049. The small coefficient is the share-count unit.

```bash
python days/19-unscaled-volume/unscaled.py
```

```text
raw beta time = 1.482253
raw beta volume = 1.731932e-06
mean |time contribution| = 4.4468
mean |volume contribution| = 4.3645
standardized beta time = 2.7049
standardized beta volume = 4.7815
```

Next a noise column is added at a fixed seed. An in-sample improvement does not count.
