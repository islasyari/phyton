def main():
    # Please enter the current date and time
    date_time = input("Enter the current date and time: ")

    # Create a a diary entry
    entry = input("Enter your diary entry: ")

    # Open the diary.txt file in append mode
    with open("diary.txt", "a") as file:
        # Write the date, time, and entry to the file
        file.write(date_time + "\n")
        file.write(entry + "\n\n")

    print("Diary entry saved successfully.")

# Call the main function
if __name__ == "__main__":
    main()
