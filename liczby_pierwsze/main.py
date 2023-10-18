def is_prime_number(number):
    for i in range(2, number):
        if number % i == 0:
            print(i)
            print(f"{number} nie jest liczbą pierwszą")
            return False
    print(f"{number} jest liczbą pierwszą")
    return True


n = int(input("podaj liczbę całkowitą: "))
print(is_prime_number(n))
