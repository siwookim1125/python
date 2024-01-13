#소유단체별 문화유산 비율 그래프출력하기(파이형)


import matplotlib.pyplot as plt
import pandas as pd

sc = pd.read_excel("pracsc.xlsx", sheet_name="Sheet1", engine="openpyxl")

temp = sc['소유단체명']
adm = []
for t in temp :
    if str(type(t)) == "<class 'str'>" :
        adm.append(t)
    else :
        adm.append('미상')

adm.sort()
print(adm)

count = []
count.append(0)
i = 0
#소유단체명이 바뀔때마다, 카운트도 새로 한다.
# for 전체데이터 :
#     if 소유단체명이 바뀌면 :
#         카운트초기화

for t in adm :
    count[i] += 1
    if t != adm[i] :
        count.append(0)
        i += 1

i = 0
print(adm)
print(count)



# print(region)
# print(count)
# print(region.__len__())

# print(i)

# gu에 담긴 데이터를 아래 형태로 데이터프레임화 하기.
# 지역구 / 문화유산갯수
# data = {
#     '지역구':region,
#     '문화유산갯수':count
# }
# df=pd.DataFrame(data)
# print(df)
# plt.rcParams['font.family'] ='Malgun Gothic'
# plt.rcParams['axes.unicode_minus'] =False
# plt.bar(region,count,)
# plt.show()