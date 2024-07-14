import random
from car import Car

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
LEFT_LIMIT = -350


class CarManager:
    def __init__(self):
        self.cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def add_car(self):
        if random.randint(1, 6) == 1:
            color = random.choice(COLORS)
            y_pos = random.randint(-250, 250)
            car = Car((320, y_pos), color)
            self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            car.move(self.speed)

            if car.xcor() < LEFT_LIMIT:
                car.clear()

        self.cars = [car for car in self.cars if car.xcor() > LEFT_LIMIT]

    def check_collision(self, player):
        for car in self.cars:
            if car.distance(player) <= 25:
                return True

        return False

    def increase_speed(self):
        self.speed += MOVE_INCREMENT
