# 제어와 반복 연습.

# 정수를 입력받아서 1부터 입력받은 정수까지의 5의 배수의 합을 구하여 출력하는 프로그램을 작성하시오.
# 입력 43
# 5, 10, 15, 20 ... 40

# 반복 (i값이 1부터 1씩 증가한다)
#     i가 5의 배수일때,
#         i값을 result에 누적한다.
#
# result 누적값 출력

# input = input()
# input = int(input)
#
# x = 0
# for i in range(input):
#     if i % 5 == 0:
#         x += i
#
# print(x)

#10개의 정수를 입력받아 입력받은 수들 중 짝수의 개수와 홀수의 개수를 각각 구하여 출력하는 프로그램을 작성하시오.

# 정수를 10회 입력받는다.
# - 10회 반복하며 정수를 입력받는다.
# - 입력받은 정수는 list 에 저장한다.
#
# list에 저장된 정수의 짝수 홀수 갯수를 카운팅.
# - list를 순차탐색하며 홀수일때, 홀수갯수 증가, 짝수일때 갯수갯수 증가.

# 반복 10회
#     정수 입력받기
#     list에 저장하기
#
# 반복 in list
#     list 값이 짝수일때,
#         짝수 갯수 증가
#     list 값이 홀수일때,
#         홀수 갯수 증가
#
# 짝수 갯수, 홀수갯수 출력


# lista = []
# counta = 0
# for i in range (10):
#     lista.append(int(input()))
#
# for i in range (10):
#     if lista [i] % 2 == 0:
#         counta +=1
#
# print ("even: " + str(counta) + ", odd: " + str(10-counta))



# 한 개의 자연수를 입력받아 그 수의 배수를 차례로 10개 출력하는 프로그램을 작성하시오.

# 정수 입력
#
# 반복 10회 i값 1씩 증가
#     i과 입력받은 정수 곱하여 출력

#input int

#in range of 10
    #multiply input value from 1-10

# x = input()
# for i in range (10):
#     print (i * x)


#자연수 n을 입력받아 출력예와 같이 출력되는 프로그램을 작성하시오.

# 3
# ⁕
# ⁕⁕
# ⁕⁕⁕
# ⁕⁕
# ⁕

