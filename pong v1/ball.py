from turtle import Turtle
import random

MOVE_DISTANCE = 20
random_angle = random.randint(-90, 90)


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.speed("fast")
        self.penup()
        self.color("red")
        self.setheading(random_angle)
        self.x_move = 10
        self.y_move = 10

    def change_direction(self):
        self.setheading(360 - self.heading())

    def move(self):
        if self.ycor() > 310 or self.ycor() < -310:
            self.bounce_x()
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
