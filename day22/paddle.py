from turtle import Turtle

SPEED = 20


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(stretch_len=1.0, stretch_wid=5.0)
        self.goto(position)

    def up(self):
        self.goto(x=self.xcor(), y=self.ycor() + SPEED)

    def down(self):
        self.goto(x=self.xcor(), y=self.ycor() - SPEED)
