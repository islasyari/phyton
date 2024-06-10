bottles = 99

while bottles > 0:
    # Print the current number of bottles
    if bottles > 1:
        print(f"{bottles} bottles of beer on the wall")
        print(f"{bottles} bottles of beer")
    else:
        print("1 bottle of beer on the wall")
        print("1 bottle of beer") #switch from singular to plural bottles
    
    # Next line of bottle (print)
    if bottles > 2:
        print("Take one down, pass it around")
        print(f"{bottles - 1} bottles of beer on the wall!")
    elif bottles == 2:
        print("Take one down, pass it around")
        print("1 bottle of beer on the wall!")
    else:
        print("Take it down, pass it around")
        print("No bottles of beer on the wall!")
    
    # reduce the number of bottles
    bottles -= 1
