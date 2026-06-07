import pandas as pd
from os import path

df = pd.read_csv(path.join(path.dirname(__file__), "data", "sales.csv"))

# 1. 결측된 판매금액은 해당 지역의 평균 판매금액으로 결측값을 대체
m = df.groupby('지역코드')['판매금액'].transform('mean')
df['판매금액'] = df['판매금액'].fillna(m)

# 2. 각 거래마다 `판매금액`과 해당 지역의 평균 판매금액의 `차이` 구하기
df['지역평균'] = df.groupby('지역코드')['판매금액'].transform('mean')
df['차이'] = abs(df['판매금액'] - df['지역평균'])

# 3. 각 지역에서 차이값의 평균을 구한 후 이 값이 가장 큰 지역의 지역코드 구하기
diff_mean = df.groupby('지역코드')['차이'].mean()
print(diff_mean.idxmax())