"""Day 3: residual sum of squares is not a substitute for the residual vector."""

from __future__ import annotations

import numpy as np

TRAIN_X = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
TRAIN_Y = np.array([2.1, 3.9, 6.2, 20.0, 10.4])


def fit_line(x: np.ndarray, y: np.ndarray) -> tuple[float, float]:
    design = np.column_stack([x, np.ones_like(x)])
    slope, intercept = np.linalg.lstsq(design, y, rcond=None)[0]
    return float(slope), float(intercept)


def main() -> None:
    slope, intercept = fit_line(TRAIN_X, TRAIN_Y)
    residual = TRAIN_Y - (slope * TRAIN_X + intercept)
    squared = residual ** 2
    rss = float(squared.sum())

    print(f"line: y = {slope:.2f} x + {intercept:.2f}")
    print(f"RSS = {rss:.3f}")
    print("t  residual  squared  share of RSS")
    for t, r, s in zip(TRAIN_X, residual, squared):
        print(f"{t:.0f}  {r:.2f}  {s:.4f}  {s / rss:.4f}")
    top = int(np.argmax(squared))
    print(f"largest squared residual at t={top + 1}")
    print(f"days 4 and 5 share of RSS = {(squared[3] + squared[4]) / rss:.4f}")
    print(f"days 1 through 3 share of RSS = {squared[:3].sum() / rss:.4f}")


if __name__ == "__main__":
    main()
