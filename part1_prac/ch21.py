import pandas as pd
from os import path

df = pd.read_csv(path.join(path.dirname(__file__), "data", "delivery_time.csv"))

# 1. 예상 도착시간보다 늦게 도착한 건수
df['예상도착시간'] = pd.to_datetime(df['예상도착시간'])
df['실제도착시간'] = pd.to_datetime(df['실제도착시간'])

df['지연시간'] = (df['실제도착시간'] - df['예상도착시간']).dt.total_seconds()

cond1 = df['지연시간'] > 0

# 2. 이 중 거리가 7km 이상인 건수
cond2 = df['거리'] > 7

df = df[cond1 & cond2]

print(len(df))