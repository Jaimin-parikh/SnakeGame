from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.tracer(0)

screen.setup(width=600, height=600)
screen.bgcolor("black")

game_flag = True
snake = Snake()
food = Food()
sb = ScoreBoard()


while game_flag:
    snake.move()
    screen.update()
    time.sleep(0.1)
    if snake.head.distance(food) < 15:
        food.hideturtle()
        food = Food()
        snake.extend()
        sb.score_tracker()

    if snake.head.xcor() <= -280 or snake.head.xcor() >= 280 or snake.head.ycor() <= -280 or snake.head.ycor() >= 280:
        game_flag = False
        sb.game_over()
    for seg in snake.segments[1::]:
        if snake.head.distance(seg) < 10:
            game_flag = False
            sb.game_over()
screen.exitonclick()
