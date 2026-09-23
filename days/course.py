"""Shared series and estimators for days 11–60.

The five closes of days 1–10 stay in the early sessions. From day 21 the
scripts read days/data/panel.csv and do not resample it.
"""

from __future__ import annotations

import csv
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
PANEL_PATH = Path(__file__).resolve().parent / "data" / "panel.csv"

FIVE_X = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
FIVE_Y = np.array([2.1, 3.9, 6.2, 20.0, 10.4])
# Volume in shares. Session 4 is the pulled-up close and the heavy print.
FIVE_V = np.array([1.0e6, 1.2e6, 0.9e6, 8.0e6, 1.5e6])


def ols(x: np.ndarray, y: np.ndarray) -> np.ndarray:
    design = np.column_stack([np.asarray(x, float), np.ones(len(x))])
    beta, *_ = np.linalg.lstsq(design, np.asarray(y, float), rcond=None)
    return beta


def ridge_slope(x: np.ndarray, y: np.ndarray, lam: float) -> np.ndarray:
    """Penalize the slope only. The intercept is free."""
    design = np.column_stack([np.asarray(x, float), np.ones(len(x))])
    gram = design.T @ design
    gram[0, 0] += lam
    return np.linalg.solve(gram, design.T @ np.asarray(y, float))


def stump(x: np.ndarray, y: np.ndarray) -> tuple[float, float, float]:
    """One split on a single feature. Returns threshold, left mean, right mean."""
    x = np.asarray(x, float)
    y = np.asarray(y, float)
    order = np.argsort(x, kind="mergesort")
    xs, ys = x[order], y[order]
    best: tuple[float, float, float, float] | None = None
    total = ys.sum()
    left_sum = 0.0
    for i in range(1, len(xs)):
        left_sum += ys[i - 1]
        if xs[i] == xs[i - 1]:
            continue
        n_left = i
        n_right = len(xs) - i
        left_mean = left_sum / n_left
        right_mean = (total - left_sum) / n_right
        sse = ((ys[:i] - left_mean) ** 2).sum() + ((ys[i:] - right_mean) ** 2).sum()
        if best is None or sse < best[0]:
            best = (float(sse), float(0.5 * (xs[i - 1] + xs[i])), float(left_mean), float(right_mean))
    assert best is not None
    return best[1], best[2], best[3]


def predict_stump(x: np.ndarray, threshold: float, left: float, right: float) -> np.ndarray:
    return np.where(np.asarray(x, float) <= threshold, left, right)


def tree_depth2(x: np.ndarray, y: np.ndarray) -> dict:
    """A depth-2 regression tree on one feature. Children split only if n >= 8."""
    x = np.asarray(x, float)
    y = np.asarray(y, float)
    root_t, root_l, root_r = stump(x, y)
    left_mask = x <= root_t

    def child(mask: np.ndarray) -> dict:
        if int(mask.sum()) < 8:
            return {"leaf": float(y[mask].mean())}
        thr, left, right = stump(x[mask], y[mask])
        return {"threshold": thr, "left": left, "right": right}

    return {"threshold": root_t, "left": child(left_mask), "right": child(~left_mask)}


def predict_tree(x: np.ndarray, tree: dict) -> np.ndarray:
    x = np.asarray(x, float)
    out = np.empty(len(x))
    left_mask = x <= tree["threshold"]
    for mask, node in ((left_mask, tree["left"]), (~left_mask, tree["right"])):
        if "leaf" in node:
            out[mask] = node["leaf"]
        else:
            out[mask] = predict_stump(x[mask], node["threshold"], node["left"], node["right"])
    return out


def load_panel() -> list[dict]:
    rows = []
    with PANEL_PATH.open(newline="") as handle:
        for row in csv.DictReader(handle):
            item = {"date": row["date"], "name": row["name"]}
            for key in ("open", "high", "low", "close", "volume", "adj_close", "market"):
                text = row[key].strip()
                item[key] = float(text) if text else float("nan")
            rows.append(item)
    return rows


def name_rows(name: str) -> list[dict]:
    return [row for row in load_panel() if row["name"] == name]


def column(rows: list[dict], key: str) -> np.ndarray:
    return np.array([row[key] for row in rows], dtype=float)


def returns(close: np.ndarray) -> np.ndarray:
    previous = close[:-1]
    return (close[1:] - previous) / previous


def sign_hit(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    return np.sign(a) == np.sign(b)


def accuracy(hits: np.ndarray) -> float:
    return float(np.mean(hits))


def fmt(value: float, digits: int = 4) -> str:
    return f"{value:.{digits}f}"
