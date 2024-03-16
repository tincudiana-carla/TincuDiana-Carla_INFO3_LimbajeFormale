def transition(state, input_char):
    if state == 'S1':
        if input_char == 'A':
            return 'S1', 'O1'
        elif input_char == 'B':
            return 'S2', 'O1'
    elif state == 'S2':
        if input_char == 'A':
            return 'S1', 'O2'
        elif input_char == 'B':
            return 'S2', 'O2'

def main():
    state = 'S1'
    while True:
        input_char = input("Introduceti intrarea (A sau B) sau 'q' pentru a iesi: ").upper()
        if input_char == 'Q':
            print("Program terminat.")
            break
        elif input_char not in ['A', 'B']:
            print("Intrare invalida! Introduceți A sau B.")
            continue

        state, output = transition(state, input_char)
        print("Stare curenta:", state)
        print("Iesire corespunzatoare:", output)

if __name__ == "__main__":
    main()
