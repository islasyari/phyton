# Conversion variables (global and constant)
POUNDS_TO_KG = 0.453592
INCHES_TO_METERS = 0.0254

def main():
    # Input
    weight_pounds = float(input("Enter your weight in pounds: "))
    height_inches = float(input("Enter your height in inches: "))

    # Conversion to Metric
    weight_kg = weight_pounds * POUNDS_TO_KG
    height_meters = height_inches * INCHES_TO_METERS

    # BMI Calculation
    bmi = weight_kg / (height_meters * height_meters)

    # BMI Categories
    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 24.9:
        category = "Normal weight"
    elif bmi < 29.9:
        category = "Overweight"
    else:
        category = "Obese"

    # Output
    print(f"Your BMI is: {bmi:.2f}")
    print(f"You are in the {category} category.")

if __name__ == "__main__":
    main()
