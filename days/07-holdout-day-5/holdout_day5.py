"""Day 7: fit on days 1-4. The only score is the residual on day 5."""

from __future__ import annotations

import numpy as np

TRAIN_X = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
TRAIN_Y = np.array([2.1, 3.9, 6.2, 20.0, 10.4])


def fit_line(x: np.ndarray, y: np.ndarray) -> tuple[float, float]:
    design = np.column_stack([x, np.ones_like(x)])
    slope, intercept = np.linalg.lstsq(design, y, rcond=None)[0]
    return float(slope), float(intercept)


def main() -> None:
    fit_x = TRAIN_X[:-1]
    fit_y = TRAIN_Y[:-1]
    slope, intercept = fit_line(fit_x, fit_y)
    train_resid = fit_y - (slope * fit_x + intercept)
    train_rss = float(np.sum(train_resid ** 2))

    exam_x = float(TRAIN_X[-1])
    exam_y = float(TRAIN_Y[-1])
    lined = slope * exam_x + intercept
    neighbor = int(np.argmin(np.abs(fit_x - exam_x)))
    copied = float(fit_y[neighbor])

    print(f"fit on t=1..4: y = {slope:.2f} x + {intercept:.2f}")
    print(f"training RSS = {train_rss:.2f}")
    print("training RSS is not the score")
    print(f"exam t=5  y={exam_y:.1f}")
    print(f"ols says {lined:.2f}, residual {exam_y - lined:.2f}")
    print(f"nearest neighbor copies t={neighbor + 1}, value {copied:.1f}, residual {exam_y - copied:.1f}")


if __name__ == "__main__":
    main()
