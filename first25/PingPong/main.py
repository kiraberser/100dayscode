from turtle import Screen;
from paddle import Paddle;
from ball import Ball;
import time 
from scoreboard import Scoreboard;


#Posición de la screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Ping Pong Game")
screen.tracer(0)

r_paddle = Paddle((360, 0))
l_paddle = Paddle((-360, 0))

ball = Ball()
scoreboard = Scoreboard()

screen.listen()

#movement
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    #Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.rebot_y()
    #Detect collision with ball 
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.rebot_x()
    #Detect R paddle misses
    if ball.xcor() > 390:
        ball.reset_position()
        scoreboard.l_point()
    #Detect L paddle misses:
    if ball.xcor() < -390:
        ball.reset_position()
        scoreboard.r_point()
    
screen.exitonclick()