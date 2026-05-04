import pandas as pd
from os import path

df = pd.read_csv(path.join(path.dirname(__file__), "data", "type1_data1.csv"))

# 1. 결측치가 있는 데이터(행)을 제거
df = df.dropna()

# 2. `views` 컬럼을 `f1` 컬럼으로 나눈 값을 새로운 컬럼으로 추가
df['f1_by_views'] = df['f1'] / df['views']

# 3. 새로운 컬럼 값 중 가장 큰 값을 가진 행의 age를 정수로 구하기
ndf = df.sort_values('f1_by_views', ascending=False)
print(int(ndf.iloc[0]['age']))

