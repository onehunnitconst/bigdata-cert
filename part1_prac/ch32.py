import pandas as pd
from os import path

df = pd.read_csv(path.join(path.dirname(__file__), "data", "school_data.csv"))

# 1. 수학, 영어, 국어 점수의 합을 구하시오
df['total_score'] = df[['수학', '영어', '국어']].sum(axis=1, numeric_only=True)

# 2. 합이 가장 큰 상위 10명을 찾으시오.
tops = df.nlargest(10, 'total_score')

# 3. 찾은 10명의 수학 평균 점수를 구하시오
result = tops['수학'].mean()
print(round(result))
