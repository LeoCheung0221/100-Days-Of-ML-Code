"""Day 4: the chord through the endpoints, scored against OLS on two losses."""

from __future__ import annotations

import numpy as np

TRAIN_X = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
TRAIN_Y = np.array([2.1, 3.9, 6.2, 20.0, 10.4])


def fit_line(x: np.ndarray, y: np.ndarray) -> tuple[float, float]:
    design = np.column_stack([x, np.ones_like(x)])
    slope, intercept = np.linalg.lstsq(design, y, rcond=None)[0]
    return float(slope), float(intercept)


def chord(x: np.ndarray, y: np.ndarray) -> tuple[float, float]:
    slope = (y[-1] - y[0]) / (x[-1] - x[0])
    intercept = y[0] - slope * x[0]
    return float(slope), float(intercept)


def report(name: str, slope: float, intercept: float) -> None:
    fitted = slope * TRAIN_X + intercept
    residual = TRAIN_Y - fitted
    l1 = float(np.abs(residual).sum())
    l2 = float(np.sum(residual ** 2))
    print(f"{name}: y = {slope:.4f} x + {intercept:.4f}")
    print("t  yhat  residual")
    for t, yhat, r in zip(TRAIN_X, fitted, residual):
        print(f"{t:.0f}  {yhat:.4f}  {r:.4f}")
    print(f"L1 = {l1:.4f}")
    print(f"L2 = {l2:.4f}")
    print(f"day 4 absolute residual = {abs(residual[3]):.4f}")
    print()


def main() -> None:
    report("chord", *chord(TRAIN_X, TRAIN_Y))
    report("ols", *fit_line(TRAIN_X, TRAIN_Y))


if __name__ == "__main__":
    main()
