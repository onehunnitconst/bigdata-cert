import pandas as pd
from os import path

df = pd.read_csv(
    path.join(path.dirname(__file__), "data", "type1_data2.csv"), index_col="year"
)

# 1. index `2001` 데이터에서 평균보다 큰 값의 개수
m1 = df.loc[2001]
m1_mean = m1.mean()
m1_count = (m1 > m1_mean).sum()

# 2. index `2003` 데이터에서 평균보다 작은 값의 개수
m2 = df.loc[2003]
m2_mean = m2.mean()
m2_count = (m2 < m2_mean).sum()

# 3. 두 개수를 더하기
print(m1_count + m2_count)
