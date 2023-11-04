import pandas as pd

nato_df = pd.read_csv('nato_phonetic_alphabet.csv')

nato_dict = {d['letter']: d['code'] for d in nato_df.to_dict(orient='records')}

is_correct = False
while not is_correct:
    try:
        users_word = input("Podaj słowo \n").upper()
        nato_word = [nato_dict[letter] for letter in users_word]
        is_correct = True
    except KeyError:
        print("Niepoprawne słowo. Podaj poprawne słowo")
        is_correct = False

print(nato_word)

