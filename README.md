<p align="center"><b>中文</b> · <a href="README.en.md">English</a></p>

# 观测席

对价格序列做估计。一日一个可运行的估计器，报告它在该样本上的残差。

第一日可以复现。查询点 `x = 4` 位于训练集内。最近邻的样本内残差为 0，普通最小二乘的样本内残差为 8.2。说明见 [第 1 天](docs/season-01/day-01.md)，实现见 [`fit_line.py`](days/01-line-that-misses/fit_line.py)。

## 复现

Python 3.8 及以上。

```bash
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
python days/01-line-that-misses/fit_line.py
```

同一组收盘与拟合值见 [`site`](site)。在该目录执行 `npm install`，再执行 `npm run dev`。

## 目录

1. [估计](docs/season-01)
2. 因子
3. 组合构建
4. 执行

2019 年的笔记在 [`archive/2019`](archive/2019)。
