from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("Black")
        self.goto(-200, 250)

    def write_level(self, level):
        self.clear()
        self.write(f"Level: {level}", False, "center", FONT)

    def game_over(self):
        self.home()
        self.write("Game Over", False, "center", FONT)
