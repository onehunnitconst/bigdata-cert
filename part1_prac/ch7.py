import pandas as pd
from os import path

df = pd.read_csv(path.join(path.dirname(__file__), "data", "type1_data1.csv"))

# 1. 모든 나이(age)에 1을 더하기
df["age"] = df["age"] + 1

# 2. 20대의 vie2cws와 30대의 views 평균의 차이 구하기
cond1 = df["age"].between(20, 29)
cond2 = df["age"].between(30, 39)

diff = abs(df[cond1]["views"].mean() - df[cond2]["views"].mean())
print(round(diff, 2))
