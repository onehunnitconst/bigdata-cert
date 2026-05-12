import pandas as pd
from os import path

df = pd.read_csv(path.join(path.dirname(__file__), "data", "type1_data1.csv"))

# 1. 결측치가 있는 행을 삭제
df = df.dropna()

# 2. 결측치가 삭제된 데이터를 이용하여 지역별 평균을 구하기
means = df.groupby(by='city').mean(numeric_only=True)

# 3. `f2` 컬럼이 가장 큰 지역
means = means.sort_values('f2', ascending=False)
print(means.index[0])