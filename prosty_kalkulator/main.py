print("*\n/\n+\n-\n")


def calc(choice_, num_a_, num_b_):
    if choice_ == "*":
        return num_a_ * num_b
    elif choice_ == "/":
        if num_b_ == 0:
            return "Dziel 0"
        return num_a_ / num_b
    elif choice_ == "+":
        return num_a_ + num_b
    elif choice_ == "-":
        return num_a_ - num_b
    else:
        return "Niepoprawne działanie"


continue_ = True
while continue_:
    choice = input("Wybierz działanie ")
    num_a = float(input("podaj pierwszą liczbę "))
    num_b = float(input("podaj drugą liczbę "))

    print(calc(choice, num_a, num_b))
    do_do_want_to_continue = input("liczymy dalej? y/n")
    if do_do_want_to_continue == "n":
        continue_ = False
