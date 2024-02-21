# 함수 prac
# def print_list(a):
#     for i in a:
#         print (i)
#
#
# lst = ["a","b","c","d","e","f"]
# print_list(lst)


# def mult(m, n):
#     print(m, " * ", n, "= ", (m * n)) # int = , works but + doesn't
#
#
# for i in range (1, 10):
#     for m in range (1, 10):
#         mult (i, m)

# ________________________________________________


# return prac

# def f2(x):
#     a = 3
#     b = 5
#     y = a * x + b
#     print(y)
#
# f2(10)
#
# def quiz():
#     x = int(input("enter x: "))
#     y = int(input("enter y: "))
#     m = input("x + y = ")
#     a = (x + y == m)
#     return a # ?????? why boolean isn't returned
# quiz ()

from functools import reduce
# r = reduce(lambda x, y: x + y, [0, 1, 2, 3, 4])
# print (r)
#
# b = reduce(lambda x, y: x ** y, [3, 3, 3])
# print (b)
# c = reduce(lambda x, y: y+x, ['ab','cd','de','fd'])
# print (c)
#
# r = map(lambda x,y: x + y, range(10))
# print (r)

# forms:
# lambda 매개변수 : 표현식
# map(함수, 리스트)
# reduce(함수, 시퀀스)
# filter(함수, 리스트)

#k = list(filter(lambda x: x % 4 != 2,  range(10)))
#print (k)


# 문자열 PRAC





aaa = [1,3,2,4,6,7,8,9,10,1]
print (aaa[:-1])
