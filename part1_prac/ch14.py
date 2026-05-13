import numpy as np
import pandas as pd
from os import path

df = pd.read_csv(path.join(path.dirname(__file__), "data", "type1_data1.csv"))

# 1. 중복 데이터 제거
df = df.drop_duplicates()

# 2. `f3`: 결측치 = 0, 'silver' = 1, `gold` = 2, `vip` = 3
dict_list = { np.nan: 0, 'silver': 1, 'gold': 2, 'vip': 3 }
df['f3'] = df['f3'].map(dict_list)

# 3. 변환된 `f3` 컬럼의 총합
print(int(df['f3'].sum()))