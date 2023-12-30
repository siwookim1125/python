삼성전자 = 50000
총평가금액 = 삼성전자 * 10
print(총평가금액)

str = "문자열"
print(str)

list = [
    "닥터 스트레인지"
    ,"스플릿"
    ,"럭키"
]

print(list)

list.append("ㅇㅇ")
list.insert(1, "ㅇㅇ")

print(list)


a = [1,2,3,4,5,6,7,8,9]
print(a)

for i in a:
    if i % 2 == 1 :
        print(i)

score = input()
score = int(score)
if 81 < score < 100:
    print('A')
elif 61 < score < 80:
    print('B')
elif 41 < score < 60:
    print('C')
elif 21 < score < 40:
    print('D')
elif 0 < score < 20:
    print('F')
else:
    print('undef')

"""
파이썬 데이터구조.
    숫자, 문자열, 참거짓
    리스트, 튜플, 딕셔너리
파이썬 제어문.
    if 조건식 :
        할일
    elif 조건식 :
        할일2
    else
        할일3
    
    for 이터레이터변수 in 리스트형객체 :
        할일
"""
