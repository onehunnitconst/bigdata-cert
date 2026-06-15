from os import path
import pandas as pd

# 미국의 인구조사 데이터(1994)를 바탕으로 만들어진 데이터다. 이 데이터에서 각 사람의 소득을 예측하면 된다. 나이, 결혼 여부, 직종 등의 컬럼이 있다.
# 1. 레이블(타깃)은 연소득이 $50,000 이상과 미만으로 구분됨(컬럼명: income)
# 2. 소득 예측값($50,000 이상일 확률)을 csv 파일로 생성
# 3. 평가 기준은 ROC-AUC로 평가
# 4. 제출 파일은 예측값만 result.csv 파일로 생성해 제출(컬럼명: pred, 1개)

train = pd.read_csv(path.join(path.dirname(__file__), "data", "train.csv"))
test = pd.read_csv(path.join(path.dirname(__file__), "data", "test.csv"))

train = train.dropna()
test = test.dropna()

cond_test_1 = test['age'] <= 0
test = test[cond_test_1]

print(train.describe())
print(test.describe())
