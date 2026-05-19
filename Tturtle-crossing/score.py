from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(-230, 260)
        self.update()

    def update(self):
        self.clear()
        self.write(f"level: {self.level}", False,'center', ('Consolas', 20, 'normal'))

    def add(self):
        self.level += 1
        self.update()

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", False,'center', ("Consolas", 20, "normal"))
