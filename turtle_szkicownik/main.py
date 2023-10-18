from turtle import Turtle, Screen

screen = Screen()
timmy = Turtle()


def move_forwards():
    timmy.forward(10)


def move_backward():
    timmy.backward(10)


def turn_left():
    timmy.left(5)


def turn_right():
    timmy.right(5)


def clear():
    timmy.clear()
    timmy.penup()
    timmy.setposition(0, 0)
    timmy.setheading(0)
    timmy.pendown()


screen.listen()
screen.onkey(key='w', fun=move_forwards)
screen.onkey(key='s', fun=move_backward)
screen.onkey(key='a', fun=turn_left)
screen.onkey(key='d', fun=turn_right)
screen.onkey(key='c', fun=clear)

screen.exitonclick()
