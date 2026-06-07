import pandas as pd
from os import path

df = pd.read_csv(path.join(path.dirname(__file__), "data", "type1_data1.csv"))

# 1. `views` 컬럼의 1사분위수, 3사분위수, IQR 계산
q1 = df['views'].quantile(q=0.25)
q3 = df["views"].quantile(q=0.75)
iqr = q3 - q1

# 2. 이상치 조건에 맞는 데이터 찾기
start = q1 - 1.5 * iqr
end = q3 + 1.5 * iqr
cond = (df['views'] < start) | (df['views'] > end)
df = df[cond]

# 3. 이상치 데이터의 `views` 컬럼 합 (정수)
print(int(df['views'].sum()))