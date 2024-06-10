# 
days = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")
steps = [] # Empty list for steps taken
#repeate over each day
for day in days:
    steps_taken = int(input(f"How many steps did you take on {day}? "))
    steps.append(steps_taken) # append the number of steps to the step list 

total = sum(steps) # calculation for total number of steps
avarage = round(total / len(steps))

for i in range(len(days)):
    print(f"You took {steps[i]}steps on {days[i]}.")

#print total and avarge steps
print(f"\nTotal steps: {total}")
print(f"Avarage steps: {avarage}")