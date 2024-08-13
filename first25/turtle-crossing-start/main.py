import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

#Create the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

#create Player
player = Player()

#create Car
car_manager = CarManager()

#create scoreboard
scoreboard = Scoreboard()

screen.listen()

#movement 
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    #scoreboard
    scoreboard.update_scoreboard()
    if player.finish():
        car_manager.fast_car()
        scoreboard.increase_level()
    else: 
        car_manager.move_car()
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()
screen.exitonclick()