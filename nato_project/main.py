import pandas as pd

nato_df = pd.read_csv('nato_phonetic_alphabet.csv')

nato_dict = {d['letter']: d['code'] for d in nato_df.to_dict(orient='records')}

users_word = input("podaj słowo \n").upper()

nato_word = [nato_dict[letter] for letter in users_word]
print(nato_word)

