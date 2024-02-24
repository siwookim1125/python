class Student:
    def __init__(self, age=0, gender="", nation="", school="NYU", major="", testscore=0):
        self.age = age
        self.gender = gender
        self.nation = nation
        self.school = school
        self.major = major
        self.testscore = testscore
    def study(self):
        self.testscore += 5
        print (f"I studied hard, so my final testscore grew up by 5%. it is now {self.testscore}%!")
        return self.testscore
    def statement(self):
        print("I am still deciding my major.")
class CSStudent(Student):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.school = "NYU Tandon"
        self.major = "Computer Science"
    def statement(self):
        print("I will major in CS.")

    def binary(self):
        print ("1000101010110101010101.....")
class BusinessStudent(Student):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.school = "NYU Stern"
        self.major = "Business"
    def statement(self):
        print("I will major in Business.")

    def valuation(self):
        print ("The internal rate of return of this firm is 30%.")
class MathStudent(Student):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.school = "NYU CAS"
        self.major = "Math"

    def statement(self):
        print("I will major in Math.")

    def calculus(self):
        print ("The answer to this question is x^2 + 2x + C.")
class LiberalStudent(Student):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.school = "NYU-undecided"
    def statement(self):
        super().statement()
        print("However, I wish to major in economics.")

    def consider(self):
        print ("I like math, but I like English too.")

class Graduation:
    def bachelor(self, **credits):
        credit_details = ", ".join([f"{key}: {value}" for key, value in credits.items()])
        return f"Congratulations! You've earned a bachelor's degree with {credit_details}, at NYU."

Richard = LiberalStudent(age=20, gender="male", nation="United States", school="NYU", major="-", testscore=80)
print("About Richard:"
      "\n age: "+ str(Richard.age) +
      "\n gender: "+ Richard.gender +
      "\n nation: "+ Richard.nation +
      "\n School: "+ Richard.school +
      "\n major: "+ Richard.major +
      "\n Mid-term testscore: " + str(Richard.testscore) + "%\n"
      )
Richard.statement()
print ("\n...\n")
Richard.consider()
print ("\n...\n")
Richard.study()
print ("\n"+"="*50)

Charles = MathStudent(age=22, gender="male", nation="China", school="NYU", major="Math", testscore=94.5)
print("About Charles:"
      "\n age: "+ str(Charles.age) +
      "\n gender: "+ Charles.gender +
      "\n nation: "+ Charles.nation +
      "\n School: "+ Charles.school +
      "\n major: "+ Charles.major +
      "\n Mid-term testscore: " + str(Charles.testscore) + "%\n"
      )
Charles.statement()
print ("\n...\n")
Charles.calculus()
print ("\n...\n")
Charles.study()
print ("\n"+"="*50)

Jane = CSStudent(age=21, gender="female", nation="Poland", school="NYU", major="CS", testscore=83)
print("About Jane:"
      "\n age: "+ str(Jane.age) +
      "\n gender: "+ Jane.gender +
      "\n nation: "+ Jane.nation +
      "\n School: "+ Jane.school +
      "\n major: "+ Jane.major +
      "\n Mid-term testscore: " + str(Jane.testscore) + "%\n"
      )
Jane.statement()
print ("\n...\n")
Jane.binary()
print ("\n...\n")
Jane.study()
print ("\n"+"="*50)

Siwoo = BusinessStudent(age=20, gender="male", nation="Korea", school="NYU", major="Business", testscore=95)
print("About Siwoo:"
      "\n age: "+ str(Siwoo.age) +
      "\n gender: "+ Siwoo.gender +
      "\n nation: "+ Siwoo.nation +
      "\n School: "+ Siwoo.school +
      "\n major: "+ Siwoo.major +
      "\n Mid-term testscore: " + str(Siwoo.testscore) + "%\n"
      )
Siwoo.statement()
print ("\n...\n")
Siwoo.valuation()
print ("\n...\n")
Siwoo.study()
print ("\n"+"="*200)


Siwoo = Graduation()
print ("\n\n\n\n\n\t\t\t\t\t\t\t\t\t\t\tSiwoo's Graduation Certificate: \n\n\n")
print(Siwoo.bachelor(GPA="3.9", Major="Business", Honors = "Summa Cum Laude"))