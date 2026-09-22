"""Day 5: refit the affine line with day 4 deleted, and record the displacement."""

from __future__ import annotations

import numpy as np

TRAIN_X = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
TRAIN_Y = np.array([2.1, 3.9, 6.2, 20.0, 10.4])


def fit_line(x: np.ndarray, y: np.ndarray) -> tuple[float, float]:
    design = np.column_stack([x, np.ones_like(x)])
    slope, intercept = np.linalg.lstsq(design, y, rcond=None)[0]
    return float(slope), float(intercept)


def main() -> None:
    full = fit_line(TRAIN_X, TRAIN_Y)
    keep = np.array([True, True, True, False, True])
    reduced = fit_line(TRAIN_X[keep], TRAIN_Y[keep])

    print(f"full:    y = {full[0]:.4f} x + {full[1]:.4f}")
    print(f"without: y = {reduced[0]:.4f} x + {reduced[1]:.4f}")
    print(f"delta slope = {reduced[0] - full[0]:.4f}")
    print(f"delta intercept = {reduced[1] - full[1]:.4f}")
    print("t  full  without  displacement")
    for x in TRAIN_X:
        a = full[0] * x + full[1]
        b = reduced[0] * x + reduced[1]
        print(f"{x:.0f}  {a:.4f}  {b:.4f}  {b - a:.4f}")
    at_four = reduced[0] * 4.0 + reduced[1]
    print(f"deleted label y_4 = {TRAIN_Y[3]:.1f}")
    print(f"refit at x=4 = {at_four:.4f}")
    print("the gap y_4 - refit is not a test score")


if __name__ == "__main__":
    main()
