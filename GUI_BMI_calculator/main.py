from tkinter import *
from tkinter import ttk


def calculate(*args):
    # BMI = masa ciała (w kg) / [wzrost (w m)]2
    value_height = float(height.get())
    value_weight = float(weight.get())
    try:
        bmi_result = value_weight / pow(value_height / 100, 2)
        bmi.set(str(round(bmi_result, 2)))
    except ZeroDivisionError:
        bmi.set("Dziel 0")


root = Tk()
root.title("BMI calculator")

mainframe = ttk.Frame(root, padding="3 3 20 20")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

height = StringVar()
entry = ttk.Entry(mainframe, width=4, textvariable=height)
entry.grid(column=1, row=1, sticky=(W, E))

weight = StringVar()
weight = ttk.Entry(mainframe, width=4, textvariable=weight)
weight.grid(column=1, row=2, sticky=(W, E))

bmi = StringVar()

ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=4, row=4, sticky=W)

ttk.Label(mainframe, text="height in cm").grid(column=4, row=1, sticky=W)

ttk.Label(mainframe, text="weight in kg").grid(column=4, row=2, sticky=W)
ttk.Label(mainframe, text="Your BMI = ").grid(column=1, row=3, sticky=W)
ttk.Label(mainframe, textvariable=bmi).grid(column=2, row=3, sticky=(W, E))

for child in mainframe.winfo_children():
    child.grid_configure(padx=6, pady=6)

entry.focus()
root.bind("<Return>", calculate)

root.mainloop()
