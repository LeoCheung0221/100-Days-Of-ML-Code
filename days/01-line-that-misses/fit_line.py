"""Day 1: a memorized neighbor versus a fitted line on one held-out point."""

from __future__ import annotations

import numpy as np

# Five closes. Day 4 is pulled up to 20; the line still has to fit all five.
TRAIN_X = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
TRAIN_Y = np.array([2.1, 3.9, 6.2, 20.0, 10.4])
ASK_X = 4.0


def nearest_y(x: float) -> float:
    index = int(np.argmin(np.abs(TRAIN_X - x)))
    return float(TRAIN_Y[index])


def fit_line() -> tuple[float, float]:
    # Closed form for y = slope * x + intercept.
    design = np.column_stack([TRAIN_X, np.ones_like(TRAIN_X)])
    slope, intercept = np.linalg.lstsq(design, TRAIN_Y, rcond=None)[0]
    return float(slope), float(intercept)


def main() -> None:
    slope, intercept = fit_line()
    remembered = nearest_y(ASK_X)
    lined = slope * ASK_X + intercept
    actual = float(TRAIN_Y[int(np.where(TRAIN_X == ASK_X)[0][0])])

    print("train points")
    for x, y in zip(TRAIN_X, TRAIN_Y):
        print(f"  x={x:.1f}  y={y:.1f}  line={slope * x + intercept:.2f}")
    print()
    print(f"line: y = {slope:.2f} x + {intercept:.2f}")
    print(f"ask x={ASK_X:.1f}, the stored y is {actual:.1f}")
    print(f"memorized neighbor says {remembered:.1f}, miss {abs(remembered - actual):.1f}")
    print(f"fitted line says {lined:.2f}, miss {abs(lined - actual):.1f}")


if __name__ == "__main__":
    main()
