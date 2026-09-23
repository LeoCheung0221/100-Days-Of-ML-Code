<p align="center"><b>中文</b> &nbsp;&nbsp;·&nbsp;&nbsp; <a href="day-17.en.md">English</a></p>

# 第 17 天 · 置信核对

[第一阶段 · 模型](README.md) · 可运行

报出的上涨概率是 0.9634。四步里实际上涨的频率是 0.75。缺口是 0.2134。说成九成六的那些步，只有四分之三真的上涨。置信和频率要并排，不能互相代替。

```bash
python days/17-confidence-check/confidence.py
```

```text
stated P(up) = 0.9634
realized up frequency = 0.75
gap = 0.2134
```

下一步的输入不再是单日价格，收益和成交量一起决定标签。
