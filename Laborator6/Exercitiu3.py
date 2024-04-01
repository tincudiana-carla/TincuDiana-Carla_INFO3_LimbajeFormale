def validate_postal_code(code):

    transitions = {
        'q0': {'1': 'q1', '2': 'q1', '3': 'q1', '4': 'q1', '5': 'q1', '6': 'q1', '7': 'q1', '8': 'q1', '9': 'q1'},
        'q1': {'0': 'q2', '1': 'q2', '2': 'q2', '3': 'q2', '4': 'q2', '5': 'q2', '6': 'q2', '7': 'q2', '8': 'q2',
               '9': 'q2'},
        'q2': {'0': 'q3', '1': 'q3', '2': 'q3', '3': 'q3', '4': 'q3', '5': 'q3', '6': 'q3', '7': 'q3', '8': 'q3',
               '9': 'q3'},
        'q3': {'0': 'q4', '1': 'q4', '2': 'q4', '3': 'q4', '4': 'q4', '5': 'q4', '6': 'q4', '7': 'q4', '8': 'q4',
               '9': 'q4'},
        'q4': {'0': 'q5', '1': 'q5', '2': 'q5', '3': 'q5', '4': 'q5', '5': 'q5', '6': 'q5', '7': 'q5', '8': 'q5',
               '9': 'q5'},
        'q5': {}
    }

    current_state = 'q0'
    for char in code:

        if char in transitions.get(current_state, {}):
            current_state = transitions[current_state][char]
        else:
            return False


    return current_state == 'q5'


print(validate_postal_code("12345"))
print(validate_postal_code("02345"))
print(validate_postal_code("123456"))
print(validate_postal_code("12a45"))
