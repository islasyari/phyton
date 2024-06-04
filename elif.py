# Define a function to calculate grade based on percentage
# Get the numeric grade
numeric_grade = int(input("Enter the numeric grade:  "))
# Check if grade is more than 90
if numeric_grade >= 90:
    print ("The letter grade is: A")  # Grading 90-100
elif numeric_grade >= 80:
    print ("The letter grade is: B")  # Grading 80-89
elif numeric_grade >= 70:
    print ("The letter grade is: C")  # Grading 70-79
elif numeric_grade >= 60:
    print ("The letter grade is: D")  # Grading 60-69 

else: 
 numeric_grade <= 59 # anything below 60 is F
 print("The letter grade is: F") 
  

