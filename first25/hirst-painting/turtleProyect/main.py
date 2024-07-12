from turtle import *
import turtle as t
from random import *
import random as random

tim = t.Turtle()
tim.speed("fastest")

t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

def draw_spirograph(gap):
    for _ in range(int(360 / gap)):
        tim.circle(100)
        tim.setheading(tim.heading() + gap)
        tim.color(random_color())
draw_spirograph(5)
        
""" timmy = t.Turtle()
 """
    
"""""
angle = 3
while angle < 10:
    for _ in range(0, angle): 
        timmy.fd(50)
        timmy.rt(360/angle)
    timmy.color(r.choice(colours))
    angle += 1 """

""" 
grade = [0, 90, 180, 270]
timmy.speed("fastest")
timmy.pensize(5)

for _ in range(100):
    timmy.setheading(random.choice(grade))
    timmy.fd(38)
    timmy.color(random_color())
"""    
screen = Screen()
screen.exitonclick()

