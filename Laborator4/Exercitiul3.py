class NFA:
    def __init__(self, alphabet, states, initial_state, accepting_states, transitions):
        self.alphabet = alphabet
        self.states = states
        self.initial_state = initial_state
        self.accepting_states = accepting_states
        self.transitions = transitions

    def accepts(self, input_string):
        current_states = {self.initial_state}

        for symbol in input_string:
            next_states = set()
            for state in current_states:
                if (state, symbol) in self.transitions:
                    next_states.update(self.transitions[(state, symbol)])
            current_states = next_states

        return bool(current_states.intersection(self.accepting_states))


def main():

    alphabet = {'a', 'b'}

    states = {'S0', 'S1', 'S2', 'S3'}

    initial_state = 'S0'

    accepting_states = {'S1'}

    transitions = {
        ('S0', 'a'): {'S2'},
        ('S0', 'b'): {'S3'},
        ('S2', 'a'): {'S1', 'S2'},
        ('S2', 'b'): {'S2'},
        ('S3', 'a'): {'S3'},
        ('S3', 'b'): {'S1', 'S3'}
    }


    nfa = NFA(alphabet, states, initial_state, accepting_states, transitions)


    test_cases = ["ab", "aab", "bb", "ba", "b", "aba", "abab"]
    for test_case in test_cases:
        if nfa.accepts(test_case):
            print(f"Input '{test_case}' is accepted.")
        else:
            print(f"Input '{test_case}' is not accepted.")


if __name__ == "__main__":
    main()
