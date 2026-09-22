"""Day 2: the same residual vector scored by absolute loss and by squared loss."""

from __future__ import annotations

import numpy as np

# Same five closes as day 1. Day 4 is the pulled-up close.
TRAIN_X = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
TRAIN_Y = np.array([2.1, 3.9, 6.2, 20.0, 10.4])


def fit_line(x: np.ndarray, y: np.ndarray) -> tuple[float, float]:
    design = np.column_stack([x, np.ones_like(x)])
    slope, intercept = np.linalg.lstsq(design, y, rcond=None)[0]
    return float(slope), float(intercept)


def main() -> None:
    slope, intercept = fit_line(TRAIN_X, TRAIN_Y)
    fitted = slope * TRAIN_X + intercept
    residual = TRAIN_Y - fitted
    absolute = np.abs(residual)
    squared = residual ** 2
    l1 = float(absolute.sum())
    l2 = float(squared.sum())

    print(f"line: y = {slope:.2f} x + {intercept:.2f}")
    print("t  y  yhat  residual  absolute  squared")
    for t, y, yhat, r, a, s in zip(TRAIN_X, TRAIN_Y, fitted, residual, absolute, squared):
        print(f"{t:.0f}  {y:.1f}  {yhat:.2f}  {r:.2f}  {a:.2f}  {s:.4f}")
    print(f"L1 = sum |r| = {l1:.2f}")
    print(f"L2 = sum r^2 = {l2:.3f}")
    print(f"day 4 share of L1 = {absolute[3] / l1:.4f}")
    print(f"day 4 share of L2 = {squared[3] / l2:.4f}")


if __name__ == "__main__":
    main()
