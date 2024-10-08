from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.all_cars = []
        self.count = 0
        self.car_speed = STARTING_MOVE_DISTANCE
        
    def create_car(self):    
        new_car = Turtle("square")
        new_car.color(random.choice(COLORS))
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.penup()
        new_car.goto(300, random.randint(-250, 250))
        self.all_cars.append(new_car)

    def move_car(self):
        for car in self.all_cars:
            car.backward(self.car_speed)
        self.count += 1
        if self.count % 6 == 0:
            self.create_car()
    
    def fast_car(self):
        self.car_speed += MOVE_INCREMENT
        
            