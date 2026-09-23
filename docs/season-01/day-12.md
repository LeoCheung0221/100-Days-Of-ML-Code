<p align="center"><b>中文</b> &nbsp;&nbsp;·&nbsp;&nbsp; <a href="day-12.en.md">English</a></p>

# 第 12 天 · 阈值

[第一阶段 · 模型](README.md) · 可运行

四步收益是 0.8571、0.5897、2.2258、−0.4800。阈值取 0.70 时，标签是 1 0 1 0。恒猜涨的准确率是 0.50。在第 11 天，同一条规则对着符号标签是 0.75。切开的位置是定义的一部分。

```bash
python days/12-threshold/threshold.py
```

```text
threshold = 0.70
returns = 0.8571 0.5897 2.2258 -0.4800
label up = 1 0 1 0
constant-up accuracy = 0.50
```

下一步把阈值挪开，准确率的变化必须一起交。
