import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("States game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
correct_answers = []

data = pd.read_csv("50_states.csv")
states_list = data.state.to_list()
zolw = turtle.Turtle()
zolw.penup()
zolw.ht()
punkty = turtle.Turtle()
punkty.ht()
punkty.penup()
punkty.setposition(x=0, y=250)
isPlaying = True
while isPlaying:
    answer_state = screen.textinput(title="Zgadnij nazwę stanu", prompt="Jaki kolejny stan zgadniesz?").title()
    if answer_state in states_list:
        correct_answers.append(answer_state)
        # print(correct_answers)
        state = data[data.state == answer_state]
        x = int(state.x.iloc[0])
        y = int(state.y.iloc[0])
        zolw.setposition(x=x, y=y)
        zolw.write(arg=answer_state, align="center", font=("Comic Sans", 10, "normal"))
        punkty.clear()
        punkty.write(arg=f" Punkty: {len(correct_answers)} / 50", align="center", font=("Comic Sans", 20, "normal"))
    elif answer_state == "Exit":
        # difference = list(set(states_list) - set(correct_answers))
        difference = [element for element in states_list if element not in correct_answers]
        df = pd.DataFrame(difference)
        df.to_csv("left_states.csv")
        isPlaying = False



punkty.clear()
punkty.write(arg=f" Twój wynik: {len(correct_answers)} / 50", align="center", font=("Comic Sans", 20, "normal"))

difference = list(set(correct_answers) - set(states_list))
print(difference)
screen.exitonclick()
