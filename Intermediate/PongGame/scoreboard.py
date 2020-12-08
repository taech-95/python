from turtle import Turtle
POSITION = "Center"
FONT = ("Arial", 70, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.update()

    def update(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align=POSITION, font=FONT)
        self.goto(100, 200)
        self.write(self.r_score, align=POSITION, font=FONT)



    def l_increase(self):
        self.l_score += 1
        self.update()

    def r_increase(self):
        self.r_score += 1
        self.update()
