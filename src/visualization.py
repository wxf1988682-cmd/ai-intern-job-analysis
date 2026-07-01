import os
from collections import Counter

import pandas as pd
import matplotlib.pyplot as plt


# 设置中文字体，避免图表中文乱码
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False


DATA_PATH = "data/processed/jobs_cleaned.csv"
FIGURE_DIR = "outputs/figures"


def load_data(file_path):
    """
    读取清洗后的岗位数据
    """
    df = pd.read_csv(file_path)
    return df


def classify_job_type(job_title):
    """
    根据岗位名称初步判断岗位方向
    """
    title = str(job_title)

    if "AIGC" in title or "大模型" in title or "Prompt" in title:
        return "AIGC"
    elif "AI" in title or "人工智能" in title:
        return "AI应用"
    elif "数据分析" in title or "数据处理" in title:
        return "数据分析/数据处理"
    elif "Python" in title:
        return "Python开发"
    elif "爬虫" in title or "数据采集" in title:
        return "爬虫/数据采集"
    elif "机器学习" in title or "算法" in title:
        return "机器学习基础"
    else:
        return "其他"


def get_job_type_counts(df):
    """
    统计岗位方向数量
    """
    df["job_type"] = df["job_title"].apply(classify_job_type)
    job_type_counts = df["job_type"].value_counts()
    return job_type_counts


def get_city_counts(df):
    """
    统计城市岗位数量
    """
    city_counts = df["location"].value_counts()
    return city_counts


def get_skill_counts(df):
    """
    统计技能关键词出现频率
    """
    all_skills = []

    for skills in df["skills"].dropna():
        skill_list = str(skills).split(",")
        for skill in skill_list:
            skill = skill.strip()
            if skill:
                all_skills.append(skill)

    skill_counts = Counter(all_skills)
    return skill_counts


def plot_city_distribution(city_counts):
    """
    绘制城市岗位数量分布柱状图
    """
    plt.figure(figsize=(8, 5))
    plt.bar(city_counts.index, city_counts.values)
    plt.title("城市岗位数量分布")
    plt.xlabel("城市")
    plt.ylabel("岗位数量")
    plt.xticks(rotation=45)
    plt.tight_layout()

    save_path = os.path.join(FIGURE_DIR, "city_distribution.png")
    plt.savefig(save_path, dpi=300)
    plt.close()


def plot_job_type_distribution(job_type_counts):
    """
    绘制岗位方向数量分布柱状图
    """
    plt.figure(figsize=(8, 5))
    plt.bar(job_type_counts.index, job_type_counts.values)
    plt.title("岗位方向数量分布")
    plt.xlabel("岗位方向")
    plt.ylabel("岗位数量")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()

    save_path = os.path.join(FIGURE_DIR, "job_type_distribution.png")
    plt.savefig(save_path, dpi=300)
    plt.close()


def plot_skill_frequency(skill_counts, top_n=15):
    """
    绘制技能关键词出现频率 Top N 柱状图
    """
    top_skills = skill_counts.most_common(top_n)
    skills = [item[0] for item in top_skills]
    counts = [item[1] for item in top_skills]

    plt.figure(figsize=(10, 5))
    plt.bar(skills, counts)
    plt.title(f"技能关键词出现频率 Top {top_n}")
    plt.xlabel("技能关键词")
    plt.ylabel("出现次数")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()

    save_path = os.path.join(FIGURE_DIR, "skill_frequency.png")
    plt.savefig(save_path, dpi=300)
    plt.close()


def plot_job_type_ratio(job_type_counts):
    """
    绘制岗位类型占比饼图
    """
    plt.figure(figsize=(7, 7))
    plt.pie(
        job_type_counts.values,
        labels=job_type_counts.index,
        autopct="%1.1f%%",
        startangle=90
    )
    plt.title("岗位类型占比")
    plt.tight_layout()

    save_path = os.path.join(FIGURE_DIR, "job_type_ratio.png")
    plt.savefig(save_path, dpi=300)
    plt.close()


def main():
    """
    主函数：读取数据并生成所有可视化图表
    """
    os.makedirs(FIGURE_DIR, exist_ok=True)

    df = load_data(DATA_PATH)

    city_counts = get_city_counts(df)
    job_type_counts = get_job_type_counts(df)
    skill_counts = get_skill_counts(df)

    plot_city_distribution(city_counts)
    plot_job_type_distribution(job_type_counts)
    plot_skill_frequency(skill_counts)
    plot_job_type_ratio(job_type_counts)

    print("可视化图表已生成，保存路径：outputs/figures/")


if __name__ == "__main__":
    main()