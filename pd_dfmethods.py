import pandas as pd
# 1. --------------------------------------------------------------- 객채간 연산
# (add, radd) (sub, rsub) (mul, rmul) (div, rdiv) (mod, rmod) (pow, rpow)
col = ['c1','c2','c3']
row = ['r1','r2','r3']
data = [[1,10,100],
        [2,20,200],
        [3,30,300]
        ]
df1 = pd.DataFrame(data, index = row, columns = col)

col2 = ['c1']
row2 = ['r1', 'r2', 'r3']
data2 = [[1],[10],[100]]
df2 = pd.DataFrame(data2, index= row2, columns= col2)

print(df1)
print (df2)

print(df1.add(1)) #scala value addition
print(df1+1) #scala value addition

#df + df (3x3 + 3x3)
print(df1+df1)

#df + df(3x3 + 1x3) ... = NaN value incurred ... can fix by fill_value() **c and r names should equal to be added up properlly
print (df1.add(df2))
print (df1.add(df2, fill_value=0.01))
print (df1.sub(df2, fill_value=0.00))
print (df1.mul(df2, fill_value=0))
print(df1.mod(5))
print(df1 ** 2) # power
#df3 = (df1.dot(df2))
#print (df3) 뭐 이런식으로..

# 2. --------------------------------------------------------------- 객체 내 연산
# round, sum, prod, abs, transpose, rank, diff, pct_change, expending, rolling, groupby, ewm

# 3. --------------------------------------------------------------- 함수 적용
# apply, applymap, pipe, agg, transform, eval

# 4. --------------------------------------------------------------- Indexing
# at,loc, iat,iloc, head, tail, multi-index

# 5. --------------------------------------------------------------- Compare & Filter

# 6. --------------------------------------------------------------- 결측제어

# 7. --------------------------------------------------------------- Sort

# 8. --------------------------------------------------------------- 결합

# 9. --------------------------------------------------------------- 가공

# 10. --------------------------------------------------------------- 정보


