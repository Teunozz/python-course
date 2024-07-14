from turtle import Turtle


class Car(Turtle):
    def __init__(self, position, color):
        super().__init__()
        self.penup()
        self.color(color)
        self.shape("square")
        self.shapesize(stretch_len=2, stretch_wid=1)
        self.goto(position)
        self.setheading(180)

    def move(self, speed):
        self.forward(speed)
