<p align="center"><a href="README.md">中文</a> · <b>English</b></p>

# 🛰️ Season 1 · Models

✨ One hundred days. Each day removes one shortcut the previous day still allowed. What rises is the constraint, not the name of a library.  
🔥 Lesson written: [Day 1 · In-sample nearest neighbor and ordinary least squares](day-01.en.md). The other days are listed and have no lesson yet.

Back to the [front page](../../README.en.md).

## 01 – 10 · Error

| Day | Session | Shortcut removed |
|---|---|---|
| [01](day-01.en.md) | Memory against a line. Day 4 closes at 20, the line misses by 8.2 | The start. The two habits must sit side by side |
| 02 | Absolute error and squared error | The same miss must be handed in as two numbers. Squaring weighs day 4 more |
| 03 | The five residuals side by side | A single total is no longer enough. Name the day that holds the error |
| 04 | A line through day 1 and day 5 only | A cruder line has to lose to least squares on the miss |
| 05 | Fit again without day 4 | Show how far one point can move the whole line |
| 06 | Ask for day 6 | That day is not in the fit. Memory can only copy a neighbor. The line must extrapolate |
| 07 | Hide day 5 and call it the exam | Error on the fitting days no longer counts |
| 08 | Keep a window of three days and slide it once | The line has to drop the earlier prices |
| 09 | Shuffle the dates and fit again | The score barely moves, so the line is shown not to know time |
| 10 | Score direction, up or down | A small price error can still get the direction wrong. Both scores are due |

## 11 – 25 · Direction

| Day | Session | Shortcut removed |
|---|---|---|
| 11 | Keep only up or down | Distance, including a miss of 8.2, is no longer an answer |
| 12 | Cut return into up and down with one threshold | You choose where the cut sits |
| 13 | Nudge the threshold | Report how sensitive accuracy is to that nudge |
| 14 | Always guess down | A baseline comes first. The model has to beat someone who looks at nothing |
| 15 | Put the two kinds of mistake in separate cells | Calling up down, and calling down up, are counted apart |
| 16 | Emit how much the day looks like an up day | Hand in one more number, between 0 and 1 |
| 17 | Check the days you called 80 percent | Confidence has to match how often those days really rise |
| 18 | Split on return and volume together | The input is no longer a single day's price |
| 19 | Leave volume unscaled | The column with more digits crowds price out. You have to see it |
| 20 | Add a column of pure noise | The score must not improve because of it |
| 21 | Switch to a fixed table of real closes | The numbers are no longer handwritten. Reading twice must match |
| 22 | Guess today from yesterday's direction | Sit it next to a coin-flip baseline |
| 23 | After three days the same way, look at the fourth | The rule is frozen. It cannot be rewritten after the result |
| 24 | Carry that rule into the next stretch of prices | The score cannot be reported on the stretch you picked |
| 25 | Hand in the direction score and the price score together | When they disagree, say which one you trust |

## 26 – 40 · Time

| Day | Session | Shortcut removed |
|---|---|---|
| 26 | Split rows into train and test at random | Keep the flattering score as a control |
| 27 | Split by time instead | The test sits entirely after the train. Print both numbers |
| 28 | Explain today's close with today's high | The script must mark that column forbidden |
| 29 | Standardize with tomorrow's open | Leakage can hide in the preprocessing |
| 30 | Each day may see only a fixed window of the past | The whole history can no longer be fit at once |
| 31 | Shrink the window to three days | The line chases one-day noise. Print that miss on its own |
| 32 | Stretch the window to sixty days | The line is still sitting in older prices. Set it beside day 31 |
| 33 | Estimate mean and variance on the training stretch only | The test stretch may not standardize itself |
| 34 | Fill a missing day from the future, then from the past | Both fills exist. The one that peeks is marked |
| 35 | After dropping halted days, check the gap | Adjacent rows are not adjacent times |
| 36 | An unadjusted jump against the same day, adjusted | A corporate action can be mistaken for a signal. Both errors are due |
| 37 | Mix several stocks, then cut by time again | They share the same day's news. The flattering score has to be visible |
| 38 | Lag the signal by one day | What disappears was simultaneous. What remains might be usable |
| 39 | Subtract one minimum round-trip cost | After that, is the earlier edge still there |
| 40 | For every improvement in this stretch, note whether the future was visible | The score needs a leakage list behind it |

## 41 – 55 · How the miss happens

| Day | Session | Shortcut removed |
|---|---|---|
| 41 | Fit the line again on a longer price history | A jump still moves the whole line. This jump is not handwritten |
| 42 | Ridge, with the slope penalized | The same jump may not move the line as far |
| 43 | Average only the nearby days | A distant jump cannot enter the answer |
| 44 | A shallow tree | It may cut the jump day out on its own |
| 45 | One level deeper | Training gets better and the next stretch gets worse. It is memorizing dates |
| 46 | Line, ridge, and tree on the next stretch | Three fits with similar training error must report which one still lives |
| 47 | Extrapolate the line to a far day | The answer may land outside any reasonable price |
| 48 | Extrapolate the tree to that same day | It only repeats a leaf. The two misses sit side by side |
| 49 | All three on the same jump day | Say who was moved, and who memorized the day |
| 50 | Let the three vote | Find a day when all three are wrong and the vote is wrong too |
| 51 | Features become the last five daily returns | The line's weights are roughly even. Print them |
| 52 | The tree uses the same five days | It will isolate one of them |
| 53 | Change the random seed | The tree's cuts move. The line barely does |
| 54 | Drop volume and run again | Whoever falls more was depending on that column |
| 55 | One sentence each on how the three miss | A single score is no longer accepted |

## 56 – 70 · One small task

| Day | Session | Shortcut removed |
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

| Day | Session | Shortcut removed |
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

| Day | Session | Shortcut removed |
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
