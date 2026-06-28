"""
岗位数据清洗模块 clean_data.py

功能：
1. 读取 data/raw/jobs_raw.csv 原始岗位数据
2. 查看数据基本情况
3. 删除重复岗位
4. 处理缺失值
5. 从岗位描述中提取技能关键词
6. 保存清洗后的数据到 data/processed/jobs_cleaned.csv
"""

import pandas as pd


RAW_DATA_PATH = "data/raw/jobs_raw.csv"
CLEANED_DATA_PATH = "data/processed/jobs_cleaned.csv"


SKILL_KEYWORDS = [
    "Python",
    "Pandas",
    "Numpy",
    "爬虫",
    "MySQL",
    "机器学习",
    "PyTorch",
    "AIGC",
    "Excel",
    "可视化",
    "技术文档",
    "requests",
    "BeautifulSoup",
    "Prompt"
]


def load_data(file_path):
    """
    读取 CSV 文件
    """
    df = pd.read_csv(file_path)
    return df


def show_basic_info(df):
    """
    查看数据基本信息
    """
    print("数据前 5 行：")
    print(df.head())

    print("\n数据行列数：")
    print(df.shape)

    print("\n字段信息：")
    print(df.info())

    print("\n缺失值统计：")
    print(df.isnull().sum())


def remove_duplicates(df):
    """
    删除重复数据
    """
    before_count = len(df)
    df = df.drop_duplicates()
    after_count = len(df)

    print(f"\n去重前数据量：{before_count}")
    print(f"去重后数据量：{after_count}")
    print(f"删除重复数据量：{before_count - after_count}")

    return df


def handle_missing_values(df):
    """
    处理缺失值
    """
    df["job_title"] = df["job_title"].fillna("未知岗位")
    df["company"] = df["company"].fillna("未知公司")
    df["location"] = df["location"].fillna("未知地点")
    df["salary"] = df["salary"].fillna("薪资面议")
    df["education"] = df["education"].fillna("不限")
    df["experience"] = df["experience"].fillna("不限")
    df["job_description"] = df["job_description"].fillna("")
    df["source"] = df["source"].fillna("未知来源")
    df["publish_date"] = df["publish_date"].fillna("未知日期")

    return df


def extract_skills(job_description):
    """
    从岗位描述中提取技能关键词

    参数：
    job_description: 岗位描述文本

    返回：
    命中的技能关键词，用逗号连接
    """
    matched_skills = []

    for skill in SKILL_KEYWORDS:
        if skill.lower() in job_description.lower():
            matched_skills.append(skill)

    return ",".join(matched_skills)


def clean_data():
    """
    数据清洗主函数
    """
    print("开始读取原始岗位数据...")

    df = load_data(RAW_DATA_PATH)

    print("\n====== 原始数据基本信息 ======")
    show_basic_info(df)

    print("\n====== 开始删除重复数据 ======")
    df = remove_duplicates(df)

    print("\n====== 开始处理缺失值 ======")
    df = handle_missing_values(df)

    print("\n====== 开始提取技能关键词 ======")
    df["skills"] = df["job_description"].apply(extract_skills)

    print("\n====== 清洗后数据预览 ======")
    print(df.head())

    df.to_csv(CLEANED_DATA_PATH, index=False, encoding="utf-8-sig")

    print(f"\n清洗后的数据已保存到：{CLEANED_DATA_PATH}")


if __name__ == "__main__":
    clean_data()