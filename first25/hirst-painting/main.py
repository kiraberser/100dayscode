from turtle import *
import turtle as t
import random 

color_list = [(233, 233, 232), (237, 232, 234), (231, 233, 238), (224, 233, 226), (207, 160, 83), (55, 88, 131), (144, 91, 40), (139, 27, 48), (221, 207, 107), (134, 177, 202), (157, 47, 85), (44, 55, 105), (170, 159, 41), (129, 189, 144), (83, 20, 43), (38, 43, 66), (185, 94, 107), (188, 139, 166), (85, 124, 181), (60, 39, 31), (89, 157, 92), (80, 153, 164), (195, 81, 72), (160, 201, 219), (45, 75, 78), (79, 75, 44), (56, 125, 121), (218, 176, 188), (166, 207, 162), (220, 182, 168)]


tim = t.Turtle()
t.colormode(255)

tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
dot_distance = 100
tim.speed("fastest")


for dot_output in range(1, dot_distance + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)
    if dot_output % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = t.Screen()
screen.exitonclick()