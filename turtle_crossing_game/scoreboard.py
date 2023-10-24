from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard (Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("black")
        self.ht()
        self.score = 0
        self.print_level()

    def print_level(self):
        self.goto(-220, 260)
        self.write(f" Level: {self.score}", align="center", font=FONT)

    def print_game_over(self):
        self.goto(0, 0)
        self.write(f" GAMEOVER", align="center", font=FONT)