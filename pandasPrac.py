#Pandas ? 엑셀과 같이 2차원 표형태 데이터를 다루는 패키지.

#DataFrame : 표형태 데이터.
#Series : 표에서 한개의 열만 떼어놓은것.

import pandas as pd

# df = pd.DataFrame(
#     [  [1,2,3],
#             [1,1,1],
#             [3,2,1]
#           ],
#     columns=["컴퓨터","수학","세계사"],
#     index=["시우","알버트","윤호"]
# )
# print(type(df))
# print(df)
#
# se = df["수학"]
# print(type(se))
# print(se)
#
# print(df > 2)
# print('각 과목 점수 합계')
# print(df.mean())

# print(df.values)
# print(df.columns)
# print(df.index)

sc = pd.read_excel("pracsc.xlsx", sheet_name="Sheet1", engine="openpyxl")
#print(sc)
#print(type(sc))

# print(sc["작업기록ID"])
# print(
#     sc.loc[:3,["작업기록ID","문화재명"]]
#       )
# print(
#     sc.iloc[:3,:3]
# )

data1 = sc.loc[:,["작업기록ID","문화재명","작업시작일자"]]
# print(data1)
#
# data1.sort_values(["작업시작일자"],ascending=True)
#
# print(data1)
#데이터 통계
# print(data1.sum())
# print(data1.loc[:,"작업시작일자"].median())
# print(data1.count())
# print(data1.min())
# print(data1.max())
#데이터 조건
#print(data1.loc[:,"작업기록ID"].str.contains("1"))

#예제문제. 10월에 작업시작한 문화재만 추려서 보여줘.
#n중으로 조건이 걸릴경우, 필터링한 데이터를 임시저장 후 다시 필터.
temp1 = data1["작업시작일자"] >= 20211000
temp2 = data1["작업시작일자"] < 20211100
print(data1[temp1 & temp2])