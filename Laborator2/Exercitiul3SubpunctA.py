def generate_strings(S, A, B, max_length, current_string):
    if len(current_string) == max_length:
        print(current_string)
        return
    if S:
        generate_strings(False, True, True, max_length, current_string + "ab")

    if A:
        generate_strings(False, True, False, max_length, current_string + "a")

    if B:
        generate_strings(False, False, True, max_length, current_string + "b")

generate_strings(True, False, False, 10, "")
