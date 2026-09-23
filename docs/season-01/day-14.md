<p align="center"><b>中文</b> &nbsp;&nbsp;·&nbsp;&nbsp; <a href="day-14.en.md">English</a></p>

# 第 14 天 · 常数基准

[第一阶段 · 模型](README.md) · 可运行

符号标签上，永远猜跌的准确率是 0.25，永远猜涨是 0.75。基准不读价格。0.75 如果没有旁边的 0.25，就没有对照。

```bash
python days/14-constant-baseline/baseline.py
```

```text
always-down accuracy = 0.25
always-up accuracy = 0.75
the baseline looks at no price
```

下一步把两种错分开计数，不再合成一个准确率。
