#2021년 월별 작업 비율 그래프출력하기(파이형)

import matplotlib.pyplot as plt
import pandas as pd

sc = pd.read_excel("pracsc.xlsx", sheet_name="Sheet1", engine="openpyxl")
df = sc['작업시작일자'].astype("string")

date = [0, #aug
        0, #sep
        0, #oct
        0  #nov
]

for txt in df:
    if "202108" in txt:
        date[0] += 1
    elif "202109" in txt:
        date[1] += 1
    elif "202110" in txt:
        date[2] += 1
    elif "202111" in txt:
        date[3] += 1

df = pd.DataFrame(date)
print(df)

df = pd.DataFrame(date, index=['8', '9', '10', '11'], columns=['yax'])

plot = df.plot.pie(y='yax', figsize=(5, 5), autopct='%1.1f%%')
plt.title('2021, Monthly Working Ratio')
plt.ylabel('')
plt.show()