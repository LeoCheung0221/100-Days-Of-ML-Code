<p align="center"><a href="#zh"><b>中文</b></a> &nbsp;&nbsp;·&nbsp;&nbsp; <a href="#en">English</a></p>

<a id="zh"></a>

# 第一阶段 · 模型

说明：[第 1 天 · 样本内最近邻与普通最小二乘](day-01.md)。其余各日列在下面。

回到 [首页](../../README.md)。

## 01 – 10 · 误差

| 天 | 实战 | 新收走的办法 |
|---|---|---|
| [01　最近邻与普通最小二乘](day-01.md) | 样本内最近邻与普通最小二乘 | 查询点落在训练集内，两种估计并排 |
| 02 | 绝对误差与平方误差 | 同一个失手要交两个数。平方会把第四天放得更重 |
| 03 | 五天的残差并排 | 不能只报总分，要指出误差集中在哪一天 |
| 04 | 只连接第一天和第五天 | 一条更笨的线，必须和最小二乘比失手 |
| 05 | 去掉第四天再拟合 | 看一个点能把整条线搬多远 |
| 06 | 询问第六天 | 训练里没有这一天。死记只能抄邻居，直线必须外推 |
| 07 | 藏起第五天当考试 | 训练时的误差不再算数 |
| 08 | 窗口只留三天，向前滑一次 | 线必须扔掉更早的价格 |
| 09 | 打乱日期后再拟合 | 成绩几乎不变，于是它被证明不识时间 |
| 10 | 改用涨跌方向打分 | 价格误差小，方向仍可能错。两个分数都要交 |

## 11 – 25 · 方向

| 天 | 实战 | 新收走的办法 |
|---|---|---|
| 11 | 只保留涨或跌 | 不能再用 8.2 这种距离 |
| 12 | 用一个阈值把收益切成涨跌 | 切在哪里要自己定 |
| 13 | 阈值挪开一点 | 准确率对这一下有多敏感，要报出来 |
| 14 | 永远猜「跌」 | 先有基准。模型必须赢过什么都不看的人 |
| 15 | 两种错分开放进表里 | 把涨说成跌，和把跌说成涨，分开计数 |
| 16 | 输出「像涨的程度」 | 多交一个 0 到 1 的数 |
| 17 | 核对说成八成的那些天 | 自信必须配得上出现的次数 |
| 18 | 涨幅和成交量一起分界 | 输入不再是单日价格 |
| 19 | 成交量不缩放就放进去 | 位数大的一列会挤走价格。你要看见这件事 |
| 20 | 加一列纯噪声 | 成绩不该因此变好 |
| 21 | 换成一份固定的真实收盘小表 | 数字不再手写。反复读取必须得到同一结果 |
| 22 | 用昨天的涨跌猜今天 | 和扔硬币的基准并排 |
| 23 | 连续三天同向，看第四天 | 规则写死，不能看完结果再改条件 |
| 24 | 把这条规则放到下一段行情 | 不许在挑选过的那段上报成绩 |
| 25 | 方向分数和价格分数同时交 | 两套分数冲突时，写明你信哪一套 |

## 26 – 40 · 时间

| 天 | 实战 | 新收走的办法 |
|---|---|---|
| 26 | 随机把行切成训练和测试 | 先留下一个虚高的成绩当对照 |
| 27 | 改成按时间切 | 测试全在训练之后。两个数都要印出来 |
| 28 | 用当天最高价解释当天收盘 | 脚本要标出这列不许用 |
| 29 | 用明天的开盘做标准化 | 泄漏可以藏在预处理里 |
| 30 | 每天只看过去一个固定窗口 | 不能再用整段历史一起拟合 |
| 31 | 窗口收成三天 | 线会跟着单日噪声走。这种失手单独印出 |
| 32 | 窗口放到六十天 | 线还停在更早的行情里。和 31 并排 |
| 33 | 均值和方差只用训练段估计 | 测试段不许自己算标准化 |
| 34 | 缺失日分别用未来和过去来填 | 两种填法都要有，偷看的那种要被标出来 |
| 35 | 删掉停牌日后检查间隔 | 行号相邻不等于时间相邻 |
| 36 | 不复权的跳空对上复权后的同一天 | 公司行动会被当成信号。两个误差都要有 |
| 37 | 多只股票先混切，再改回按时间切 | 它们共享同一天的消息。虚高要被看见 |
| 38 | 信号整体滞后一天 | 消失的部分是同时信息，留下的才可能用 |
| 39 | 扣掉一个最小来回成本 | 扣完之后，此前那点优势还在不在 |
| 40 | 为本段每一个变好的结果注明是否看见了未来 | 成绩单后面必须附一张泄漏清单 |

## 41 – 55 · 失手的方式

| 天 | 实战 | 新收走的办法 |
|---|---|---|
| 41 | 在更长的价格上重做直线 | 跳空仍会搬走整条线。这次跳空不是手写的 |
| 42 | 岭回归，斜率被罚 | 同一个跳空，线不许搬那么远 |
| 43 | 只平均附近几天 | 远处的跳空进不了答案 |
| 44 | 一棵浅树 | 它可以把跳空那天单独切开 |
| 45 | 树再深一层 | 训练更好，换一段更差。它在背日期 |
| 46 | 线性、岭、树换到下一段 | 训练误差接近的三个，要报谁还活着 |
| 47 | 线性对很远的一天外推 | 答案可以落在不合理的价格外 |
| 48 | 树对同一天外推 | 它只会重复一片叶子。两种失手并排 |
| 49 | 三个模型在同一个跳空日 | 写明谁错在被搬走，谁错在背住了那天 |
| 50 | 三个模型投票 | 找出三个都错、投票也错的一天 |
| 51 | 特征改成过去五日收益 | 线性给每天的权重大致接近。把权重印出来 |
| 52 | 树用同样的五日 | 它会把其中一天单独切开 |
| 53 | 换一个随机种子 | 树的切法变了，线性几乎不变 |
| 54 | 拿掉成交量再跑 | 谁掉得多，谁就依赖这一列 |
| 55 | 为三个模型各写一句失手方式 | 不许再只交一个分数 |

## 56 – 70 · 一个小任务

| 天 | 实战 | 新收走的办法 |
|---|---|---|
| 56 | 用一句话写死任务：用过去猜下一日收益 | 表、目标、不许用的列，先写进程序再跑 |
| 57 | 程序拒绝当天的最高价、最低价、收盘价 | 违规列出现时要失败，不能悄悄用上 |
| 58 | 按年份切 | 切分规则写死，不按行号 |
| 59 | 基准是永远猜收益为 0 | 模型必须和基准并排 |
| 60 | 线性减去基准 | 赢的那一点要落到具体的日子上 |
| 61 | 树减去同一个基准 | 与 60 用同一张表、同一切分 |
| 62 | 只在最有把握的一成天数上计误差 | 剩下九成不许拿来把平均数冲好看 |
| 63 | 按月拆开误差 | 找出有没有一个月独撑全年 |
| 64 | 删掉那一个月再算 | 结论还在，才算数 |
| 65 | 换第二只股票 | 流程不改。第一只的结论不许自动带过去 |
| 66 | 收益改成相对市场的超额 | 要解释的是超出市场的部分 |
| 67 | 把市场列前移一天 | 因此变好的成绩标成无效 |
| 68 | 整套流程收成一个函数 | 第二张表必须走同一入口 |
| 69 | 写下成交假设 | 按收盘价成交，没有滑点。假设写进输出 |
| 70 | 用十行讲完这个任务 | 讲稿里的每个数字都要能在输出里找到 |

## 71 – 85 · 贵的错

| 天 | 实战 | 新收走的办法 |
|---|---|---|
| 71 | 失手分成跳空、平静日、方向反了 | 三类计数取代单一误差 |
| 72 | 只看平静日 | 误差小要被说成「这些天本来就好猜」 |
| 73 | 只数方向反了的天数 | 这个次数可以和平均误差排名不同 |
| 74 | 误差最大的五天归类 | 五天若同类，平均误差就是这一类在说话 |
| 75 | 方向反了扣 1，跳空日扣 3 | 计费一变，排名允许对调 |
| 76 | 漏掉一次大跌，对比误报一次小涨 | 两种错分成两列 |
| 77 | 提高阈值，只在更有把握时开口 | 开口次数下降，剩下的判断单独计费 |
| 78 | 降低阈值，几乎每天都开口 | 平均数变温和，贵的错还在。两个表并排 |
| 79 | 用新的计费重排线性和树 | 平均误差的赢家可以在这里输掉 |
| 80 | 写明你愿意承受的那一种错 | 选择必须对应计费表里的一列 |
| 81 | 高波动的周和低波动的周分开 | 先定义波动，再拆误差 |
| 82 | 在高波动周里数线性的跳空 | 要有计数 |
| 83 | 在低波动周里看树是否在背噪声 | 对照更深的那棵树，换到这张表上 |
| 84 | 三类错误、两段波动，放进同一张表 | 这张表取代全文的平均误差 |
| 85 | 用这张表留下一个模型 | 决定只能引用表中的一格 |

## 86 – 100 · 讲给另一个工程师

| 天 | 实战 | 新收走的办法 |
|---|---|---|
| 86 | 十行写清起止日期和来源 | 只看这十行就要能找到同一份数据 |
| 87 | 十行写清每一列为什么能用 | 和程序里的拒绝清单一致 |
| 88 | 换一种启动方式再跑 | 误差对到小数点后两位 |
| 89 | 基准、线性、树并排进讲稿 | 讲稿不许出现程序里没有的数 |
| 90 | 三个失手的日子，每个一句原因 | 原因落到三类错误之一 |
| 91 | 拒绝一个特征，附上前后排名 | 拒绝要有两个数 |
| 92 | 把「如果成交」写成三行假设 | 假设里不出现利润 |
| 93 | 滑点加一个最小单位再排一次 | 排名变了就改讲稿，没变也要写明 |
| 94 | 删掉最得意的月份，重做留下谁的决定 | 决定若翻转，以删掉之后的为准 |
| 95 | 换一只股票走同一个函数 | 改日期和三个失手日，流程不改 |
| 96 | 收成一页：任务、切分、基准、三类错 | 四个标题都在这一页里 |
| 97 | 从这一页列出一个仍然开放的漏洞 | 漏洞要能对应到某一天的修法 |
| 98 | 补上那个漏洞再跑 | 成绩允许变差，变差的数留在讲稿里 |
| 99 | 全流程再跑一次 | 讲稿里的数和这次输出一致 |
| 100 | 对着这一页把失败讲完 | 听众应能复述：数据到哪一天、什么不许用、哪三类错、为什么不下单 |

---

<p align="center"><a href="#zh">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <a href="#en"><b>English</b></a></p>

<a id="en"></a>

# Phase I · Models

Note: [Day 1 · In-sample nearest neighbor and ordinary least squares](day-01.md#en). The remaining days are listed below.

Back to the [front page](../../README.md#en).

## 01 – 10 · Error

| Day | Session | Shortcut removed |
|---|---|---|
| [01　Nearest neighbor and OLS](day-01.md#en) | In-sample nearest neighbor and ordinary least squares | The query lies in the training set. The two estimators sit side by side |
| 02 | Absolute error and squared error | The same miss must be handed in as two numbers. Squaring weighs day 4 more |
| 03 | The five residuals side by side | A single total is no longer enough. Name the day that holds the error |
| 04 | A line through day 1 and day 5 only | A cruder line has to lose to least squares on the miss |
| 05 | Fit again without day 4 | Show how far one point can move the whole line |
| 06 | Ask for day 6 | That day is not in the fit. Memory can only copy a neighbor. The line must extrapolate |
| 07 | Hide day 5 and call it the exam | Error on the fitting days no longer counts |
| 08 | Keep a window of three days and slide it once | The line has to drop the earlier prices |
| 09 | Shuffle the dates and fit again | The score barely moves, so the line is shown not to know time |
| 10 | Score direction, up or down | A small price error can still get the direction wrong. Both scores are due |

## 11 – 25 · Direction

| Day | Session | Shortcut removed |
|---|---|---|
| 11 | Keep only up or down | Distance, including a miss of 8.2, is no longer an answer |
| 12 | Cut return into up and down with one threshold | You choose where the cut sits |
| 13 | Nudge the threshold | Report how sensitive accuracy is to that nudge |
| 14 | Always guess down | A baseline comes first. The model has to beat someone who looks at nothing |
| 15 | Put the two kinds of mistake in separate cells | Calling up down, and calling down up, are counted apart |
| 16 | Emit how much the day looks like an up day | Hand in one more number, between 0 and 1 |
| 17 | Check the days you called 80 percent | Confidence has to match how often those days really rise |
| 18 | Split on return and volume together | The input is no longer a single day's price |
| 19 | Leave volume unscaled | The column with more digits crowds price out. You have to see it |
| 20 | Add a column of pure noise | The score must not improve because of it |
| 21 | Switch to a fixed table of real closes | The numbers are no longer handwritten. Reading twice must match |
| 22 | Guess today from yesterday's direction | Sit it next to a coin-flip baseline |
| 23 | After three days the same way, look at the fourth | The rule is frozen. It cannot be rewritten after the result |
| 24 | Carry that rule into the next stretch of prices | The score cannot be reported on the stretch you picked |
| 25 | Hand in the direction score and the price score together | When they disagree, say which one you trust |

## 26 – 40 · Time

| Day | Session | Shortcut removed |
|---|---|---|
| 26 | Split rows into train and test at random | Keep the flattering score as a control |
| 27 | Split by time instead | The test sits entirely after the train. Print both numbers |
| 28 | Explain today's close with today's high | The script must mark that column forbidden |
| 29 | Standardize with tomorrow's open | Leakage can hide in the preprocessing |
| 30 | Each day may see only a fixed window of the past | The whole history can no longer be fit at once |
| 31 | Shrink the window to three days | The line chases one-day noise. Print that miss on its own |
| 32 | Stretch the window to sixty days | The line is still sitting in older prices. Set it beside day 31 |
| 33 | Estimate mean and variance on the training stretch only | The test stretch may not standardize itself |
| 34 | Fill a missing day from the future, then from the past | Both fills exist. The one that peeks is marked |
| 35 | After dropping halted days, check the gap | Adjacent rows are not adjacent times |
| 36 | An unadjusted jump against the same day, adjusted | A corporate action can be mistaken for a signal. Both errors are due |
| 37 | Mix several stocks, then cut by time again | They share the same day's news. The flattering score has to be visible |
| 38 | Lag the signal by one day | What disappears was simultaneous. What remains might be usable |
| 39 | Subtract one minimum round-trip cost | After that, is the earlier edge still there |
| 40 | For every improvement in this stretch, note whether the future was visible | The score needs a leakage list behind it |

## 41 – 55 · How the miss happens

| Day | Session | Shortcut removed |
|---|---|---|
| 41 | Fit the line again on a longer price history | A jump still moves the whole line. This jump is not handwritten |
| 42 | Ridge, with the slope penalized | The same jump may not move the line as far |
| 43 | Average only the nearby days | A distant jump cannot enter the answer |
| 44 | A shallow tree | It may cut the jump day out on its own |
| 45 | One level deeper | Training gets better and the next stretch gets worse. It is memorizing dates |
| 46 | Line, ridge, and tree on the next stretch | Three fits with similar training error must report which one still lives |
| 47 | Extrapolate the line to a far day | The answer may land outside any reasonable price |
| 48 | Extrapolate the tree to that same day | It only repeats a leaf. The two misses sit side by side |
| 49 | All three on the same jump day | Say who was moved, and who memorized the day |
| 50 | Let the three vote | Find a day when all three are wrong and the vote is wrong too |
| 51 | Features become the last five daily returns | The line's weights are roughly even. Print them |
| 52 | The tree uses the same five days | It will isolate one of them |
| 53 | Change the random seed | The tree's cuts move. The line barely does |
| 54 | Drop volume and run again | Whoever falls more was depending on that column |
| 55 | One sentence each on how the three miss | A single score is no longer accepted |

## 56 – 70 · One small task

| Day | Session | Shortcut removed |
|---|---|---|
| 56 | Freeze the task in one sentence: from the past, guess the next day's return | Table, target, and forbidden columns go into the program before the run |
| 57 | The program refuses today's high, low, and close | A forbidden column must fail the run, not get used quietly |
| 58 | Split by year | The split is frozen. Row numbers do not decide it |
| 59 | The baseline always guesses a return of 0 | The model has to sit beside the baseline |
| 60 | Line minus baseline | The bit you win has to land on particular days |
| 61 | Tree minus the same baseline | Same table and same split as day 60 |
| 62 | Score error only on the most confident tenth of days | The other nine tenths cannot be used to flatter the average |
| 63 | Split error by month | Find whether one month carries the year |
| 64 | Delete that month and score again | The conclusion counts only if it is still there |
| 65 | Switch to a second stock | The procedure does not change. The first stock's conclusion does not travel |
| 66 | Turn return into excess over the market | What must be explained is the part beyond the market |
| 67 | Shift the market column forward by one day | A score that improves because of that shift is marked void |
| 68 | Fold the procedure into one function | A second table must enter through the same door |
| 69 | Write the fill assumption | Fill at the close, no slippage. The assumption is part of the output |
| 70 | Tell the task in ten lines | Every number in the telling has to be findable in the output |

## 71 – 85 · Costly mistakes

| Day | Session | Shortcut removed |
|---|---|---|
| 71 | Split misses into jumps, quiet days, and wrong direction | Three counts replace one error |
| 72 | Look only at quiet days | A small error has to be said as "these days were easy" |
| 73 | Count only the days the direction was wrong | That count may rank models differently from average error |
| 74 | Classify the five largest errors | If they are the same kind, the average is that kind speaking |
| 75 | Charge 1 for a wrong direction and 3 for a jump day | When the tariff changes, the ranking may flip |
| 76 | Missing a large drop, against flagging a small rise | The two mistakes get two columns |
| 77 | Raise the threshold and speak only when more sure | Fewer calls. The remaining calls are charged on their own |
| 78 | Lower the threshold and speak almost every day | The average looks mild and the expensive mistakes remain. Both tables sit together |
| 79 | Rerank the line and the tree under the new tariff | The winner on average error can lose here |
| 80 | Name the mistake you are willing to carry | The choice has to point at one column of the tariff |
| 81 | Separate high-volatility weeks from low ones | Define volatility first, then split the error |
| 82 | In the high-volatility weeks, count the line's jumps | The count has to be there |
| 83 | In the low-volatility weeks, see whether the tree is memorizing noise | Set it against the deeper tree, on this table |
| 84 | Three mistakes and two volatility regimes, one count table | This table replaces the average error for the rest of the season |
| 85 | Keep one model by citing that table | The decision may cite only one cell |

## 86 – 100 · Tell another engineer

| Day | Session | Shortcut removed |
|---|---|---|
| 86 | Ten lines for the start date, end date, and source | Those ten lines alone must locate the same data |
| 87 | Ten lines for why each column is allowed | This matches the program's refusal list |
| 88 | Run it a second way | The error matches to two decimal places |
| 89 | Baseline, line, and tree side by side in the telling | The telling may not contain a number the program did not print |
| 90 | Three missed days, one cause each | Each cause is one of the three mistake kinds |
| 91 | Refuse one feature and attach the ranking before and after | A refusal needs two numbers |
| 92 | Write "if this were filled" as three lines of assumption | Profit does not appear in the assumption |
| 93 | Add one minimum unit of slippage and rank again | If the ranking moves, the telling changes. If it does not, say so |
| 94 | Delete the favorite month and remake the keep-or-drop decision | If the decision flips, the later one stands |
| 95 | Another stock, the same function | Dates and the three missed days change. The procedure does not |
| 96 | One page: task, split, baseline, three mistakes | All four headings are on that page |
| 97 | From that page, name one hole still open | The hole has to point at a day's repair |
| 98 | Close that hole and run again | The score may get worse. The worse number stays in the telling |
| 99 | Run the whole procedure once more | The numbers in the telling match this output |
| 100 | Tell the failure from that page | A listener can repeat: through which date, what is forbidden, which three mistakes, and why there is no order |
