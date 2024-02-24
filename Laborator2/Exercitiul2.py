def generate_strings(iterations):
    strings = set()

    def generate(S):
        if len(S) > 0 and S[0] == S[-1]:
            strings.add(S)

        if len(S) < iterations * 2:
            generate('a' + S + 'a')
            generate('b' + S + 'b')

    generate('')
    return strings

iterations = 3
generated_strings = generate_strings(iterations)

for i in range(1, iterations + 1):
    iteration_strings = [string for string in generated_strings if len(string) == i * 2]
    sorted_strings = sorted(iteration_strings)
    print(f'Iterația {i}: {", ".join(sorted_strings)}')
