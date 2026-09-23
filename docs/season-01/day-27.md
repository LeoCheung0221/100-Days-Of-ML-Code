<p align="center"><b>中文</b> &nbsp;&nbsp;·&nbsp;&nbsp; <a href="day-27.en.md">English</a></p>

# 第 27 天 · 按时间切分

[第一阶段 · 模型](README.md) · 可运行

按时间切，测试方向准确率是 0.5417。同一条序列上的随机切分是 0.4583。两个都印。这一次时间切更高。单标的的随机切分没有变高。混进第二只股票、让同一天出现在训练和测试两侧，是第 37 天。

```bash
python days/27-time-split/time_split.py
```

```text
time-split test accuracy = 0.5417
random-split test accuracy = 0.4583
the test of the time split sits entirely after the train
```

下一步用当日最高价解释当日收盘，并标明这列不许用。
