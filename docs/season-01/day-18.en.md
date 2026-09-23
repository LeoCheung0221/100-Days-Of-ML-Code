<p align="center"><a href="day-18.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 18 · Return and volume

[Phase I · Models](../../README.en.md) · runs

On the sign of the return, 3 of the 4 steps are up. Requiring volume above the median of the five volumes, 1200000, keeps only session 4. The label changed because a second column entered, not because the prices were refit.

```bash
python days/18-return-volume/volume_split.py
```

```text
median volume = 1200000
up on return alone = 3
up on return and volume = 1
sessions kept = 4
```

Next volume enters a regression unscaled, and the units rewrite the coefficient.
