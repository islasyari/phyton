import datetime
from datetime import timedelta
def main():
    birth_year = int(input("What year were you born? "))
    birth_month = int(input("What month were you born (as a number)? "))
    birth_day = int(input("What day of the month were you born? "))

    # Create a datetime object for the user's birthday
    birthday = datetime.datetime(birth_year, birth_month, birth_day)

    # Get the current date and time
    current_date = datetime.datetime.now()

    # Calculate the difference between the current date and the user's birthday
    age = current_date - birthday

    # Calculate the age in days, years, months, weeks, and hours
    age_in_days = age.days
    age_in_years = age_in_days // 365.25
    age_in_months = (age_in_days % 365.25) // 30.436875
    age_in_weeks = age_in_days // 7
    age_in_hours = age.total_seconds() // 3600

    # Format and print the results
    print(f"Your birthday is: {birthday.strftime('%Y-%m-%d')}")
    print(f"Difference is {age_in_days} days")
    print(f"You are {age_in_years} years old")
    print(f"You are {age_in_months} months old")
    print(f"You are {age_in_weeks} weeks old")
    print(f"You are {age_in_hours} hours old")

    # Rest of the program logic goes here
main()

