import pandas as pd
from os import path

df = pd.read_csv(path.join(path.dirname(__file__), "data", "type1_data1.csv"))

# 1. `f4` 컬럼 데이터에 `FJ`가 포함된 데이터 찾기
# `f4`는 MBTI 유형이므로 3번째와 4번째 글자가 `FJ`인 경우를 찾는다.
df['f4_new'] = df['f4'].str[2:4]
cond = df['f4_new'] == 'FJ'
df = df[cond]

# 2. 찾은 데이터 중 `f2` 컬럼의 평균 구하기
# 반올림 후 소수 둘째자리까지
fj_mean = df['f2'].mean()
print(round(fj_mean, 2))