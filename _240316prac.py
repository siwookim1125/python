import pandas as pd
from IPython.display import display

df = pd.read_csv("https://raw.githubusercontent.com/Datamanim/datarepo/main/youtube/youtube.csv",index_col=0)
# display(df.columns)
# display(df.head(10))
# #1
# result = df["channelTitle"].value_counts()
# print(result[0:10].index)


# 일요일에 인기있었던 영상들중 가장많은 영상 종류(categoryId)는 무엇인가?
# df['시간'] = pd.to_datetime(df['trending_date2'])
# print(df['시간'])
# print(df['trending_date2'])

# df['주말'] = df['시간'].dt.weekday #요일 번호 0 월 ~ 6 일
# df['주말'] = df['시간'].dt.day_name() #요일 이름
# print(df['주말'])

# df1 = df[df['주말'] == 6]
# print(df1[df1['likes'] > 0])
# 최종 답
# print(df1[df1['likes'] > 0].categoryId.value_counts().index[0])

# df1 = df.loc[:,['categoryId','likes','trending_date2']]
# print(df1[df1['likes'].max()])
# print(df1[ df1['likes'] > 0 ].value_counts())


#각 요일별 인기 영상들의 categoryId는 각각 몇개 씩인지 하나의 데이터 프레임으로 표현하라
# https://teddylee777.github.io/pandas/pandas-groupby/  #groupby내용 정리
df['요일'] = pd.to_datetime(df['trending_date2'])
# print(df['요일'])
g = df.groupby([df['요일'].dt.day_name(),'categoryId'],as_index=False).size()
print(g)

result= g.pivot(index='categoryId',columns='요일')
print(result)


# target2= df.loc[df.view_count!=0]
# t = target2.copy()
# t['ratio'] = (target2['comment_count']/target2['view_count']).dropna()
# result = t.sort_values(by='ratio', ascending=False).iloc[0]
# print(result)