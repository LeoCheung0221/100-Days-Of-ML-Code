"""Day 6: a query outside the training support. No label, so no residual."""

from __future__ import annotations

import numpy as np

TRAIN_X = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
TRAIN_Y = np.array([2.1, 3.9, 6.2, 20.0, 10.4])
ASK_X = 6.0


def fit_line(x: np.ndarray, y: np.ndarray) -> tuple[float, float]:
    design = np.column_stack([x, np.ones_like(x)])
    slope, intercept = np.linalg.lstsq(design, y, rcond=None)[0]
    return float(slope), float(intercept)


def main() -> None:
    slope, intercept = fit_line(TRAIN_X, TRAIN_Y)
    neighbor = int(np.argmin(np.abs(TRAIN_X - ASK_X)))
    copied = float(TRAIN_Y[neighbor])
    extrapolated = slope * ASK_X + intercept

    print(f"training support = [{TRAIN_X[0]:.0f}, {TRAIN_X[-1]:.0f}]")
    print(f"ask x={ASK_X:.0f}")
    print("y_6 is not in the sample")
    print(f"nearest neighbor copies t={neighbor + 1}, value {copied:.1f}")
    print(f"line: y = {slope:.2f} x + {intercept:.2f}")
    print(f"extrapolated value = {extrapolated:.2f}")
    print(f"gap between the two estimates = {extrapolated - copied:.2f}")
    print("residual is undefined")


if __name__ == "__main__":
    main()
