import pandas as pd
from os import path

df = pd.read_csv(path.join(path.dirname(__file__), "data", "type1_data1.csv"))

# 1. `views` 컬럼의 표준편차
std_dev = df['views'].std()

# 2. `age` 컬럼의 이상치(소수점 나이, 음수 나이, 0) 제거
cond = (df['age'] <= 0 | (df['age'] != round(df['age'])) )
df = df[~cond]

# 3. 이상치 제거 전후의 `views` 컬럼 표준편차를 더하여 반올림 푸 소수 둘째자리까지 구하기
std_dev_2 = df['views'].std()

result = std_dev + std_dev_2

print(round(result, 2))