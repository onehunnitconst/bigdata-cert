import pandas as pd
from os import path

df = pd.read_csv(path.join(path.dirname(__file__), "data", "delivery_time.csv"))

# 1. 연도와 월을 기준으로 주문 수를 집계하시오
df["주문시간"] = pd.to_datetime(df["주문시간"])
df["order_my"] = df["주문시간"].dt.strftime("%Y%m")
monthly_order = df.groupby("order_my").size().sort_values(ascending=False)
print(monthly_order.index[0])
