from turtle import Screen
import time
from paddle import Paddle

screen = Screen()
screen.setup(1000, 700)
screen.bgcolor("black")
screen.title("Pong game")
screen.tracer(0)

paddle1 = Paddle()
paddle2 = Paddle()
paddle1.create_paddle(450, 40)
paddle2.create_paddle(-450, 40)

screen.listen()
screen.onkey(paddle1.up, "Up")
screen.onkey(paddle1.down, "Down")

screen.onkey(paddle2.up, "w")
screen.onkey(paddle2.down, "s")




game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.2)
    paddle1.move()
    paddle2.move()
screen.exitonclick()
