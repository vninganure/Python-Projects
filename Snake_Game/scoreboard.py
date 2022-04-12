from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Arial', 24, 'normal')
CDENTER = 0

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("White")
        self.penup()
        self.goto(CDENTER, 260)
        self.hideturtle()
        self.display_score()

    def display_score(self):
        self.write(f"Score= {self.score}", True, ALIGNMENT, FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.display_score()





