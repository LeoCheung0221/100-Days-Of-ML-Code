<p align="center"><a href="README.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Phase I · Models

Note: days 1 through 80 have notes, linked in the table. The remaining days are titles only.

Back to the [front page](../../README.en.md).

## 01 – 10 · Error

| Day | Session | What you learn today |
|---|---|---|
| [01　Nearest neighbor and OLS](day-01.en.md) | In-sample nearest neighbor and ordinary least squares | The query lies in the training set. The two estimators sit side by side |
| [02　Absolute and squared error](day-02.en.md) | Absolute loss and squared loss on one residual | Session 4 is 0.4928 of L1 and 0.6997 of L2 |
| [03　Residuals, point by point](day-03.en.md) | Open the RSS into five coordinates | The scalar 96.339 does not say where the loss sits |
| [04　The chord through the endpoints](day-04.en.md) | Chord and OLS in the same affine class | Higher L2 for the chord, and a lower L1 is possible |
| [05　Refit without day 4](day-05.en.md) | Delete session 4 and solve the normal equations again | The slope falls by 1.1729. Displacement is not a holdout score |
| [06　A query off the training support](day-06.en.md) | Query x = 6. There is no y₆ | The neighbor copies 10.4, the line extrapolates to 18.33, and the residual is undefined |
| [07　Hold out day 5](day-07.en.md) | Fit on the first four sessions and score session 5 alone | Training RSS = 42.05 does not count |
| [08　A three-day window](day-08.en.md) | Three sessions, slid forward once | The slope rises from 2.0500 to 8.0500. An earlier row has weight 0 |
| [09　Shuffle the dates](day-09.en.md) | Permute row order and keep the pairs | β̂ and RSS do not move. The invariance is row order, not the calendar coordinate |
| [10　Up or down](day-10.en.md) | Level residuals beside the sign of the one-day move | Session 5 has the smaller absolute residual and the wrong sign |

## 11 – 25 · Direction

| Day | Session | What you learn today |
|---|---|---|
| [11　Direction labels](day-11.en.md) | Keep only up or down | The score is now a direction hit, not a price distance. |
| [12　A threshold](day-12.en.md) | Cut return into up and down with one threshold | The four returns are 0.8571, 0.5897, 2.2258, and −0.4800. |
| [13　Threshold sensitivity](day-13.en.md) | Nudge the threshold | The constant-up accuracy is 0.75, 0.50, and 0.25 at thresholds 0.50, 0.70, and 0.90. |
| [14　A constant baseline](day-14.en.md) | Always guess down | On the sign labels, always guessing down scores 0.25 and always guessing up scores 0.75. |
| [15　Two kinds of misclassification](day-15.en.md) | Put the two kinds of mistake in separate cells | Under the constant-up rule, up called down happens 0 times and down called up happens 1 time. |
| [16　Degree of being up](day-16.en.md) | Emit how much the day looks like an up day | The slope 3.27, passed through a sigmoid, is 0.9634. |
| [17　A check on stated confidence](day-17.en.md) | Check the days you called 80 percent | The stated probability of an up move is 0.9634. |
| [18　Return and volume](day-18.en.md) | Split on return and volume together | On the sign of the return, 3 of the 4 steps are up. |
| [19　Unscaled volume](day-19.en.md) | Leave volume unscaled | The raw coefficient on volume is 1.731932e-06 and the raw coefficient on the date is 1.482253. |
| [20　A noise column](day-20.en.md) | Add a column of pure noise | The noise column uses seed 0, fixed in advance. |
| [21　A fixed close table](day-21.en.md) | Switch to the frozen close table in the repository | The table is days/data/panel.csv. |
| [22　Yesterday's direction](day-22.en.md) | Guess today from yesterday's direction | Yesterday's adjusted sign predicts today and hits 36/77, accuracy 0.4675. |
| [23　Three days the same way](day-23.en.md) | After three days the same way, look at the fourth | The rule is in the program before the count: after three adjusted moves of the same sign, predict that the fourth matches. |
| [24　The rule on the next stretch](day-24.en.md) | Carry that rule into the next stretch of prices | The cut date is 2024-02-28. |
| [25　Direction and price together](day-25.en.md) | Hand in the direction score and the price score together | Yesterday's return predicts today's return. |

## 26 – 40 · Time

| Day | Session | What you learn today |
|---|---|---|
| [26　A random split](day-26.en.md) | Split rows into train and test at random | Seed 1, training fraction 0.70, and the sign of the lagged return predicts the next step. |
| [27　A split by time](day-27.en.md) | Split by time instead | The time split scores 0.5417. |
| [28　Today's high](day-28.en.md) | Explain today's close with today's high | The high is on the same row as the close, and the script marks it FORBIDDEN. |
| [29　Standardize with a future open](day-29.en.md) | Standardize with tomorrow's open | Scaling the close by the mean and standard deviation of every open, including opens after that close, gives a return-regression RSS of 0.2642. |
| [30　A fixed lookback](day-30.en.md) | Each day may see only a fixed window of the past | On the last day the value from fitting every adjusted close is 12.1976. |
| [31　Noise in a three-day window](day-31.en.md) | Shrink the window to three days | Predicting the last adjusted close, the three-day slope is −0.1195 and the twenty-day slope is 0.0251. |
| [32　A sixty-day window](day-32.en.md) | Stretch the window to sixty days | On the same last session the sixty-day slope is 0.0353 and the absolute miss is 0.4426. |
| [33　Standardize on the training stretch](day-33.en.md) | Estimate mean and variance on the training stretch only | The training-stretch mean and standard deviation of the return are 0.003241 and 0.022132. |
| [34　Two ways to fill a gap](day-34.en.md) | Fill a missing day from the future, then from the past | AAA's close on 2024-02-01 is blank. |
| [35　Gaps after a halt](day-35.en.md) | After dropping halted days, check the gap | Row numbers 35 and 36 are adjacent. |
| [36　Adjusted and unadjusted](day-36.en.md) | An unadjusted jump against the same day, adjusted | On 2024-03-11 the unadjusted return is −0.4938 and the adjusted return is 0.0124. |
| [37　Several names, mixed split](day-37.en.md) | Mix several stocks, then cut by time again | AAA and BBB are stacked, and the sign of the same-day market return predicts each name. |
| [38　Lag the signal one day](day-38.en.md) | Lag the signal by one day | The same-day market sign matches the same-day adjusted sign on 0.6795 of sessions. |
| [39　A minimum round trip](day-39.en.md) | Subtract one minimum round-trip cost | Hold AAA when yesterday's market rose. |
| [40　A leakage list](day-40.en.md) | For every improvement in this stretch, note whether the future was visible | The list has six lines, and every line has future=yes: today's high on day 28, later opens in the scale on day 29, the whole-sample scale on day 33, the next-close fill on day 34, a shared date across names on day 37, and the same-day market return on day 38. |

## 41 – 55 · How the miss happens

| Day | Session | What you learn today |
|---|---|---|
| [41　The line on a longer sample](day-41.en.md) | Fit the line again on a longer price history | The adjusted return on 2024-02-28 is 0.1349. |
| [42　Ridge](day-42.en.md) | Ridge, with the slope penalized | The penalty is on the slope only, λ = 20000, and the intercept is free. |
| [43　A local average](day-43.en.md) | Average only the nearby days | The query date is 2024-03-20. |
| [44　A shallow tree](day-44.en.md) | A shallow tree | The train uses the first 59 adjusted closes. |
| [45　A deeper tree](day-45.en.md) | One level deeper | Depth 1 has train SSE 2.6315 and later SSE 0.5669. |
| [46　Three fits, next sample](day-46.en.md) | Line, ridge, and tree on the next stretch | Train SSE is 10.1623 for the line, 16.3596 for ridge, and 1.3953 for the tree. |
| [47　Linear extrapolation](day-47.en.md) | Extrapolate the line to a far day | The query is t = 118, forty steps past the last training abscissa. |
| [48　A tree does not extrapolate](day-48.en.md) | Extrapolate the tree to that same day | The same query is t = 118. |
| [49　One jump, three models](day-49.en.md) | All three on the same jump day | The adjusted close on 2024-02-28 is 12.0142. |
| [50　A vote of three](day-50.en.md) | Let the three vote | On the later stretch, the step dated 2024-03-29 has the line, ridge, and the tree all wrong on direction, and the vote is wrong as well. |
| 51 | Features become the last five daily returns | The line's weights are roughly even. Print them |
| 52 | The tree uses the same five days | It will isolate one of them |
| 53 | Change the random seed | The tree's cuts move. The line barely does |
| 54 | Drop volume and run again | Whoever falls more was depending on that column |
| 55 | One sentence each on how the three miss | A single score is no longer accepted |

## 56 – 70 · One small task

| Day | Session | What you learn today |
|---|---|---|
| 56 | Freeze the task in one sentence: from the past, guess the next day's return | Table, target, and forbidden columns go into the program before the run |
| 57 | The program refuses today's high, low, and close | A forbidden column must fail the run, not get used quietly |
| 58 | Split by year | The split is frozen. Row numbers do not decide it |
| 59 | The baseline always guesses a return of 0 | The model has to sit beside the baseline |
| 60 | Line minus baseline | The bit you win has to land on particular days |
| 61 | Tree minus the same baseline | Same table and same split as day 60 |
| 62 | Score error only on the most confident tenth of days | The other nine tenths cannot be used to flatter the average |
| 63 | Split error by month | Find whether one month carries the year |
| 64 | Delete that month and score again | The conclusion counts only if it is still there |
| 65 | Switch to a second stock | The procedure does not change. The first stock's conclusion does not travel |
| 66 | Turn return into excess over the market | What must be explained is the part beyond the market |
| 67 | Shift the market column forward by one day | A score that improves because of that shift is marked void |
| 68 | Fold the procedure into one function | A second table must enter through the same door |
| 69 | Write the fill assumption | Fill at the close, no slippage. The assumption is part of the output |
| 70 | Tell the task in ten lines | Every number in the telling has to be findable in the output |

## 71 – 85 · Costly mistakes

| Day | Session | What you learn today |
|---|---|---|
| 71 | Split misses into jumps, quiet days, and wrong direction | Three counts replace one error |
| 72 | Look only at quiet days | A small error has to be said as "these days were easy" |
| 73 | Count only the days the direction was wrong | That count may rank models differently from average error |
| 74 | Classify the five largest errors | If they are the same kind, the average is that kind speaking |
| 75 | Charge 1 for a wrong direction and 3 for a jump day | When the tariff changes, the ranking may flip |
| 76 | Missing a large drop, against flagging a small rise | The two mistakes get two columns |
| 77 | Raise the threshold and speak only when more sure | Fewer calls. The remaining calls are charged on their own |
| 78 | Lower the threshold and speak almost every day | The average looks mild and the expensive mistakes remain. Both tables sit together |
| 79 | Rerank the line and the tree under the new tariff | The winner on average error can lose here |
| 80 | Name the mistake you are willing to carry | The choice has to point at one column of the tariff |
| 81 | Separate high-volatility weeks from low ones | Define volatility first, then split the error |
| 82 | In the high-volatility weeks, count the line's jumps | The count has to be there |
| 83 | In the low-volatility weeks, see whether the tree is memorizing noise | Set it against the deeper tree, on this table |
| 84 | Three mistakes and two volatility regimes, one count table | This table replaces the average error for the rest of the season |
| 85 | Keep one model by citing that table | The decision may cite only one cell |

## 86 – 100 · Tell another engineer

| Day | Session | What you learn today |
|---|---|---|
| 86 | Ten lines for the start date, end date, and source | Those ten lines alone must locate the same data |
| 87 | Ten lines for why each column is allowed | This matches the program's refusal list |
| 88 | Run it a second way | The error matches to two decimal places |
| 89 | Baseline, line, and tree side by side in the telling | The telling may not contain a number the program did not print |
| 90 | Three missed days, one cause each | Each cause is one of the three mistake kinds |
| 91 | Refuse one feature and attach the ranking before and after | A refusal needs two numbers |
| 92 | Write "if this were filled" as three lines of assumption | Profit does not appear in the assumption |
| 93 | Add one minimum unit of slippage and rank again | If the ranking moves, the telling changes. If it does not, say so |
| 94 | Delete the favorite month and remake the keep-or-drop decision | If the decision flips, the later one stands |
| 95 | Another stock, the same function | Dates and the three missed days change. The procedure does not |
| 96 | One page: task, split, baseline, three mistakes | All four headings are on that page |
| 97 | From that page, name one hole still open | The hole has to point at a day's repair |
| 98 | Close that hole and run again | The score may get worse. The worse number stays in the telling |
| 99 | Run the whole procedure once more | The numbers in the telling match this output |
| 100 | Tell the failure from that page | A listener can repeat: through which date, what is forbidden, which three mistakes, and why there is no order |
