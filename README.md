<p align="center"><b>中文</b> &nbsp;&nbsp;·&nbsp;&nbsp; <a href="README.en.md">English</a></p>

<h1 align="center">观测席</h1>

<p align="center">价格研究，分四阶段推进。每一阶段一百日，每日一次可复现的计算。</p>

<br>

查询 `x = 4`，位于训练集内。

| | 最近邻 | 普通最小二乘 |
|---|---:|---:|
| 样本内残差 | 0 | 8.2 |
| 输出 | 20.0 | 11.79 |

<p align="center">拟合 &nbsp; <code>ŷ = 3.27x − 1.29</code></p>

<p align="center">
<a href="docs/season-01/day-01.md">第 1 日说明</a>
&nbsp;&nbsp;·&nbsp;&nbsp;
<a href="days/01-line-that-misses/fit_line.py">实现</a>
&nbsp;&nbsp;·&nbsp;&nbsp;
<a href="site">曲线</a>
</p>

## 复现

Python 3.8 及以上，于仓库根目录执行。

```bash
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
python days/01-line-that-misses/fit_line.py
```

曲线页在 [`site`](site)。进入该目录后执行 `npm install`，再执行 `npm run dev`。

## 阶段

| 阶段 | 主题 |
|---|---|
| 第一阶段 | [**模型**](docs/season-01) |
| 第二阶段 | **因子** |
| 第三阶段 | **组合与约束** |
| 第四阶段 | **执行** |

<p align="right"><sub>2019 年笔记见 <a href="archive/2019">archive/2019</a></sub></p>
