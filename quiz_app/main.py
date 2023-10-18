import json

f = open('questions.json', encoding='utf8')

data = json.load(f)
score = 0
liczba_pytan = 0
for i in data:
    liczba_pytan +=1
    print(i["question"])
    print("A.", i["answers"][0]["text"])
    print("B.", i["answers"][1]["text"])
    print("C.", i["answers"][2]["text"])

    correct_choice = False
    while not correct_choice:
        answer = input("Podaj poprawną odpowiedź: ")
        if answer.upper() == 'A' and i["answers"][0]["correct"] == True:
            print("Poprawna odpowiedź")
            score += 1
            correct_choice = True
        elif answer.upper() == 'B' and i["answers"][1]["correct"] == True:
            print("Poprawna odpowiedź")
            score += 1
            correct_choice = True
        elif answer.upper() == 'C' and i["answers"][2]["correct"] == True:
            print("Poprawna odpowiedź")
            score += 1
            correct_choice = True
        elif answer.upper() == 'A' or answer.upper() == 'B' or answer.upper() == 'C':
            print("Niestety nie jest to poprawna odpowiedź")
            correct_choice = True
        else:
            print("nie ma takiej opcji")
f.close()
print(f"Zdobyłeś {score} punkty na  {liczba_pytan}")
