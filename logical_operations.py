# Prompt the user for two integer inputs
num1 = int(input("Enter an integer: "))
num2 = int(input("Enter another integer: "))

# Logical comparisons using the input integers
print("Both numbers greater than 0:", num1 > 0 and num2 > 0)
print("Both numbers greater than 100:", num1 > 100 and num2 > 100)
print("Either number is even?", num1 % 2 == 0 or num2 % 2 == 0)
print("Either number is less than 100?", num1 < 100 or num2 < 100)
print("num1 is not equal to num2:", num1 != num2)
print("num1 is not 0:", not num1 == 0)
