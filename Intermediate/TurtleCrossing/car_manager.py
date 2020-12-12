from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(1,3)
        self.setheading(-180)
        self.car_position()
        self.color(random.choice(COLORS))

    def reset_position(self):
            new_x = random.randint(150,300)
            self.goto(new_x, self.ycor())

    def increase_speed(self):
        new_speed = STARTING_MOVE_DISTANCE + MOVE_INCREMENT
        self.forward(new_speed)

    def car_move_forward(self):
        self.forward(STARTING_MOVE_DISTANCE)

    def car_position(self):
        car_x = random.randint(-100, 250)
        car_y = random.randint(-200, 200)
        self.goto(car_x, car_y)
