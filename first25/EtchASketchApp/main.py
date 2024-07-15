from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []

def game(x, y):
    is_race_on = False
    for turtle_index in range(0, 6):
        new_turtle = Turtle(shape="turtle")
        new_turtle.penup()
        new_turtle.goto(x, y)
        new_turtle.color(colors[turtle_index])
        y += 30
        turtles.append(new_turtle)
    if user_bet:
        is_race_on = True
        while is_race_on:
            for turtle in turtles: 
                if turtle.xcor() > 230:
                    is_race_on = False
                    winning_color = turtle.pencolor()
                    if winning_color == user_bet:
                        print(f"You've won! The {winning_color} turtle is the winner!")
                    else:
                        print(f"You've lost! The {winning_color} is the winner!")
                random_x = randint(0, 10)
                turtle.forward(random_x)
game(x=-230, y=-100)
screen.exitonclick()
