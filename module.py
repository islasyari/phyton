import random # module to generate random numbers.

def main():
    try:
        random_number = random.randint(1, 100) #set numbers to generate from 1 through 100.
        number_guesses = 0

        while True:
            guess = int(input("Guess a number between 1 and 100: ")) # have the user enter a guess. 
            number_guesses += 1

            difference = abs(guess - random_number) # this calculates the difference between gues and the number.

            if difference <= 5:
                print("Very Hot")
            elif difference <= 15:
                print("Hot")
            elif difference <= 25:
                print("Cool")
            else:
                print("Cold")

            if guess == random_number: # check if guess was correct. 
                print("Congratulations! You guessed the correct number.")
                break # break out of the loop. 
# print the number of guesses the user made. 
        print("Number of guesses:", num_guesses)

    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
