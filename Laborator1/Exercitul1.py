def concatenate(s1, s2):
    return s1 + s2

def inverse(s):
    return s[::-1]

def substituie(s, a, b):
    return s.replace(a, b)

def lungime(s):
    return len(s)

def display_menu():
    print("Meniu:")
    print("1. Concatenare")
    print("2. Inversare")
    print("3. Substitutie")
    print("4. Lungimea unui sir")
    print("5. Iesire")

def print_red(text):
    print("\033[91m {}\033[00m" .format(text))

def main():

    while True:
        display_menu()
        choice = input("Alege o optiune: ")

        if choice == '1':
            s1 = input("Introdu primul șir: ")
            s2 = input("Introdu al doilea șir: ")
            result = concatenate(s1, s2)
            print_red("Concatenarea celor două șiruri este:")
            print(result)

        elif choice == '2':
            s = input("Introdu sirul pentru inversare: ")
            result = inverse(s)
            print_red("Inversul sirului este:")
            print(result)

        elif choice == '3':
            s = input("Introdu un sir de caractere: ")
            a = input("Introdu simbolul a: ")
            b = input("Introdu simbolul b: ")
            result = substituie(s, a, b)
            print_red("Sirul rezultat după substituire:")
            print(result)

        elif choice == '4':
            s = input("Introdu un sir de caractere: ")
            result = lungime(s)
            print_red("Lungimea sirului este:")
            print(result)

        elif choice == '5':
            print_red("La revedere!")
            break

        else:
            print_red("Optiune invalida. Te rog sa introduci o optiune valida.")


if __name__ == "__main__":
    main()
