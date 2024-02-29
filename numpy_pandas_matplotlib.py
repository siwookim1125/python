import numpy as np
import pandas as pd
# --------------------------------------------------------------- pandas
# The most basic form of pandas Dataframe
values = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
index = ["one", "two", "three"]
columns = ['A', 'B', 'C']

df = pd.DataFrame(values, index = index, columns = columns)
print (df)
# --------------------------------------------------------------- calling methods
print(df.head(2)) # front 2 row
print (df.tail(1)) # end 1 row

print (df['C']) # column
# --------------------------------------------------------------- reading external files
#c = pd.read_excel("pracsc.xlsx", sheet_name="Sheet1", engine="openpyxl")
#print(c)
# --------------------------------------------------------------- numpy


# --------------------------------------------------------------- ML Workflow
'''
1) Acquisition (of data)
2) Inspection and Exploration (EDA_ Exploratory Data Analysis)
3) Preprocessing and Cleaning 
4) Modelling and training
5) Evaluation
'''
# --------------------------------------------------------------- Data Splitting
'''
Total Data: 20000
X_train: 18000
Y_train: 18000 (shown and learned)

X_test: 2000
Y_test: 2000 (unseen and tested)

test result --> accuracy of the model
'''
# --------------------------------------------------------------- Data Splitting using zip method
x, y = zip(['a',1],['b',2],['c',3])
print (x) #tuple
print (y) #tuple


