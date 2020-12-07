from turtle import Turtle

ALIGN = "center"
# tuple[str, int, str]
FONT = ("Arial", 16, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.score = 0
        self.goto(0, 275)
        self.write_score()

    def write_score(self):
        self.write(f"Your Score is :  {self.score}", False, ALIGN, font=FONT)

    def increase_score(self):
        self.clear()
        self.score += 1
        self.write_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", False, ALIGN, FONT)
