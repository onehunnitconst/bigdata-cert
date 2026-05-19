import pandas as pd
from os import path

df = pd.read_csv(path.join(path.dirname(__file__), "data", "type1_data1.csv"))

# 1. `subscribed` 컬럼이 2024년 2월인 데이터
# `subscribed` 컬럼은 yyyy-MM-dd 형식
cond = df["subscribed"].str.startswith("2024-02")
df = df[cond]

# 2. 위에서 찾은 데이터 중 `f3` 컬럼이 gold인 데이터의 개수
gold = df['f3'] == 'gold'
print(gold.sum())