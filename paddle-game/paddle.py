from turtle import Turtle
from venv import create


class Paddle():

    def __init__(self):
        self.paddles = {"player1": self.create("r"), "player2": self.create("l")}
        self.player1_move_up = False
        self.player1_move_down = False
        self.player2_move_up = False
        self.player2_move_down = False
        self.bot_direction = "up"

    def create(self, player):
        paddle = Turtle(shape="square")
        paddle.penup()
        paddle.color("white")
        paddle.shapesize(stretch_wid=5, stretch_len=1)
        if player == "l":
            paddle.goto(-550, 0)
        else:
            paddle.goto(550, 0)
        return paddle

    def player1_start_up(self):
        self.player1_move_up = True

    def player1_stop_up(self):
        self.player1_move_up = False

    def player1_start_down(self):
        self.player1_move_down = True

    def player1_stop_down(self):
        self.player1_move_down = False

    def player2_start_up(self):
        self.player2_move_up = True

    def player2_stop_up(self):
        self.player2_move_up = False

    def player2_start_down(self):
        self.player2_move_down = True

    def player2_stop_down(self):
        self.player2_move_down = False

    def go_up(self, paddle_holder):
        self.paddles[paddle_holder].sety(self.paddles[paddle_holder].ycor() + 10)

    def go_down(self, paddle_holder):
        self.paddles[paddle_holder].sety(self.paddles[paddle_holder].ycor() - 10)