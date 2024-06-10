def bubble_sort(names):
    n = len(names)
    for i in range(n - 1):
        for j in range(n - 1 - i):
                if names[j] > names[j + 1]: # organize is they are in wrong order
                     names[j], names[j + 1] = names[j + 1], names[j]
def main():
    names = []
    for _ in range(5): # have user enter 5 names
        name = input("Enter a name: ")
        names.append(name)
        
    bubble_sort(names) # Sorth the name using bubble sort 
    print("Sorted list:",names)

    names.reverse() # Reverse the sorted list
    print("Reversed list:",names)

if __name__=="__main__":
     main()
