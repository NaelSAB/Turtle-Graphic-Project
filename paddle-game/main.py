from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from score import Score
import time

screen = Screen()
screen.setup(1200,600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

def middle_line():
    line = Turtle()
    line.color("white")
    line.penup()
    line.goto(0, 300)
    line.pendown()
    line.setheading(270)
    line.hideturtle()
    for _ in range(0, 16):
        line.pendown()
        line.forward(20)
        line.penup()
        line.forward(20)


paddles = Paddle()
ball = Ball()
screen.listen()
score = Score()
screen.onkeypress(paddles.player1_start_up, "Up")
screen.onkeyrelease(paddles.player1_stop_up, "Up")
screen.onkeypress(paddles.player1_start_down, "Down")
screen.onkeyrelease(paddles.player1_stop_down, "Down")
screen.onkeypress(paddles.player2_start_up, "w")
screen.onkeyrelease(paddles.player2_stop_up, "w")
screen.onkeypress(paddles.player2_start_down, "s")
screen.onkeyrelease(paddles.player2_stop_down, "s")
middle_line()


Is_game_on = True
while Is_game_on:
    screen.update()
    time.sleep(0.01)

    if paddles.player1_move_up and paddles.paddles["player1"].ycor() < 250:
        paddles.go_up("player1")
    if paddles.player1_move_down and paddles.paddles["player1"].ycor() > -250:
        paddles.go_down("player1")
    if paddles.player2_move_up and paddles.paddles["player2"].ycor() < 250:
        paddles.go_up("player2")
    if paddles.player2_move_down and paddles.paddles["player2"].ycor() > -250:
        paddles.go_down("player2")
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(paddles.paddles["player2"]) < 50 and ball.xcor() < -540 or ball.distance(paddles.paddles["player1"]) < 50 and ball.xcor() < 540:
        ball.bounce_x()

    if ball.xcor() > 580:
        ball.new_round("player2")
        score.add("r")
        score.update()

    if ball.xcor() < -580:
        ball.new_round("player1")
        score.add("l")
        score.update()

screen.exitonclick()