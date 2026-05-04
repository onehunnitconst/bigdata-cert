from os import path
import pandas as pd

df = pd.read_csv(path.join(path.dirname(__file__), "data", "type1_data1.csv"))

# 0이 아닌 데이터 행 구하기
count_not_zero = df['f5'] != 0
df = df[count_not_zero]

# views 컬럼 결측치를 views 컬럼 최솟값으로 채우기
min = df['views'].min()
df['views'] = df['views'].fillna(min)

# views 컬럼의 중앙값을 계산해 정수로 구하기
median = df['views'].median()
median = int(median)

print(median)