import pandas as pd
from os import path

df = pd.read_csv(path.join(path.dirname(__file__), "data", "delivery_time.csv"))

# 1. 주문시간과 실제도착시간의 차이를 분 단위로 계산
df['주문시간'] = pd.to_datetime(df['주문시간'])
df['실제도착시간'] = pd.to_datetime(df['실제도착시간'])

df['diff'] = (df['실제도착시간'] - df['주문시간']).dt.total_seconds() / 60

# 2. 앱 종류별로 평균 도착시간을 계산
df = df.groupby(by='앱종류')['diff'].mean()

# 3. 평균적으로 가장 빠른 앱 종류를 찾고 해당 앱의 평균 도착시간을 분으로 반올림하여 정수로 구하기
print(round(df.min()))