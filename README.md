# 基于 Python 的 AI 实习岗位信息爬取与数据分析系统

## 一、项目简介

本项目面向 AI 实习、Python 开发、数据处理、AIGC 等方向的岗位信息，使用 Python 对岗位数据进行采集、清洗、分析和可视化，最终总结当前实习岗位中常见的技能要求、城市分布、岗位类型和能力需求。

项目的主要目标是通过真实岗位数据，分析 AI / Python / 数据处理方向实习生需要掌握的核心技能，并将分析结果用于个人实习求职准备和简历优化。

## 二、项目背景

作为一名数学与计算机交叉专业的本科生，我希望在暑期寻找 AI 应用、Python 数据处理或数据分析相关实习。但在准备实习初期，我对不同岗位的技能要求、工具要求和项目要求还不够清晰。

因此，本项目尝试通过 Python 对招聘岗位信息进行整理和分析，帮助自己明确学习重点，例如 Python、Pandas、Numpy、爬虫、MySQL、机器学习基础、PyTorch、AIGC 工具和技术文档整理等能力。

## 三、项目功能

本项目计划实现以下功能：

1. 采集 AI 实习、Python 开发、数据处理等相关岗位信息；
2. 对岗位名称、公司、城市、薪资、学历要求、技能关键词等字段进行清洗；
3. 统计岗位中出现频率较高的技能要求；
4. 分析不同城市、不同岗位方向的岗位分布情况；
5. 通过图表展示技能词频、岗位城市分布、薪资范围等结果；
6. 总结适合本科生准备实习的技能路线。

## 四、技术栈

* Python
* requests
* BeautifulSoup
* Pandas
* Numpy
* Matplotlib
* Seaborn
* Jupyter Notebook
* Git / GitHub

## 五、项目目录结构

```text
ai-intern-job-analysis/
│
├── README.md
├── requirements.txt
├── .gitignore
│
├── data/
│   ├── raw/
│   │   └── jobs_raw.csv
│   └── processed/
│       └── jobs_cleaned.csv
│
├── src/
│   ├── crawler.py
│   ├── clean_data.py
│   ├── analysis.py
│   └── visualization.py
│
├── notebooks/
│   └── analysis_demo.ipynb
│
├── outputs/
│   └── figures/
│       ├── skill_frequency.png
│       ├── city_distribution.png
│       └── salary_distribution.png
│
└── docs/
    └── resume_project_draft.md
```

## 六、当前进度

* [x] 完成项目选题
* [x] 完成项目目录结构设计
* [x] 完成 README 初稿
* [ ] 完成岗位数据采集
* [ ] 完成数据清洗
* [ ] 完成技能关键词统计
* [ ] 完成数据可视化
* [ ] 完成项目总结文档

## 七、预期分析结果

本项目计划输出以下分析结果：

1. AI / Python / 数据处理实习岗位高频技能词；
2. 不同岗位方向的能力要求对比；
3. 岗位城市分布情况；
4. 实习岗位薪资范围分布；
5. 面向本科生的实习准备建议。

## 八、项目价值

通过本项目，我能够系统练习 Python 数据处理流程，包括数据采集、数据清洗、数据分析、数据可视化和项目文档整理。同时，该项目也可以帮助我更清楚地了解 AI / Python / 数据处理方向实习岗位的真实要求，并为后续简历投递和面试准备提供依据。

## 九、后续计划

接下来将继续完善以下内容：

1. 编写岗位信息采集脚本；
2. 整理岗位数据字段；
3. 使用 Pandas 进行数据清洗；
4. 提取岗位描述中的技能关键词；
5. 使用 Matplotlib / Seaborn 进行可视化分析；
6. 完善 GitHub 项目文档；
7. 将项目整理为简历项目经历。
