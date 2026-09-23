<p align="center"><a href="day-39.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 39 · A round-trip cost

[Phase I · Models](../../README.en.md) · runs

What you learn today: the rule was written down in advance. When yesterday's market rose, the position is long AAA, and the position is the sign of yesterday's market return. The gross mean return is −0.0024. The round-trip cost is 0.0020. The net mean is −0.0044. The gross return was already negative. There was no positive edge for the cost to remove.

## Plain-language account

The position is fixed before today's AAA return is seen, and it uses only yesterday's market return. When yesterday's market return is positive, the position is long. Under the sign rule, a negative market return yesterday is a short position, and a zero sign is recorded as long. The holding return that day is this position times AAA's adjusted simple return. The mean of those holding returns is −0.0024.

The round-trip cost 0.0020 is subtracted from that mean. The net mean is −0.0024 − 0.0020 = −0.0044. The cost moves an average that was already negative down by another 0.0020. There was no positive gross mean on the other side of zero. If the gross mean were positive, the cost would have a chance to turn a positive into a negative, which is a cost removing an edge. Here the gross mean is −0.0024. The edge is absent before the cost is applied. The cost did not destroy a positive edge, because the gross return was already negative.

The rule is this one, committed in advance. It is not the rule left over after signs and lags have been swapped on the table. Today does not search for a rule whose gross mean is positive.

## Core

```text
gross mean return = -0.0024
round-trip cost = 0.0020
net mean return = -0.0044
```

The market return and AAA's adjusted return are both simple returns. The position is the sign of the market-return series with the last item dropped, and a zero sign is recorded as long. The gross return is that position times AAA's return series with the first item dropped. The cost is the constant 0.0020, subtracted once from the mean.

−0.0024 is the mean holding return before the cost. −0.0044 is the mean after subtracting 0.0020. The two negatives are read gross first, then net. Seeing −0.0024 first shows that the cost's role is not the removal of a positive expectation. A positive expectation would have to appear on the gross line. That line does not show one.

0.0020 is a round-trip deduction written down in advance and applied to the mean. It is not a broker schedule estimated from turnover after the fact. Today does not change the number, and it does not search for a cost assumption that would make the net positive. Under the written 0.0020, the net is −0.0044.

## Further out

A cost experiment has a fixed order. Write the rule down, report the gross mean, then subtract the cost. Changing the rule after seeing the sign of the gross mean produces a positive gross that is the product of a search. The net that remains after the cost is then not the result of the precommitted rule. Today's order holds: the rule is the sign of yesterday's market return, a rise yesterday is a long position, the gross mean is −0.0024, the cost is 0.0020, and the net is −0.0044.

Yesterday's lagged sign accuracy is 0.4026, already below 0.5. Today puts the same kind of lagged information into a position, and the mean holding return is −0.0024. Both prints sit on the side where there is no positive edge to hand to a cost. Accuracy below one half does not automatically equal a negative mean return, because the size of the return and a sign hit are not the same number. Today prints the mean return directly, so −0.0024 does not have to be inferred from 0.4026. Each number is computed on its own. The gross line is −0.0024.

The net mean −0.0044 is lower than the gross mean −0.0024 by the written 0.0020. That gap says the cost, on this table, takes another slice off a holding return that was already negative. A sentence that says the cost destroyed an edge needs a positive number on the gross line first. −0.0024 leaves that sentence with nothing to attach to. The rule is not taken back and rewritten: the position is still the sign of yesterday's market return. Flipping the position after the three prints, and obtaining some positive gross, belongs to another search. It does not belong to the rule written down today.

Next, the earlier designs already marked as seeing the future are collected into a list of six lines. Every line is marked future=yes. A higher score on those lines is not recorded as a result.

Gross mean −0.0024, round-trip cost 0.0020, net −0.0044. No positive edge existed before costs.

Report gross before net; searching rules after seeing −0.0024 is a different experiment than today's pre-committed sign rule.

**Costs.** Net mean −0.0044 after round-trip 0.0020—sign rules and fee-adjusted means are different reports.

## What the run showed

```bash
python days/39-round-trip/round_trip.py
```

The script should print the gross mean return −0.0024, the round-trip cost 0.0020, and the net mean return −0.0044. The implementation is [`round_trip.py`](../../days/39-round-trip/round_trip.py).

Hand in one precommitted rule and three numbers. The gross return −0.0024 is already negative. The cost did not destroy a positive edge, because that edge is not in the gross return.
