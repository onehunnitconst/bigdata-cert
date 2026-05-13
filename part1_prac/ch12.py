import pandas as pd
from os import path

df = pd.read_csv(path.join(path.dirname(__file__), "data", "type1_data1.csv"))

# 1. 결측치가 가장 많은 두 컬럼을 찾으시오
print(df.isnull().sum().sort_values(ascending=False))

# 2. 첫 번째로 결측치가 많은 컬럼에서 결측치가 있는 데이터(행)를 삭제하시오
df = df.dropna(subset=['f1'])

# 3. 두 번째로 결측치가 많은 컬럼을 최빈값으로 대체하시오
freq = df['f3'].mode()[0]
df['f3'] = df['f3'].fillna(freq)

# 4. `f3` 컬럼의 `gold` 값을 가진 데이터의 수를 정수형으로 구하시오.
print(sum(df['f3'] == 'gold'))