from turtle import Turtle


class Scoreboard (Turtle):

    def __init__(self, x_pos):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_scoreboard()
        self.goto(x=x_pos, y=200)

    def update_scoreboard(self):
        pass

