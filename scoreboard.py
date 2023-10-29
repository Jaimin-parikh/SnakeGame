from turtle import Turtle

FONT = ("Courier", 20, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        self.score = 0
        super().__init__()
        self.pu()
        self.sety(270)
        self.hideturtle()
        self.color("white")
        self.write(arg="Score : 0", move=False, align="center", font=FONT)

    def score_tracker(self):
        self.clear()
        self.score += 1
        self.write(arg=f"Score : {self.score}", move=False, align="center", font=FONT)

    def game_over(self):
        self.setpos(0,0)
        self.write(arg="Game Over!!", move=False, align="center", font=FONT)
