import random
from player import Player


def get_players():
    choice = input("Podaj liczbę graczy od 2-4: $ ")
    players = []
    while True:
        if choice.isdigit():
            choice = int(choice)
            if 2 <= choice <= 4:
                print(f"Wybrałeś grę w ${choice} osoby")
                break
            else:
                choice = input("Podaj prawidłową cyfrę od 2-4: $ ")
        else:
            choice = input("Podaj prawidłową cyfrę od 2-4: $ ")
    for i in range(choice):
        player_name = input("Podaj imię gracza: $ ")
        player = Player(player_name)
        players.append(player)
    return players


def roll():
    cube_1 = random.randint(1, 6)
    cube_2 = random.randint(1, 6)
    rolls = [cube_1, cube_2]
    return rolls


def game():
    players = get_players()
    game_in_progress = True
    while game_in_progress:
        for player in players:
            roll_again = True
            print(f"Teraz gra: {player.get_name()} wynik: {player.get_total_score()}")
            turn_result = 0
            while roll_again:
                rolls = roll()
                print(rolls)
                if rolls[0] == 1 and rolls[1] == 1:
                    turn_result = 25
                    print(f"Wynik rundy: {turn_result}")
                    player.set_total_score(turn_result)
                    if player.get_total_score() >= 50:
                        game_in_progress = False
                    break
                elif rolls[0] == 1 or rolls[1] == 1:
                    turn_result = 0
                    print(f"Wynik rundy: {turn_result}")
                    break
                else:
                    turn_result += rolls[0] + rolls[1]
                    print(f"Wynik rundy: {turn_result}")
                do_you_want_to_roll = input(f"{player.get_name()} chcesz rzucać dalej T/N ")
                if do_you_want_to_roll.upper() != 'T' or player.get_total_score() >= 50:
                    player.set_total_score(turn_result)
                    print(player.get_total_score())
                    roll_again = False
                    if player.get_total_score() >= 50:
                        game_in_progress = False
    for player in players:
        print()
        print(f"{player.get_name()} wynik: {player.get_total_score()}")


game()
