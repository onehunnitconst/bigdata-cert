import pandas as pd
from os import path

df = pd.read_csv(path.join(path.dirname(__file__), "data", "type1_data1.csv"))

# 1. 주어진 데이터에서 문자 자료형 컬럼을 삭제
df = df.select_dtypes(exclude='object')

# 2. 숫자 자료형 컬럼의 결측치를 0으로 대체
df = df.fillna(0)

# 3. 각 행의 합이 3000보다 큰 값의 개수를 정수로 구하기
# 합 = age + views + f1 + f2 + f5
df['total'] = df['age'] + df['views'] + df['f1'] + df['f2'] + df['f5']
cond = df['total'] > 3000
print(df[cond].count()['total'])