from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
turtle_colours = ["green", "blue", "pink", "yellow", "red", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
users_choice = screen.textinput("Kto zwycięży", "Podaj jaki kolor wygra:")
is_played = True

turtles = []

for turtle_index in range(0, 6):
    turtle = Turtle("turtle")
    turtle.color(turtle_colours[turtle_index])
    turtle.penup()
    turtle.goto(x=-230, y=y_positions[turtle_index])
    turtles.append(turtle)

while is_played:
    for turtle in turtles:
        random_speed = random.randint(0, 10)
        turtle.forward(random_speed)
        if turtle.xcor() > 230:
            color = turtle.pencolor()
            if color == users_choice:
                print(f"You win the color is {color}")

            else:
                print(f"You loose! the color is {color}")
            is_played = False


screen.exitonclick()
