import random
from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "bold")
DATA_FILE = "high_score.txt"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.speed(0)
        self.score = 0
        with open(DATA_FILE) as score_file:
            self.high_score = int(score_file.read())
        self.goto(0, 250)
        self.write_score()

    def increase_score(self):
        self.score += 1
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"Score: {self.score}, High score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(DATA_FILE, mode="w") as score_file:
                score_file.write(str(self.high_score))
        self.score = 0
        self.write_score()
