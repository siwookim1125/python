import pandas as pd
import numpy as np
import datetime as dt


channel =pd.read_csv('https://raw.githubusercontent.com/Datamanim/datarepo/main/youtube/channelInfo.csv')
video =pd.read_csv('https://raw.githubusercontent.com/Datamanim/datarepo/main/youtube/videoInfo.csv')
# print(channel.head())
# print(video.head())


# 각 비디오는 10분 간격으로 구독자수, 좋아요, 싫어요수, 댓글수가 수집된것으로 알려졌다.
# 공범 EP1의 비디오정보 데이터중 --조건1
# 수집간격이 5분 이하, 20분이상인 데이터 --조건2
# 구간( 해당 시점 전,후) 의 시각을 모두 출력하라 --조건3

# 조건1
ep1 = video.loc[video.videoname.str.contains('1')].sort_values('ct')
# print(ep1)

# # 조건2. diff는 한 객체 내에서 열과 열 / 행과 행의 차이를 출력하는 메서드 입니다. 출처 https://wikidocs.net/156786
# date = pd.to_datetime(ep1['ct'])
# # print(date.diff(1)) #시리즈 내에서 이전행과 값 차이
#
# result = ep1[
#     ( date.diff(1) >= dt.timedelta(minutes=20) )
#     | ( date.diff(1) <= dt.timedelta(minutes=5) ) # 시리즈 각 값들과 비교
# ]
# print(result)
#
# # 조건3. 조건2 결과의 인덱스를 바탕으로 전 후 인덱스를 포함하여 결과출력
# print(video.loc[[720,721,722,723,1635,1636,1637],])

#조건2 수업때 한 loop문 버전
for i in range(ep1.index.max()-1) :
    # print(video.loc[i,])
    # 1번인덱스 - 0번인덱스 부터 index.max()인덱스 - index.max()-1인덱스 까지 비교.
    diff = pd.to_datetime(ep1.loc[i+1,'ct']) - pd.to_datetime(ep1.loc[i,'ct'])
    diff2 = diff / np.timedelta64(1,'s')

    if (diff2 <= 300.0) | (diff2 >= 1200.0) : #두 조건의 and or 연산시, 연산우선순위 모호함때문에 반드시 소괄호로 묶어서 표현필요.
        print(diff)
        print(ep1.loc[i+1,]) # 기준인덱스가 i+1이므로,
        print('########################')

# 조건3. 조건2 결과의 인덱스를 바탕으로 전 후 인덱스를 포함하여 결과출력. 수업때 한 방법이 정확한 결과 도출. diff 라는 기능에 문제가 있는듯.
print(video.loc[[9,10,11,417,418,419,720,721,722,723,1635,1636,1637],])

## 문법 확인용 start
# print(video.index.max() - 1)
# print(dt.datetime.strptime("05", "%m"))

# diff = pd.to_datetime(ep1.loc[2,'ct']) - pd.to_datetime(ep1.loc[1,'ct'])
# print( type(diff / np.timedelta64(1,'s')) )
## 문법 확인용 end





#각 에피소드의 시작날짜(년-월-일)를 에피소드 이름과 묶어 데이터 프레임으로 만들고 출력하라
# print(video.columns)
# 데이터프레임에서 별개로 시리즈를 뽑아도, index정보를 기존 데이터프레임과 공유함.
# date = video['ct'].str[:10].sort_values()
# df2 = pd.concat([date,video['videoname']], axis=1)
# print(df2.drop_duplicates('videoname'))

#“공범” 컨텐츠의 경우 19:00시에 공개 되는것으로 알려져있다.
# 공개된 날의 21시의 viewcnt, ct, videoname 으로 구성된 데이터 프레임을 viewcnt를 내림차순으로 정렬하여 출력하라