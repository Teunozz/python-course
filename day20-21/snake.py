from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for i in range(0, 3):
            self.add_segment((i * -20, 0))

    def add_segment(self, position):
        segment = Turtle(shape="square")
        segment.color("white")
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            if seg_num != 0:
                new_x = self.segments[seg_num - 1].xcor()
                new_y = self.segments[seg_num - 1].ycor()
                self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def setheading(self, heading: int):
        self.head.setheading(heading)

    def up(self):
        if self.head.heading() != DOWN:
            self.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.setheading(RIGHT)