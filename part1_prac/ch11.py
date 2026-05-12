import pandas as pd
from os import path

df = pd.read_csv(path.join(path.dirname(__file__), "data", "type1_data1.csv"))

# 1. 결측치 제거
df = df.dropna()

# 2. 앞에서부터 70% 데이터 구하기
# 데이터 70% 지점의 index가 소수점으로 계산될 경우 소수점 버림
pivot = int(len(df) * 0.7)
df = df.iloc[:pivot]

# 3. 앞에서 구한 데이터에서 views의 3사분위수에서 1사분위수를 뺀 값을 소수점 이하를 버리고 정수 부분만 구하기
q3 = df['views'].quantile(0.75)
q1 = df['views'].quantile(0.25)
print(int(q3 - q1))