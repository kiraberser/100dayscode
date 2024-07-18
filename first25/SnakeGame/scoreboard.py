from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.score = 0
        self.penup()
        self.goto(0, 260)
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.write(f"Score = {self.score}", align="center", font=("Arial", 24, "normal"))
    
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
        
    def game_over(self):
        self.hideturtle()
        self.goto(0, 0)
        self.write("Game over.", align="center", font=("Arial", 24, "normal"))
    
        