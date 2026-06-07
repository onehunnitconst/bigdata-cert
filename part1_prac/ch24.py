import pandas as pd
from os import path

df = pd.read_csv(path.join(path.dirname(__file__), "data", "delivery_time.csv"))

# 1. 사용자별 주문 거리의 합계가 50km 이상인 사람들의 결제 방식
dist = df.groupby(by='user')['거리'].sum()

cond1 = dist >= 50
dist = dist[cond1]

cond2 = df['user'].isin(dist.index)
df = df[cond2]

# 2. 이 결제 방식 중 가장 빈도가 높은 수
payment_methods = df['결제종류'].value_counts()
print(payment_methods.iloc[0])