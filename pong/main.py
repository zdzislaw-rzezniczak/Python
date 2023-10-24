from turtle import Screen, Turtle

from ball import Ball
from paddle import Paddle
import time

from scoreboard import Scoreboard

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
ball = Ball()
scoreboard_left_paddle = Scoreboard(-100)
scoreboard_right_paddle = Scoreboard(100)

paddle_left = Paddle(-350)
paddle_right = Paddle(350)

screen.listen()
screen.onkey(paddle_right.up, "Up")
screen.onkey(paddle_right.down, "Down")
screen.onkey(paddle_left.up, "w")
screen.onkey(paddle_left.down, "s")
scoreboard_left_paddle.write(paddle_left.score, align="center", font=("Courier", 80, "normal"))
scoreboard_right_paddle.write(paddle_right.score, align="center", font=("Courier", 80, "normal"))


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(paddle_right) < 50 and ball.xcor() > 320 or ball.distance(paddle_left) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        paddle_left.score += 1
        time.sleep(0.5)
        scoreboard_left_paddle.clear()
        print(f"player left score: {paddle_left.score}")
        scoreboard_left_paddle.write(paddle_left.score, align="center", font=("Courier", 80, "normal"))
        ball.setposition(0,0)


    if ball.xcor() < -380:
        paddle_right.score += 1

        print(f"player right score: {paddle_right.score}")
        scoreboard_right_paddle.clear()
        scoreboard_right_paddle.write(paddle_right.score, align="center", font=("Courier", 80, "normal"))
        time.sleep(0.5)
        ball.setposition(0, 0)



screen.exitonclick()
