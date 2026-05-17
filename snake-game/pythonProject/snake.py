from turtle import Turtle
Start_Poss = [(0,0), (-20,0), (-40,0)]
move_distance = 20

class Snake:
    def __init__(self):
        self.snake_len = []
        self.create_snake()
        self.snake_head = self.snake_len[0]

    def create_snake(self):
        for poss in Start_Poss:
            self.add_tail(poss)

    def add_tail(self, poss):
        snake = Turtle(shape="square")
        snake.color("white")
        snake.penup()
        snake.goto(poss)
        self.snake_len.append(snake)

    def extend(self):
        self.add_tail(self.snake_len[-1].position())

    def move(self):
        for snake_num in range(len(self.snake_len) - 1, 0, -1):
            new_x = self.snake_len[snake_num - 1].xcor()
            new_y = self.snake_len[snake_num - 1].ycor()
            self.snake_len[snake_num].goto(new_x, new_y)
        self.snake_head.forward(move_distance)

    def up(self):
        if self.snake_head.heading() != 270:
            self.snake_head.setheading(90)

    def down(self):
        if self.snake_head.heading() != 90:
            self.snake_head.setheading(270)

    def left(self):
        if self.snake_head.heading() != 0:
            self.snake_head.setheading(180)

    def right(self):
        if self.snake_head.heading() != 180:
            self.snake_head.setheading(0)
