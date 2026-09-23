<p align="center"><a href="../../docs/season-01/day-29.md">中文讲解</a> · <a href="../../docs/season-01/day-29.en.md">English</a></p>

# 第 29 天 · 用未来开盘标准化

用全部开盘的均值和标准差缩放收盘，包括该收盘之后的开盘，收益回归的 RSS 是 0.2642。只用过去收盘缩放，RSS 是 0.2650。差是 0.0008。泄漏的识别不靠分数变得更好，靠缩放的自变量里有以后的开盘。

```bash
python days/29-future-open/future_open.py
```
