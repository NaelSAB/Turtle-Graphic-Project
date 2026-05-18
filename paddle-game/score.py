from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score_r = 0
        self.score_l = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update()

    def update(self):
        self.clear()
        self.goto(-100,200)
        self.write(f"{self.score_l}", False, 'center', ('Arial', 75, 'normal'))
        self.goto(100,200)
        self.write(f"{self.score_r}", False, 'center', ('Arial', 75, 'normal'))

    def add(self, direction):
        if direction == "l":
            self.score_r +=1
        if direction == "r":
            self.score_l +=1
