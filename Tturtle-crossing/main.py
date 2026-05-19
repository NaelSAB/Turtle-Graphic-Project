import turtle
from math import trunc
from turtle import Screen
from car import Cars
from player import Player
from score import Score
import time

def is_player_hit_the_car(car):
    if ((abs(player.xcor() - car.xcor()) < 30 and abs(player.ycor() - car.ycor()) < 20)):
        return True
    else:
        return False

screen = Screen()

screen.setup(600,600)
screen.title("Turtle Crossing")
screen.tracer(0)

player = Player()
car_manager = Cars()
score = Score()

screen.listen()
screen.onkey(player.move, "w")

Is_game_on = True

while (Is_game_on):
    time.sleep(0.1)
    screen.update()
    for car in car_manager.all_cars:
        if (is_player_hit_the_car(car)):
            Is_game_on = False
            score.game_over()

    if player.ycor() > 300:
        car_manager.cars_speed()
        player.go_back()
        score.add()
    car_manager.create_car()
    car_manager.move_cars()

screen.exitonclick()