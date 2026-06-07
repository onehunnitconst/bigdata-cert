import pandas as pd
from os import path

df = pd.read_csv(path.join(path.dirname(__file__), "data", "delivery_time.csv"))

# 1. 점심시간에 주문된 배달 데이터
df['주문시간'] = pd.to_datetime(df['주문시간'])
df['실제도착시간'] = pd.to_datetime(df['실제도착시간'])
cond1 = df['주문시간'].dt.hour.between(10, 13-1)
df = df[cond1]

# 2. 점심시간 주문 건 중 과속(50km/h 이싱)한 주문 수를 정수로 구하기
df['배달시간'] = (df['실제도착시간'] - df['주문시간']).dt.total_seconds()
print(sum((df['거리'] / df['배달시간'] * 3600) >= 50))