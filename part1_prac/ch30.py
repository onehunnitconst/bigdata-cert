import pandas as pd
from os import path

df = pd.read_csv(path.join(path.dirname(__file__), "data", "delivery_time.csv"))

# 1. 평일/주말 건수
df['주문시간'] = pd.to_datetime(df['주문시간'])

# 2. 평일/주말 차이
df['주말'] = df['주문시간'].dt.dayofweek >= 5
print(abs(sum(~df['주말']) - sum(df['주말'])))