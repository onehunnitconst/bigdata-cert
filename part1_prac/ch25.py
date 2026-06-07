import pandas as pd
from os import path

df = pd.read_csv(path.join(path.dirname(__file__), "data", "delivery_time.csv"))

# 1. 각 사용자별로 첫 주문과 마지막 주문 사이의 시간 간격 (일 단위)
df['주문시간'] = pd.to_datetime(df['주문시간'])
user_order_time = df.groupby('user')['주문시간']
interval = (user_order_time.max() - user_order_time.min()).dt.days

# 2. 시간차가 0일인 사용자를 제외하고, 나머지 사용자들의 평균 시간 간격을 계산 (일 단위)
cond1 = interval != 0
interval = interval[cond1]
mean = interval.mean()

# 3. 평균 시간 간격보다 긴 시간 간격을 가진 사용자의 수를 정수로 구하기
cond2 = interval > mean
print(len(interval[cond2]))