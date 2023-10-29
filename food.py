from turtle import Turtle
from random import randint


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.color("blue")
        self.shape("circle")
        self.shapesize(stretch_wid=0.6, stretch_len=0.6)
        self.pu()
        x_cor = randint(-280, 280)
        y_cor = randint(-280, 280)
        position = (x_cor, y_cor)
        self.setpos(position)
