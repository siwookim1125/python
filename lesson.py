import numpy as np # numpy 패키지 로드하여 np로 사용
# 리스트에서 행렬생성
# a = [
#       [1,2,3]
#     , [4,5,6]
# ]
# b = np.array(a)
# print(b[0,0])
#
# print(b.ndim)
#
# print(b.shape)


# print(np.arange(10)) # 1씩 증가하는 1차원 배열(시작이 0부터)
# print(np.arange(2,10))

# print(np.zeros((2,2)))  # 영행렬 생성
# print(np.ones((2,3)))  # 유닛행렬
#
# print(np.full((2,3), 5)) # 모든 원소가 5인 2*3행렬 얘로 주로 씀.
# print(np.eye(3)) # 단위행렬

# a = np.arange(21)
# print(a)
# b = a.reshape((3,7))
# print(b)

# lst = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# arr = np.array(lst)
# print(arr)
#
# list = np.arange(1,10)
# brr = list.reshape(3,3)
# print(brr)
#
# a = brr[:2,:]
# print(a)

# lst = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# arr = np.array(lst)
# arr = arr[:2,:2]
# print(arr)
#
# list = np.arange(1,10)
# brr = list.reshape(3,3)
# brr = brr[:2,:2]
# print(brr)
#
# c = arr ^ 2 #
# print(c)

# a = np.array([1,2,3])
# b = np.array([4,5,6])
#
# # 각 요소 더하기
# c = a + b
# c= np.add(a, b)
# print(c) # [-3 -3 -3]
#
# # 각 요소 곱하기
# # c = a*b
# c = np.multiply(a, b)
# print(c) #[4 10 18]
#
# # 각 요소 나누기
# # c = a/b
# c = np.divide(a,b)
# print(c) # [0.25 0.4 0.5]

# arr1 = [
#     [1,2],
#     [1,10]
# ]
# arr2 = [
#     [5,6],
#     [7,8]
# ]
# a = np.array(arr1)
# b = np.array(arr2)
#
# #c = a * b
# c = np.dot(a, b)
# print(c)

#d = a ^ 2 # 행렬 곱이 아니네
# print(d)

# # 모든 원소의 합
# print(a.sum())
# # 모든 원소의 곱
# print(a.prod())
# # 모든 원소의 편차
# print(a.std())
# # 모든 원소의 평균
# print(a.mean())

# 난수 매트릭스
# x = np.random.uniform(size=25)
# x.reshape(5,5)
# print(x)

# 정규분포

s = np.random.normal(0, 1, 1000)

import matplotlib.pyplot as plt
plt.hist(s)
plt.show()

print('test')