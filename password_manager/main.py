import json
from functools import partial
from tkinter import *
from tkinter import messagebox
import pass_gen
import pyperclip


# ---------------------------- SEARCH ENTRY ------------------------------- #
def find_password():
    try:
        with open("data.json", "r") as json_file:
            data = json.load(json_file)
            website = entry_website.get()

            if website in data:
                password = data[website]['password']
                pyperclip.copy(password)
                messagebox.showinfo("Hasło", f"Hasło: {password} pomyślnie skopiowane")
            else:
                messagebox.showinfo("No entry", "Brak wpisu w bazie.")

    except FileNotFoundError:
        messagebox.showinfo("File not found", "Plik nie został znaleziony.")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = entry_website.get()
    email = entry_email.get()
    password = entry_password.get()
    new_data = {website: {
        "email": email,
        "password": password
    }}

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showwarning("No content", "uzupełnij dane")
    else:
        try:
            with open("data.json", "r") as json_file:
                # text_file.write(f"{website} | {email} | {password}\n")
                data = json.load(json_file)
                data.update(new_data)
        except FileNotFoundError:
            with open("data.json", "w") as json_file:
                json.dump(new_data, json_file, indent=4)
        else:
            with open("data.json", "w") as json_file:
                json.dump(data, json_file, indent=4)

        entry_website.delete(0, END)
        entry_password.delete(0, END)
        messagebox.showinfo("Saved to a file", "Pomyślnie zapisano do pliku")


def open_popup():
    top = Toplevel(window)
    top.geometry("350x75")
    top.title("Saved to a file")
    Label(top, text="Pomyślnie zapisano do pliku", font='Arial 18 bold').place(x=10, y=20)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
label_website = Label(text="Website:")
label_email = Label(text="Email/Username:")
label_password = Label(text="Password:")
entry_website = Entry(width=30)
entry_website.focus()
entry_email = Entry(width=30)
entry_email.insert(0, "zdzichrz@gmail.com")
entry_password = Entry(width=30)
button_gen_passwd = Button(text="Generate", width=7, command=partial(pass_gen.generate_password,
                                                                     entry_password=entry_password))
button_search = Button(text="Search", width=7, command=find_password)
button_add = Button(text="Add", width=36, command=save)

canvas.grid(column=1, row=0)
label_website.grid(column=0, row=1)
label_email.grid(column=0, row=2)
label_password.grid(column=0, row=3)
entry_website.grid(column=1, row=1)

entry_email.grid(column=1, row=2)
entry_password.grid(column=1, row=3)
button_search.grid(column=2, row=1)
button_gen_passwd.grid(column=2, row=3)
button_add.grid(column=1, row=4, columnspan=2)
window.mainloop()
