<p align="center"><a href="day-01.md">🇨🇳 中文</a> · 🇬🇧 <b>English</b></p>

# 🛰️ Day 1 · The line lets the flare go

✨ [Season 1 · Models](README.en.md) · 🟢 runs · 📉 no orders

Welcome to the observation deck. No vocabulary lesson first. Five lights are already in the sky. Four of them walk a quiet route. The fourth is yanked to the top of the dome. The navigator has to answer, out loud, where that light is now.

Two habits. One sky. One stores the flare and misses by **0**. One draws a route that can still serve all five days, says **11.79**, and misses by **8.2**. That gap is the first lesson of machine learning on a price.

---

## 🌌 Five sessions

| 🗓️ Day | 💰 Close | 📐 Line | 👀 What you see |
|---|---:|---:|---|
| 1 | 2.1 | 1.98 | lifting off along the route |
| 2 | 3.9 | 5.25 | a little above the line |
| 3 | 6.2 | 8.52 | still near it |
| 🔥 **4** | **20.0** | **11.79** | **the flare** |
| 5 | 10.4 | 15.06 | the light falls back, the line keeps climbing |

The other four days drift upward by about 2 a day. Day 4 does not negotiate. The close stands at **20**. Everyone on the deck stares at it. A model that only stares at it is done with today's story before it begins.

---

## 🧠 Memory · pocket the flare

Memory is simple enough to shine.

It finds the nearest of the five days and repeats that close. The question is day 4, so the nearest day is day 4, and it says **20.0**. Miss **0**. Clean. Brilliant. As if it had never been wrong.

✨ It wins this day because it put this day in its pocket.  
✨ On a day the pocket already holds, it looks like a genius.  
✨ On a day the pocket does not hold, it can only copy a neighbor. That reveal waits for day 6.

Today's question lets memory see 20. A miss of zero is a trophy for storage, not a trophy for prediction.

---

## 📐 The line · one route for the whole sky

The line does not memorize prices. It borrows from all five days at once:

```text
y = 3.27x − 1.29
```

Put day 4 back in: `3.27 × 4 − 1.29 = 11.79`.

This is least squares. Square each gap from a close to the route, add them, and keep the slope and intercept that make the sum smallest. Hauling the whole route up to 20 would throw the other four days farther off, and the sum of squares would look worse. The route refuses to abandon the sky for one lamp.

So you get the picture worth keeping: 🔥 the gold point sits at 20, and the blue route passes under it at **11.79**. The vertical mark between them is the miss.

| 🎭 Habit | 🗣️ Says | 💥 Miss | 🏆 Where it wins |
|---|---:|---:|---|
| 🧠 Memory | 20.0 | **0** | perfect on a day it has seen |
| 📐 Line | 11.79 | **8.2** | able to answer all five, so day 4 has to yield |

`20.0 − 11.79 = 8.21`, printed as **8.2**. Not a slip of the pen. The signed cost of one line that still has to carry five days.

---

## 🎬 Watch first, then run

The page and the script share one set of closes. Open [`site`](../../site), run `npm install`, then `npm run dev`.

You will see:

1. 🌑 The axes come on. The sky is still empty
2. ✨ Five sessions drop in, one by one
3. 🔥 Day 4 stops at 20, labeled as a flare
4. 💙 The line draws from lower left to upper right and passes under 20
5. ⚡ A dashed vertical falls, marked **miss 8.2**

Replay is the button at the bottom. The page only watches. It sends no order. Later backtests meet LAT's history, not a live book.

From the repository root, print the same numbers:

```bash
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
python days/01-line-that-misses/fit_line.py
```

🐍 Python 3.8 or newer. The script should print `y = 3.27 x + -1.29`, memory miss `0.0`, line miss `8.2`. The file is [`days/01-line-that-misses/fit_line.py`](../../days/01-line-that-misses/fit_line.py).

---

## 🧭 The sentence you leave with

> ✨ A line does not store the prices it has seen. It chooses a route, and the day off the route gets said wrong.

Memory is a perfect piece of amber. Day 4 is sealed inside it, the miss is zero, and it cannot walk out of that day. The line gives up a zero miss at liftoff, and buys a route that can catch day 1, day 2, day 3, and day 5. Every later story about a model being "accurate" on a price has to pass this question first: did it memorize the flare, or did it pay for the whole sky.

---

## 🚀 Tomorrow removes a shortcut

Today you may still hand in one error. Tomorrow the same miss must be written as two numbers: absolute error, and squared error. Squaring hangs more weight on day 4's lamp, and the ranking can change.

Do not spend today's zero as if prediction were already learned:

| 📅 | 🔮 What opens next |
|---|---|
| Day 6 | Ask for a session the fit never stored. Memory copies a neighbor. The line has to fly outward |
| Day 7 | Hide day 5 and call it the exam. A pretty score on the fitting days no longer counts |

🟢 Day 1 can be run, told, and watched again. The next lamp is not lit yet.
