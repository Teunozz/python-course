from turtle import Turtle, Screen
import random

screen = Screen()
screen.colormode(255)

rinus = Turtle()
rinus.speed(0)


def gen():
    return random.randint(0, 255)


for _ in range(60):
    rinus.pencolor(gen(), gen(), gen())
    rinus.circle(100)
    rinus.setheading(rinus.heading() + 6)

screen.exitonclick()
