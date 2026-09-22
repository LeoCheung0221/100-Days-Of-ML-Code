<p align="center"><a href="#zh"><b>中文</b></a> &nbsp;&nbsp;·&nbsp;&nbsp; <a href="#en">English</a></p>

<a id="zh"></a>

<h1 align="center">观测席</h1>

<p align="center">价格研究，分四阶段推进。每一阶段一百日，每日一次可复现的计算。</p>

<p align="center">
<a href="#phase-1"><b>第一阶段 · 模型</b></a>
&emsp;&emsp;
<b>第二阶段 · 因子</b>
&emsp;&emsp;
<b>第三阶段 · 组合与约束</b>
&emsp;&emsp;
<b>第四阶段 · 执行</b>
</p>

---

<a id="phase-1"></a>

## 第一阶段 · 模型

每日的计算写在当日文档里。这里只列标题。第 1 日已可运行。

### 01 – 10

- [**01**　最近邻与普通最小二乘](docs/season-01/day-01.md)
- **02**　绝对误差与平方误差
- **03**　五天残差并排
- **04**　端点连线
- **05**　去掉第四日再拟合
- **06**　训练支撑外的查询
- **07**　留出第五日
- **08**　三日窗口
- **09**　打乱日期
- **10**　涨跌方向

### 11 – 20

- **11**　涨跌标签
- **12**　阈值
- **13**　阈值灵敏度
- **14**　常数基准
- **15**　两类误分
- **16**　上涨程度
- **17**　置信核对
- **18**　涨幅与成交量
- **19**　未缩放的成交量
- **20**　噪声列

### 21 – 30

- **21**　固定收盘表
- **22**　滞后一日的方向
- **23**　连续三日同向
- **24**　规则移到下一段
- **25**　方向与价格并报
- **26**　随机切分
- **27**　按时间切分
- **28**　当日最高价
- **29**　用未来开盘标准化
- **30**　固定历史窗口

### 31 – 40

- **31**　三日窗口的噪声
- **32**　六十日窗口
- **33**　训练集标准化
- **34**　缺失的两种填法
- **35**　停牌后的间隔
- **36**　复权与未复权
- **37**　多标的混切
- **38**　信号滞后一日
- **39**　最小往返成本
- **40**　泄漏清单

### 41 – 50

- **41**　更长样本上的直线
- **42**　岭回归
- **43**　局部平均
- **44**　浅层树
- **45**　更深的树
- **46**　三种拟合换样本
- **47**　线性外推
- **48**　树不外推
- **49**　同一跳空日
- **50**　三模型投票

### 51 – 60

- **51**　五日收益的线性权重
- **52**　五日收益上的树
- **53**　随机种子
- **54**　去掉成交量
- **55**　三种失手
- **56**　下一日收益
- **57**　拒绝当日价格
- **58**　按年切分
- **59**　零收益基准
- **60**　线性相对基准

### 61 – 70

- **61**　树相对基准
- **62**　最高置信的十分之一
- **63**　按月残差
- **64**　去掉主导月份
- **65**　第二只股票
- **66**　超额收益
- **67**　市场列前移
- **68**　单一入口
- **69**　成交假设
- **70**　十行任务

### 71 – 80

- **71**　三类残差
- **72**　平静日
- **73**　方向错误的天数
- **74**　最大的五笔残差
- **75**　差异化计费
- **76**　漏报与误报
- **77**　提高阈值
- **78**　降低阈值
- **79**　计费后重排
- **80**　可承受的错误

### 81 – 90

- **81**　波动分段
- **82**　高波动周的跳空
- **83**　低波动周的树
- **84**　残差计数表
- **85**　按表保留模型
- **86**　样本区间与来源
- **87**　列的可用性
- **88**　再次复现
- **89**　基准、线性、树并排
- **90**　三个失手日

### 91 – 100

- **91**　拒绝一个特征
- **92**　成交假设三行
- **93**　最小滑点
- **94**　去掉最优月份
- **95**　换股票，同一函数
- **96**　一页说明
- **97**　一处仍开放
- **98**　补上该处
- **99**　全流程再运行
- **100**　讲完这次失败

---

<p align="right"><sub>2019 年笔记见 <a href="archive/2019">archive/2019</a></sub></p>

---

<a id="en"></a>

<p align="center"><a href="#zh">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <a href="#en"><b>English</b></a></p>

<h1 align="center">Observation Deck</h1>

<p align="center">A price study in four phases. One hundred days in each phase. One reproducible calculation each day.</p>

<p align="center">
<a href="#phase-1-en"><b>Phase I · Models</b></a>
&emsp;&emsp;
<b>Phase II · Factors</b>
&emsp;&emsp;
<b>Phase III · Portfolio and constraints</b>
&emsp;&emsp;
<b>Phase IV · Execution</b>
</p>

---

<a id="phase-1-en"></a>

## Phase I · Models

Each day's calculation is in its own note. Only the titles are listed here. Day 1 runs.

### 01 – 10

- [**01**　Nearest neighbor and OLS](docs/season-01/day-01.md#en)
- **02**　Absolute and squared error
- **03**　Residuals, point by point
- **04**　The chord through the endpoints
- **05**　Refit without day 4
- **06**　A query off the training support
- **07**　Hold out day 5
- **08**　A three-day window
- **09**　Shuffle the dates
- **10**　Up or down

### 11 – 20

- **11**　Direction labels
- **12**　A threshold
- **13**　Threshold sensitivity
- **14**　A constant baseline
- **15**　Two kinds of misclassification
- **16**　Degree of being up
- **17**　A check on stated confidence
- **18**　Return and volume
- **19**　Unscaled volume
- **20**　A noise column

### 21 – 30

- **21**　A fixed close table
- **22**　Yesterday's direction
- **23**　Three days the same way
- **24**　The rule on the next stretch
- **25**　Direction and price together
- **26**　A random split
- **27**　A split by time
- **28**　Today's high
- **29**　Standardize with a future open
- **30**　A fixed lookback

### 31 – 40

- **31**　Noise in a three-day window
- **32**　A sixty-day window
- **33**　Standardize on the training stretch
- **34**　Two ways to fill a gap
- **35**　Gaps after a halt
- **36**　Adjusted and unadjusted
- **37**　Several names, mixed split
- **38**　Lag the signal one day
- **39**　A minimum round trip
- **40**　A leakage list

### 41 – 50

- **41**　The line on a longer sample
- **42**　Ridge
- **43**　A local average
- **44**　A shallow tree
- **45**　A deeper tree
- **46**　Three fits, next sample
- **47**　Linear extrapolation
- **48**　A tree does not extrapolate
- **49**　One jump, three models
- **50**　A vote of three

### 51 – 60

- **51**　Linear weights on five returns
- **52**　A tree on the same five
- **53**　The random seed
- **54**　Drop volume
- **55**　Three ways of missing
- **56**　Next-day return
- **57**　Refuse today's prices
- **58**　Split by year
- **59**　A zero-return baseline
- **60**　The line against the baseline

### 61 – 70

- **61**　The tree against the baseline
- **62**　The most confident tenth
- **63**　Residuals by month
- **64**　Drop the month that carries the year
- **65**　A second name
- **66**　Excess return
- **67**　Shift the market column
- **68**　One entry point
- **69**　The fill assumption
- **70**　The task in ten lines

### 71 – 80

- **71**　Three residual classes
- **72**　Quiet days
- **73**　Days the direction was wrong
- **74**　The five largest residuals
- **75**　A tariff on mistakes
- **76**　A miss and a false alarm
- **77**　A higher threshold
- **78**　A lower threshold
- **79**　Rank again under the tariff
- **80**　The mistake you will carry

### 81 – 90

- **81**　Split by volatility
- **82**　Jumps in high-volatility weeks
- **83**　The tree in quiet weeks
- **84**　A residual count
- **85**　Keep a model by that count
- **86**　Span and source
- **87**　Which columns are allowed
- **88**　Reproduce again
- **89**　Baseline, line, and tree
- **90**　Three missed days

### 91 – 100

- **91**　Refuse one feature
- **92**　Three lines on the fill
- **93**　One unit of slippage
- **94**　Drop the best month
- **95**　Another name, same function
- **96**　One page
- **97**　One hole still open
- **98**　Close that hole
- **99**　Run the whole path again
- **100**　Tell the failure

---

<p align="right"><sub>Notes from 2019 are in <a href="archive/2019">archive/2019</a></sub></p>
