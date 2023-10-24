import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

STARTING_POSITION = (0, -280)

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
screen.listen()
screen.onkey(player.go_up, "Up")
counter = 0
cars = []
scoreboard = Scoreboard()
speed = 5

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    counter += 1
    if counter == 5:
        car = CarManager()
        cars.append(car)
        counter = 0

    for car in cars:
        car.move(speed)
        if player.distance(car) < 25:
            player.color("red")
            if player.distance(car) < 20:
                scoreboard.print_game_over()
                game_is_on = False

        if player.ycor() > 270:
            scoreboard.clear()
            scoreboard.score += 1
            scoreboard.print_level()
            player.setposition(STARTING_POSITION)
            speed += 10

screen.exitonclick()
