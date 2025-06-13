# 导入所需库
import pandas as pd
import numpy as np

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr

plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体
plt.rcParams['axes.unicode_minus'] = False   # 正常显示负号

# 1. 读取数据（假设数据文件名为“上证指数历史日K数据.xlsx”，包含 trade_date, close, vol 三列）
df = pd.read_excel(r"C:\Users\36418\Desktop\上证指数历史日K数据.xlsx", engine='openpyxl')

# 2. 数据预处理
df = df.sort_values("trade_date")  # 按日期升序
df = df.reset_index(drop=True)

# 3. 计算每日收益率（波动性常用对数收益率）
df["return"] = np.log(df["close"] / df["close"].shift(1))
# 去除第一行（因无法计算收益率）
df = df.dropna()

# 4. 描述性统计分析
desc_stats = df[["return", "vol"]].describe()
print("描述性统计：")
print(desc_stats)

# 5. 相关性分析（皮尔逊相关系数）
corr, p_value = pearsonr(df["return"], df["vol"])
print(f"\n日收益率与成交量的皮尔逊相关系数: {corr:.4f}，p值: {p_value:.4e}")
if p_value < 0.05:
    print("相关系数通过了显著性检验，可以认为两者存在统计相关性。")
else:
    print("相关系数未通过显著性检验，二者相关性不显著。")


N = 100
df_part = df.iloc[:N].copy()

# 确保 trade_date 是字符串类型，并转为 datetime 格式，便于美化x轴
df_part["trade_date"] = pd.to_datetime(df_part["trade_date"])

# -- 收盘价折线图 --
plt.figure(figsize=(10, 5))
plt.plot(df_part["trade_date"], df_part["close"], label="收盘价")
plt.xlabel("日期")
plt.ylabel("收盘价")
plt.title("上证指数收盘价（前100日）")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
# 横坐标美化：每隔10个日期显示一个label
plt.gca().xaxis.set_major_locator(plt.MaxNLocator(10))
plt.savefig("收盘价_前100日.png", dpi=200)
plt.close()

# -- 成交量折线图 --
plt.figure(figsize=(10, 5))
plt.plot(df_part["trade_date"], df_part["vol"], label="成交量", color="orange")
plt.xlabel("日期")
plt.ylabel("成交量")
plt.title("上证指数成交量（前100日）")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.gca().xaxis.set_major_locator(plt.MaxNLocator(10))
plt.savefig("成交量_前100日.png", dpi=200)
plt.close()

# -- 收益率与成交量散点图 --
plt.figure(figsize=(8, 5))
plt.scatter(df_part["return"], df_part["vol"], alpha=0.6)
plt.xlabel("日收益率")
plt.ylabel("成交量")
plt.title("上证指数日收益率与成交量关系（前100日）")
plt.tight_layout()
plt.savefig("收益率_成交量散点图_前100日.png", dpi=200)
plt.close()

# -- 相关性热力图（全量或前N行均可）--
plt.figure(figsize=(5, 4))
sns.heatmap(df_part[["return", "vol"]].corr(), annot=True, cmap="coolwarm")
plt.title("收益率与成交量相关性热力图（前100日）")
plt.tight_layout()
plt.savefig("相关性热力图_前100日.png", dpi=200)
plt.close()