import pandas as pd
from os import path

df = pd.read_csv(path.join(path.dirname(__file__), "data", "type1_data1.csv"))

# 1. `views` 컬럼이 1000 이하인 데이터 (결측치 제외)
# 결측치 제거
df = df.dropna(subset=['views'])
cond = df['views'] <= 1000
df = df[cond]

# 2. 앞에서 구한 데이터 중 `f4` 컬럼의 최빈값
# f4 컬럼은 MBTI 유형이 저장되어 있음
print(df['f4'].mode()[0])