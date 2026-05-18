from math import radians
from turtle import Turtle
import random
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.new_round("player")

    def new_round(self, paddle_holder):
        self.goto(0,0)
        self.x_move = 10
        self.y_move = 10
        if paddle_holder == "player1":
            self.x_move *= -1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
