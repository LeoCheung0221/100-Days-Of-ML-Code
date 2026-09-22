<p align="center"><a href="day-01.md">中文</a> · <b>English</b></p>

# ✦ Day 1 · The line lets the pulled-up day go

[Season 1](README.en.md) · Models · runs

Five closing prices. Day 4 is pulled up to 20. The other four sit near a line. Today compares two habits, and both have to answer day 4.

| Day | Close | Line |
|---|---:|---:|
| 1 | 2.1 | 1.98 |
| 2 | 3.9 | 5.25 |
| 3 | 6.2 | 8.52 |
| **4** | **20.0** | **11.79** |
| 5 | 10.4 | 15.06 |

---

## Compare

The navigator has two habits.

**Memory** finds the nearest of the five days and repeats that close. The question is day 4, so it says 20 and misses by 0. It wins this day because it stored this day.

**The line** fits all five points as `y = 3.27x − 1.29`, then substitutes x = 4 and says 11.79. The fit is least squares: add up the squared gaps from the five points to the line, and keep the slope and intercept that make that sum smallest. Pulling the whole line up to 20 would push the other four days farther away, and the sum of squares would grow. So the line passes under 20.

| Habit | Says | Miss |
|---|---:|---:|
| Memory | 20.0 | 0 |
| Line | 11.79 | 8.2 |

8.2 is not a rounding accident. 20.0 − 11.79 = 8.21, printed as 8.2. It is the cost of one line that still has to serve all five days.

Day 4 is inside the five points. Memory's miss is 0 because the question allows it to see the answer. Day 6 is the first day that asks for a session the fit has not stored. Day 7 is the first day that hides day 5 and calls it an exam.

---

## Run

From the repository root:

```bash
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
python days/01-line-that-misses/fit_line.py
```

Python 3.8 or newer. The printed line, 11.79, and 8.2 should match the tables above. The script is in [`days/01-line-that-misses`](../../days/01-line-that-misses).

The same numbers are drawn in [`site`](../../site). From that directory, run `npm install`, then `npm run dev`. Day 4 stops at 20, the line passes underneath, and the vertical mark reads a miss of 8.2. The page sends no order.

---

## Say

> A line does not store the prices it has seen. It chooses a route, and the day that sits off the route gets said wrong.

Memory can miss by zero on a day it has stored. On another day, or on a price it did not store, it can only copy a neighbor. The line gives up a zero miss from the start, and buys a route that can also answer the other days.

The next day removes "hand in one error." The same 8.2 has to be written as an absolute error and a squared error. Squaring puts more weight on day 4.
