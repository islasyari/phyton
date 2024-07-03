def main():
    user_input = input("Enter a character: ")

    # show the input
    while len(user_input) != 1:
        print("Please enter exactly one character.")
        user_input = input("Enter a character: ")

    # create the ASCII value
    ascii_value = ord(user_input)

    # this will show the result
    print(f"The ASCII value of {user_input} is {ascii_value}")


if __name__ == "__main__":
    main()
