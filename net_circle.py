from turtle import Turtle

class Net(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.speed("fastest")
        self.pu()
        self.goto(0, -645)
        self.setheading(90)
        self.shapesize(stretch_len=24, stretch_wid=1)
        
    def move_forward(self):
        self.pd()
        self.forward(1300)
        
        
class Circle(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.speed("fastest")
        self.pu()
        self.goto(0, -188)
        self.pd()
        self.circle(188)