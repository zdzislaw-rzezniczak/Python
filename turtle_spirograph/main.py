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


timmy.speed(0)

for i in range(200):
    timmy.circle(100)
    timmy.color(change_color())
    timmy.left(2)

screen = Screen()
screen.exitonclick()
