import pandas as pd
from os import path

df = pd.read_csv(path.join(path.dirname(__file__), "data", "type1_data1.csv"))

# subscribed 컬럼에서 가장 빈도수가 많은 날짜 구하기
df = df['subscribed'].value_counts()
vc = df.index[0]

# 앞에서 구한 날짜의 일(day) 값을 정수로 구하기
print(int(vc[-2:]))