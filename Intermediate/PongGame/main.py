from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

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
    time.sleep(0.15)
    ball.move()
    screen.update()

    if ball.ycor() > 280 or ball.ycor() < -280:
        #відбиття від поверхні
        ball.bounce()


screen.exitonclick()
