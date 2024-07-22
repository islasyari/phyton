def two_letter_combinations(characters):
    for char1 in characters:
        for char2 in characters:
            yield char1 + char2 #Yield statements.

def main():
    characters = ['a', 'b', 'c'] #List to generate from.
    combinations = two_letter_combinations(characters)
    for combination in combinations: #
        print(combination)

main()
