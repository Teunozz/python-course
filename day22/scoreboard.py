from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 48, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.goto(0, 230)
        self.write_score()

    def increase_l_score(self):
        self.l_score += 1
        self.write_score()

    def increase_r_score(self):
        self.r_score += 1
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"{self.l_score} : {self.r_score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over!", align=ALIGNMENT, font=FONT)
