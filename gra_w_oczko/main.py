import random

deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,
        2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,
        2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,
        2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11, ]


# Druga wersja gry figury 2-3-4

# deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 11,
#         2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 11,
#         2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 11,
#         2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 11, ]


def computers_choice():
    computers_deck = []
    sum_ = 0
    while sum_ < 17:
        computer_choice = random.choice(deck)
        deck.remove(computer_choice)
        computers_deck.append(computer_choice)
        sum_ = sum(computers_deck)

    return computers_deck


def player_choice():
    players_deck = []
    do_we_play = True
    while do_we_play:
        players_choice = random.choice(deck)
        deck.remove(players_choice)
        players_deck.append(players_choice)
        print(f"Twoja talia: {players_deck}")

        if sum(players_deck) > 21:
            return players_deck

        next_turn = input("Czy dobierasz kolejną kartę? t/n ")
        if next_turn.lower() == 't':
            do_we_play = True
        else:
            do_we_play = False
    return players_deck


def check_the_win(computer_deck, player_deck):
    if len(player_deck) == 2 and sum(deck) == 22:
        return "Perskie oczko wygrałeś"
    elif sum(player_deck) > 21:
        return "Przekroczyłeś 21 przegrałeś"
    elif sum(computer_deck) > 21:
        return "Wygrałeś"
    elif sum(computer_deck) == sum(player_deck):
        return "Remis"
    elif sum(computer_deck) > sum(player_deck):
        return "Przegrałeś"
    else:
        return "Wygrałeś"


def the_game():
    print("\nZaczynamy nową grę: \n")
    computer = computers_choice()
    print(f"Pierwsza karta krupiera to: {computer[0]}")
    player = player_choice()
    print(check_the_win(computer, player))
    print(f"Talia krupiera {computer}: suma {sum(computer)}")
    print(f"Twoja talia: {player}: suma {sum(player)}")


while True:
    the_game()
