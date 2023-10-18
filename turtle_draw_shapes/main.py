import turtle
from turtle import Turtle, Screen, color
import random

timmy = Turtle()
timmy.shape("turtle")
turtle.colormode(255)


def change_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b



num_sides = 3
for _ in range(10):
    for i in range(num_sides):
        timmy.forward(100)
        timmy.left(360 / num_sides)
    num_sides += 1
    timmy.color(change_color())

screen = Screen()
screen.exitonclick()
