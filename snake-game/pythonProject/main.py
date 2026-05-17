from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time

screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up ,"Up")
screen.onkey(snake.down ,"Down")
screen.onkey(snake.left ,"Left")
screen.onkey(snake.right ,"Right")


Is_game_on = True
while Is_game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    if snake.snake_head.distance(food) < 15:
        food.refresh()
        score.add_score()
        snake.extend()

    if snake.snake_head.xcor() > 280 or snake.snake_head.xcor() < -280 or snake.snake_head.ycor() > 280 or snake.snake_head.ycor() < -280:
        Is_game_on = False
        score.game_over()

    for snake_body in snake.snake_len[1:]:
        if snake.snake_head.distance(snake_body) < 10:
            Is_game_on = False
            score.game_over()

screen.exitonclick()