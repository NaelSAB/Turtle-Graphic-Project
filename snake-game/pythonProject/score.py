import turtle
from turtle import Turtle

Align = "center"
Font = ('Courier', 20, 'normal')

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.score}", False, Align, Font)

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", False, Align, Font)


    def add_score(self):
        self.score +=1
        self.clear()
        self.update_score()
