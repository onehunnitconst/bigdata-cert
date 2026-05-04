import pandas as pd
from os import path

df = pd.read_csv(path.join(path.dirname(__file__), "data", "type1_data1.csv"))

# 1. `views` 컬럼의 결측 데이터를 0으로 대체
df = df.fillna(0)

# 2. `views` 컬럼에서 상위 10번째 값 구하기
df = df.sort_values('views', ascending=False)
views_10 = df.iloc[9]['views']

# 3. `views` 컬럼에서 상위 10개의 값을 상위 10번쩨 값으로 대체
df.iloc[:10, -1] = views_10

# 4. `views` 컬럼의 전체 합을 정수로 구하기
print(int(df['views'].sum()))
