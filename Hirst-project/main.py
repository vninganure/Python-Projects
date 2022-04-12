# import colorgram
#
# colors = colorgram.extract("Hirst-Image.jpg", 30)

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     colors = (r, g, b)
#     color_list.append(colors)
import turtle

color_list = [(201, 164, 112), (239, 246, 241), (152, 75, 50), (221, 201, 138), (57, 95, 126), (170, 152, 44), (138, 31, 20), (135, 163, 183), (196, 94, 75), (49, 121, 88), (143, 177, 149), (95, 75, 77), (76, 39, 32), (164, 146, 157), (16, 98, 71), (232, 176, 165), (54, 46, 48), (32, 61, 76), (22, 83, 89), (182, 204, 176), (141, 22, 25), (86, 147, 127), (45, 66, 85), (8, 68, 53), (177, 94, 97), (222, 177, 182), (109, 128, 151)]

from turtle import *
import random

tim = Turtle()
turtle.colormode(255)


for i in range(11):
    for j in range(11):
        tim.dot(20, random.choice(color_list))
        tim.penup()
        tim.forward(30)
    tim.right(90)

scr = turtle.Screen()
scr.exitonclick()