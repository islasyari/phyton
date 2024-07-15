class NotNumericError(Exception):
    pass

def main():
    while True:
        try:
            user_input = input("Enter a number: ")
            if not user_input.isnumeric():
                raise NotNumericError
        except NotNumericError:
            print("Error: Invalid input. Please enter a valid number.")
        else:
            print("Input is valid.")
            break
        finally:
            print("End of program execution.")

if __name__ == "__main__":
    main()
