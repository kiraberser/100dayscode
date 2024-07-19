from turtle import Turtle, Screen
import time 
from snake import Snake
from food import Food
from scoreboard import Score

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score_count = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score_count.increase_score()
    #Detect collision with wall.
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        score_count.game_over()
        
    for segment in snake.list[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score_count.game_over()
            
    #detect collision with tail.
    #if head collides with any segment in the tail
        #trigger game_over
        
screen.exitonclick()

#slice
        
    

## Tracer, time.sleep(), screen.update(), 