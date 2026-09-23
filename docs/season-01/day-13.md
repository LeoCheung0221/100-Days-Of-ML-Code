<p align="center"><b>中文</b> &nbsp;&nbsp;·&nbsp;&nbsp; <a href="day-13.en.md">English</a></p>

# 第 13 天 · 阈值灵敏度

[第一阶段 · 模型](README.md) · 可运行

恒猜涨的准确率在阈值 0.50、0.70、0.90 上分别是 0.75、0.50、0.25。阈值增加 0.40，准确率下降 0.50。只报其中一个准确率，读者不知道它靠的是哪一刀。

```bash
python days/13-threshold-sensitivity/sensitivity.py
```

```text
threshold  accuracy
0.50  0.75
0.70  0.50
0.90  0.25
```

下一步先放一个什么都不看的基准：永远猜跌。
