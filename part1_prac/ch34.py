import pandas as pd
from os import path

df = pd.read_csv(path.join(path.dirname(__file__), "data", "school_data.csv"))
df_s = pd.read_csv(path.join(path.dirname(__file__), "data", "school_data_science.csv"))

# 1. 두 CSV 파일을 학생 순서로 병합
df = pd.concat([df, df_s], axis=1)

# 2. 수학, 영여, 국어, 과학 평균
df['평균'] = df[['수학', '영어', '국어', '과학']].mean(axis=1)

# 3. 평균이 60점 이상인 인원 수
cond = df['평균'] > 60

result = len(df[cond])
print(result)
