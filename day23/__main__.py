import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
step = 0
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.add_car()
    car_manager.move_cars()

    if car_manager.check_collision(player):
        scoreboard.game_over()
        game_is_on = False

    if player.has_finished():
        player.reset()
        car_manager.increase_speed()
        scoreboard.increase_level()

    step += 1

screen.exitonclick()
