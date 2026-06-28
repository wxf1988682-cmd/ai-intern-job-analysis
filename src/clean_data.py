"""
clean_data.py

用于对岗位数据进行清洗，包括读取原始数据、去重、缺失值处理、
字段规范化和技能关键词提取。
"""

from pathlib import Path

import pandas as pd


# 项目根目录
BASE_DIR = Path(__file__).resolve().parent.parent

# 原始数据路径
RAW_DATA_PATH = BASE_DIR / "data" / "raw" / "jobs_raw.csv"

# 清洗后数据路径
PROCESSED_DATA_PATH = BASE_DIR / "data" / "processed" / "jobs_cleaned.csv"


def extract_skills(description: str) -> str:
    """
    从岗位描述中提取常见技能关键词。

    参数:
        description: 岗位描述文本

    返回:
        用逗号连接的技能关键词字符串
    """
    skill_keywords = [
        "Python",
        "Pandas",
        "Numpy",
        "爬虫",
        "requests",
        "BeautifulSoup",
        "MySQL",
        "SQL",
        "机器学习",
        "PyTorch",
        "sklearn",
        "AIGC",
        "Excel",
        "Matplotlib",
        "Seaborn",
        "数据清洗",
        "数据分析",
        "可视化",
        "技术文档",
    ]

    matched_skills = []

    for skill in skill_keywords:
        if skill.lower() in description.lower():
            matched_skills.append(skill)

    return ",".join(matched_skills)


def clean_job_data():
    """
    清洗岗位数据的主函数。
    """
    print("Start cleaning job data...")

    # 1. 读取原始数据
    df = pd.read_csv(RAW_DATA_PATH, encoding="utf-8")

    print("原始数据预览：")
    print(df.head())

    # 2. 删除重复数据
    df = df.drop_duplicates()

    # 3. 删除岗位名称或岗位描述为空的数据
    df = df.dropna(subset=["job_title", "job_description"])

    # 4. 去除文本字段前后的空格
    text_columns = [
        "job_title",
        "company",
        "city",
        "salary",
        "education",
        "experience",
        "job_description",
    ]

    for col in text_columns:
        df[col] = df[col].astype(str).str.strip()

    # 5. 提取技能关键词
    df["skills"] = df["job_description"].apply(extract_skills)

    # 6. 保存清洗后的数据
    df.to_csv(PROCESSED_DATA_PATH, index=False, encoding="utf-8-sig")

    print("数据清洗完成！")
    print(f"清洗后数据已保存到：{PROCESSED_DATA_PATH}")


if __name__ == "__main__":
    clean_job_data()