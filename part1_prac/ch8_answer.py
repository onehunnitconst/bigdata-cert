import pandas as pd
from os import path

df = pd.read_csv(path.join(path.dirname(__file__), "data", "type1_data1.csv"))

# 1. `subscribed` 컬럼이 2024년 2월인 데이터
# `subscribed` 컬럼은 yyyy-MM-dd 형식
df['subscribed'] = pd.to_datetime(df['subscribed'])

df['year'] = df['subscribed'].dt.year
df['month'] = df['subscribed'].dt.month

# 2. 위에서 찾은 데이터 중 `f3` 컬럼이 gold인 데이터의 개수
cond1 = df['year'] == 2024
cond2 = df['month'] == 2
cond3 = df['f3'] == 'gold'

df = df[cond1 & cond2 & cond3]
print(len(df))