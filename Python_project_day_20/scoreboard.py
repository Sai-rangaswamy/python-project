from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.score = 0
        self.color("white")
        self.goto(0, 270)
        self.pendown()
        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.clear()
        self.write(f"SCORE ; {self.score}", align="center", font=("Arial", 10, "bold"))

    def increase_score(self):
        self.score += 1
        self.update_score()

    def game_over(self):
        self.penup()
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Arial", 20, "bold"))
