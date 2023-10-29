from turtle import Screen
from snake import Snake
import time

screen = Screen()
screen.tracer(0)

screen.setup(width=600, height=600)
screen.bgcolor("black")


game_flag = True
snake = Snake()

while game_flag:
    snake.move()
    screen.update()
    time.sleep(0.1)


screen.exitonclick()
