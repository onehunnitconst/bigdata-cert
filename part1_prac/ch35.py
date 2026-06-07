import pandas as pd
from os import path

df = pd.read_csv(path.join(path.dirname(__file__), "data", "school_data.csv"))
df_s = pd.read_csv(path.join(path.dirname(__file__), "data", "school_data_social.csv"))

# 1. 두 CSV를 이름 기준으로 합치기
df_m = pd.merge(df, df_s, on='이름')

# 2. 영어교사가 장선생, 사회교사가 오선생인 학생들 필터링
cond_1 = df_m['영어교사'] == '장선생'
cond_2 = df_m['사회교사'] == '오선생'

df_m = df_m[cond_1 & cond_2]

# 3. 필터링된 학생들의 수학 점수를 모두 더하기
result = df_m['수학'].sum()
print(result)
