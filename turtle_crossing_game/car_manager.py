from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(1, 2)
        self.rand_starting_y_pos = random.randint(-250, 250)
        self.goto(x=280, y=self.rand_starting_y_pos)
        self.rand_color = random.choice(COLORS)
        self.color(self.rand_color)

    def move(self, speed):
        new_x = self.xcor() - speed
        self.goto(new_x, y=self.ycor())
