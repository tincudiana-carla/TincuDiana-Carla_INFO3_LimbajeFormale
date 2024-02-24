def generate_strings(max_length):
    productions = [("X", "")]
    while productions:
        symbol, current_string = productions.pop(0)
        if len(current_string) == max_length:
            print(current_string)
        else:
            if symbol == "X":
                productions.insert(0, ("Y", current_string + "0"))
                productions.insert(0, ("Z", current_string + "1"))
            elif symbol == "Y":
                productions.insert(0, ("X", current_string + "2"))
                productions.insert(0, ("X", current_string))
            elif symbol == "Z":
                productions.insert(0, ("Z", current_string + "3"))
                productions.insert(0, ("Z", current_string + "4"))
generate_strings(4)
