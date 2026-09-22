"""Day 10: price residuals and the sign of the one-day move, on the same fit."""

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
    fitted = slope * TRAIN_X + intercept
    residual = TRAIN_Y - fitted
    move = np.diff(TRAIN_Y)
    fitted_move = np.diff(fitted)
    hit = np.sign(move) == np.sign(fitted_move)

    print(f"line: y = {slope:.2f} x + {intercept:.2f}")
    print(f"fitted one-day move = {fitted_move[0]:.2f} on every step")
    print("t  y  yhat  residual  dy  dyhat  hit")
    for i in range(1, len(TRAIN_X)):
        print(
            f"{i + 1:.0f}  {TRAIN_Y[i]:.1f}  {fitted[i]:.2f}  {residual[i]:.2f}"
            f"  {move[i - 1]:.1f}  {fitted_move[i - 1]:.2f}  {int(hit[i - 1])}"
        )
    print(f"direction hits = {int(hit.sum())} / {len(hit)}")
    print(f"day 4 |residual| = {abs(residual[3]):.2f}, hit = {int(hit[2])}")
    print(f"day 5 |residual| = {abs(residual[4]):.2f}, hit = {int(hit[3])}")


if __name__ == "__main__":
    main()
