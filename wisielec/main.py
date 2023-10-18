import random
from art import stages

word_list = ['banan', 'gruszka', 'marchew', 'pietruszka', 'pomidor']
random_word = random.choice(word_list)
random_word_length = len(random_word)
display = ['_'] * random_word_length
print(random_word)
number_of_lives = 6


# def print_display():
#     for i in range(random_word_length):
#         print(display[i], end=" ")
#     print()

def print_display():
    print(f"{' '.join(display)}")


def choose_a_letter():
    is_in_word = False
    global number_of_lives
    players_choice = input("Zgadnij literę w słowie: ").lower()

    for i in range(random_word_length):
        letter = random_word[i]
        if players_choice == letter:
            display[i] = letter
            is_in_word = True

    if not is_in_word:
        number_of_lives -= 1
        # print(number_of_lives)
        print(stages[number_of_lives])


def check_for_blanks():
    for i in range(random_word_length):
        if display[i] == '_':
            return True
    return False


still_playing = True
print_display()

while still_playing:
    choose_a_letter()
    print_display()
    if number_of_lives == 0:
        still_playing = False
        print("Przegrałeś")
    if not check_for_blanks():
        still_playing = False
        print("Wygrałeś")
