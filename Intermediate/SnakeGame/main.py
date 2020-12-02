# Snake Game challenge

from turtle import Turtle, Screen
from snake import Snake
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
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.left, "Left")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
game_is_on = True

while game_is_on:
    time.sleep(0.2)
    screen.update()
    snake.move()


screen.exitonclick()