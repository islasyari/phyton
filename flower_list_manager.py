def main():
    flower_list = [] # empty lists to store flower names.

    while True: 
        flower = input("Enter the name of a flower (or 'done' to finish): ")

        if flower.lower() =="done":
            break
        flower_list.append(flower)
    
    flower_list.sort()


    #print the sorted list with a number next to each flower

    for i, flower in enumerate(flower_list, start=1):
        print(f"{i}. {flower}")

    # ask user to input a specific flower
    search_flower = input("Enter the name of a flower to search for: ")

    # Check if the flower is in the list
    if search_flower in flower_list:
        print(f"the flower '{search_flower}' is found in the list.")
    else:
        print(f"the flower '{search_flower}' is not found in the lists.")

# ask to search for flower
main()  

