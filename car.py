from turtle import*
#class 내부에 선언된 변순느 클래스변수 , __init__에 self...로 선언된건 인스턴스 변수이다
class Car:
    def __init__(self, speed, color, model):
        self.speed = speed
        self.color = color
        self.model = model
        self.turtle = Turtle()
        self.turtle.shape("car.gif")

    def drive(self):
        self.turtle.forward(self.speed)

    def leftTurn(self):
        self.turtle.left(90)

    def __str__(self):
        msg = "speed : " + str(self.speed) + "\ncolor : " + self.color + "\nmodel : " + self.model
        return msg

register_shape("car.gif")
myCar = Car(200, "red", "lamborgini")
for i in range(200):
    myCar.drive()
    myCar.leftTurn()

