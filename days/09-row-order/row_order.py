"""Day 9: permute the row order of the pairs. OLS does not move."""

from __future__ import annotations

import numpy as np

TRAIN_X = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
TRAIN_Y = np.array([2.1, 3.9, 6.2, 20.0, 10.4])
# A fixed presentation order. Not chosen to flatter the fit.
ROW_ORDER = np.array([2, 4, 3, 0, 1])


def fit_line(x: np.ndarray, y: np.ndarray) -> tuple[float, float]:
    design = np.column_stack([x, np.ones_like(x)])
    slope, intercept = np.linalg.lstsq(design, y, rcond=None)[0]
    return float(slope), float(intercept)


def rss(x: np.ndarray, y: np.ndarray, slope: float, intercept: float) -> float:
    residual = y - (slope * x + intercept)
    return float(np.sum(residual ** 2))


def main() -> None:
    slope, intercept = fit_line(TRAIN_X, TRAIN_Y)
    original = rss(TRAIN_X, TRAIN_Y, slope, intercept)

    shuffled_x = TRAIN_X[ROW_ORDER]
    shuffled_y = TRAIN_Y[ROW_ORDER]
    slope2, intercept2 = fit_line(shuffled_x, shuffled_y)
    permuted = rss(shuffled_x, shuffled_y, slope2, intercept2)

    print(f"original: y = {slope:.4f} x + {intercept:.4f}")
    print(f"RSS = {original:.4f}")
    print(f"row order = {ROW_ORDER.tolist()}")
    print("pairs kept intact")
    print(f"permuted: y = {slope2:.4f} x + {intercept2:.4f}")
    print(f"RSS = {permuted:.4f}")
    print(f"delta slope = {slope2 - slope:.3e}")
    print(f"delta RSS = {permuted - original:.3e}")


if __name__ == "__main__":
    main()
