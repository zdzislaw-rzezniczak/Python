from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270


class Paddle(Turtle):

    def __init__(self, x_position):
        super().__init__()
        self.segment = Turtle("square")
        self.segment.shapesize(stretch_wid=1, stretch_len=5)
        self.segment.speed("fastest")
        self.segment.penup()
        self.segment.color("white")
        self.segment.setposition(x=x_position, y=0)
        self.segment.setheading(UP)
        self.score = 0

    def move(self):
        if self.segment.ycor() > 280:
            self.segment.setheading(DOWN)
        elif self.segment.ycor() < -280:
            self.segment.setheading(UP)


    def up(self):

        self.segment.setheading(UP)
        self.segment.forward(MOVE_DISTANCE)

    def down(self):
        self.segment.setheading(DOWN)
        self.segment.forward(MOVE_DISTANCE)

    def difference_(self, turtle_position):

        return self.segment.pos() - turtle_position
