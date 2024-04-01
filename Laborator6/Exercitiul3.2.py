class State:
    def __init__(self, name):
        self.name = name
        self.transitions = {}

    def add_transition(self, symbol, state):
        if symbol in self.transitions:
            self.transitions[symbol].add(state)
        else:
            self.transitions[symbol] = {state}

    def get_transitions(self, symbol):
        return self.transitions.get(symbol, set())

    def __repr__(self):
        return self.name

def build_nfa():
    start_state = State("start")
    accept_state = State("accept")

    start_state.add_transition('a', start_state)
    start_state.add_transition('b', start_state)
    start_state.add_transition('c', start_state)
    start_state.add_transition('a', accept_state)

    accept_state.add_transition('b', accept_state)
    accept_state.add_transition('c', accept_state)

    return start_state, accept_state

def is_accepted(input_string):
    current_states = {start_state}
    for symbol in input_string:
        next_states = set()
        for state in current_states:
            next_states |= state.get_transitions(symbol)
        current_states = next_states

    count_a = input_string.count('a')
    count_b = input_string.count('b')
    count_c = input_string.count('c')
    return any(state == accept_state and count_a == count_b == count_c > 0 for state in current_states)

start_state, accept_state = build_nfa()

input_string = input("Introduceti sirul ")

if is_accepted(input_string):
    print("Este acceptat in limbaj")
else:
    print("Nu este acceptat in limbaj")
