# list the numbers from 1 to 300
for num in range(1, 301):
    # Check if the number is divisible by 7 and a multiple of 5
    if num % 7 == 0 and num % 5 == 0:
        # Print the number
        print(num)
