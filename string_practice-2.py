def main():
    # Example string
    example_string = "Hello, Python programmers!"

    # TODO: Iterate through the string and print each character
    print("Iterating through the string:")
    for char in example_string:
        print(char)

    # TODO: Find and print the character with the minimum ASCII value in the string
    print("\nCharacter with the minimum ASCII value:")
    min_char = min(example_string)
    print(min_char)

    # TODO: Find and print the character with the maximum ASCII value in the string
    print("\nCharacter with the maximum ASCII value:")
    max_char = max(example_string)
    print(max_char)

    # TODO: Find and print the index of the first occurrence of 'o' in the string
    print("\nIndex of 'o':")
    index_of_o = example_string.index('o')
    print(index_of_o)

    # TODO: Convert the string into a list of characters and print the list
    print("\nConverting string to a list of characters:")
    char_list = list(example_string)
    print(char_list)

    # TODO: Count and print the number of occurrences of 'o' in the string
    print("\nCount of 'o' in the string:")
    count_of_o = example_string.count('o')
    print(count_of_o)


main()

