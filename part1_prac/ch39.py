import pandas as pd
from os import path

df = pd.read_csv(path.join(path.dirname(__file__), "data", "monthly_sales.csv"))

# 1. 지역(Region)과 월(Jan, Feb, Mar)별 매출(Sales) 합계를 구하시오.
melted = pd.melt(
    df,
    id_vars='Region',
    value_vars=['Jan', 'Feb', 'Mar'],
    var_name='Month',
    value_name='Sales',
)

sales = melted.groupby(['Region', 'Month']).sum().reset_index()

# 2. 위에서 구한 결과 중, 매출 합계(Sales)가 1400을 초과하는 경우가 몇 건인지 구하시오.
cond = sales['Sales'] > 1400
print(len(sales[cond]))