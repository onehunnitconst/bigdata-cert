import pandas as pd
from os import path

df = pd.read_csv(path.join(path.dirname(__file__), "data", "delivery_time.csv"))

def calc_delivery_fee(dist):
    if dist < 5:
        return 2000
    if dist < 10:
        return 4000
    if dist < 15:
        return 6000
    return 8000


# 1. 배달료 계산
df['배달료'] = df['거리'].apply(calc_delivery_fee)

# 2. 연도-월별로 배달료의 총합 집계
df['주문시간'] = pd.to_datetime(df['주문시간'])
df['order_my'] = df['주문시간'].dt.strftime('%Y-%m')

monthly_fee = df.groupby('order_my')['배달료'].sum()
max_month = monthly_fee.idxmax()
print(max_month, monthly_fee[max_month])