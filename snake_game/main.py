from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)
food = Food()
scoreboard = Scoreboard()

snake = Snake()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

snake.create_snake()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.2)
    snake.move()

    if snake.segments[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.score += 1
        scoreboard.refresh()

    # Zderzenie ze ścianami
    if (snake.segments[0].xcor() > 280 or snake.segments[0].xcor() < -280 or snake.segments[0].ycor() > 280 or
            snake.segments[0].ycor() < -280):
        snake.snake_reset()
        scoreboard.set_high_score()
    # scoreboard.game_over()
    # game_is_on = False

    # Zderzenie z ogonem
    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment) < 10:
            snake.snake_reset()
            scoreboard.set_high_score()

            # game_is_on = False
            # scoreboard.game_over()

screen.exitonclick()
