import random
from turtle import Turtle

COLORS = ["red","orange","yellow","green","purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager():
    def __init__(self):
        self.all_cars = []

        self.moving_distance = STARTING_MOVE_DISTANCE
    
    def create_car(self):
        random_chance = random.randint(1,6)
        if random_chance==1:
            random_y = random.randint(-250,250)

            car = Turtle()
            car.shape("square")
            car.shapesize(stretch_wid=1,stretch_len=2)
            car.color(random.choice(COLORS))
            car.penup()
            car.goto(300,random_y)
            car.seth(180)
            
            self.all_cars.append(car)

    def move_car(self):
        for car in self.all_cars:
            car.forward(self.moving_distance)

    def update_car_speed(self):
        self.moving_distance += MOVE_INCREMENT