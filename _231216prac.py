# #list,tuple,looping prac
# list = ['a',
#         'b',
#         'c',
#         'd'
#         ]
# list.insert(1, '0')
# print(list)
# print(len(list))
# del list[3]
# print(list)
# print (max(list)) #ascii로 변환
# print (min(list)) #ascii로 변환
# print(len(list))
# print(list[2:])
# print(list[::2])
# print(list[1::2])
# print(list[::-1])
# print(list[3::-1]) # ??
#
# list2 = ['1',
#          'f',
#          'z',
#          'h'
#          ]
#
# print("\n".join(list[2].join(list2)))
#
# print(sorted(list)+sorted(list2))
# print(sorted(list+list2))
#
#
# tuple = ("t1",
#          "t2",
#          "t3"
#          )
#
# print(type(tuple))
# itypeError = (1)
# print(type(itypeError))
# itypeCorrected = (1,)
# print(type(itypeCorrected))


temptuple = ('ta',
             'tb',
             'tc',
             'td',
             'te',
             'tf',
             'tg'
             )
print(type(temptuple))
print(len(temptuple))

#V = (random.choices(string.ascii_lowercase)) #unpacking
for i in temptuple:
    print(i)

#for loop 다시 배워야할듯.
#changes