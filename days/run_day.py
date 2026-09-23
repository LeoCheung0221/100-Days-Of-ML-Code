"""Days 11–50. Each day_xx prints the numbers its note quotes."""

from __future__ import annotations

import datetime as dt

import numpy as np

from days.course import (
    FIVE_V,
    FIVE_X,
    FIVE_Y,
    PANEL_PATH,
    accuracy,
    column,
    fmt,
    load_panel,
    name_rows,
    ols,
    predict_stump,
    predict_tree,
    returns,
    ridge_slope,
    sign_hit,
    stump,
    tree_depth2,
)


def _five_returns() -> np.ndarray:
    return (FIVE_Y[1:] - FIVE_Y[:-1]) / FIVE_Y[:-1]


def _sigmoid(value: float) -> float:
    return float(1.0 / (1.0 + np.exp(-value)))


def _aaa() -> list[dict]:
    return name_rows("AAA")


def _complete(rows: list[dict]) -> list[dict]:
    return [row for row in rows if np.isfinite(row["close"]) and np.isfinite(row["adj_close"])]


def _panel_pair() -> tuple[list[dict], list[dict]]:
    aaa = _complete(_aaa())
    bbb = _complete(name_rows("BBB"))
    shared = set(row["date"] for row in aaa) & set(row["date"] for row in bbb)
    aaa = [row for row in aaa if row["date"] in shared]
    bbb = [row for row in bbb if row["date"] in shared]
    return aaa, bbb


def day_11() -> None:
    slope, intercept = ols(FIVE_X, FIVE_Y)
    fitted = slope * FIVE_X + intercept
    hits = sign_hit(np.diff(FIVE_Y), np.diff(fitted))
    print("score = direction hits", f"{int(hits.sum())}/{len(hits)}")
    print("day 4 absolute price residual =", fmt(abs(FIVE_Y[3] - fitted[3]), 2))
    print("that residual is not the score")


def day_12() -> None:
    simple = _five_returns()
    tau = 0.70
    label = simple > tau
    pred = np.ones(len(simple), dtype=bool)
    print("threshold =", fmt(tau, 2))
    print("returns =", " ".join(fmt(v, 4) for v in simple))
    print("label up =", " ".join("1" if v else "0" for v in label))
    print("constant-up accuracy =", fmt(accuracy(pred == label), 2))


def day_13() -> None:
    simple = _five_returns()
    pred = np.ones(len(simple), dtype=bool)
    print("threshold  accuracy")
    for tau in (0.50, 0.70, 0.90):
        print(f"{tau:.2f}  {accuracy(pred == (simple > tau)):.2f}")


def day_14() -> None:
    up = _five_returns() > 0
    print("always-down accuracy =", fmt(accuracy(np.zeros(len(up), dtype=bool) == up), 2))
    print("always-up accuracy =", fmt(accuracy(np.ones(len(up), dtype=bool) == up), 2))
    print("the baseline looks at no price")


def day_15() -> None:
    up = _five_returns() > 0
    pred_up = np.ones(len(up), dtype=bool)
    print("up called down =", int((up & ~pred_up).sum()))
    print("down called up =", int((~up & pred_up).sum()))


def day_16() -> None:
    slope = float(ols(FIVE_X, FIVE_Y)[0])
    print("slope =", fmt(slope, 2))
    print("P(up) = sigmoid(slope) =", fmt(_sigmoid(slope), 4))
    print("the same score is attached to every step")


def day_17() -> None:
    stated = _sigmoid(float(ols(FIVE_X, FIVE_Y)[0]))
    realized = float(np.mean(_five_returns() > 0))
    print("stated P(up) =", fmt(stated, 4))
    print("realized up frequency =", fmt(realized, 2))
    print("gap =", fmt(stated - realized, 4))


def day_18() -> None:
    simple = _five_returns()
    volume = FIVE_V[1:]
    median = float(np.median(FIVE_V))
    both = (simple > 0) & (volume > median)
    print("median volume =", f"{median:.0f}")
    print("up on return alone =", int((simple > 0).sum()))
    print("up on return and volume =", int(both.sum()))
    kept = " ".join(str(i + 2) for i, flag in enumerate(both) if flag)
    print("sessions kept =", kept or "none")


def day_19() -> None:
    design = np.column_stack([FIVE_X, FIVE_V])
    beta, *_ = np.linalg.lstsq(design, FIVE_Y, rcond=None)
    raw_share = np.abs(design * beta)
    scale = design.std(axis=0)
    design_z = (design - design.mean(axis=0)) / scale
    beta_z, *_ = np.linalg.lstsq(design_z, FIVE_Y, rcond=None)
    print("raw beta time =", f"{beta[0]:.6f}")
    print("raw beta volume =", f"{beta[1]:.6e}")
    print("mean |time contribution| =", f"{raw_share[:, 0].mean():.4f}")
    print("mean |volume contribution| =", f"{raw_share[:, 1].mean():.4f}")
    print("standardized beta time =", f"{beta_z[0]:.4f}")
    print("standardized beta volume =", f"{beta_z[1]:.4f}")


def day_20() -> None:
    noise = np.random.default_rng(0).normal(size=5)
    x = FIVE_X[:-1]
    y = FIVE_Y[:-1]
    base = ols(x, y)
    rss_base = float(np.sum((y - (base[0] * x + base[1])) ** 2))
    design = np.column_stack([x, noise[:-1], np.ones(len(x))])
    beta, *_ = np.linalg.lstsq(design, y, rcond=None)
    rss_noise = float(np.sum((y - design @ beta) ** 2))
    exam_x, exam_y = float(FIVE_X[-1]), float(FIVE_Y[-1])
    base_err = abs(exam_y - (base[0] * exam_x + base[1]))
    noise_err = abs(exam_y - (beta[0] * exam_x + beta[1] * noise[-1] + beta[2]))
    print("fit on t=1..4, score on t=5")
    print("in-sample RSS without noise =", fmt(rss_base, 4))
    print("in-sample RSS with noise =", fmt(rss_noise, 4))
    print("holdout absolute error without noise =", fmt(base_err, 4))
    print("holdout absolute error with noise =", fmt(noise_err, 4))
    print("the in-sample drop is not an improvement")


def day_21() -> None:
    text = PANEL_PATH.read_text()
    aaa = _aaa()
    blank = sum(1 for row in aaa if not np.isfinite(row["close"]))
    print("path = days/data/panel.csv")
    print("rows =", len(load_panel()))
    print("second read matches =", str(text == PANEL_PATH.read_text()).lower())
    print("AAA dates", aaa[0]["date"], "..", aaa[-1]["date"])
    print("AAA blank closes =", blank)
    print("the table is not resampled")


def day_22() -> None:
    close = column(_complete(_aaa()), "adj_close")
    move = np.diff(close)
    hits = sign_hit(move[1:], move[:-1])
    print("predict today's adj move with yesterday's sign")
    print("hits =", f"{int(hits.sum())}/{len(hits)}")
    print("accuracy =", fmt(accuracy(hits), 4))
    print("coin-flip baseline = 0.5000")


def day_23() -> None:
    move = np.diff(column(_complete(_aaa()), "adj_close"))
    hits = []
    for i in range(3, len(move)):
        window = np.sign(move[i - 3 : i])
        if np.all(window == window[0]) and window[0] != 0:
            hits.append(bool(np.sign(move[i]) == window[0]))
    hits_arr = np.array(hits, dtype=bool)
    print("rule = after three equal signs, predict the fourth matches")
    print("events =", len(hits_arr))
    print("hits =", int(hits_arr.sum()))
    print("accuracy =", fmt(accuracy(hits_arr), 4))
    print("the rule is fixed before the count")


def day_24() -> None:
    rows = _complete(_aaa())
    close = column(rows, "adj_close")
    dates = [row["date"] for row in rows]
    move = np.diff(close)
    cut = dates[len(dates) // 2]
    later, early = [], []
    for i in range(3, len(move)):
        window = np.sign(move[i - 3 : i])
        if not (np.all(window == window[0]) and window[0] != 0):
            continue
        hit = bool(np.sign(move[i]) == window[0])
        (later if dates[i + 1] > cut else early).append(hit)
    early_arr = np.array(early, dtype=bool)
    later_arr = np.array(later, dtype=bool)
    print("cut date =", cut)
    print("early events =", len(early_arr), "accuracy =", fmt(accuracy(early_arr), 4))
    print("early accuracy is not the score")
    print("later events =", len(later_arr), "accuracy =", fmt(accuracy(later_arr), 4))


def day_25() -> None:
    close = column(_complete(_aaa()), "adj_close")
    actual = returns(close)[1:]
    pred = returns(close)[:-1]
    err = np.abs(actual - pred)
    hits = sign_hit(actual, pred)
    small = err <= np.median(err)
    print("lag-1 return forecast")
    print("direction accuracy =", fmt(accuracy(hits), 4))
    print("mean absolute return error =", fmt(float(err.mean()), 4))
    print("days with a small price error and the wrong sign =", int((small & ~hits).sum()))
    print("for a sign decision, trust the direction accuracy")


def _split_score(x: np.ndarray, y: np.ndarray, train: np.ndarray) -> float:
    beta = ols(x[train], y[train])
    pred = beta[0] * x[~train] + beta[1]
    return accuracy(sign_hit(y[~train], pred))


def _lag_xy() -> tuple[np.ndarray, np.ndarray]:
    simple = returns(column(_complete(_aaa()), "adj_close"))
    return simple[:-1], simple[1:]


def day_26() -> None:
    x, y = _lag_xy()
    train = np.zeros(len(y), dtype=bool)
    train[np.random.default_rng(1).choice(len(y), size=int(0.7 * len(y)), replace=False)] = True
    print("split = random, seed 1, train fraction 0.70")
    print("test direction accuracy =", fmt(_split_score(x, y, train), 4))
    print("this number is the control")


def day_27() -> None:
    x, y = _lag_xy()
    cut = int(0.7 * len(y))
    train = np.zeros(len(y), dtype=bool)
    train[:cut] = True
    random_train = np.zeros(len(y), dtype=bool)
    random_train[np.random.default_rng(1).choice(len(y), size=cut, replace=False)] = True
    print("time-split test accuracy =", fmt(_split_score(x, y, train), 4))
    print("random-split test accuracy =", fmt(_split_score(x, y, random_train), 4))
    print("the test of the time split sits entirely after the train")


def day_28() -> None:
    rows = _complete(_aaa())
    close = column(rows, "close")
    high = column(rows, "high")
    beta_high = ols(high[1:], close[1:])
    beta_lag = ols(close[:-1], close[1:])
    resid_high = close[1:] - (beta_high[0] * high[1:] + beta_high[1])
    resid_lag = close[1:] - (beta_lag[0] * close[:-1] + beta_lag[1])
    print("column high = FORBIDDEN")
    print("in-sample RSS close~high =", fmt(float(np.sum(resid_high ** 2)), 4))
    print("in-sample RSS close~lagged close =", fmt(float(np.sum(resid_lag ** 2)), 4))


def day_29() -> None:
    rows = _complete(_aaa())
    close = column(rows, "close")
    opened = column(rows, "open")
    leaky = (close - opened.mean()) / opened.std()
    causal = np.full(len(close), np.nan)
    for i in range(5, len(close)):
        window = close[:i]
        causal[i] = (close[i] - window.mean()) / window.std()
    target = returns(close)
    mask = np.isfinite(causal[:-1])

    def rss(feature: np.ndarray) -> float:
        beta = ols(feature[:-1][mask], target[mask])
        resid = target[mask] - (beta[0] * feature[:-1][mask] + beta[1])
        return float(np.sum(resid ** 2))

    print("leaky scale uses every open, including later ones")
    print("RSS of return on leaky close =", fmt(rss(leaky), 4))
    print("RSS of return on past-only close =", fmt(rss(causal), 4))
    print("the leaky scale is a function of later opens")


def day_30() -> None:
    close = column(_complete(_aaa()), "adj_close")
    t = np.arange(len(close), dtype=float)
    full = ols(t, close)
    local = ols(t[-20:], close[-20:])
    query = t[-1]
    print("lookback = 20")
    print("full-sample value at last t =", fmt(float(full[0] * query + full[1]), 4))
    print("window value at last t =", fmt(float(local[0] * query + local[1]), 4))
    print("the full sample is not the information set")


def day_31() -> None:
    close = column(_complete(_aaa()), "adj_close")
    t = np.arange(len(close), dtype=float)
    end = len(close) - 1
    short = ols(t[end - 3 : end], close[end - 3 : end])
    long = ols(t[end - 20 : end], close[end - 20 : end])
    actual = float(close[end])
    print("three-day slope =", fmt(float(short[0]), 4))
    print("twenty-day slope =", fmt(float(long[0]), 4))
    print("three-day absolute miss =", fmt(abs(actual - (short[0] * t[end] + short[1])), 4))
    print("twenty-day absolute miss =", fmt(abs(actual - (long[0] * t[end] + long[1])), 4))


def day_32() -> None:
    close = column(_complete(_aaa()), "adj_close")
    t = np.arange(len(close), dtype=float)
    end = len(close) - 1
    short = ols(t[end - 3 : end], close[end - 3 : end])
    long = ols(t[end - 60 : end], close[end - 60 : end])
    actual = float(close[end])
    print("sixty-day slope =", fmt(float(long[0]), 4))
    print("three-day slope =", fmt(float(short[0]), 4))
    print("sixty-day absolute miss =", fmt(abs(actual - (long[0] * t[end] + long[1])), 4))
    print("three-day absolute miss =", fmt(abs(actual - (short[0] * t[end] + short[1])), 4))


def day_33() -> None:
    simple = returns(column(_complete(_aaa()), "adj_close"))
    x, y = simple[:-1], simple[1:]
    cut = int(0.7 * len(y))
    train_x, test_x, train_y, test_y = x[:cut], x[cut:], y[:cut], y[cut:]

    def mse(mu_used: float, sigma_used: float) -> float:
        beta = ols((train_x - mu_used) / sigma_used, train_y)
        pred = beta[0] * ((test_x - mu_used) / sigma_used) + beta[1]
        return float(np.mean((test_y - pred) ** 2))

    train_mu, train_sd = float(train_x.mean()), float(train_x.std())
    all_mu, all_sd = float(x.mean()), float(x.std())
    print("train mean/std =", fmt(train_mu, 6), fmt(train_sd, 6))
    print("whole-sample mean/std =", fmt(all_mu, 6), fmt(all_sd, 6))
    print("test MSE, scale from the training stretch =", fmt(mse(train_mu, train_sd), 6))
    print("test MSE, scale from the whole sample =", fmt(mse(all_mu, all_sd), 6))
    print("the whole-sample scale sees the test stretch")


def day_34() -> None:
    rows = _aaa()
    blank = next(i for i, row in enumerate(rows) if not np.isfinite(row["close"]))
    print("blank date =", rows[blank]["date"])
    print("fill from the previous close =", fmt(float(rows[blank - 1]["close"]), 4))
    print("fill from the next close =", fmt(float(rows[blank + 1]["close"]), 4))
    print("the next close sees the future")


def day_35() -> None:
    rows = _aaa()
    dates = [dt.date.fromisoformat(row["date"]) for row in rows]
    for i in range(len(dates) - 1):
        business = int(np.busday_count(dates[i], dates[i + 1]))
        if business > 1:
            print("row numbers", i, i + 1)
            print("dates", dates[i].isoformat(), dates[i + 1].isoformat())
            print("business-day gap =", business)
            print("adjacent rows are not adjacent sessions")
            return
    raise RuntimeError("no halt gap")


def day_36() -> None:
    rows = _complete(_aaa())
    raw_ret = returns(column(rows, "close"))
    adj_ret = returns(column(rows, "adj_close"))
    i = int(np.argmax(np.abs(raw_ret - adj_ret)))
    print("date =", rows[i + 1]["date"])
    print("unadjusted return =", fmt(float(raw_ret[i]), 4))
    print("adjusted return =", fmt(float(adj_ret[i]), 4))
    print("both numbers are due")


def day_37() -> None:
    aaa, bbb = _panel_pair()

    def xy(rows: list[dict]) -> tuple[np.ndarray, np.ndarray, list[str]]:
        feature = returns(column(rows, "market"))
        target = returns(column(rows, "adj_close"))
        return feature, target, [row["date"] for row in rows[1:]]

    xa, ya, da = xy(aaa)
    xb, yb, db = xy(bbb)
    x = np.r_[xa, xb]
    y = np.r_[ya, yb]
    dates = np.array(da + db)
    train = np.zeros(len(y), dtype=bool)
    train[np.random.default_rng(1).choice(len(y), size=int(0.7 * len(y)), replace=False)] = True
    order = np.argsort(dates, kind="mergesort")
    time_train = np.zeros(len(y), dtype=bool)
    time_train[order[: int(0.7 * len(y))]] = True
    print("pooled AAA and BBB")
    print("random-split test accuracy =", fmt(_split_score(x, y, train), 4))
    print("time-split test accuracy =", fmt(_split_score(x, y, time_train), 4))
    print("the random split can train and test on the same date")


def day_38() -> None:
    rows = _complete(_aaa())
    market = returns(column(rows, "market"))
    target = returns(column(rows, "adj_close"))
    print("same-day market sign accuracy =", fmt(accuracy(sign_hit(target, market)), 4))
    print("lagged-one-day market sign accuracy =", fmt(accuracy(sign_hit(target[1:], market[:-1])), 4))
    print("what disappeared was simultaneous")


def day_39() -> None:
    rows = _complete(_aaa())
    market = returns(column(rows, "market"))
    target = returns(column(rows, "adj_close"))
    position = np.sign(market[:-1])
    position[position == 0] = 1.0
    gross = position * target[1:]
    cost = 0.002
    print("gross mean return =", fmt(float(gross.mean()), 4))
    print("round-trip cost =", fmt(cost, 4))
    print("net mean return =", fmt(float(gross.mean() - cost), 4))


def day_40() -> None:
    print("leakage list")
    print("day 28  today's high explains today's close  future=yes")
    print("day 29  scale uses later opens  future=yes")
    print("day 33  scale uses the test stretch  future=yes")
    print("day 34  fill from the next close  future=yes")
    print("day 37  random split shares a date across names  future=yes")
    print("day 38  same-day market return  future=yes")
    print("a higher score on any of these lines is not a result")


def _level() -> tuple[np.ndarray, np.ndarray, list[str], int]:
    rows = _complete(_aaa())
    close = column(rows, "adj_close")
    t = np.arange(len(close), dtype=float)
    return t, close, [row["date"] for row in rows], int(0.75 * len(close))


def _train_test():
    t, close, _, cut = _level()
    return t[:cut], close[:cut], t[cut:], close[cut:]


def day_41() -> None:
    t, close, dates, _ = _level()
    jump = int(np.argmax(np.abs(returns(close)))) + 1
    beta = ols(t, close)
    keep = np.ones(len(close), dtype=bool)
    keep[jump] = False
    reduced = ols(t[keep], close[keep])
    print("jump date =", dates[jump])
    print("adjusted return that day =", fmt(float(returns(close)[jump - 1]), 4))
    print("slope with the jump =", fmt(float(beta[0]), 6))
    print("slope without the jump =", fmt(float(reduced[0]), 6))
    print("intercept with the jump =", fmt(float(beta[1]), 4))
    print("intercept without the jump =", fmt(float(reduced[1]), 4))
    print("fitted at the jump, with =", fmt(float(beta[0] * t[jump] + beta[1]), 4))
    print("fitted at the jump, without =", fmt(float(reduced[0] * t[jump] + reduced[1]), 4))


def day_42() -> None:
    t, close, _, _ = _level()
    print("lambda = 20000, penalty on the slope only")
    print("ols slope =", fmt(float(ols(t, close)[0]), 4))
    print("ridge slope =", fmt(float(ridge_slope(t, close, lam=20000.0)[0]), 4))


def day_43() -> None:
    t, close, dates, _ = _level()
    jump = int(np.argmax(np.abs(returns(close)))) + 1
    query = min(jump + 15, len(close) - 1)
    neighbors = np.argsort(np.abs(t - t[query]), kind="mergesort")[:5]
    beta = ols(t, close)
    print("query date =", dates[query])
    print("neighbor dates =", " ".join(dates[i] for i in neighbors))
    print("jump date in the neighbors =", str(jump in set(neighbors.tolist())).lower())
    print("local mean =", fmt(float(close[neighbors].mean()), 4))
    print("ols at the query =", fmt(float(beta[0] * t[query] + beta[1]), 4))


def day_44() -> None:
    t, y, _, _ = _train_test()
    threshold, left, right = stump(t, y)
    line = ols(t, y)
    print("train sessions =", len(t))
    print("split when t >", fmt(threshold, 2))
    print("left mean =", fmt(left, 4), "right mean =", fmt(right, 4))
    print("train SSE stump =", fmt(float(np.sum((y - predict_stump(t, threshold, left, right)) ** 2)), 4))
    print("train SSE line =", fmt(float(np.sum((y - (line[0] * t + line[1])) ** 2)), 4))


def day_45() -> None:
    train_t, train_y, test_t, test_y = _train_test()
    shallow = stump(train_t, train_y)
    deep = tree_depth2(train_t, train_y)
    pairs = {
        "depth1": (predict_stump(train_t, *shallow), predict_stump(test_t, *shallow)),
        "depth2": (predict_tree(train_t, deep), predict_tree(test_t, deep)),
    }
    for name, (train_hat, test_hat) in pairs.items():
        print(f"train SSE {name} =", fmt(float(np.sum((train_y - train_hat) ** 2)), 4))
        print(f"later SSE {name} =", fmt(float(np.sum((test_y - test_hat) ** 2)), 4))


def day_46() -> None:
    train_t, train_y, test_t, test_y = _train_test()
    line = ols(train_t, train_y)
    ridge = ridge_slope(train_t, train_y, lam=20000.0)
    tree = tree_depth2(train_t, train_y)
    preds = {
        "line": (line[0] * train_t + line[1], line[0] * test_t + line[1]),
        "ridge": (ridge[0] * train_t + ridge[1], ridge[0] * test_t + ridge[1]),
        "tree": (predict_tree(train_t, tree), predict_tree(test_t, tree)),
    }
    later = {}
    print("model  train_SSE  later_SSE")
    for name, (train_hat, test_hat) in preds.items():
        train_sse = float(np.sum((train_y - train_hat) ** 2))
        test_sse = float(np.sum((test_y - test_hat) ** 2))
        later[name] = test_sse
        print(f"{name}  {train_sse:.4f}  {test_sse:.4f}")
    print("still alive on the later stretch =", min(later, key=later.get))


def day_47() -> None:
    t, close, _, _ = _level()
    beta = ols(t, close)
    query = float(t[-1] + 40)
    value = float(beta[0] * query + beta[1])
    print("query t =", fmt(query, 0))
    print("line value =", fmt(value, 4))
    print("observed adj close min =", fmt(float(close.min()), 4))
    print("observed adj close max =", fmt(float(close.max()), 4))
    print("outside the observed range =", str(value < close.min() or value > close.max()).lower())


def day_48() -> None:
    t, close, _, _ = _level()
    query = float(t[-1] + 40)
    tree_value = float(predict_tree(np.array([query]), tree_depth2(t, close))[0])
    beta = ols(t, close)
    print("query t =", fmt(query, 0))
    print("tree value =", fmt(tree_value, 4))
    print("line value =", fmt(float(beta[0] * query + beta[1]), 4))
    print(
        "tree stays inside the training range =",
        str(close.min() - 1e-9 <= tree_value <= close.max() + 1e-9).lower(),
    )


def day_49() -> None:
    t, close, dates, _ = _level()
    jump = int(np.argmax(np.abs(returns(close)))) + 1
    line = ols(t, close)
    ridge = ridge_slope(t, close, lam=20000.0)
    tree = tree_depth2(t, close)
    actual = float(close[jump])
    later = min(jump + 10, len(close) - 1)
    hats = {
        "line": (float(line[0] * t[jump] + line[1]), float(line[0] * t[later] + line[1])),
        "ridge": (float(ridge[0] * t[jump] + ridge[1]), float(ridge[0] * t[later] + ridge[1])),
        "tree": (
            float(predict_tree(np.array([t[jump]]), tree)[0]),
            float(predict_tree(np.array([t[later]]), tree)[0]),
        ),
    }
    print("jump date =", dates[jump])
    print("adj close =", fmt(actual, 4))
    print("line slope =", fmt(float(line[0]), 4), "ridge slope =", fmt(float(ridge[0]), 4))
    for name, (hat, hat_later) in hats.items():
        print(f"{name} at jump = {hat:.4f}  residual = {actual - hat:.4f}  ten later = {hat_later:.4f}")


def day_50() -> None:
    train_t, train_y, test_t, test_y = _train_test()
    _, _, dates, cut = _level()
    line = ols(train_t, train_y)
    ridge = ridge_slope(train_t, train_y, lam=20000.0)
    tree = tree_depth2(train_t, train_y)
    pred = np.column_stack(
        [
            line[0] * test_t + line[1],
            ridge[0] * test_t + ridge[1],
            predict_tree(test_t, tree),
        ]
    )
    actual_move = np.diff(test_y)
    pred_move = np.diff(pred, axis=0)
    wrong = np.sign(pred_move) != np.sign(actual_move)[:, None]
    vote = np.sign(np.sign(pred_move).sum(axis=1))
    vote_wrong = vote != np.sign(actual_move)
    all_three = wrong.all(axis=1) & vote_wrong
    step_dates = dates[cut + 1 :]
    index = int(np.argmax(all_three)) if all_three.any() else int(np.argmax(vote_wrong))
    print("later date =", step_dates[index])
    print("line wrong =", str(bool(wrong[index, 0])).lower())
    print("ridge wrong =", str(bool(wrong[index, 1])).lower())
    print("tree wrong =", str(bool(wrong[index, 2])).lower())
    print("vote wrong =", str(bool(vote_wrong[index])).lower())
    print("days all three and the vote are wrong =", int(all_three.sum()))


DAYS = {i: globals()[f"day_{i}"] for i in range(11, 51)}


def main(day: int) -> None:
    DAYS[day]()
