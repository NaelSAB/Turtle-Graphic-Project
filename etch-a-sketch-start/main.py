from turtle import Turtle, Screen

sam = Turtle()
screen = Screen()


def move_forwards():
    sam.forward(10)

def move_right():
    sam.right(10)

def move_left():
    sam.left(10)

def move_back():
    sam.back(10)

def clean_screen():
    sam.clear()
    sam.penup()
    sam.home()
    sam.pendown()

screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_back)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="c", fun=clean_screen)
screen.exitonclick()
