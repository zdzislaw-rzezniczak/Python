import random
from tkinter import *
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"
current_word = {}
to_learn = {}

try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    df_sp_pl = pd.read_csv("data/es-pl.csv")
    dict_sp_pl = df_sp_pl.to_dict(orient="records")
else:
    dict_sp_pl = data.to_dict(orient="records")


def get_random_word():
    global current_word, after_change
    window.after_cancel(after_change)
    current_word = random.choice(dict_sp_pl)
    current_word_es = current_word['Spanish']

    canvas.itemconfig(text_language, text="Spanish", fill="black")
    canvas.itemconfig(text_word, text=current_word_es, fill="black")
    canvas.itemconfig(canvas_image, image=card_front)
    after_change = window.after(3000, func=flip_card)
    return current_word


def flip_card():
    print(current_word)
    current_word_pl = current_word['Polish']
    canvas.itemconfig(canvas_image, image=new_image)
    canvas.itemconfig(text_language, text="Polish", fill="white")
    canvas.itemconfig(text_word, text=current_word_pl, fill="white")


def is_known():
    dict_sp_pl.remove(current_word)
    print(len(to_learn))
    data = pd.DataFrame(dict_sp_pl)
    data.to_csv("data/words_to_learn.csv", index=False)
    get_random_word()


window = Tk()
window.title("Flash card")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)
after_change = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, highlightthickness=0, background=BACKGROUND_COLOR)

card_front = PhotoImage(file="images/card_front.png")
canvas_image = canvas.create_image(404, 265, image=card_front)

text_language = canvas.create_text(400, 150, text="Spanish", fill="black", font='Ariel 40 italic')
text_word = canvas.create_text(400, 263, text="", fill="black", font='Ariel 60 bold')
word = get_random_word()
canvas.itemconfig(text_word, text=word["Spanish"])
image_right = PhotoImage(file="images/right.png")
button_right = Button(image=image_right, highlightthickness=0, command=is_known)
image_wrong = PhotoImage(file="images/wrong.png")
button_wrong = Button(image=image_wrong, highlightthickness=0, command=get_random_word)

new_image = PhotoImage(file="images/card_back.png")

canvas.grid(column=0, row=0, columnspan=2)
button_right.grid(column=1, row=1)
button_wrong.grid(column=0, row=1)

window.mainloop()
