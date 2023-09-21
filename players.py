from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.speed("fastest")
        self.paddle = []
        self.create_shape()

    def create_shape(self):
        self.pu()
        self.shape("square")
        self.shapesize(stretch_wid=8, stretch_len=1.5)
        self.color("white")
        
    def go_up(self):
        if self.ycor() < 340:
            new_y = self.ycor() + 40
            self.goto(self.xcor(), new_y)
    
    def go_down(self):
        if self.ycor() > -340:
            new_y = self.ycor() - 40
            self.goto(self.xcor(), new_y)