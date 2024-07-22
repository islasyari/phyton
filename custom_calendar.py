import calendar
import datetime

def main():
    current_year = datetime.datetime.now().year
    birth_month = input("Enter your birth month (1-12): ")
    
    try:
        birth_month = int(birth_month)
        if birth_month < 1 or birth_month > 12:
            raise ValueError
    except ValueError:
        print("Invalid input. Please enter a valid month (1-12).")
        return
    
    calendar_text = calendar.month(current_year, birth_month)
    print(calendar_text)

main()
