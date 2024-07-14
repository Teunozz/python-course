from turtle import Turtle, Screen
import random
import colorgram

colors = colorgram.extract("shit_painting.jpg", 30)
color_tuples = []
for color in colors:
    rgb = color.rgb
    color_tuples.append((rgb.r, rgb.g, rgb.b))

screen = Screen()
screen.colormode(255)

rinus = Turtle()
rinus.speed(0)
rinus.pensize(0)
rinus.penup()
rinus.hideturtle()

rinus.goto(-350, -350)

for _ in range(10):
    for _ in range(10):
        rinus.fillcolor(random.choice(color_tuples))
        rinus.dot(20, random.choice(color_tuples))
        rinus.forward(70)
    rinus.backward(700)
    rinus.left(90)
    rinus.forward(70)
    rinus.right(90)

screen.exitonclick()
