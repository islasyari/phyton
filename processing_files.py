def main():
    file_name = input("Enter a file name: ")

    total = 0
    count = 0

    try:
        with open(file_name, "r") as file:
            for line in file:
                try:
                    number = float(line.strip())
                    total += number
                    count += 1
                    print(f"{number:,.2f}")
                except ValueError:
                    print("Invalid number format")

        print(f"Total: {total:,.2f}")
        print(f"Number of entries: {count}")
        if count > 0:
            average = total / count
            print(f"Average: {average:,.2f}")
        else:
            print("Average: N/A")

    except FileNotFoundError:
        print("File not found")

if __name__ == "__main__":
    main()


