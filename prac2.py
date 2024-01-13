
import matplotlib.pyplot as plt
import pandas as pd

# 예시데이터
# data = {
#     '과목':["컴퓨터","수학","세계사"],
#     '점수':[30,54,100]
# }
# df=pd.DataFrame(data)
# #plt 한글깨짐 해결법
# plt.rcParams['font.family'] ='Malgun Gothic'
# plt.rcParams['axes.unicode_minus'] =False
#
# plt.bar(df['과목'],df['점수'])
# plt.xlabel('과목')
# plt.ylabel('점수')
# plt.show()

#지역구별 문화유산 갯수 그래프출력하기(막대형)

sc = pd.read_excel("pracsc.xlsx", sheet_name="Sheet1", engine="openpyxl")
se1 = sc['작업소재지명']

gu = []
for txt in se1 :
    #print(type(txt))
    if str(type(txt)) == "<class 'str'>" :
        temp = txt.split(' ')
        #print(temp[1])
        gu.append(temp[1])
gu.sort()
print(gu)

region = []
count = []
i = 0
# print(region.__len__())
region.append(gu[0])
count.append(0)
# print(region.__len__())
# print(region)
for t in gu :
    count[i] += 1
    if t != region[i] :
        region.append(t)
        count.append(0)
        i += 1


print(region)
# print(region.__len__())
print(count)
# print(i)
# for Java
# j = 0;
# for(int index = 0; index < gu.size(); index++)
# {
#     if(gu[index] != region[j]){
#         region.append(gu[index])
#         j++;
#     }
#
# }

# gu에 담긴 데이터를 아래 형태로 데이터프레임화 하기.
# 지역구 / 문화유산갯수
data = {
    '지역구':region,
    '문화유산갯수':count
}
df=pd.DataFrame(data)
print(df)
plt.rcParams['font.family'] ='Malgun Gothic'
plt.rcParams['axes.unicode_minus'] =False
plt.bar(region,count,)
plt.show()