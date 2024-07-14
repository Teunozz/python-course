import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()

screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # Wall collision
    if ball.ycor() >= 290 or ball.ycor() <= -290:
        ball.flip_y()

    # Collision with left paddle
    if ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.flip_x()

    # Collision with right paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.flip_x()

    # Left miss detection
    if ball.xcor() < -380:
        scoreboard.increase_r_score()
        ball.reset()

    # Right miss detection
    if ball.xcor() > 380:
        scoreboard.increase_l_score()
        ball.reset()

screen.exitonclick()
