from art import logo
import random

print(logo)

print("Witaj w grze zgadnij liczbę!!")
print("Myślę o liczbie od 1 do 100")


def choose_level():
    while True:
        difficulty = input("Wybierz poziom trudności: 'easy', 'hard' ")
        if difficulty.lower() == 'easy':
            return 10
        elif difficulty.lower() == 'hard':
            return 5


def guess_the_number(random_number_, tries_):
    attempts_number = tries_ - 1
    for i in range(tries):
        players_choice_ = input("wybierz liczbę 1-100: ")
        while not players_choice_.isdigit():
            players_choice_ = input("wybierz poprawną liczbę")

        players_choice_ = int(players_choice_)
        if random_number_ > players_choice_:
            print("Niestety wygenerowana liczba jest większa")
            print(f"Zostało jeszcze {attempts_number} prób")
        elif random_number_ < players_choice_:
            print("Niestety wygenerowana liczba jest mniejsza")
            print(f"Zostało jeszcze {attempts_number} prób")
        elif random_number_ == players_choice_:
            print(f"Super trafiłeś wygenerowana liczba to {random_number_}")
            return True
        attempts_number -= 1


tries = choose_level()
random_number = random.randint(1, 100)
# print(random_number)
guess_the_number(random_number, tries)
