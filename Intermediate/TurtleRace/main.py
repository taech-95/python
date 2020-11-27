from turtle import Turtle, Screen
from random import *
# turtle = Turtle(shape="turtle")
screen = Screen()
screen.setup(width=600, height=600)

# 1 challenge from day 19
#
# def move_forward():
#     turtle.forward(10)
#
#
# def move_backward():
#     turtle.back(10)
#
#
# def turn_right():
#     turtle.right(10)
#
#
# def turn_left():
#     turtle.left(10)
#
#
# def clear():
#     turtle.clear()
#     turtle.penup()
#     turtle.home()
#     turtle.pendown()
#
#
# turtle.speed(5)
# turtle.pensize(5)
# screen.listen()
# screen.onkey(turn_left, "Up")
# screen.onkey(turn_right, "Down")
# screen.onkey(move_forward, "Right")
# screen.onkey(move_backward, "Left")
# screen.onkey(clear, "H"


is_race_on = False
all_turtles = []

user_choice = screen.textinput("Make your bet", prompt="Which turtle will win the race. Chose the color ")
colors = ["red", "orange", "yellow", "blue", "green", "purple"]
start_x = -250
start_y = -150

for turtle in range(0, 6):
    turtle = Turtle(shape="turtle")
    all_turtles.append(turtle)
    turtle.penup()
    turtle_color = choice(colors)
    turtle.color(turtle_color)
    colors.remove(turtle_color)
    turtle.goto(x=start_x, y=start_y)
    start_y += 75

if user_choice:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() >= 270:
            winning_color = turtle.pencolor()
            if user_choice == winning_color:
                print("You win !!!")
            else:
                print(f"You Lose, the winner color is {turtle.pencolor()}")
            is_race_on = False

        rand_distance: int = randint(2, 13)
        turtle.forward(rand_distance)

screen.exitonclick()
# print(user_choice)


# turtle.goto(x=-250, y=-200)
