import os
from collections import Counter

import pandas as pd
import matplotlib.pyplot as plt


# =========================
# 1. 解决中文显示问题
# =========================

plt.rcParams["font.sans-serif"] = ["Microsoft YaHei"]
plt.rcParams["axes.unicode_minus"] = False


# =========================
# 2. 路径设置
# =========================

DATA_PATH = "data/processed/jobs_cleaned.csv"
FIGURE_DIR = "outputs/figures"


# =========================
# 3. 岗位类型分类函数
# =========================

def classify_job_type(job_title):
    """
    根据岗位名称中的关键词，粗略判断岗位方向。
    """

    job_title = str(job_title)

    if "AIGC" in job_title or "AI应用" in job_title or "AI 产品" in job_title:
        return "AI应用/AIGC"
    elif "数据分析" in job_title or "数据处理" in job_title:
        return "数据分析/数据处理"
    elif "爬虫" in job_title or "数据采集" in job_title:
        return "爬虫/数据采集"
    elif "机器学习" in job_title or "算法" in job_title:
        return "机器学习基础"
    elif "Python" in job_title:
        return "Python开发"
    else:
        return "其他"


# =========================
# 4. 绘制城市岗位数量分布图
# =========================

def plot_city_distribution(df):
    """
    统计不同城市的岗位数量，并绘制柱状图。
    """

    city_counts = df["location"].value_counts()

    plt.figure(figsize=(10, 6))
    plt.bar(city_counts.index, city_counts.values)

    plt.title("城市岗位数量分布")
    plt.xlabel("城市")
    plt.ylabel("岗位数量")
    plt.xticks(rotation=45)

    plt.tight_layout()

    save_path = os.path.join(FIGURE_DIR, "city_distribution.png")
    plt.savefig(save_path, dpi=300)
    plt.close()

    print(f"城市岗位数量分布图已保存：{save_path}")


# =========================
# 5. 绘制岗位方向数量分布图
# =========================

def plot_job_type_distribution(df):
    """
    根据岗位名称判断岗位方向，并绘制岗位方向数量分布柱状图。
    """

    df["job_type"] = df["job_title"].apply(classify_job_type)
    job_type_counts = df["job_type"].value_counts()

    plt.figure(figsize=(10, 6))
    plt.bar(job_type_counts.index, job_type_counts.values)

    plt.title("岗位方向数量分布")
    plt.xlabel("岗位方向")
    plt.ylabel("岗位数量")
    plt.xticks(rotation=30)

    plt.tight_layout()

    save_path = os.path.join(FIGURE_DIR, "job_type_distribution.png")
    plt.savefig(save_path, dpi=300)
    plt.close()

    print(f"岗位方向数量分布图已保存：{save_path}")


# =========================
# 6. 绘制技能关键词频率图
# =========================

def plot_skill_frequency(df):
    """
    拆分 skills 字段，统计技能关键词出现次数，并绘制柱状图。
    """

    all_skills = []

    for skills in df["skills"].dropna():
        skill_list = str(skills).split(",")
        for skill in skill_list:
            skill = skill.strip()
            if skill:
                all_skills.append(skill)

    skill_counts = Counter(all_skills)

    # 取出现次数最多的前 15 个技能
    top_skills = skill_counts.most_common(15)

    skills = [item[0] for item in top_skills]
    counts = [item[1] for item in top_skills]

    plt.figure(figsize=(12, 6))
    plt.bar(skills, counts)

    plt.title("技能关键词出现频率 Top 15")
    plt.xlabel("技能关键词")
    plt.ylabel("出现次数")
    plt.xticks(rotation=45)

    plt.tight_layout()

    save_path = os.path.join(FIGURE_DIR, "skill_frequency.png")
    plt.savefig(save_path, dpi=300)
    plt.close()

    print(f"技能关键词频率图已保存：{save_path}")


# =========================
# 7. 主函数
# =========================

def main():
    """
    主函数：读取清洗后的岗位数据，并生成三张可视化图表。
    """

    if not os.path.exists(DATA_PATH):
        print(f"未找到数据文件：{DATA_PATH}")
        print("请先运行 python src/clean_data.py 生成 jobs_cleaned.csv")
        return

    os.makedirs(FIGURE_DIR, exist_ok=True)

    df = pd.read_csv(DATA_PATH)

    

    print("成功读取清洗后的岗位数据")
    print(f"数据规模：{df.shape[0]} 行，{df.shape[1]} 列")

    plot_city_distribution(df)
    plot_job_type_distribution(df)
    plot_skill_frequency(df)

    print("全部可视化图表生成完成")


if __name__ == "__main__":
    main()