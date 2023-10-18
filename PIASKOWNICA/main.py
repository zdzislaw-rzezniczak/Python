<<<<<<< HEAD
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
=======
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
>>>>>>> bdaf571 (turtle commit)
