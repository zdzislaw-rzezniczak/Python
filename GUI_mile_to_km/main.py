from functools import partial
from tkinter import *

FONT = ("Comic Sans MS", 25, "normal")


def change_label(label):
    try:
        miles_value = float(miles_input.get())
        km_value = round(miles_value * 1.609344, 2)
        label.config(text=km_value)
    except:
        label.config(text="NaN", fg='#f00')


window = Tk()
window.title("Mile na km")

# window.minsize(500, 300)
miles_input = Entry(width=10, font=FONT)
miles_lbl = Label(text="mile", font=FONT)
is_equal_lbl = Label(text="równa się:", font=FONT)
km_value_lbl = Label(text="0", font=FONT)
km_lbl = Label(text="km", font=FONT)
button = Button(text="Przelicz", command=partial(change_label, label=km_value_lbl), font=FONT)

miles_input.grid(column=1, row=0, padx=20, pady=20)
miles_lbl.grid(column=2, row=0, padx=20, pady=20)
is_equal_lbl.grid(column=0, row=1, padx=20, pady=20)
km_value_lbl.grid(column=1, row=1, padx=20, pady=20)
km_lbl.grid(column=2, row=1, padx=20, pady=20)
button.grid(column=1, row=2, padx=20, pady=20)

window.mainloop()
