import pandas as pd
from os import path

df = pd.read_csv(path.join(path.dirname(__file__), "data", "delivery_time.csv"))

# 1. 주문이 가장 많이 발생한 연-월
df['주문시간'] = pd.to_datetime(df['주문시간'])
df['order_my'] = df['주문시간'].dt.strftime('%Y-%m')
monthly_order = df.groupby('order_my').size().sort_values(ascending=False)

frequent_month = monthly_order.index[0]

# 2. 해당 연-월에 '배고팡' 앱을 통한 주문 중 '앱결제'로 결제된 주문의 비율을 계산
cond1 = df['order_my'] == frequent_month
cond2 = df['앱종류'] == '배고팡'

df2 = df[cond1 & cond2]

cond3 = df2['결제종류'] == '앱결제'

rate = round(len(df2[cond3]) / len(df2), 2)