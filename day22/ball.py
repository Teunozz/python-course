from turtle import Turtle

SPEED = 10


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.goto((0, 0))

        self.delta_x = SPEED
        self.delta_y = SPEED

        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.delta_x
        new_y = self.ycor() + self.delta_y
        self.goto(new_x, new_y)

    def flip_y(self):
        self.delta_y *= -1

    def flip_x(self):
        self.delta_x *= -1
        self.move_speed *= 0.9

    def reset(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.flip_x()
