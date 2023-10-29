from turtle import Turtle, Screen

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
screen = Screen()
screen.listen()


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

    def extend(self):
        self.create_snake(self.segments[-1].pos())

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            new_position = self.segments[i - 1].pos()
            self.segments[i].goto(new_position)
        self.head.fd(20)
        screen.onkeypress(self.up, "Up")
        screen.onkeypress(self.down, "Down")
        screen.onkeypress(self.left, "Left")
        screen.onkeypress(self.right, "Right")

    def up(self):
        if self.head.heading() == DOWN:
            pass
        else:
            self.head.seth(UP)

    def down(self):
        if self.head.heading() == UP:
            pass
        else:
            self.head.seth(DOWN)

    def left(self):
        if self.head.heading() == RIGHT:
            pass
        else:
            self.head.seth(LEFT)

    def right(self):
        if self.head.heading() == LEFT:
            pass
        else:
            self.head.seth(RIGHT)
