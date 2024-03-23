import pandas as pd
#from IPython.display import display

df = pd.read_csv("https://raw.githubusercontent.com/Datamanim/datarepo/main/youtube/youtube.csv",index_col=0)
#df.head()

#1
# result = df["channelTitle"].value_counts()
# print(result[0:10].index)

#2

# r = df.loc[df.likes < df.dislikes]
# print(r["channelTitle"].unique())

#3

# result = df[["channelTitle","channelId"]]
# final = result.drop_duplicates().channelId.value_counts()
# print(type(final))
# #print(final)
# print(final.index) #index type
# print(final.values) #ndarray type
# print(final[final>1].size)


# print(df["channelTitle"].unique().size)
# print(df["channelId"].unique().size)

#5

df['ratio'] = df['view_count'] / df['comment_count'].replace(0, pd.NA) # 근데 view_count는 0일 수 있음, view가 존재하는데 댓글이 안 달린 경우에는 연산이 어떻게 되는거지? <--- gpt로 해결
ratio_filtered = df[df['ratio'] > 0]
ratio_sorted = ratio_filtered.sort_values(by='ratio', ascending=False)
print(ratio_sorted)
print(ratio_sorted.tail(1)) #내가해냄 ㅋ

#6
print(ratio_sorted.head(1))

#7

df['likeratio'] = df['likes'] / df['dislikes'].replace(0, pd.NA)
ratio_filtered2 = df[df['likeratio'] > 0]
ratio_sorted2 = ratio_filtered2.sort_values(by='likeratio', ascending=False)
print(ratio_sorted2.head(1)) #왜 1부터 세지?

#8

result = df[["channelTitle","trending_date2"]]
final = result.drop_duplicates().channelTitle.value_counts()
print(final.head(1)) # ??? 내가해냄 어케했지?????????

#9 20회(20일)이상 인기동영상 리스트에 포함된 동영상의 숫자는?
channel = df['channelTitle'].value_counts().reset_index()
print (channel[channel['count'] > 20]) # 아 이건안되네


