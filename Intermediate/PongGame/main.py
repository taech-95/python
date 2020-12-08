from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
scoreboard = Scoreboard()
user_paddle = Paddle((350, 0))
computer_paddle = Paddle((-350, 0))
ball = Ball()
screen.listen()
screen.onkey(user_paddle.go_up, "Up")
screen.onkey(user_paddle.go_down, "Down")

screen.onkey(computer_paddle.go_up, "w")
screen.onkey(computer_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.05)
    ball.move()
    screen.update()

    if ball.ycor() > 270 or ball.ycor() < -270:
        # відбиття від поверхні
        ball.bounce_y()
    # відбиття від поверхні гравців
    if ball.distance(user_paddle) < 50 and ball.xcor() > 320 or ball.distance(computer_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        ball.increase_speed()

    if ball.xcor() > 380:
        ball.reset_position()
        ball.reset_speed()
        scoreboard.l_increase()
    if ball.xcor() < -380:
        ball.reset_position()
        ball.reset_speed()
        scoreboard.r_increase()
    else:
        pass

screen.exitonclick()
