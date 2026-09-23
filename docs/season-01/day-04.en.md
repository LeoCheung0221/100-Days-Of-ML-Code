<p align="center"><a href="day-04.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 4 · The endpoint chord

[Phase I · Models](../../README.en.md) · runs

What you learn today: the endpoint chord and ordinary least squares are the same affine class. The chord's absolute loss 12.0000 is below the line's 16.6600. The chord's squared loss 136.3837 is above the line's 96.3390. One shape, two losses, opposite ranks.

## Plain-language account

Hold only the first close and the fifth, and draw the segment between them. The closes are 2.1 and 10.4, four steps apart. The slope is `(10.4 − 2.1) / (5 − 1) = 2.075` and the intercept is 0.025, so the chord is `ŷ = 2.075x + 0.025`. It is a straight line, the same class as `ŷ = 3.27x − 1.29`. The class matches. The rule that picks the coefficients does not. The chord sees two endpoints. Least squares sees the sum of squares on all five points.

Score both lines on all five points. Absolute loss is 12.0000 for the chord and 16.6600 for least squares, so the chord is smaller. Squared loss is 136.3837 for the chord and 96.3390 for least squares, so the chord is larger. Session 4's absolute residual is 11.6750 on the chord and 8.2100 on the line. "The chord is always worse" is a squared-loss sentence. "The chord is always better" is an absolute-loss sentence. Each sentence promotes one loss to the whole comparison.

The chord cannot beat least squares on squared loss. Least squares is defined as the minimum of that sum inside this affine class. Any other slope and intercept, including this chord, has a sum of squares at least as large. Absolute loss has no such guarantee. The chord can win there, and on these five points it does.

Session 4's cell is larger on the chord but total `L1` is still smaller—middle sessions can be closer on the chord. Squared loss punishes the large session-4 miss more heavily, which is why `L2` reverses the rank.

## Core

The chord uses only `(1, 2.1)` and `(5, 10.4)`:

```text
β₁ = (10.4 − 2.1) / (5 − 1) = 2.075
β₀ = 2.1 − 2.075 × 1 = 0.025
ŷ = 2.075x + 0.025
```

Ordinary least squares remains the day-1 solution. Both lines are scored on all five points.

| Fit | L1 | L2 | session-4 \|r\| |
|---|---:|---:|---:|
| Endpoint chord | 12.0000 | 136.3837 | 11.6750 |
| Ordinary least squares | 16.6600 | 96.3390 | 8.2100 |

On `L2` the chord is larger. That is the definition of least squares inside one affine class, not a property of this particular sample. On `L1` there is no matching theorem. Today's absolute-loss minimizer is still not computed. The computed fact is narrower: this chord can be smaller on `L1` and larger on `L2` at the same time.

Do not rank the fits by the session-4 residuals 11.6750 and 8.2100 alone. That cell is one of five. The ranks that matter are the full `L1` and the full `L2`. Day 2 already showed that one cell can have very different shares in the two norms. Today the full norms themselves reverse.

| Fit | Coefficient rule | Wins on L1 (this sample) | Wins on L2 |
|---|---|---|---|
| Chord | endpoints (1,5) | yes (12.0000) | no |
| OLS | min sum of squares | no (16.6600) | yes (96.3390) |

## Further out

A common swap in model comparison is to choose the loss you win and then call the win "the better model." Linear factors, ridge, and trees sit in different classes, and even one class can be fit under different objectives. One reported error cannot say whether the rank survives a change of norm.

These two lines share a function class. The only difference is how the coefficients are chosen. The class can still reverse the rank: 12.0000 against 16.6600 on `L1`, 136.3837 against 96.3390 on `L2`. When two fits are compared, name the class and name the loss. An advantage on one loss is not a claim that the line is better on every loss. Out-of-sample rank is a later question. Both losses today are on the five training points.

Pitch decks that show only the loss where the chord wins mislead; slides should carry all four totals. Day 5 deleting session 4 moves OLS, not the chord's endpoint formula. Day 9 row shuffle does not change either line's coefficients when pairs stay intact.

## What the run showed

```bash
python days/04-endpoint-chord/endpoint_chord.py
```

The script should print the chord `ŷ = 2.075x + 0.025` and the losses in the table. The implementation is [`endpoint_chord.py`](../../days/04-endpoint-chord/endpoint_chord.py).

Hand in one rank reversal inside one affine class. Do not call the chord always worse, and do not call it always better. It cannot win on squared loss, by definition. It can win on absolute loss, and here that win is 12.0000 against 16.6600. Day 5 removes session 4 from the estimation sample and records how far the line moves. That move is not an exam score.

Self-check: all four loss cells present? Session-4 \|r\| not substituted for full norms? Model card lists class, coefficient rule, training loss, and reported loss.
