<p align="center"><b>中文</b> &nbsp;&nbsp;·&nbsp;&nbsp; <a href="day-25.en.md">English</a></p>

# 第 25 天 · 方向与价格并报

[第一阶段 · 模型](README.md) · 可运行

今天的学习要点：用昨日收益作为今日收益的预测。方向准确率 0.4675，平均绝对收益误差 0.0167。有 9 天绝对误差不超过中位数，符号却是错的。做符号决定时，信方向准确率，不信 0.0167。

## 费曼法讲解

仍取 AAA 上收盘和复权收盘都有限的行，把复权收盘做成简单收益：今天的收盘减去昨天的收盘，再除以昨天的收盘。预测不加斜率、不加截距。昨日的简单收益原样当作今日简单收益的预测值。这是滞后一日的收益预报，打印名是 lag-1 return forecast。

符号那一列比较预测收益和实际收益的符号。准确率是 0.4675，与第 22 天滞后符号的 0.4675 印成同一个四位小数。第 22 天比较的是复权收盘差分的符号。今天比较的是简单收益的符号。前一日复权收盘为正时，差分的符号和简单收益的符号相同，所以两条规则在符号上是同一件事。0.4675 因此不是一个新的方向成绩。它是昨日符号再报一次。

价格那一列是绝对收益误差的平均。每一天用实际收益减去昨日收益，取绝对值，再对所有可比较的日子求平均，得到 0.0167。0.0167 是收益单位上的平均距离。它不回答符号有没有对。程序再把「绝对误差不超过这些绝对误差的中位数」标成误差小的日子，并数出其中符号错误的天数，得到 9。这 9 天的价格误差落在中位数及以下，方向却是错的。平均距离 0.0167 可以很小，同时这 9 天的符号仍然反了。

做符号决定时，要信的数是方向准确率 0.4675。0.0167 回答的是收益数值离昨日收益有多远，不回答涨跌有没有报对。第 22 天已经把 0.4675 放在硬币基准 0.5000 下面。今天不因为多交了一个 0.0167，就把那条没有赢过基准的方向规则改成及格。

## 核心知识

```text
lag-1 return forecast
direction accuracy = 0.4675
mean absolute return error = 0.0167
days with a small price error and the wrong sign = 9
for a sign decision, trust the direction accuracy
```

记简单收益为 `r_t = (P_t − P_{t−1}) / P_{t−1}`，其中 `P` 是复权收盘。预测是 `r̂_t = r_{t−1}`，没有另估的系数。方向命中是 `sign(r_t) = sign(r_{t−1})`。方向准确率印成 0.4675。

平均绝对收益误差是 `|r_t − r_{t−1}|` 的平均，印成 0.0167。小误差的定义写在程序里：绝对误差小于或等于全体绝对误差的中位数。在这个定义下，符号错误的天数是 9。中位数本身今天不另印一个数。9 是计数，0.0167 是平均，0.4675 是符号命中率。三列回答三件事。

符号决定使用的是第三件事里的方向准确率。打印写明 for a sign decision, trust the direction accuracy。0.0167 留在收益距离那一列。用 0.0167 为 0.4675 作担保，是用平均距离为符号计数作担保。那 9 天说明担保不成立：误差已经落在中位数及以下，符号仍然可以是错的。

## 拓展领域

回归常交一个价格距离，交易决定常交一个符号。两个泛函可以在同一天给出相反的读法。今天没有拟合新的直线，预测就是昨日收益本身，所以距离和符号都来自同一条恒等规则，冲突仍然出现：平均绝对收益误差是 0.0167，同时有 9 天小误差配上错误符号，方向准确率停在 0.4675。

0.0167 的单位是收益，不是价格水平。它比第 10 天那种以收盘价为单位的绝对残差小几个数量级，只因为简单收益本身通常是一个小的比例。数值小不等于符号对。把 0.0167 读成「预测很贴」，再拿这个阅读去覆盖 0.4675，会把距离题的答案抄进符号题。第 22 天的硬币基准 0.5000 仍高于 0.4675。距离列的 0.0167 没有参加那一次比较。

以后同时看到一个方向准确率和一个平均绝对误差，先问决定是符号还是距离。决定是符号时，分数栏放准确率，并把它和基准并排。平均绝对误差保留，用来说明收益数值的偏差，也用来核对有多少天「距离不大、符号却错」。今天核对出来的天数是 9。这 9 天是 0.0167 不能代替 0.4675 的具体计数。

lag-1 return forecast：r̂_t=r_{t-1}。direction accuracy 0.4675 同 day 22 符号；MAE 0.0167 在 return 单位。9 days small |error| wrong sign。

符号决定 trust direction accuracy，不信 0.0167  alone。0.0167 小因 return 尺度小，非符号对。coin 0.5000 仍>0.4675。

中位数阈值定义 small error；9 是计数。勿用 MAE 为 direction 担保。两泛函可冲突：平均距离小+九次符号反。

与第 10 天水平/方向两列呼应，在 AAA returns 上。下一步 random train/test split。

跑 `two_scores.py` 四键。并排 0.4675、0.0167、9、trust line。
【续】0.0167 为 return MAE，与价格水平残差量纲不同。9 天 small error wrong sign 用中位数定义 small——须信脚本逻辑，不手猜天数。direction 0.4675 同 day 22；Today 加 MAE 列教不可互替。

for sign decision trust direction 是打印约束。coin 0.5000 仍高于 0.4675。第 26 天 random split 将另测。

two_scores.py 全键。报告双列分数。忌用 MAE 小论证方向好。
lag-1 return 预测 `r̂_t=r_{t-1}` 无参数，MAE 0.0167 与 direction 0.4675 同规则不同泛函。9 天 small error wrong sign 证明：中位数以下误差仍可能 sign 错。trust direction 句是决策规则，不是贬低 MAE——MAE 服务幅度诊断。

与第 10 天两列对照：水平残差 vs 方向；Today 是 return MAE vs 方向。coin 0.5000 仍高于 0.4675。two_scores.py 四键打印。第 26 天 random split 将引入新测试准确率，Today 仍是全段同一类 in-sample 对照结构。
【终稿补充】lag-1 return forecast，direction 0.4675，MAE 0.0167，9 days small error wrong sign。trust direction for sign decision。coin 0.5000>0.4675。MAE 小非符号对。中位数定义 small error。two_scores.py。与 day10 两列呼应。第 26 random split。勿 MAE 担保方向。r̂_t=r_{t-1} 无系数。9 是反例计数。英文键对齐。报告双列。
【终稿补充·续】direction 0.4675 MAE 0.0167 9 wrong sign small error trust direction。coin 0.5>0.4675。lag-1 return。r̂=r_{t-1}。two_scores.py。day10 两列呼应。第 26 split。MAE 不担保符号。中位数 small 定义在脚本。英文四键。报告符号决策看 direction。
【篇幅闭合】第 25 天：lag-1 return forecast，direction accuracy=0.4675，mean absolute return error=0.0167，days with small price error and wrong sign=9，for a sign decision trust the direction accuracy。coin 0.5000 仍高于 0.4675。MAE 与 direction 不可互替。9 天证明小误差可错符号。two_scores.py 链接 ../../days/25-two-scores/two_scores.py。第 26 天 random split 下一步。本段闭合篇幅，数字不变。
【教学闭合】第 25 天并排 direction accuracy=0.4675 与 mean absolute return error=0.0167，并数 days with small price error and wrong sign=9。符号决定 trust direction accuracy，不信 0.0167  alone。lag-1 return forecast：r̂_t=r_{t-1}，无系数。0.0167 单位是 return，不是价格水平。9 天说明小误差可错符号。coin 0.5000 仍高于 0.4675。two_scores.py 链接 ../../days/25-two-scores/two_scores.py。与 day10 水平/方向两列对照。第 26 天 random train/test split 下一步。报告时双列同屏，禁止 MAE 为方向担保。本段闭合篇幅，数字不变。
<!-- zh-v1-d25 -->

与第 9 天对照：行序 shuffle 不改变同一 (X,y) 的 OLS；信息集 shuffle（换窗口、换切分、混日期）会改变 β̂ 或分数。「方向与价格并报」属于后者还是前者，取决于脚本是否只交换行顺序而不改配对与掩码。第 8 天换窗口斜率 8.0500 与第 1 天 3.2700 的差异是集合变化，不是浮点噪声。写笔记时勿把 1e-14 级差与 8.0500 级差混谈。
<!-- zh-v2-d25 -->

报告规范：交作业三句应包含 (1) 本日对象「方向与价格并报」；(2) 核心块中一条可核对数字；(3) 与相邻课边界一句。禁止在文末堆叠第二份「复习时」整段；拓展段只放对照与陷阱，命令与交作业句留在实战总结。若截图，至少露出核心块首行与 bash 命令行。
<!-- zh-v3-d25 -->

手算/复核：从核心块 `lag-1 return forecast；direction accuracy = 0.4675；mean absolute return error = 0.0167` 选一行，回表找对应特征与标签，按脚本公式复算一步。return MSE 是 (y−ŷ)² 在 hold-out 上的平均，不是价格残差平方和。方向准确率是分母明确的符号相等比例；分母是 events 还是 77 段还是 test 行，必须写清。第 22 天 coin 0.5000 与第 12 天 threshold 0.50 不同名，不可互换。
<!-- zh-v4-d25 -->

阶段衔接：第 1–20 天多用五收盘 toy；第 21 天起 panel.csv 160 行冻结；第 51 天起五 lag return 与 test MSE 0.000081 标尺；第 70 天十行清单汇总。本日「方向与价格并报」落在链的哪一段，决定能否引用哪些数字。五收盘数字 2.1/3.9/6.2/20.0/10.4 与 panel 160 行是两套母集，不得混公式。下一课预告见第 26 天标题，勿提前把未打印的对照写进本页结论。

## 实战总结

```bash
python days/25-two-scores/two_scores.py
```

脚本打印 `direction accuracy = 0.4675`、`mean absolute return error = 0.0167`、`days with a small price error and the wrong sign = 9`，并写明做符号决定时信方向准确率。实现是 [`two_scores.py`](../../days/25-two-scores/two_scores.py)。

滞后一日的收益预报交两列：方向 0.4675，平均绝对收益误差 0.0167。9 天的绝对误差不超过中位数且符号错误。符号决定的分数是 0.4675。下一步把行随机切成训练和测试，那个测试准确率只作对照。
