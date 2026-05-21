import turtle
import pandas
from numpy.ma.core import squeeze

screen = turtle.Screen()
screen.title("U.S. States")
image = "blank_states_img.gif"
screen.addshape(image)
screen.setup(725, 491)
turtle.shape(image)
data = pandas.read_csv("50_states.csv")
states_list = data.state.str.lower().to_list()
try:
    data_answers = pandas.read_csv("answers_data.csv")
except FileNotFoundError:
    data_answers = pandas.DataFrame(columns=["state", "x", "y"])
answers_list= []

def add_state(data):
    answer_letter = turtle.Turtle()
    answer_letter.penup()
    answer_letter.hideturtle()
    answer_letter.goto(data.x, data.y)
    answer_letter.write(data.state)
    answers_list.append(data)

def save_answer(list):
    answer_data = pandas.DataFrame(list)
    answer_data.to_csv("answers_data.csv", index=False)

def get_answers():
    for _, data in data_answers.iterrows():
        add_state(data)

get_answers()
score = len(answers_list)
while len(answers_list) < 50:
    answer_state = screen.textinput(title=f"Guess the State {score}/50", prompt="what's another state's name?").lower()
    if answer_state in states_list:
        state_data = data[data.state.str.lower() == answer_state].squeeze()
        print(type(state_data))
        add_state(state_data)
        save_answer(answers_list)
        score = len(answers_list)

screen.exitonclick()
