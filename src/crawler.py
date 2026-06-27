"""
crawler.py

用于采集 AI 实习、Python 开发、数据处理等岗位信息。
第一阶段可以先使用手动整理的岗位数据，后续再逐步完善爬虫逻辑。
"""


def crawl_jobs():
    """
    采集岗位信息的主函数。

    后续计划采集字段：
    - job_title: 岗位名称
    - company: 公司名称
    - city: 城市
    - salary: 薪资
    - education: 学历要求
    - experience: 经验要求
    - job_description: 岗位描述
    - skills: 技能关键词
    """
    print("Start crawling job information...")


if __name__ == "__main__":
    crawl_jobs()