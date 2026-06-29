import pandas as pd
from collections import Counter


def load_data(file_path):
    """
    读取清洗后的岗位数据
    """
    df = pd.read_csv(file_path)
    return df


def analyze_basic_info(df):
    """
    分析数据基本信息
    """
    print("=" * 50)
    print("一、数据基本信息")
    print("=" * 50)

    print("岗位数据总行数：", df.shape[0])
    print("岗位数据总列数：", df.shape[1])

    print("\n字段名称：")
    print(df.columns.tolist())

    print("\n前5行数据：")
    print(df.head())


def analyze_city_distribution(df):
    """
    统计不同城市的岗位数量
    """
    print("\n" + "=" * 50)
    print("二、城市岗位数量分布")
    print("=" * 50)

    city_counts = df["location"].value_counts()

    print(city_counts)

    return city_counts


def classify_job_type(job_title):
    """
    根据岗位名称，简单判断岗位方向

    注意：
    这是一个基础版本，不是机器学习分类。
    它的本质是关键词规则判断。
    """

    title = str(job_title).lower()

    if "aigc" in title or "prompt" in title or "大模型" in title:
        return "AIGC/AI应用方向"
    elif "数据分析" in title or "数据处理" in title or "data" in title:
        return "Python数据分析/数据处理方向"
    elif "爬虫" in title or "采集" in title or "crawler" in title:
        return "Python爬虫/数据采集方向"
    elif "机器学习" in title or "算法" in title or "machine learning" in title:
        return "机器学习基础方向"
    elif "python" in title:
        return "Python开发方向"
    else:
        return "其他方向"


def analyze_job_type_distribution(df):
    """
    统计不同岗位方向的数量
    """
    print("\n" + "=" * 50)
    print("三、岗位方向数量分布")
    print("=" * 50)

    df["job_type"] = df["job_title"].apply(classify_job_type)

    job_type_counts = df["job_type"].value_counts()

    print(job_type_counts)

    return job_type_counts


def analyze_skill_frequency(df):
    """
    统计 skills 字段中各技能关键词出现次数
    """
    print("\n" + "=" * 50)
    print("四、技能关键词出现频率")
    print("=" * 50)

    all_skills = []

    for skills in df["skills"]:
        if pd.isna(skills):
            continue

        skill_list = str(skills).split(";")

        for skill in skill_list:
            skill = skill.strip()
            if skill:
                all_skills.append(skill)

    skill_counts = Counter(all_skills)

    skill_counts_series = pd.Series(skill_counts).sort_values(ascending=False)

    print(skill_counts_series)

    return skill_counts_series


def main():
    """
    主函数：负责组织整个分析流程
    """

    file_path = "data/processed/jobs_cleaned.csv"

    df = load_data(file_path)

    analyze_basic_info(df)

    analyze_city_distribution(df)

    analyze_job_type_distribution(df)

    analyze_skill_frequency(df)


if __name__ == "__main__":
    main()