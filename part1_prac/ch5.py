import pandas as pd
from os import path

df = pd.read_csv(path.join(path.dirname(__file__), "data", "type1_data1.csv"))

# 1. `f4` 컬럼 데이터에 `FJ`가 포함된 데이터를 찾으시오
df['f4_new'] = df['f4'].str[2:4]

cond = df['f4_new'] == 'FJ'
df = df[cond]

# 2. 찾은 데이터 중에서 `f2` 컬럼의 평균값을 구하시오. (반올림 후 소수 둘째자리까지 계산)
print(round(df['f2'].mean(), 2))