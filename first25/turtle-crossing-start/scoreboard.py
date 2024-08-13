from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = 1
        self.penup()
        self.goto(-290, 250)
        
    def update_scoreboard(self):
        self.write(f"Level: {self.score}", align="left", font=FONT)
        
    def increase_level(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
    
    def game_over(self):
        self.goto(0, 0)
        self.write("Game over.", align="center", font=FONT)    
