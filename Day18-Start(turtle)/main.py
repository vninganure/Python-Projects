import turtle
from turtle import *
import random
tim = Turtle()

colors = ["cyan", "midnight blue", "lime", "peru", "yellow", "crimson", "indigo", "maroon", "pale violet red", "black"]

side = [0,90,180,270]
tim.speed("fastest")
turtle.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color
def spiral_drawing(gap_size):
    for _ in range(int(360/gap_size)):
        tim.circle(100)
        tim.setheading(tim.heading()+gap_size)
        tim.color(random_color())

spiral_drawing(10)




my_turtle_screen = Screen()
my_turtle_screen.exitonclick()
