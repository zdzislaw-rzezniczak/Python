import random

do_you_want_to_play = True


def play():
    user_choice = input("Wybierz swój ruch papier 'p', kamien 'k' nozyczki 'n': ")
    if user_choice.lower() != 'p' or 'n' or 'k':
        user_choice = input("podaj poprawny symbol 'p n k': ")
    computer_choice = random.choice(['p', 'k', 'n'])
    print(computer_choice)
    did_you_win = winner(user_choice, computer_choice)
    print(did_you_win)


def winner(user_choice, computer_choice):
    # p>k k>n n>p
    if user_choice == computer_choice:
        return 'Remis'
    elif (user_choice == 'p' and computer_choice == 'k' or user_choice == 'k' and computer_choice == 'n' or
          user_choice == 'n' and computer_choice == 'p'):
        return 'Wygrałeś'
    else:
        return 'Przegrałeś'


while do_you_want_to_play:
    play()
    gramy = input("Czy gramy dalej T/N? ")
    if gramy.upper() != 'T':
        do_you_want_to_play = False

