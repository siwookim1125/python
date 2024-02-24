import string


class Car:
    color="black"
    kind="electric"
    topspeed=300
    curspeed=0

    def __init__(self,color,kind):
        self.color = color
        self.kind = kind
        if self.kind == "electric" :
            self.topspeed = 300
        else:
            self.topspeed = 100

    def drive(self):
        self.curspeed = self.curspeed + 10
        return self.curspeed;

# models = Car()
# print(
#     models.__str__()
#     # models.color +", "+ models.kind + ", " + str(models.topspeed)
# )
# model3 = Car("white", "gasoline")
# print(
#     model3.color +", "+ model3.kind + ", " + str(model3.topspeed) + ", " + str(model3.curspeed)
# )
# model3.drive()
# print(
#     model3.color +", "+ model3.kind + ", " + str(model3.topspeed) + ", " + str(model3.curspeed)
# )

class Tesla(Car):
    battery = 70
    fsdkind = "none"

    def __init__(self,battery,fsd, color):
        Car.color = color
        Car.kind = "electric"
        self.battery = battery
        self.fsdkind = fsd
    def fsd(self):
        if self.kind == "full":
            return "do not drive your self!!"
        elif self.kind == "half":
            return "do concentrate!"
        else :
            return "drive your self!"

modelY = Tesla(150, "full", "black")
print(
    modelY.color +", "+ modelY.kind + ", " + str(modelY.topspeed) + ", " + str(modelY.curspeed)
    +"\n"+ str(modelY.battery) + ", " + str(modelY.fsdkind)
)