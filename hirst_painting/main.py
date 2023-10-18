from random import random, choice

import colorgram
from turtle import Turtle, Screen

# Extract 6 colors from an image.
# colors = colorgram.extract('hirst.jpg', 30)
#
#
# color_separations = []
# for color in colors:
#     rgb = color.rgb
#     color_separations.append((rgb.r, rgb.g, rgb.b))


color_separations = [(249, 248, 244), (250, 245, 248), (243, 250, 246), (236, 244, 250), (236, 224, 80), (197, 7, 71), (195, 164, 13), (201, 75, 15), (231, 54, 132), (110, 179, 216), (217, 163, 101), (27, 105, 168), (35, 186, 109), (19, 29, 168), (13, 23, 66), (212, 135, 177), (233, 223, 7), (199, 33, 132), (13, 183, 212), (230, 166, 199), (126, 189, 162), (8, 49, 28), (40, 132, 77), (128, 219, 232), (58, 12, 25), (67, 22, 7), (114, 90, 210), (146, 216, 199), (179, 17, 8), (233, 66, 34)]

timmy = Turtle()

timmy.penup()
timmy.goto(-300, -300)
timmy.pendown()
postion_y = -250
timmy.fillcolor("violet")
screen = Screen()
screen.colormode(255)

for _ in range(10):
    for i in range(10):
        color = choice(color_separations)
        timmy.pencolor(color)
        timmy.pendown()
        timmy.dot(20)
        print(timmy.pos())
        timmy.penup()
        timmy.forward(50)
    timmy.goto(-300, postion_y)
    postion_y += 50


screen.exitonclick()


