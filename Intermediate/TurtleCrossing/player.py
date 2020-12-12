from turtle import  Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.color("green")
        self.goto(STARTING_POSITION)

    def cross_road(self):
        if self.ycor() > 280:
            self.goto(STARTING_POSITION)
            return True

    def move_forward(self):
        new_y = self.ycor() + 10
        self.goto(self.xcor(), new_y)

