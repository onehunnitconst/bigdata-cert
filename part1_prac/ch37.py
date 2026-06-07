import pandas as pd
from os import path

df = pd.read_csv(path.join(path.dirname(__file__), "data", "store_sales.csv"))

# 1. 각 행에서 판매수량과 단가를 이용하여 매출액을 계산하시요.
df['매출액'] = df['판매수량'] * df['단가']

# 2. 요일을 평일과 주말로 구분하고, 매장별 평일과 주말 매출액 합계를 구하시오.
df['구분'] = df['요일'].isin(['토', '일']).map({True: '주말', False: '평일'})
sales = df.groupby(['매장코드', '구분']).sum(numeric_only=True).unstack()

# 3. 매장별 평일과 주말 매출액 차이를 절대값으로 구하시요. 이후, 모든 매장 중 가장 큰 절대값 차이를 찾으시오
diff = abs(sales['매출액', '주말'] - sales['매출액', '평일'])
print(diff.max())