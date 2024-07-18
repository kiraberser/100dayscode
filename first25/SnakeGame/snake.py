from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.list = []
        self.create_snake()
        self.head = self.list[0]
        
    def create_snake(self):    
        for position in STARTING_POSITION:
            self.add_segment(position)
    
    def add_segment(self, position):
        new_turtle = Turtle("square")
        new_turtle.penup()
        new_turtle.goto(position)
        new_turtle.color("white")
        self.list.append(new_turtle)
            
    def extend(self):
        #add new segment to the snake
        self.add_segment(self.list[-1].position())
    
    def move(self):
        for segment_new in range(len(self.list) - 1, 0, -1):
            cx = self.list[segment_new - 1].xcor()
            cy = self.list[segment_new - 1].ycor()
            self.list[segment_new].goto(cx, cy)
        self.head.forward(MOVE_DISTANCE)
        
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
        
