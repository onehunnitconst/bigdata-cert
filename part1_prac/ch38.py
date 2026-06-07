import pandas as pd
from os import path

df = pd.read_csv(path.join(path.dirname(__file__), "data", "region_sales.csv"))

# 1. 각 Region과 Channel 조합별로 제품(Product) A, B의 총 판매액을 계산하시오.
sales = pd.pivot_table(df, index=['Region', 'Channel'], columns='Product', values='Sales', aggfunc='sum')

# 2. 제품 A의 매출 비율(A비율)을 구하시요. A비율=(제품 A 판매액)• (제품 A 판매액+ 제품 B 판매액)
sales['ARate'] = sales['A'] / (sales['A'] + sales['B'])

# 3. A비율 중 최댓값을 찾아 반올림하여 소수 둘째 자리까지 구하시오.
print(round(sales['ARate'].max(), 2))