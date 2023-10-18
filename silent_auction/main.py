import os

do_you_want_to_add_auctioneer = True
lista = []

while do_you_want_to_add_auctioneer:
    name = input("podaj swoje imię ")
    bid = int(input("Podaj kwotę licytacji "))
    lista.append({"imie": name, "kwota": bid})
    add_actioneer = input("Czy dodać kolejną osobę t/n ")
    if add_actioneer.lower() == "n":
        do_you_want_to_add_auctioneer = False
        os.system('cls')


max_ = 0
imie = ""
for slownik in lista:
    if max_ < slownik["kwota"]:
        max_ = slownik["kwota"]
        imie = slownik["imie"]

print(f"Wygral/a {imie} z kwotą {max_}")
