alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
            'w', 'x', 'y', 'z']

direction = input("wpisz 'koduj' aby zakodować wiadomość, 'dekoduj' aby odszyfrować ")
text = input("Wpisz swój tekst:\n").lower()
shift = int(input("Podaj wartość przesunięcia "))

# mozna jeszcze użyć funkcji index() position = alphabet.index(letter) szybsze i łatwiejsz

def encrypt(text_, shift_):
    word = []
    for letter in text_:
        i = 0
        for element in alphabet:
            if element == letter:
                if i + shift_ >= len(alphabet):
                    new_sign_position = i - len(alphabet) + shift_
                    word.append(alphabet[new_sign_position])
                else:
                    new_sign_position = i + shift_
                    word.append(alphabet[new_sign_position])
            i += 1
        if letter not in alphabet:
            word.append(letter)
            i += 1
    print(f"{''.join(word)}")


def decrypt(text_, shift_):
    decoded_word = []
    for letter in text_:
        i = 0
        for element in alphabet:
            if element == letter:
                if i - shift_ < 0:
                    new_sign_position = len(alphabet) + i - shift_
                    decoded_word.append(alphabet[new_sign_position])
                else:
                    new_sign_position = i - shift_
                    decoded_word.append(alphabet[new_sign_position])
            i += 1
        if letter not in alphabet:
            decoded_word.append(letter)
            i += 1
    print(f"{''.join(decoded_word)}")


if direction == 'k':
    encrypt(text, shift)
else:
    decrypt(text, shift)
