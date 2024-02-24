alphabet = ['0', '1', '2']
def generate_combinations(alphabet, length):
    all_combinations = []
    stack = [('', length)]
    while stack:
        current_combination, current_length = stack.pop()
        if current_length == 0:
            all_combinations.append(current_combination)
        else:
            for char in alphabet:
                stack.append((current_combination + char, current_length - 1))

    return all_combinations

for length in range(1, 6):
    palindromes = generate_combinations(alphabet, length)
    palindromes = [palindrome for palindrome in palindromes if palindrome == palindrome[::-1]]
    palindromes.sort()
    print(f"Palindroame de lungime {length}: {' '.join(palindromes)}")
