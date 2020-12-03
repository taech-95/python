# Snake Game challenge

from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

# positions = [(0, 0), (-20, 0), (-40, 0)]
# for position in positions:
#     body = Turtle(shape="square")
#     body.penup()
#     body.color("white")
#     body.goto(position)
# snake_game_segment1 = Turtle(shape="square")
# snake_game_segment1.color("white")
#
# snake_game_segment2 = Turtle(shape="square")
# snake_game_segment2.color("white")
# snake_game_segment2.goto(-20, 0)
#
# snake_game_segment3 = Turtle(shape="square")
# snake_game_segment3.color("white")
# snake_game_segment3.goto(-40, 0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.left, "Left")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
game_is_on = True

while game_is_on:
    time.sleep(0.15)
    screen.update()
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend_snake()
        scoreboard.increase_score()

    # detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        scoreboard.game_over()

    # detect collision with tail
    # for segment  in snake.snake_segments:
        #     #     if segment == snake.head:
        #     #         continue
    for segment in snake.snake_segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()
screen.exitonclick()
