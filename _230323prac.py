import pandas as pd
from IPython.display import display

df = pd.read_csv("https://raw.githubusercontent.com/Datamanim/datarepo/main/youtube/youtube.csv",index_col=0)


#각 요일별 인기 영상들의 categoryId는 각각 몇개 씩인지 하나의 데이터 프레임으로 표현하라
# https://teddylee777.github.io/pandas/pandas-groupby/  #groupby내용 정리
# df['요일'] = pd.to_datetime(df['trending_date2']).dt.day_name()
#
# g = df.groupby([df['요일'],'categoryId'],as_index=False).size()
# print(g)
#
# result= g.pivot(index='categoryId',columns='요일')
# print(result)



###############################################################################################################

channel =pd.read_csv('https://raw.githubusercontent.com/Datamanim/datarepo/main/youtube/channelInfo.csv')
video =pd.read_csv('https://raw.githubusercontent.com/Datamanim/datarepo/main/youtube/videoInfo.csv')
# display(channel.head())
# display(video.head())


# 각 데이터의 ‘ct’컬럼을 시간으로 인식할수 있게 datatype을 변경하고
# video 데이터의 videoname의 각 value 마다 몇개의 데이터씩 가지고 있는지 확인하라

# time = pd.to_datetime(channel['ct'])
# time2 = pd.to_datetime(video['ct'])
# print(time)
# print(time2)
# print( pd.concat(time,time2) )

# print(video.videoname.value_counts())


# 수집된 각 video의 가장 최신화 된 날짜의 viewcount값을 출력하라
