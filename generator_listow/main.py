with open("./Input/Names/invited_names.txt") as f:
    mylist = f.read().splitlines()

for name in mylist:
    with open("./Input/Letters/starting_letter.txt") as starting_file:
        with open(f"./Output/ReadyToSend/{name}.txt", mode="w") as file:
            new_letter = starting_file.read().replace("[name]", f"{name}")
            file.write(f"{new_letter}")