from turtle import Turtle, Screen
import random

screen = Screen()
screen.colormode(255)

rinus = Turtle()
rinus.pensize(5)
rinus.speed(0)

angles = [0, 90, 180, 270]


def random_color_gen():
    return random.randint(0, 255)


while True:
    rinus.pencolor((random_color_gen(), random_color_gen(), random_color_gen()))
    rinus.left(random.choice(angles))
    rinus.forward(10)
