def calculate_interest(principal, rate, time):
    simple_interest = (principal * rate * time) / 100
    return simple_interest

principal_amount = float(input("Enter the principal amount: "))
interest_rate = float(input("Enter the interest rate as a whole number (5% would be 5): "))
investment_time = int(input("Enter the investment time in whole years: "))

calculated_interest = calculate_interest(principal_amount, interest_rate, investment_time)

print(f"The simple interest for a principal amount of ${principal_amount:,.2f} at an interest rate of {interest_rate}% over a period of {investment_time} years is: ${calculated_interest:,.2f}")
