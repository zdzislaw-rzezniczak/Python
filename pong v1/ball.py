from turtle import Turtle
import random

MOVE_DISTANCE = 20
random_angle = random.randint(-90, 90)


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.ball = Turtle("circle")
        self.ball.speed("fast")
        self.ball.penup()
        self.ball.color("red")
        self.ball.setheading(random_angle)

    def change_direction(self):
        self.ball.setheading(360 - self.ball.heading())

    def move(self):
        if self.ball.ycor() > 310 or self.ball.ycor() < -310:
            self.change_direction()

        self.ball.forward(MOVE_DISTANCE)

    def position_(self):
        return self.ball.pos()