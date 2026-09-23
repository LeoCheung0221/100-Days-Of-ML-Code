<p align="center"><a href="day-16.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 16 · A score for up

[Phase I · Models](../../README.en.md) · runs

What you learn today: putting the slope 3.27 into the sigmoid gives 0.9634. The same score is attached to every step. The affine one-day difference is constant, so this score cannot rank the four steps by confidence.

## Plain-language account

The direction output of the previous days was a hard 1: call up on every step. Today a degree is placed in front of that 1. The slope already estimated, 3.27, is passed through the sigmoid. The sigmoid maps a real number into a number between 0 and 1. The input 3.27 is positive, and the output is 0.9634.

This 0.9634 depends only on the slope. The slope is one coefficient of the whole line `ŷ = 3.27x − 1.29`, not the return of a particular step. The four actual returns are not the same. They are 0.8571, 0.5897, 2.2258, and −0.4800. The degree score does not read those four numbers. It reads 3.27 once, and then copies the result onto every step. Each of the four steps is labeled 0.9634.

The copy is a fact about the shape of the line. The one-day difference of the affine line is

```text
Δŷ_t = 3.27
```

for t = 2, 3, 4, 5. The difference does not change with t, so the sigmoid's input does not change with t, and the output does not change with t either. There is no high step and no low step in the degree. Sort the four steps by this score and they tie. A score that is the same on every step cannot say that one step is held with more confidence than another.

The value 0.9634 is also not yet the frequency of up moves on these four steps. A frequency counts how many returns are positive, and that check is the next chapter. Today's precise statement stops at ranking: because the affine one-day difference is constant, the single number sigmoid(3.27) = 0.9634 covers all four steps, and it cannot separate them by confidence.

## Core

```text
σ(z) = 1 / (1 + exp(−z))
z = β₁ = 3.27
σ(3.27) = 0.9634
```

The score vector on the four steps is

```text
0.9634, 0.9634, 0.9634, 0.9634
```

It is a constant vector. The difference between any two steps is 0. There is no step index whose score is strictly larger than another's. A confidence ranking needs at least two distinct values. There are none here.

The input is constant because the difference of an affine function in t is the slope, and the slope is not a function of t. If the score used information that belonged to one step, the input would contain that step's return, or that step's price residual. Today's input contains only 3.27. The day-4 step, whose absolute residual is 8.21, and the day-5 step, whose absolute residual is 4.66 and whose direction misses, do not turn 0.9634 into two numbers. The degree score writes the same number on both days.

The value 0.9634 is also not a cell of the four-cell table from day 15. That table counts a hard classification: for always-up, down-called-up is 1 and up-called-down is 0. The sigmoid does not make that hard call and then count. It maps the slope to a number between 0 and 1 and copies the number four times. The map is monotone: a larger slope moves the number closer to 1. It does not check how many of the four steps are in fact positive. That check needs another number, placed beside 0.9634.

The direct consequence of being unable to rank is that these four steps cannot be ordered into a first and a second by "more like up." If the task is to keep only the step with the highest score, this rule cannot hand that step over, because the four scores are equal. What it can hand over is one shared degree, 0.9634, and the fact that the degree comes from the slope rather than from the return of a single step.

## Further out

Replacing a hard label with a score between 0 and 1 is often described as the rule beginning to state a confidence. A confidence distinguishes cases only when it can vary across them. A rule that prints 0.9634 on all four steps is stating how large the slope of the whole line is. It is not stating how clear the up-or-down call is on one step. The slope already fixed the direction on day 11: a positive slope is the rule that calls up on every step. The sigmoid turns that positive sign into a decimal near 1. How near it sits is decided by the size of 3.27, not by how far the four returns sit from one another.

So 0.9634 is read as the degree written once and shared by the four steps. It does not assign a different confidence to each step. The frequency has not been computed. Under this definition the four steps have the same degree. If a later score uses a feature of a single step, the four numbers can differ, and a ranking can exist. Today's feature is one slope on the whole sample, and the ranking does not exist.

There is also a reading that connects the constant score to the baseline. On day 14, always-up hands in 1 on every step as a sign. Today the degree hands in 0.9634 on every step. Both outputs do not change with t. The difference is the literal values 1 and 0.9634. The literal value changed, and the ability to rank did not appear. Judging this score includes a separate question: can it separate the four steps? It cannot. A score that cannot separate them cannot be used to pick out the day held with more confidence.

Sigmoid slope score 0.9634 repeats on all four steps because `Δŷ` is constant; that is not confidence ranking. Day 17 will show stated 0.9634 vs realized frequency 0.75. Level residuals 8.21 and 4.66 do not enter the sigmoid input in today's script.
Constant 0.9634 on all steps means no confidence ranking; day 17 adds the frequency check.
Without per-step features, σ(β₁) cannot rank days—day 17 adds the frequency gap check on the same constant score.
## What the run showed

```bash
python days/16-up-score/up_score.py
```

The script prints the slope 3.27, `P(up) = sigmoid(slope) = 0.9634`, and states that the same score is attached to every step. The implementation is [`up_score.py`](../../days/16-up-score/up_score.py).

The value 0.9634 comes from the slope, not from the step-by-step differences among the four returns. The affine one-day difference is constantly 3.27, so this score for up cannot rank the four steps by confidence.
