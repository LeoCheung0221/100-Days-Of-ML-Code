<p align="center"><b>中文</b> &nbsp;&nbsp;·&nbsp;&nbsp; <a href="day-50.en.md">English</a></p>

# 第 50 天 · 三模型投票

[第一阶段 · 模型](README.md) · 可运行

后一段里，2024-03-29 这一步，直线、岭回归和树的方向都错，投票也错。这样的日子有 8 天。多数并没有把三个错误收成一个正确。

```bash
python days/50-vote/vote.py
```

```text
later date = 2024-03-29
line wrong = true
ridge wrong = true
tree wrong = true
vote wrong = true
days all three and the vote are wrong = 8
```

下一步才会把特征改成过去五日收益。本日停在这三个模型的投票上。
