from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.ht()
        self.speed("fastest")
        self.color("white")
        self.goto(x=0, y=270)

        with open("data.txt", mode="r") as file:
            high_score_from_file = int(file.read())

        self.high_score = high_score_from_file
        self.score = 0

        self.refresh()

    def refresh(self):
        self.clear()
        str_score = f"Wynik: {self.score} High score: {self.high_score}"
        self.write(arg=str_score, move=False, align="center", font=("Comic Sans", 12, "normal"))
        # self.set_high_score()

    def set_high_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.refresh()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(arg="GAME OVER", move=False, align="center", font=("Comic Sans", 12, "normal"))
