# import pandas as pd
# import requests

# url = "https://push2his.eastmoney.com/api/qt/stock/kline/get"
# params = {
#     "secid": "1.000001",  # 上证指数
#     "fields1": "f1,f2,f3,f4,f5,f6",
#     "fields2": "f51,f52,f53,f54,f55,f56,f57,f58,f59,f60,f61",
#     "klt": "101",   # 101=日K
#     "fqt": "1",     # 复权方式
#     "beg": "19900101",
#     "end": "20250611",
# }
# headers = {
#     "User-Agent": "Mozilla/5.0"
# }
# r = requests.get(url, params=params, headers=headers)
# data = r.json()["data"]["klines"]
# df = pd.DataFrame([i.split(",") for i in data],
#                   columns=["trade_date","open","close","high","low","vol","amount","amplitude","chg","pct_chg"])
# df = df[["trade_date","close","vol"]]
# df.to_excel("上证指数历史日K数据.xlsx", index=False)
# print("已保存为Excel文件")

import pandas as pd
import requests

url = "https://push2his.eastmoney.com/api/qt/stock/kline/get"
params = {
    "secid": "1.000001",  # 上证指数
    "fields1": "f1,f2,f3,f4,f5,f6",
    "fields2": "f51,f52,f53,f54,f55,f56,f57,f58,f59,f60,f61",
    "klt": "101",   # 101=日K
    "fqt": "1",     # 复权方式
    "beg": "19900101",
    "end": "20250611",
}
headers = {
    "User-Agent": "Mozilla/5.0"
}
r = requests.get(url, params=params, headers=headers)
data = r.json()["data"]["klines"]
df = pd.DataFrame([i.split(",") for i in data],
                  columns=["trade_date", "open", "close", "high", "low", "vol", "amount", "amplitude", "chg", "pct_chg", "turnover"])
df = df[["trade_date", "close", "vol"]]
df.to_excel("上证指数历史日K数据.xlsx", index=False)
print("已保存为Excel文件")