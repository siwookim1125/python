# 학생
#  속성은 공통과목점수들로. 몇개.
#
#  constructor는 과목 속성들을 binding 할수 있게 만들고,
#
#  method는 시험.으로. 과목 속성들 점수를 바꾸는 기능
#
#
# 하위클래스
#  컴퓨터공학부 학생
#  경제학부 학생
#  건축학부 학생
#
# 각 학부에 맞도록 추가적인 전공과목 한개씩 추가
# method 내용 overwritting


class student:
    math = 90
    english = 100
    chemistry = 85
    economics = 95

    def mathscore(self):
        return (95)

    def study(self):
        self.math += 5


jina = student()
rob = student()

import oop
jina.mathscore()

#class universitystudent(student):
    #...
