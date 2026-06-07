import pandas as pd
from os import path

df = pd.read_csv(path.join(path.dirname(__file__), "data", "type1_data1.csv"))

# 1. 결측치를 바로 뒤에 있는 값으로 대체
df = df.bfill()

# 2. `city`와 `f2` 컬럼을 기중느로 그룹합 계산
df = df.groupby(by=['city', 'f2']).sum(numeric_only=True)

# 3. `views` 값이 세번째로 큰 city 이름
df = df.sort_values(by='views', ascending=False)
print(df.iloc[2].name[0])