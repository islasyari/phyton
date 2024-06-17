def factorial(n):
    if n == 0 or n == 1: # defining a function
        return 1
    else:
        return n * factorial(n - 1) # define the base case

def main():
    n = int(input("Enter a non-negative integer: ")) #request user to input whole nuber.
    result = factorial(n)
    print(f"The factorial of {n} is {result}.")

main()
