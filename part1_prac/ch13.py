import pandas as pd
from os import path

df = pd.read_csv(path.join(path.dirname(__file__), "data", "type1_data1.csv"))

# 1. `f1` 컬럼에 결측치가 있는 데이터만 선택
cond = df['f1'].isnull()
df = df[cond]

# 2. 선택된 데이터에서 `age` 컬럼의 평균값을 구하시오
# (반올림 후 소수 첫째자리까지 구하기)
result = df['age'].mean()
print(round(result, 1))
