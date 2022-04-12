import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. State Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_state = []


while len(guessed_state)<51:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/50 correct state", prompt="whats the another state name?").title()

    if answer_state == "Exit":
        unguessed_state = [n for n in all_states if n not in guessed_state]
        df = pandas.DataFrame(unguessed_state)
        df.to_csv("learn_new_states.csv")
        break
    if answer_state in all_states:
        guessed_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)






