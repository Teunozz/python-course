from turtle import Turtle, Screen
import random

screen = Screen()
screen.colormode(255)

rinus = Turtle()


def gen():
    return random.randint(0, 255)


sides = 3
for _ in range(7):
    rinus.pencolor(gen(), gen(), gen())
    for _ in range(sides):
        rinus.forward(100)
        rinus.left(360 / sides)
    sides += 1

screen.exitonclick()
