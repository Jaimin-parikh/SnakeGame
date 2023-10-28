from turtle import Turtle

POSITIONS = [(0, 0), (20, 0), (40, 0)]


class Snake:
    def __init__(self):
        self.segments = []
        for position in POSITIONS:
            self.create_snake(position)
        self.head = self.segments[0]

    def create_snake(self, position):
        t = Turtle(shape="square")
        t.pu()
        t.color("white")
        t.setpos(position)
        self.segments.append(t)

    def move(self):
        for i in range(len(self.segments)-1, 0, -1):
            new_position = self.segments[i-1].pos()
            self.segments[i].goto(new_position)
        self.head.fd(20)
