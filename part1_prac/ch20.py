import pandas as pd
from os import path

df = pd.read_csv(path.join(path.dirname(__file__), "data", "type1_data1.csv"))

# 1. 연도 구분 없이 월별로 숫자형 컬럼 구하기
df['subscribed'] = pd.to_datetime(df['subscribed'])
df['sub_month'] = df['subscribed'].dt.month

df = df.groupby(by='sub_month').sum(numeric_only=True)

# 2. 합계 중 `views`가 가장 작은 값을 가진 월
df = df.sort_values(by='views')
print(df.index[0])