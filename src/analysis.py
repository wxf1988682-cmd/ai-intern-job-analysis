"""
analysis.py

用于分析 AI / Python / 数据处理方向实习岗位数据，包括：
1. 技能关键词频率统计
2. 城市岗位数量统计
3. 岗位类型统计
"""

from pathlib import Path
from collections import Counter

import pandas as pd


# 项目根目录
BASE_DIR = Path(__file__).resolve().parent.parent

# 清洗后数据路径
CLEANED_DATA_PATH = BASE_DIR / "data" / "processed" / "jobs_cleaned.csv"

# 分析结果输出目录
REPORT_DIR = BASE_DIR / "outputs" / "reports"


def analyze_skill_frequency(df: pd.DataFrame) -> pd.DataFrame:
    """
    统计岗位中技能关键词出现频率。
    """
    skill_counter = Counter()

    for skills in df["skills"].dropna():
        skill_list = str(skills).split(",")

        for skill in skill_list:
            skill = skill.strip()
            if skill:
                skill_counter[skill] += 1

    skill_df = pd.DataFrame(
        skill_counter.items(),
        columns=["skill", "frequency"]
    )

    skill_df = skill_df.sort_values(
        by="frequency",
        ascending=False
    )

    return skill_df


def analyze_city_distribution(df: pd.DataFrame) -> pd.DataFrame:
    """
    统计不同城市的岗位数量。
    """
    city_df = df["city"].value_counts().reset_index()
    city_df.columns = ["city", "job_count"]

    return city_df


def classify_job_type(job_title: str) -> str:
    """
    根据岗位名称粗略划分岗位类型。
    """
    if "AI" in job_title or "AIGC" in job_title:
        return "AI/AIGC方向"
    elif "Python" in job_title:
        return "Python开发/数据分析方向"
    elif "数据" in job_title:
        return "数据处理/数据分析方向"
    elif "机器学习" in job_title:
        return "机器学习方向"
    elif "爬虫" in job_title:
        return "爬虫/数据采集方向"
    else:
        return "其他方向"


def analyze_job_type_distribution(df: pd.DataFrame) -> pd.DataFrame:
    """
    统计岗位类型分布。
    """
    df["job_type"] = df["job_title"].apply(classify_job_type)

    job_type_df = df["job_type"].value_counts().reset_index()
    job_type_df.columns = ["job_type", "job_count"]

    return job_type_df


def analyze_jobs():
    """
    岗位数据分析主函数。
    """
    print("Start analyzing job data...")

    # 确保输出目录存在
    REPORT_DIR.mkdir(parents=True, exist_ok=True)

    # 读取清洗后的数据
    df = pd.read_csv(CLEANED_DATA_PATH, encoding="utf-8-sig")

    print("清洗后数据预览：")
    print(df.head())

    # 1. 技能频率分析
    skill_df = analyze_skill_frequency(df)
    skill_output_path = REPORT_DIR / "skill_frequency.csv"
    skill_df.to_csv(skill_output_path, index=False, encoding="utf-8-sig")

    print("\n技能关键词频率统计：")
    print(skill_df)

    # 2. 城市分布分析
    city_df = analyze_city_distribution(df)
    city_output_path = REPORT_DIR / "city_distribution.csv"
    city_df.to_csv(city_output_path, index=False, encoding="utf-8-sig")

    print("\n城市岗位数量分布：")
    print(city_df)

    # 3. 岗位类型分析
    job_type_df = analyze_job_type_distribution(df)
    job_type_output_path = REPORT_DIR / "job_type_distribution.csv"
    job_type_df.to_csv(job_type_output_path, index=False, encoding="utf-8-sig")

    print("\n岗位类型分布：")
    print(job_type_df)

    print("\n岗位数据分析完成！")
    print(f"分析结果已保存到：{REPORT_DIR}")


if __name__ == "__main__":
    analyze_jobs()