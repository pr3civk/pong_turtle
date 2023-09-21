from turtle import Turtle
from random import choice
from time import sleep


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.pu()
        self.shape("circle")
        self.color("white")
        self.shapesize(1.5, 1.5)
        self.x_move = 4
        self.y_move = 4
        
        
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        sleep(0.01)
        self.goto(new_x, new_y)
    
    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        
    def reset_position(self):
        self.goto(0, 0)
        sleep(0.4)
