from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.ht()
        self.speed("fastest")
        self.color("white")
        self.goto(x=0, y=270)
        self.score = 0
        self.refresh()

    def refresh(self):
        self.clear()
        str_score = f"Wynik: {self.score}"
        self.write(arg=str_score, move=False, align="center", font=("Comic Sans", 12, "normal"))

    def game_over(self):
        self.goto(0,0)
        self.write(arg="GAME OVER", move=False, align="center", font=("Comic Sans", 12, "normal"))
