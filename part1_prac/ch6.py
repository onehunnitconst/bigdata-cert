import pandas as pd
from os import path

df = pd.read_csv(path.join(path.dirname(__file__), "data", "type1_data1.csv"))

# 1. `f3` 컬럼이 gold이면서 `f2` 컬럼이 2인 데이터 찾기
cond1 = df['f3'] == 'gold'
cond2 = df['f2'] == 2
df = df[cond1 & cond2]

# 2. 찾은 데이터에서 `f1` 컬럼의 분산 구하기
# 반올림 후 소수 둘째자리까지
f1_var = df['f1'].var()
print(round(f1_var, 2))