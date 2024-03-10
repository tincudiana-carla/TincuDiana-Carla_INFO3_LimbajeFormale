class FiniteAutomaton:
    def __init__(self):
        self.current_state = 'A'

    def transition(self, symbol):
        if self.current_state == 'A':
            if symbol == '0':
                self.current_state = 'B'
        elif self.current_state == 'B':
            if symbol == '1':
                self.current_state = 'B'
            elif symbol == '0':
                self.current_state = 'A'

    def final_state(self):
        return self.current_state


def main():
    sequences = ["010", "110", "1001"]

    for sequence in sequences:
        automaton = FiniteAutomaton()
        for symbol in sequence:
            automaton.transition(symbol)
        print(f"For sequence {sequence}, final state is {automaton.final_state()}")


if __name__ == "__main__":
    main()
