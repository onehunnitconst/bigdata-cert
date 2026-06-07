import pandas as pd
from os import path

df = pd.read_csv(path.join(path.dirname(__file__), "data", "school_data.csv"))

# 1. 과목에 상관없이 점수가 가장 작은 점수 25개를 찾으시오
melted_df = df.melt(id_vars=['이름'], value_vars=['수학', '영어', '국어'])

melted_df = melted_df.nsmallest(25, 'value')

# 2. 찾은 점수 25개의 합을 정수로 구하시오
result = melted_df['value'].sum()
print(result)