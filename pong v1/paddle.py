from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270


class Paddle(Turtle):

    def __init__(self, x_position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.speed("fastest")
        self.penup()
        self.color("white")
        self.setposition(x=x_position, y=0)
        self.setheading(UP)
        self.score = 0

    def move(self):
        if self.ycor() > 280:
            self.setheading(DOWN)
        elif self.ycor() < -280:
            self.setheading(UP)


    def up(self):

        self.setheading(UP)
        self.forward(MOVE_DISTANCE)

    def down(self):
        self.setheading(DOWN)
        self.forward(MOVE_DISTANCE)


