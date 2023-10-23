from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270


class Paddle:

    def __init__(self):
        self.segments = []

    def create_paddle(self, x_position, y_position):
        segment = Turtle("square")
        segment.shapesize(stretch_wid=1, stretch_len=5)
        segment.speed("fastest")
        segment.penup()
        segment.color("white")
        segment.setposition(x=x_position, y=y_position)
        y_position -= 20
        self.segments.append(segment)
        self.segments[0].setheading(UP)

    def move(self):
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        y = self.segments[0].ycor()
        y += 20
        self.segments[0].sety(y)
        self.segments[0].left(180)

    def down(self):
        self.segments[0].left(180)
