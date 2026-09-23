<p align="center"><a href="day-47.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 47 · Linear extrapolation

[Phase I · Models](../../README.en.md) · runs

What you learn today: the query is t = 118, forty index steps past the last abscissa. The line takes the value 13.3936 there. Observed adjusted closes run from 9.8971 to 12.1679. 13.3936 lies outside that interval. The affine class is defined beyond the support. Being defined is a different fact from the value still lying among prices already seen.

## Plain-language account

The lines in the previous days were drawn on indices that had already appeared. Today the query sits 40 steps past the last index in the sample, and the script prints t = 118. Those 40 steps have no adjusted close. The line does not lose its formula. It is still slope times t plus intercept, with coefficients from ordinary least squares on all 79 adjusted closes. Substitute t = 118 and the value is 13.3936.

Among adjusted closes already seen, the minimum is 9.8971 and the maximum is 12.1679. 13.3936 is larger than 12.1679. The script therefore prints outside the observed range = true. The interval is an interval of prices, not of indices. t = 118 is of course past the largest index; that is how the query was placed. true says something else: the computed price 13.3936 is also outside the minimum and maximum of prices already seen.

The affine class {β₀ + β₁ t} returns a number for every real t. The support is the set of indices used in the fit. Outside that support the formula still evaluates, and 13.3936 is the number it evaluates to. Evaluability means the function class does not stop writing at the last index. It does not mean 13.3936 ever appeared as an adjusted close in the sample. The highest adjusted close in the sample stops at 12.1679.

The claim is the two sentences together. The line is defined at t = 118, and the value is 13.3936. That value lies outside the observed adjusted-close interval [9.8971, 12.1679].

## Core

The fit uses all 79 adjusted closes, not the 59-session training cut. The cut from days 44 through 46 is not used today. The query is the last abscissa plus 40, printed as 118.

```text
query t = 118
line value = 13.3936
observed adj close min = 9.8971
observed adj close max = 12.1679
outside the observed range = true
```

The test is: the fitted value is below the sample minimum adjusted close, or above the sample maximum. 13.3936 > 12.1679, so the flag is true. The lower end 9.8971 is not crossed. The upper end is.

There is no label at t = 118, so a residual is undefined. 13.3936 is not an error. It is a function value. Calling it an extrapolation error would require a close that was not observed. The sample does not provide that close.

The full-sample slope on day 41 is 0.029901, positive. The query is 40 steps past the last index, so the fitted value keeps walking along that positive slope. At 13.3936 it is already above the sample maximum adjusted close 12.1679. A positive slope and a far enough query leave the observed price interval. Today prints that fact as true, together with 13.3936 and 12.1679.

## Further out

Extrapolation shows up when a holding date sits further out than the estimation sample: a slope fit on a historical index is read at some t after the sample ends. An affine function permits the reading, because its domain is the whole real line. The result is then compared, separately, with the range of prices already seen. The excess of 13.3936 over 12.1679 is the whole numerical content of this comparison. The excess is not a realized profit or loss, because t = 118 has no trade price.

Support and domain are different notes. Support is the indices the data occupy. Domain is where the function class agrees to evaluate. An ordinary least-squares line is wide on the second and narrow on the first. The tree on the next day reverses the arrangement: past the support it does not follow a slope, and it repeats the rightmost leaf mean. Today the line's arrangement is fixed. The defined value is 13.3936. It lies outside the observed interval.

Day 41's deletion showed that one jump on 79 points barely moves the slope. The slope is still there, so extrapolation multiplies that slope past the support. A jump that does not twist the slope does not remove 13.3936 at t = 118. The two days are two facts.

13.3936 lies above the maximum 12.1679. The lower end is not crossed: 9.8971 remains below the fitted value. The flag true is decided at the upper end. A query that landed on an index already seen would still leave the affine function defined, and the value could fall inside [9.8971, 12.1679]. Today the query is the last abscissa plus 40, so definition and range show up together: t = 118 has a function value, and that value is not among the prices already seen.

## What the run showed

```bash
python days/47-extrapolate/extrapolate.py
```

The script should print `query t = 118`, `line value = 13.3936`, observed adjusted-close minimum `9.8971`, maximum `12.1679`, and `outside the observed range = true`. The implementation is [`extrapolate.py`](../../days/47-extrapolate/extrapolate.py).

Hand in the function value outside the support, and where it sits relative to the prices already seen. Day 48 gives the same t = 118 to a depth-2 tree. The tree has no slope outside the support. It repeats the rightmost leaf mean.
