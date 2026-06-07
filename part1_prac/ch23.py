import pandas as pd
from os import path

df = pd.read_csv(path.join(path.dirname(__file__), "data", "delivery_time.csv"))

# 1. 각 결제 종류별로 실제 도착시간이 예상 도착시간보다 늦은 주문의 비율
df['예상도착시간'] = pd.to_datetime(df['예상도착시간'])
df['실제도착시간'] = pd.to_datetime(df['실제도착시간'])

df['지연시간'] = (df['실제도착시간'] - df['예상도착시간']).dt.total_seconds()
df['지연여부'] = df['지연시간'] > 0

result = df.groupby(by='결제종류')['지연여부'].mean()

# 2. 비율 중 가장 큰 값을 반올림하여 소수 둘째자리까지 구하기
print(round(result.max(), 2))