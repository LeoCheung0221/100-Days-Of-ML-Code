"""Day 8: one affine fit on days 1-3, then the window slides onto days 2-4."""

from __future__ import annotations

import numpy as np

TRAIN_X = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
TRAIN_Y = np.array([2.1, 3.9, 6.2, 20.0, 10.4])


def fit_line(x: np.ndarray, y: np.ndarray) -> tuple[float, float]:
    design = np.column_stack([x, np.ones_like(x)])
    slope, intercept = np.linalg.lstsq(design, y, rcond=None)[0]
    return float(slope), float(intercept)


def report(name: str, x: np.ndarray, y: np.ndarray) -> tuple[float, float]:
    slope, intercept = fit_line(x, y)
    residual = y - (slope * x + intercept)
    rss = float(np.sum(residual ** 2))
    print(f"{name}: y = {slope:.4f} x + {intercept:.4f}")
    print(f"rows t={x[0]:.0f}..{x[-1]:.0f}")
    print(f"RSS = {rss:.4f}")
    return slope, intercept


def main() -> None:
    first = report("window", TRAIN_X[:3], TRAIN_Y[:3])
    print()
    second = report("slid", TRAIN_X[1:4], TRAIN_Y[1:4])
    print()
    print(f"delta slope = {second[0] - first[0]:.4f}")
    print("day 1 is no longer in the information set")
    print("day 4 has entered")


if __name__ == "__main__":
    main()
