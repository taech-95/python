from turtle import Turtle

ALIGN = "center"
# tuple[str, int, str]
FONT = ("Arial", 16, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        with open("highscore.txt") as data:
              self.highscore = int(data.read())
        # self.highscore = 0
        self.color("white")
        self.hideturtle()
        self.score = 0
        self.goto(0, 275)
        self.write_score()

    def write_score(self):
     
        self.write(f"Your Score is :  {self.score}, Highscore is: {self.highscore}", False, ALIGN, font=FONT)

    def increase_score(self):
        self.clear()
        self.score += 1
        self.write_score()

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("highscore.txt", mode="w") as data:
                data.write(f"{self.highscore}")
        self.score = 0
        self.clear()
        self.write_score()


    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("Game Over", False, ALIGN, FONT)
