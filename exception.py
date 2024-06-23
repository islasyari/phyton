def square_number(): #
    while True:
        try:
            number = input("Enter a number to square: ")
            squared_number = int(number) ** 2
            print(f"The square of {number} is {squared_number}.")
            break
        except ValueError:
            print("Invalid. Please enter a valid number.")
            break

square_number()
