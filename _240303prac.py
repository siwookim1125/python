import pandas as pd
from IPython.display import display

df = pd.read_csv("https://raw.githubusercontent.com/Datamanim/datarepo/main/youtube/youtube.csv",index_col=0)
# display(df.head())
# #1
# result = df["channelTitle"].value_counts()
# print(result[0:10].index)

print(df["channelId"])


