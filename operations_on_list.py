def display_available_seats(seats):
    print("Available seats:")
    for seat in seats:
        print(seat, end=" ")
    print()

def ticket_purchase_process(seats):
    while True:
        seat_number = int(input("Select a seat number (enter 0 to finish): "))
        
        if seat_number == 0:
            break
        
        if seat_number not in seats:
            print("Invalid seat number. Please choose again.")
            continue
        
        seats.remove(seat_number)
        display_available_seats(seats)

def main():
    seats = list(range(1, 21))
    display_available_seats(seats)
    ticket_purchase_process(seats)

if __name__ == "__main__":
    main()
