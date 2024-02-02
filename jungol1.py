#3-3

# x input
# loop i until input
# when i = 1, print * i times
# when i = 2, print * i times
# when i = 3, print * i times

# print * x times until x = 0

# x = int(input())
# for i in range (x + 1):
#         print ("*" * i)
#
# for i in range (x):
#     print ("*" * (x-i-1))


#3-4

# structure:
# n+2
# spce, n, spce
# spce, spce, n-2, spce, spce
# # spce, n, spce
# n+2

# x = input
# x = x + 2
# for i in range x:
#   print "*" x times
#   x = x - 2

# x = int(input()) + 2
# y = x - 2
# s = y

# for i in range (x):
#     print (" " * (i) + "*" * x + " " * (i))
#     x = x - 2
# for i in range (s-1):
#     print (" " * (y-2-2*i) + "*" * s + " " * (y-2-2*i))
#     s = s + 2
# issue with this pattern

# 3-9
# #
# ##
# ###
#  ##
#   #

# input = 3

# x = int(input())
# for i in range (x+1):
#     print ("#"* i)
#
# for i in range (x-1):
#     print (" "*(i+1)+"#"*(x-(i+1)))

#문자열 2-3

# a = []
# n = 0
# x = input()
# a.extend(x)
# print (a)
# size = len(a)
# for i in range (size):
#     for n in range (size):
#         if (i >= size):
#             i = i-i
#         print (a[i])
#         i += 1
#     print ("\n")

# i = from 0 to len of list
# another loop from 0 to len of list


#배열1 형성1

#input 10
#append 10 str to a list
# for 0 in range 10
#   print list [10[i]

# a = []
# for i in range (10):
#     a.append (input())
# print (a)
#
# for i in range (0, 10):
#     print (a[(9-i)])

# 100 inputs
# for i from 0 to 100,
#   if -1 input, end loop and print lst[n, n-1, n-2]

#배열1 형평4
# lst = []
# n = 0
# for i in range (100):
#     x = input()
#     lst.append(x)
#     if x == "-1":
#         print(lst[i-1] + ", " + lst[i-2] + ", " + lst[i-3])


#리스트2 형평10
#input 5 vocabs
# append them in a list

# for i = 0 to 5
#   if a letter is a substring in any of letters
#       append them to a list
#   elif a phrase is substring
#       append them to a list


# lst = []
# lst2 = []
#
# for i in range (5):
#     x = input()
#     lst.append(x)
# print ("letter")
# l = input()
# print ("phrase")
# p = input()
#
# for i in range(5):
#     if l in lst[i]:
#         lst2.append(lst[i])
#     elif p in lst[i]:
#         lst2.append(lst[i])
#
# print (lst2)
#

# 리스트 3 형성평가 2

# input x <-- becomes the size of list
# input y <-- becomes factor

# x = int(input())
# y = int(input())
# lst = []
# for i in range (x):
#     if (i % y == 0):
#         lst.append("True")
#     else:
#         lst.append("False")
#
# print (lst)

