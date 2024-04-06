import pandas as pd
import numpy as np
import datetime as dt


channel =pd.read_csv('https://raw.githubusercontent.com/Datamanim/datarepo/main/youtube/channelInfo.csv')
video =pd.read_csv('https://raw.githubusercontent.com/Datamanim/datarepo/main/youtube/videoInfo.csv')
# print(channel.head())
# print(video.head())


# 각 비디오는 10분 간격으로 구독자수, 좋아요, 싫어요수, 댓글수가 수집된것으로 알려졌다.
# 공범 EP1의 비디오정보 데이터중 수집간격이 5분 이하, 20분이상인 데이터 구간( 해당 시점 전,후) 의 시각을 모두 출력하라

# print(video.index.max() - 1)
# print(dt.datetime.strptime("05", "%m"))

# diff = pd.to_datetime(video.loc[2,'ct']) - pd.to_datetime(video.loc[1,'ct'])
# print( type(diff / np.timedelta64(1,'s')) )
#
# for i in range(video.index.max() - 1) :
#     # print(video.loc[i,])
#     diff = pd.to_datetime(video.loc[i+1,'ct']) - pd.to_datetime(video.loc[i,'ct'])
#     diff2 = diff / np.timedelta64(1,'s')
#
#     if diff2 < 300.0  :
#         print(diff)
#         print(video.loc[i,])
#         print('########################')
#
#     if diff2 > 1200.0  :
#         print(diff)
#         print(video.loc[i,])
#         print('########################')


#각 에피소드의 시작날짜(년-월-일)를 에피소드 이름과 묶어 데이터 프레임으로 만들고 출력하라
# print(video.columns)
# 데이터프레임에서 별개로 시리즈를 뽑아도, index정보를 기존 데이터프레임과 공유함.
date = video['ct'].str[:10].sort_values()
df2 = pd.concat([date,video['videoname']], axis=1)
print(df2.drop_duplicates('videoname'))

#“공범” 컨텐츠의 경우 19:00시에 공개 되는것으로 알려져있다.
# 공개된 날의 21시의 viewcnt, ct, videoname 으로 구성된 데이터 프레임을 viewcnt를 내림차순으로 정렬하여 출력하라