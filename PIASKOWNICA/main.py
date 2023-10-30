from tkinter import *
from functools import partial

window = Tk()
window.title("My first GUI Program")
window.minsize(500, 300)

my_label = Label(text="Cześć Zocha")
my_label.pack()


def change_label(label):
    new_text = input1.get()
    label.config(text=new_text)


button = Button(text="change", command=partial(change_label, label=my_label))
button.pack()

input1 = Entry(width=10)
input1.pack()

window.mainloop()
