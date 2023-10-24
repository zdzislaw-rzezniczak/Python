from turtle import Screen
import time
from paddle import Paddle
from ball import Ball

screen = Screen()
screen.setup(1000, 700)
screen.bgcolor("black")
screen.title("Pong game")
screen.tracer(0)

paddle1 = Paddle(450)
paddle2 = Paddle(-450)
ball = Ball()

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
    ball.move()

    if ball.distance(paddle1) < 20 or ball.distance(paddle2) < 20:
        ball.bounce_x()


screen.exitonclick()
