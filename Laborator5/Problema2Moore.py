def mealy_transition(current_state, input_char):
    if current_state == 'Q1':
        if input_char == 'X':
            return 'Q2', 'O1'
        elif input_char == 'Y':
            return 'Q1', 'O1'
    elif current_state == 'Q2':
        if input_char == 'X':
            return 'Q1', 'O2'
        elif input_char == 'Y':
            return 'Q2', 'O2'

def main():
    current_state = 'Q1'
    while True:
        input_char = input("Introduceti intrarea (X sau Y) sau 'q' pentru a iesi: ").upper()
        if input_char == 'Q':
            print("Program terminat.")
            break
        elif input_char not in ['X', 'Y']:
            print("Intrare invalida! Introduceti X sau Y.")
            continue

        next_state, output = mealy_transition(current_state, input_char)
        print("Stare curenta:", next_state)
        print("Iesire corespunzatoare:", output)
        current_state = next_state

if __name__ == "__main__":
    main()
