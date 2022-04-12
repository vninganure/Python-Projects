from turtle import Turtle, Screen
import random


screen = Screen()
is_race_on = False
screen.setup(width=500, height=400)
bet = screen.textinput(title="Make a guess", prompt="Choose one color and bet on it!")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
ax = 70
turtle_set = []

for i in range(0,6):
    new_turtle = Turtle("turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=ax)
    ax = ax-30
    turtle_set.append(new_turtle)

if bet:
    is_race_on = True

while is_race_on:
    for turtle in turtle_set:
        turtle.forward(random.randint(0,10))
        if turtle.xcor() > 230:
            winning_turtle = turtle.pencolor()
            if winning_turtle == bet:
                print(f"Hey you have won the race, the {winning_turtle} color turtle is winner!!")
            else:
                print(f"Hey you have lost the race, the {winning_turtle} color turtle is winner!!")
            is_race_on = False


screen.exitonclick()
