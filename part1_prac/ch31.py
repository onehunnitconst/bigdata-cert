import pandas as pd
from os import path

df = pd.read_csv(path.join(path.dirname(__file__), "data", "delivery_time.csv"))

# 1. 'user' 뒤 숫자값만 추출
df['uid'] = df['user'].str[5:].astype(int)

# 2. 추출된 숫자값을 모두 합한 값을 정수로 구하기
print(sum(df['uid']))