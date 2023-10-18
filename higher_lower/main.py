from art import logo, vs
from game_data import data
from random import randint

is_playing = True
score = 0

while is_playing:
    random_number = randint(0,len(data)-1)
    random_number2 = randint(0, len(data)-1)
    person1 = data[random_number]
    person2 = data[random_number2]
    print(f"Compare A: {person1['name']}, a {person1['description']} from {person1['country']}")
    print(vs)
    print(f"Compare B: {person2['name']}, a {person2['description']} from {person2['country']}")
    players_answer = input("Która osoba ma więcej followersów. Wpisz 'A' lub 'B': ").upper()
    if players_answer == 'A':
        players_choice = person1
        other = person2
    elif players_answer == 'B':
        players_choice = person2
        other = person1
    if players_choice["follower_count"] > other["follower_count"]:
        score += 1
        print(f"Super. Gramy dalej. Twój wynik to: {score}\n")
    else:
        print(f"Przykro mi zła odpowiedź. Twój wynik to: {score}\n")
        is_playing = False

