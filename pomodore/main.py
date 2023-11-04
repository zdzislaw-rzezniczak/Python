from functools import partial
from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
checkmark = "✔"
timer = NONE


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_txt, text="00:00")
    title_lbl.config(text="Timer")
    checkbox_label.config(text="")
    global reps
    reps = 0



# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    reps += 1

    if reps % 8 == 0:
        count_down(long_break_sec)
        title_lbl.config(text="Break", fg=RED)
        window.attributes('-topmost', 1)
        window.attributes('-topmost', 0)

    if reps % 2 == 0:
        count_down(short_break_sec)
        title_lbl.config(text="Break", fg=PINK)
        window.attributes('-topmost', 1)
        window.attributes('-topmost', 0)

    else:
        count_down(work_sec)
        title_lbl.config(text="Work", fg=GREEN)
        window.attributes('-topmost', 1)
        window.attributes('-topmost', 0)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_txt, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            global checkmark
            checkbox_label.config(text=checkmark)
            checkmark += "✔"


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodore")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_txt = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))

button_start = Button(text="Start", command=start_timer)
button_reset = Button(text="Reset", command=reset_timer)

checkbox_label = Label(font=(FONT_NAME, 20, "normal"), fg=GREEN, bg=YELLOW)

title_lbl = Label(text="Timer", font=(FONT_NAME, 35, "normal"), fg=GREEN, bg=YELLOW)
title_lbl.grid(column=1, row=0)
canvas.grid(column=1, row=1)
canvas.grid(column=1, row=1)
button_start.grid(column=0, row=2)
button_reset.grid(column=2, row=2)
checkbox_label.grid(column=1, row=3)

window.mainloop()
