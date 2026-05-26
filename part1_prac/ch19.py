import pandas as pd
from os import path

df = pd.read_csv(path.join(path.dirname(__file__), "data", "type1_data1.csv"))


# 1. 결측치를 바로 뒤에 있는 값으로 대체
# 단, 가장 뒤의 데이터의 경우 가장 가까운 값으로 대체
df = df.bfill()

# 2. city와 f2 컬럼을 기준으로 그룹합을 계산
df = df.groupby(['city', 'f2']).sum(numeric_only=True)
df = df.sort_values(by='views', ascending=False)

# 3. views 값이 세번째로 큰 city 이름
third_city = df.iloc[2].name[0]
print(third_city)
