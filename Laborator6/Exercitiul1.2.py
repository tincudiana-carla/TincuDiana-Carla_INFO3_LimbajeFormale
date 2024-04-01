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

    start_state.add_transition('0', start_state)
    start_state.add_transition('1', accept_state)
    accept_state.add_transition('1', accept_state)

    return start_state, accept_state

def is_accepted(input_string):
    current_states = {start_state}
    for symbol in input_string:
        next_states = set()
        for state in current_states:
            next_states |= state.get_transitions(symbol)
        current_states = next_states

    count_0 = input_string.count('0')
    count_1 = input_string.count('1')
    return any(state == accept_state and count_0 > count_1 for state in current_states)

start_state, accept_state = build_nfa()

input_string = input("Introduceti sirul ")

if is_accepted(input_string):
    print("Este acceptat in limbaj")
else:
    print("Nu este acceptat in limbaj")
